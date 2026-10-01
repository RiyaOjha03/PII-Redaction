from presidio_analyzer import PatternRecognizer, Pattern
gstin_recognizer = PatternRecognizer( supported_entity = "GST_IN",
                                     patterns = [Pattern(name="gstin_number", regex=r'\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}', score=0.8)],
                                     context =  [
                                                "gst number",
                                                "gst no",
                                                "gstin",
                                                "gst identification number",
                                                "gst registration number",
                                                "gst id",
                                                "gst details",
                                                "goods and service tax number",
                                                "tax identification number",
                                                "business gst number",
                                                "gst certificate",
                                                "gstin number",
                                                "company gst",
                                                "firm gst",
                                                "organization gst",
                                                "tax gst"
                                            ]
                                                
                                   )