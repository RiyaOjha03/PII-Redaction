from presidio_analyzer import PatternRecognizer, Pattern
ayushman_id_recognizer = PatternRecognizer( supported_entity = "AYUSHMAN_ID",
                                     patterns = [Pattern(name="ayushman_id", regex=r'(?:\d{4}\s?\d{4}\s?\d{4}\s?\d{2})', score=0.95)],
                                     context =  [
                                                "ayushman id",
                                                "ABHA ID",
                                                "ABHA_ID",
                                                "abha id",
                                                "abha number",
                                                "health id",
                                                "health card number",
                                                "ayushman bharat id",
                                                "ayushman health id",
                                                "abha card",
                                                "Ayushman Bharat program",
                                                "ayushman card",
                                                "ayushman beneficiary id",
                                                "national health id",
                                                "abha address",
                                                "health id number",
                                                "ayushman bharat health id",
                                                "abha health number",
                                                "pmjay id",
                                                "pmjay beneficiary id"
                                            ]
                                                
                                   )