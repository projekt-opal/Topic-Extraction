# -*- coding: utf-8 -*-
"""
Created on Wed May  2 15:40:19 2018

@author: Daniel
"""

from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
from flask_restful import Resource, Api
from rasa_nlu.model import Metadata, Interpreter
import requests
import configparser
from nif import NIFDocument as NIFDocument
from nif import NIFContent as NIFContent

app = Flask(__name__)
api = Api(app)

config = configparser.RawConfigParser()
config.read('conf/conf.cnf')

agdistis_url=config.get('agdistis','agdistis_url')
interpreter = Interpreter.load(config.get('rasa','rasa_model'))
host=config.get('flask','host')

#adds enitites from rasa to a nif-document
def add_nif_entities(reference_context,base_uri,entities,doc):
    for ent in entities:
        nif_content=NIFContent.NIFContent(base_uri+'#'+str(ent['start'])+','+str(ent['end']))
        nif_content.set_begin_index(ent['start'])
        nif_content.set_end_index(ent['end'])
        nif_content.set_reference_context(reference_context)
        nif_content.set_taClassRef('http://example/'+ent['entity'])
        nif_content.set_anchor_of(ent['value'])
        doc.addContent(nif_content)
    return doc
                               
#webservice for entity recognition
@app.route('/nifEntityRecognition/', methods=['POST'])
def annotate_nif_string():
    string=request.data.decode()
    doc=NIFDocument.nifStringToNifDocument(string)
    #replace of comma with whitespace for tokenizer
    res=interpreter.parse(doc.nifContent[0].is_string.replace(',',' ').replace('"',' ').replace('\\',''))
    base_uri=doc.nifContent[0].uri[0:doc.nifContent[0].uri.find('#')]
    app.logger.debug(res)
    doc=add_nif_entities(doc.nifContent[0].uri,base_uri,res['entities'],doc)
    app.logger.debug(doc.get_nif_string())
    resp = make_response(doc.get_nif_string())
    resp.headers['content'] = 'application/x-turtle'
    
    return resp
#webservice for recognition and liking
@app.route('/nifa2kb/', methods=['POST'])
def annotate_nif_string_Linking():
    string=request.data.decode()
    doc=NIFDocument.nifStringToNifDocument(string)
    print(doc)
    app.logger.debug(doc.nifContent[int(doc.get_referenced_contex_id())].is_string)
    #replace of comma with whitespace for tokenizer
    res=interpreter.parse(doc.nifContent[int(doc.get_referenced_contex_id())].is_string.replace(',',' ').replace('"',' ').replace('\\',''))
    base_uri=doc.nifContent[0].uri[0:doc.nifContent[0].uri.find('#')]
    app.logger.debug(res)
    doc=add_nif_entities(doc.nifContent[0].uri,base_uri,res['entities'],doc)
    #doc.nifContent[int(doc.get_referenced_contex_id())].is_string=doc.nifContent[int(doc.get_referenced_contex_id())].is_string.replace('\\','\\\\')
    ag_string=doc.get_nif_string()
    app.logger.debug(ag_string)
    #get links from agdsitis
    resp=requests.post(agdistis_url,ag_string.encode('utf-8'))
    app.logger.debug(resp.content.decode())
    
    
    resp = make_response(resp.content)
    resp.headers['content'] = 'application/x-turtle'
    app.logger.debug(resp)
    
    return resp

#tool demo
@app.route('/dataToNifEntityRecognition/', methods=['POST'])
def annotate_nif_string_data_toNif():
    string=request.data.decode()
    doc=NIFDocument.NIFDocument()
    base_uri="http://example.com"
    uri=base_uri+'#char=0'+','+str(len(string))
    nif_content=NIFContent.NIFContent(uri)
    nif_content.is_string=string
    nif_content.begin_index=0
    nif_content.end_index=len(string)
    doc.addContent(nif_content)
    res=interpreter.parse(string)
    doc=add_nif_entities(nif_content.uri,base_uri,res['entities'],doc)
    return doc.get_nif_string()

@app.route('/entityRecognition/', methods=['POST'])
def annotate_string():
    string=request.data.decode()
    print(string)
    #replace of comma with whitespace for tokenizer
    res=interpreter.parse(string)
    resp = make_response(str(res))
    resp.headers['content'] = 'application/x-json'
    
    return resp

if __name__ == '__main__':
    app.run(host=host,debug=True)