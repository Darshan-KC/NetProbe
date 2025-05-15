import ipaddress

def parse_cidr(cidr_input):
    try:
        network = ipaddress.ip_network(cidr_input, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as e:
        raise ValueError(f"Invalid CIDR input: {e}")

def parse_range(start_ip, end_ip):
    try:
        start = ipaddress.IPv4Address(start_ip)
        end = ipaddress.IPv4Address(end_ip)
        if start > end:
            raise ValueError("Start IP must be less than or equal to End IP")
        return [str(ipaddress.IPv4Address(ip)) for ip in range(int(start), int(end) + 1)]
    except ipaddress.AddressValueError as e:
        raise ValueError(f"Invalid IP address: {e}")

def validate_ip(ip_address_string):
    try:
        ipaddress.IPv4Address(ip_address_string)
        return True
    except ipaddress.AddressValueError:
        return False