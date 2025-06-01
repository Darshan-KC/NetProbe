import pytest
from sweeper.pinger import ping_host

# Test functions
def test_ping_host_reachable(monkeypatch):
    # Mocking ping_host to simulate a reachable IP
    monkeypatch.setattr("sweeper.pinger.ping_host", lambda ip: True)
    assert ping_host("192.168.1.1") == True