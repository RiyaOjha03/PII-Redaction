import os
import sys
import logging

# External libraries
import pandas as pd
import numpy as np
import regex
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer.predefined_recognizers import PhoneRecognizer, DateRecognizer
from presidio_anonymizer.entities import OperatorConfig
from presidio_analyzer import PatternRecognizer , Pattern
import fitz
import pymongo



# self made library imports
from faker_data.faker_replacements import generate_fake_value_for_entity
from recognizers.ifsc_recog import ifsc_recognizer
from recognizers.phone_recog import PhoneRecognizer
from recognizers.pin_code_recog import pincode_recognizer
from recognizers.state_recog import state_recognizer
from recognizers.voter_id_recog import voter_id_recognizer
from recognizers.aadhaar_recog import aadhaar_recognizer
from recognizers.ayushman_id_recog import ayushman_id_recognizer
from recognizers.driving_licence_num_recog import driving_licence_recognizer
from recognizers.gst_recog import gstin_recognizer
from registry_manager import set_up
from entity_recogniser import entity_sender
