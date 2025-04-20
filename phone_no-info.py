import phonenumbers
from phonenumbers import carrier, geocoder, timezone, phonenumberutil

def get_phone_info(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)
        
        # Get basic validation info
        is_valid = phonenumbers.is_valid_number(parsed_number)
        is_possible = phonenumbers.is_possible_number(parsed_number)
        number_type = phonenumberutil.number_type(parsed_number)
        number_type_str = {
            phonenumberutil.PhoneNumberType.MOBILE: "Mobile",
            phonenumberutil.PhoneNumberType.FIXED_LINE: "Fixed Line",
            phonenumberutil.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
            phonenumberutil.PhoneNumberType.TOLL_FREE: "Toll Free",
            phonenumberutil.PhoneNumberType.PREMIUM_RATE: "Premium Rate",
            phonenumberutil.PhoneNumberType.SHARED_COST: "Shared Cost",
            phonenumberutil.PhoneNumberType.VOIP: "VoIP",
            phonenumberutil.PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
            phonenumberutil.PhoneNumberType.PAGER: "Pager",
            phonenumberutil.PhoneNumberType.UAN: "Universal Access Number",
            phonenumberutil.PhoneNumberType.UNKNOWN: "Unknown"
        }.get(number_type, "Unknown")
        
        # Get carrier information
        carrier_name = carrier.name_for_number(parsed_number, "en")
        
        # Get geographical information
        region = geocoder.description_for_number(parsed_number, "en")
        
        # Get timezone information
        time_zones = timezone.time_zones_for_number(parsed_number)
        
        # Format the output
        info = f"""
Phone Number Information:
------------------------
Number: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}
National Format: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)}
Country Code: +{parsed_number.country_code}
National Number: {parsed_number.national_number}
Country: {region}
Carrier: {carrier_name}
Timezone: {', '.join(time_zones)}
Number Type: {number_type_str}
Valid: {'Yes' if is_valid else 'No'}
Possible: {'Yes' if is_possible else 'No'}
"""
        return info
        
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    phone = input("Enter phone number with country code (e.g., +919876543210): ")
    print(get_phone_info(phone))