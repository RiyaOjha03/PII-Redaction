from presidio_analyzer import PatternRecognizer, Pattern
from presidio_analyzer.predefined_recognizers import PhoneRecognizer
class CustomPhoneRecognizer(PhoneRecognizer):
    def __init__(self):
        super().__init__()
        
        self.context = [
            "phone", "mobile", "cell", "contact", "telephone", 
            "contact number", "reach me at", "whatsapp", "call",
            "call me on", "ring me on","call at","Number","No.", "contact is" ,"contact me on","contact me at","contact me"
        ]
        self.patterns =[
                        Pattern(name = "plane_phone_number",regex =r'\b[6-9][0-9]{9}' ,score = 0.9),
                        Pattern(name = "phone_number_with_cc",regex =r'\+91[-\s]?[6-9][0-9]{9}' , score = 0.9)

            
        ]