import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ambari_package(host):
    p = host.package("ambari-server")
    assert p.is_installed


def test_ambari_socket(host):
    s = host.socket("tcp://8080")
    assert s.is_listening
