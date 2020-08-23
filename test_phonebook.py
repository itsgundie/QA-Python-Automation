
import unittest

from ClassPhonebook import PhoneBook


class TestPhonebook(unittest.TestCase):
	def test_lookup_by_name(self):
		phonebook = PhoneBook()
		phonebook.add("Paul", "12345678910")
		number = phonebook.lookup("Paul")
		self.assertEqual("12345678910", number)

	def test_name_missing(self):
		phonebook = PhoneBook()
		with self.assertRaises(KeyError):
			phonebook.lookup("missing")

	@unittest.skip("Work In Progress")
	def test_empty_phonebook_is_consistent(self):
		phonebook = PhoneBook()
		self.assertTrue(phonebook.is_consistent())
