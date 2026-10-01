from presidio_analyzer import PatternRecognizer, Pattern
driving_licence_recognizer = PatternRecognizer( supported_entity = "DRIVING_LICENCE",
                                     patterns = [Pattern(name="driving_licence", regex=r'\b[A-Z]{2}[0-9]{2}\s?[0-9]{4}\s?[0-9]{7}\b', score=0.8)],
                                     context =  [   "driving license",
                                                    "driver's license",
                                                    "driving licence",
                                                    "dl number",
                                                    "license number",
                                                    "licence number",
                                                    "dl no",
                                                    "motor vehicle license",
                                                    "transport license",
                                                    "driving permit",
                                                    "learner's license",
                                                    "permanent driving license",
                                                    "commercial driving license",
                                                    "personal driving license",
                                                    "RTO license",
                                                    "license id",
                                                    "DL-ID",
                                                    "DL number",
                                                    "Driver ID",
                                                    "driver licence"
                                                    ]
                                                
                                   )