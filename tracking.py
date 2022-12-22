
import phonenumbers
number="+250780772249"
from phonenumbers import geocoder
ch_number=phonenumbers.parse(number,"CH")#Country & history
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier

service_number=phonenumbers.parse(number,"RO")#Real Organisation
print(carrier.name_for_number(service_number,"en"))
