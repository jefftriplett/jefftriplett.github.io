import subprocess

import pytest


@pytest.fixture(scope="session")
def justfile():
    process = subprocess.Popen(
        ["just", "--summary"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    stdout, _ = process.communicate()
    output = stdout.decode("utf-8").strip()
    yield output


def test_bootstrap(justfile):
    assert "bootstrap" in justfile.split()


def test_cibuild(justfile):
    assert "cibuild" in justfile.split()


def test_console(justfile):
    assert "console" in justfile.split()


def test_server(justfile):
    assert "server" in justfile.split()


def test_setup(justfile):
    assert "setup" in justfile.split()


def test_test(justfile):
    assert "test" in justfile.split()


def test_update(justfile):
    assert "update" in justfile.split()
