from presidio_analyzer import AnalyzerEngine

def entity_sender(result):
    entities = set()
    for res in result:
        entities.add(res.entity_type)
    entities = sorted(entities)
    return entities