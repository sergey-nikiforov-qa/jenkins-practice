import pytest
from utils.logger import Logger


def test_something(hello):
    Logger.info("Running test")
    assert 1
