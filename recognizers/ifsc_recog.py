from presidio_analyzer import PatternRecognizer, Pattern
ifsc_recognizer = PatternRecognizer( supported_entity = "IFSC_CODE",
                                     patterns = [Pattern(name="ifsc_pattern", regex=r'\b[A-Z]{4}0[A-Z0-9]{6}\b', score=0.8)],
                                     context =  ["bank", "branch", "IFSC", "account"]
                                                
                                   )