# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):

        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        addresses = re.findall(email_pattern, self.email_addresses)

        addresses.sort()

        return addresses

email_addresses = "john@doe.com, person@somewhere.org"
parser = EmailAddressParser(email_addresses)
result = parser.parse()
print(result)  
