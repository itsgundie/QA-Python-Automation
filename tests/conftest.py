"""Shared fixtures."""

import pytest

from phonebook.phonenumbers import Phonebook


@pytest.fixture
def phonebook(tmpdir):
    """Provide an empty Phonebook"""
    return Phonebook(tmpdir)

