import pytest
import sweeper.pinger

# Test functions
def test_ping_host_reachable(monkeypatch):
    # Mocking ping_host to simulate a reachable IP
    monkeypatch.setattr("sweeper.pinger.ping_host", lambda ip: True)
    assert sweeper.pinger.ping_host("192.168.1.1") == True

def test_ping_host_unreachable(monkeypatch):
    # Mocking ping_host to simulate an unreachable IP
    monkeypatch.setattr("sweeper.pinger.ping_host", lambda ip: False)
    assert sweeper.pinger.ping_host("10.255.255.1") == False