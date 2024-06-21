import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import NumberParseException, PhoneNumberType

def get_phone_info(phone_number):
    try:
        # Parsing the phone number
        number = phonenumbers.parse(phone_number, None)
        
        if not phonenumbers.is_valid_number(number):
            print("Invalid phone number.")
            return
        
        # Getting the country and region information
        country_code = phonenumbers.region_code_for_number(number)
        country_name = geocoder.country_name_for_number(number, "en")
        
        # Getting the number type
        number_type = phonenumbers.number_type(number)
        number_type_str = 'Unknown'
        if number_type == PhoneNumberType.MOBILE:
            number_type_str = 'Mobile'
        elif number_type == PhoneNumberType.FIXED_LINE:
            number_type_str = 'Fixed line'
        elif number_type == PhoneNumberType.FIXED_LINE_OR_MOBILE:
            number_type_str = 'Fixed line or mobile'
        elif number_type == PhoneNumberType.TOLL_FREE:
            number_type_str = 'Toll-free'
        elif number_type == PhoneNumberType.PREMIUM_RATE:
            number_type_str = 'Premium rate'
        elif number_type == PhoneNumberType.SHARED_COST:
            number_type_str = 'Shared cost'
        elif number_type == PhoneNumberType.VOIP:
            number_type_str = 'VoIP'
        elif number_type == PhoneNumberType.PERSONAL_NUMBER:
            number_type_str = 'Personal number'
        elif number_type == PhoneNumberType.PAGER:
            number_type_str = 'Pager'
        elif number_type == PhoneNumberType.UAN:
            number_type_str = 'Universal access number'
        elif number_type == PhoneNumberType.VOICEMAIL:
            number_type_str = 'Voicemail'
        
        # Getting the carrier information
        operator = carrier.name_for_number(number, "en")
        
        # Getting the geographic location information
        location = geocoder.description_for_number(number, "en")
        
        # Getting the time zone information
        timezone_info = timezone.time_zones_for_number(number)
        
        # Active status
        time_active = 'Active' if phonenumbers.is_valid_number_for_region(number, country_code) else 'Inactive'
        
        # Additional description
        description = 'Personal' if number_type == PhoneNumberType.PERSONAL_NUMBER else 'Business'
        
        # Formatting the number
        formatted_number = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_national = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.NATIONAL)
        formatted_number_e164 = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
        formatted_number_rfc3966 = phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.RFC3966)
        
        # Printing the information
        print(f'Phone number information:')
        print(f'Country: {country_name} ({country_code})')
        print(f'Number type: {number_type_str}')
        print(f'Operator: {operator}')
        print(f'Location: {location}')
        print(f'Time active: {time_active}')
        print(f'Description: {description}')
        print(f'Timezone info: {timezone_info}')
        print(f'Formatted number (International): {formatted_number}')
        print(f'Formatted number (National): {formatted_number_national}')
        print(f'Formatted number (E.164): {formatted_number_e164}')
        print(f'Formatted number (RFC3966): {formatted_number_rfc3966}')
        
    except NumberParseException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    phone_number = input('Enter phone number (including country code): ')
    get_phone_info(phone_number)