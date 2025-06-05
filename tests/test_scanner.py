import pytest
from sweeper.scanner import scan_ips


@pytest.fixture
def mock_ping(monkeypatch):
    monkeypatch.setattr("sweeper.pinger.ping_host", lambda ip: ip.endswith("1") or ip.endswith("2"))

def test_scan_ips_basic(mock_ping):
    ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    results = scan_ips(ips, threads=2)
    assert results == {
        "192.168.1.1": True,
        "192.168.1.2": True,
        "192.168.1.3": False
    }