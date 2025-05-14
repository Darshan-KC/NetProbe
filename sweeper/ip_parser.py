import ipaddress

class IPAddressParser:
    def __init__(self):
        pass

    def validate_ip(ip_address_str:str):
        try:
            ipaddress.ip_address(ip_address_str)
            return True
        except ValueError:
            return False