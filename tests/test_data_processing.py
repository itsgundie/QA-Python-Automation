"""Tests for data processing"""

from phonebook.data_processing import clean_phonenumber


def test_clean_phonenumber():
    assert "1234567890" == clean_phonenumber("123 456-78-90")
