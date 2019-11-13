# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:15:22 2019

@author: Jan
"""

from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config

#with open("C:/Users/Jan/Desktop/Opal/CRF/trainingfileOpal.json",'r',encoding='utf8') as f:
#        content = f.read()
trainer=Trainer(config.load("/home/zafar/Opal/CRF/conf/confCRF.yml"))
model=trainer.train(load_data("/home/zafar/Opal/CRF/train_file.json"))
print(model.parse('This public health intelligence profile describes the trends and patterns in the prevalence of dementia in Camden. It is one of a series of profiles on Mental Health.'))
trainer.persist("opal-model")
