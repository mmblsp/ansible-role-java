import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_java_availability(host):
    cmd = host.run('java -version; javac -version')
    assert cmd.rc == 0
