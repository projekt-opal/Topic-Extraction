# Topic-Extraction
OPAL component to extract entities such as places, keywords from dataset descriptions to improve relevant dataset seraching.

## Requirements
Python version 3.x, rasa_nlu

## Usage Instructions

### 1. Generation of training and testing data (rasa_nlu format)
The component assumes the training and testing data (annotated manually or automatically) is contained in .txt file where each training example is a single line consisting of annotated text. In topic extraction, we focus on 5 entity types, namely: place, person, date and keyword. An example annotation is as shown below

```
This is a Housing Benefit dataset for all new claims and change of circumstances received by the <entity type=place uri=null>London</entity> Borough of Barnet in the second half of <entity type=date uri=null>2015</entity>.
```



## Credits

[Data Science Group (DICE)](https://dice-research.org/) at [Paderborn University](https://www.uni-paderborn.de/)

This work has been supported by the German Federal Ministry of Transport and Digital Infrastructure (BMVI) in the project [Open Data Portal Germany (OPAL)](http://projekt-opal.de/) (funding code 19F2028A).
