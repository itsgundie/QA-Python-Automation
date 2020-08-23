
import unittest

from Phonebook.ClassPhonebook import PhoneBook


class TestPhonebook(unittest.TestCase):

	def setUp(self) -> None:
		self.phonebook = PhoneBook()

	def test_lookup_by_name(self):
		self.phonebook.add("Paul", "12345678910")
		number = self.phonebook.lookup("Paul")
		self.assertEqual("12345678910", number)

	def test_name_missing_get_error(self):
		with self.assertRaises(KeyError):
			self.phonebook.lookup("missing")

	def test_is_consistent_empty_phonebook(self):
		self.assertTrue(self.phonebook.is_consistent())

	def test_is_consistent_different_entries(self):
		self.phonebook.add("Paul", "12345678910")
		self.phonebook.add("John", "01234567891")
		self.assertTrue(self.phonebook.is_consistent())

	def test_inconsistent_duplicate_entries(self):
		self.phonebook.add("George", "23456789101")
		self.phonebook.add("Ringo", "23456789101")
		self.assertFalse(self.phonebook.is_consistent())

	def test_inconsistent_duplicate_prefix(self):
		self.phonebook.add("Paul", "12345678910")
		self.phonebook.add("Ringo", "1234")
		self.assertFalse(self.phonebook.is_consistent())

	def test_phonebook_adding_name_and_num(self):
		self.phonebook.add("Ozzy", "666")
		self.assertIn("Ozzy", self.phonebook.get_names())
		self.assertIn("666", self.phonebook.get_numbers())

