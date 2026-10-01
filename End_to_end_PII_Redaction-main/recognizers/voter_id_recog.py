from presidio_analyzer import PatternRecognizer, Pattern
voter_id_recognizer = PatternRecognizer ( supported_entity = "VOTER_ID",
                                        patterns = [Pattern(name = "voter_id", regex = r'\b[A-Z]{3}[0-9]{7}\b',score = 0.8)],
                                        context = [
                                            "voter id", 
                                            "voter identification", 
                                            "election card", 
                                            "voter card", 
                                            "EPIC number", 
                                            "EPIC", 
                                            "elector photo identity card", 
                                            "voter registration", 
                                            "voter details", 
                                            "voter information", 
                                            "election commission id", 
                                            "voter slip"    
                                        ]
                                       )