# faker_replacements.py
from faker import Faker

# Initialize Faker
fake = Faker()

# Dictionary to map entity types to faker generation functions
entity_to_fake_format = {
    "AU_ABN": lambda text: fake.bothify("## ### ### ###"),  # 11-digit format
    "AU_ACN": lambda text: fake.bothify("### ### ###"),     # 9-digit format
    "AU_MEDICARE": lambda text: fake.bothify("#### ###### #"),
    "AU_TFN": lambda text: fake.bothify("### ### ###"),
    
    "CREDIT_CARD": lambda text: fake.credit_card_number(card_type='visa'),
    "CRYPTO": lambda text: fake.sha256(),
    
    "DATE_TIME": lambda text: fake.date_time().strftime("%Y-%m-%d %H-%M-%S"),
    "EMAIL_ADDRESS": lambda text: fake.user_name() + "@cutie.com",
    "IBAN_CODE": lambda text: fake.iban(),
    
    "IND_STATE": lambda text: fake.state(),
    "IFSC_CODE": lambda text: fake.bothify(text="????0######").upper(),
    "AADHAAR": lambda text: fake.numerify("#### #### ####"),
    "IN_PAN": lambda text: fake.bothify("?????####?"),  # e.g. ABCDE1234F
    "IN_PASSPORT": lambda text: fake.bothify("?#######"),  # e.g. A1234567
    "IN_VEHICLE_REGISTRATION": lambda text: fake.bothify("??##??####"),  # e.g. KA01AB1234
    "VOTER_ID": lambda text: fake.bothify("???#######").upper(),
    "PIN_CODE": lambda text: fake.bothify("######"),
    "GST_IN": lambda text: fake.bothify("##?????####?#Z#").upper(),
    "AYUSHMAN_ID": lambda text: fake.bothify("#### #### #### ##"),
    "DRIVING_LICENCE": lambda text: fake.bothify("??## ###########"),
    
    
    "IP_ADDRESS": lambda text: fake.ipv4(),
    "LOCATION": lambda text: fake.city(),
    
    "MEDICAL_LICENSE": lambda text: fake.bothify("??####"),
    
    "NRP": lambda text: fake.word(),
    "PERSON": lambda text: fake.name(),
    "PHONE_NUMBER": lambda text: fake.numerify("+91 ##########"),
    
    "SG_NRIC_FIN": lambda text: fake.bothify("?#######?"),  # Singapore NRIC/FIN format
    "TITLE": lambda text: fake.prefix(),
    
    "UK_NHS": lambda text: fake.bothify("###-###-####"),
    "UK_NINO": lambda text: fake.bothify("??######?"),  # National Insurance Number
    
    "URL": lambda text: fake.url(),
    
    "US_BANK_NUMBER": lambda text: fake.numerify("##########"),
    "US_DRIVER_LICENSE": lambda text: fake.bothify("S########"),  # varies by state
    "US_ITIN": lambda text: fake.numerify("9##-7#-####"),
    "US_PASSPORT": lambda text: fake.bothify("#########"),  # 9-digit
    "US_SSN": lambda text: fake.ssn(),
}

# Function to generate fake value for a given entity type
def generate_fake_value_for_entity(entity_type):
    if entity_type in entity_to_fake_format:
        return entity_to_fake_format[entity_type](None)  # Call the function to generate the fake value
    return None
