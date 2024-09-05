# core/phone_lookup.py

import phonenumbers
from phonenumbers import geocoder, carrier

def phone_lookup(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)
        
        # Validate the phone number
        if not phonenumbers.is_valid_number(parsed_number):
            return {"error": "Invalid phone number"}
        
        # Get country and carrier information
        country = geocoder.description_for_number(parsed_number, "en")
        phone_carrier = carrier.name_for_number(parsed_number, "en")
        region = phonenumbers.region_code_for_number(parsed_number)
        region_name = geocoder.description_for_number(parsed_number, "en")

        result = {
            "phone_number": phone_number,
            "valid": phonenumbers.is_valid_number(parsed_number),
            "country": country,
            "carrier": phone_carrier,
            "region": region_name,  # Region (State/Province)
            "region_code": region
        }
        return result
    except Exception as e:
        return {"error": f"Error processing phone number: {e}"}
