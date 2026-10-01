from presidio_analyzer import PatternRecognizer, Pattern
pincode_recognizer = PatternRecognizer ( supported_entity = "PIN_CODE",
                                        patterns = [Pattern(name = "pin_code", regex = r'\b[1-9][0-9]{5}\b',score = 0.8)],
                                        context = ["pin code","PIN CODE","PIN","ZIP CODE","ZIP","zip code",
                                                   # States
                                                    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
                                                    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
                                                    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
                                                    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
                                                    "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
                                                    "West Bengal",
                                                    
                                                    # Union Territories
                                                    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
                                                    "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"]
                                       )