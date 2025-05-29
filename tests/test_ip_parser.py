import pytest
from sweeper.ip_parser import parse_cidr, parse_range

def test_parse_cidr_valid():
    result = parse_cidr("192.168.1.0/30")
    expected = ["192.168.1.1", "192.168.1.2"]
    assert result == expected

def test_parse_cidr_invalid():
    with pytest.raises(ValueError):
        parse_cidr("invalid_cidr")

def test_parse_range_valid():
    result = parse_range("192.168.1.1", "192.168.1.3")
    expected = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    assert result == expected