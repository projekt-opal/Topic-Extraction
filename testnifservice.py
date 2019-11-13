# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:57:11 2019

@author: Jan
"""

import requests

url='http://localhost:5000/entityRecognition/'

data = '@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n@prefix nif: <http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#> .\n@prefix itsrdf: <http://www.w3.org/2005/11/its/rdf#> .\n@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n<http://example.com#char=0,515>\n        a                     nif:RFC5147String , nif:String, nif:Context ;\n        nif:beginIndex        "0"^^xsd:nonNegativeInteger ;\n        nif:endIndex          "515"^^xsd:nonNegativeInteger ;\n        nif:isString          "The dataset describes the effect of soil type, soil sterilisation and drought treatment on survival rate and growth of Howea belmoreana and Howea forsteriana, grown from seed in an experiment on Lord Howe Island for 30 months. The data describe the number of surviving plants per replicate, as well as height and number of leaves of individual plants at two timepoints. The work was carried out by Dr Owen Osborne and Prof. Vincent Savolainen, Imperial College London, and was funded by the NERC grant NE/M015742/1."^^xsd:string .\n'.encode('utf-8')
data2 = 'The dataset describes the effect of soil type, soil sterilisation and drought treatment on survival rate and growth of Howea belmoreana and Howea forsteriana, grown from seed in an experiment on Lord Howe Island for 30 months. The data describe the number of surviving plants per replicate, as well as height and number of leaves of individual plants at two timepoints. The work was carried out by Dr Owen Osborne and Prof. Vincent Savolainen, Imperial College London, and was funded by the NERC grant NE/M015742/1.'.encode('utf-8')
r = requests.post(url,data=data2)
print(r.text)