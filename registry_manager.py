#importing the custom recognizers
from presidio_analyzer import AnalyzerEngine
from recognizers.ifsc_recog import ifsc_recognizer
from recognizers.phone_recog import CustomPhoneRecognizer
from recognizers.pin_code_recog import pincode_recognizer
from recognizers.state_recog import state_recognizer
from recognizers.voter_id_recog import voter_id_recognizer
from recognizers.aadhaar_recog import aadhaar_recognizer
from recognizers.ayushman_id_recog import ayushman_id_recognizer
from recognizers.driving_licence_num_recog import driving_licence_recognizer
from recognizers.gst_recog import gstin_recognizer
# from recognizers.med_insurance_recog import med_insurance_recognizer

def set_up(analyzer):
    try:
        analyzer.registry.remove_recognizer("PHONE_NUMBER")
        
    except Exception as exception:
        print("recognizer already removed or doesnot exists.", {exception})

    analyzer.registry.add_recognizer(CustomPhoneRecognizer())
    analyzer.registry.add_recognizer(pincode_recognizer)
    analyzer.registry.add_recognizer(state_recognizer)
    analyzer.registry.add_recognizer(ifsc_recognizer)
    analyzer.registry.add_recognizer(voter_id_recognizer)
    analyzer.registry.add_recognizer(aadhaar_recognizer)
    analyzer.registry.add_recognizer(ayushman_id_recognizer)
    analyzer.registry.add_recognizer(driving_licence_recognizer)
    analyzer.registry.add_recognizer(gstin_recognizer)
    # analyzer.registry.add_recognizer(med_insurance_recognizer)
