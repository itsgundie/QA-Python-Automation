"""Tests for Phonebook class."""

import pytest


def test_lookup_by_name(phonebook):
    phonebook.add("Paul", "1234")
    assert "1234" == phonebook.lookup("Paul")


@pytest.mark.skip("WIP")
def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Paul", "1234")
    assert "Paul" in phonebook.names()


def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Paul")


def test_empty_phonebook_is_consistent(phonebook):
    assert phonebook.is_consistent()


def test_is_consistent_with_different_entries(phonebook):
    phonebook.add("Paul", "12345")
    phonebook.add("John", "012345")
    assert phonebook.is_consistent()


def test_inconsistent_with_duplicate_entries(phonebook):
    phonebook.add("George", "12345")
    phonebook.add("Ringo", "12345")
    assert not phonebook.is_consistent()


def test_inconsistent_with_duplicate_prefix(phonebook):
    phonebook.add("Ozzy", "12345")
    phonebook.add("Dio", "123")
    assert not phonebook.is_consistent()

