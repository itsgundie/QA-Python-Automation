
import unittest

from ClassPhonebook import PhoneBook


class TestPhonebook(unittest.TestCase):

	def setUp(self) -> None:
		self.phonebook = PhoneBook()

	def test_lookup_by_name(self):
		self.phonebook.add("Paul", "12345678910")
		number = self.phonebook.lookup("Paul")
		self.assertEqual("12345678910", number)

	def test_name_missing(self):
		with self.assertRaises(KeyError):
			self.phonebook.lookup("missing")

	def test_empty_phonebook_is_consistent(self):
		self.assertTrue(self.phonebook.is_consistent())

	def test_is_consistent(self):
		self.phonebook.add("Paul", "12345678910")
		self.assertTrue(self.phonebook.is_consistent())
		self.phonebook.add("John", "01234567891")
		self.assertTrue(self.phonebook.is_consistent())
		self.phonebook.add("George", "12345678910")
		self.assertTrue(self.phonebook.is_consistent())
		self.phonebook.add("George", "1234")
		self.assertTrue(self.phonebook.is_consistent())
