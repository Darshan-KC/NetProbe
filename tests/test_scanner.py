import pytest
import sweeper.scanner


@pytest.fixture
def mock_ping(monkeypatch):
    monkeypatch.setattr("sweeper.scanner.ping_host", lambda ip: ip.endswith("1") or ip.endswith("2"))

def test_scan_ips_basic(mock_ping):
    ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
    results = sweeper.scanner.scan_ips(ips, threads=2)
    assert results == {
        "192.168.1.1": True,
        "192.168.1.2": True,
        "192.168.1.3": False
    }