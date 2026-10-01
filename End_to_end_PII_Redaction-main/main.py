#main.py
from imports import *

#reading text 
with open("test2.txt") as f:
    test2 = f.read()


#Initialize analyzer
analyzer = AnalyzerEngine()


#Initialize anonymizer
anonymizer = AnonymizerEngine()

#calling set_up registry for addn and removal of custom recog
set_up(analyzer)
result = analyzer.analyze(text=test2,language="en")

#send entities to user to select
print(entity_sender(result))


#Prepare the operators for anonymization
operators = {}
for res in result:
    entity_type = res.entity_type
    fake_value = generate_fake_value_for_entity(entity_type)
    if fake_value:
        operators[entity_type] = OperatorConfig("replace", {"new_value": fake_value})

#Perform anonymization
redacted_result = anonymizer.anonymize(text=test2, analyzer_results=result, operators=operators)
print(redacted_result)
