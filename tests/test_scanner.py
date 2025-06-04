import pytest
from sweeper.scanner import scan_ips


@pytest.fixture
def mock_ping(monkeypatch):
    monkeypatch.setattr("sweeper.pinger.ping_host", lambda ip: ip.endswith("1") or ip.endswith("2"))