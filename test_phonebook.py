import pytest

from class_phonebook import Phonebook


@pytest.fixture
def phonebook(tmpdir):
    """Gives an empty Phonebook"""
    return Phonebook(tmpdir)


def test_lookup_by_name(phonebook):
    phonebook.add("Paul", "12345678910")
    assert "12345678910" == phonebook.lookup("Paul")


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Paul", "12345678910")
    assert "Paul" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Paul")
