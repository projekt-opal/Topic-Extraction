# Topic-Extraction
OPAL component to extract entities such as places, keywords from dataset descriptions to improve relevant dataset seraching. This repository contains all data and utilities to train and test a topic extraction model.

## Requirements
python version 3.x, rasa_nlu

## Usage Instructions

### 1. Generation of training and testing data (rasa_nlu format).
The component assumes the training and testing data (annotated manually or automatically) is contained in .txt file where each training example is a single line consisting of annotated text. In topic extraction, we focus on 5 entity types, namely: place, person, date and keyword. An example annotation is as shown below

```
This is a Housing Benefit dataset for all new claims and change of circumstances received by the <entity type=place uri=null>London</entity> Borough of Barnet in the second half of <entity type=date uri=null>2015</entity>.
```
To generate training and testing data, run the following command by adjusting paths to input training and testing (.txt) files and output files accordingly.

```
python generateOpalTrainingData.py
```
Once the command is finished, the files are generated at the desired output location.

### 2. Train the topic extraction model.

Once the training file is generated from the above step, create a model by adjusting the paths to map to the training and configuration file and running the command


```
python opalPersister.py
```
The above command generates a persistent model which could be found under the base directory of the project. Note that, one can create several models which could be found in the model folder's default directory.

### 3: Test the generated model.

Once a model is generated, it can be tested using the test data. To test the model, run the following command

```
python -m rasa_nlu.evaluate \
    --data path/to/test.json \
    --model path/to/model/default/model_20180323-145833
```
Note that, in the above command, model specifies the model to evaluate on the test data specified with data.

## Credits

[Data Science Group (DICE)](https://dice-research.org/) at [Paderborn University](https://www.uni-paderborn.de/)

This work has been supported by the German Federal Ministry of Transport and Digital Infrastructure (BMVI) in the project [Open Data Portal Germany (OPAL)](http://projekt-opal.de/) (funding code 19F2028A).
