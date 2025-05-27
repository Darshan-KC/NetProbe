import pytest
from sweeper.ip_parser import parse_cidr, parse_range

def test_parse_cidr_valid():
    result = parse_cidr("192.168.1.0/30")
    expected = ["192.168.1.1", "192.168.1.2"]
    assert result == expected