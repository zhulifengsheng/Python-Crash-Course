import unittest

from country_codes import get_country_code

class CountryCodesTestCase(unittest.TestCase):
	
	def test_get_country_code(self):
		country_code = get_country_code('Andorra')
		self.assertEqual(country_code, 'ad')
		
unittest.main()
