import unittest
from unittest.mock import patch, mock_open

from expression_transformer import expression_transform, filename_validator, datetime_validator, phone_number_validator, \
    extract_all_hyperlinks, extract_title_and_content


class TestExpressionTransformer(unittest.TestCase):
    def test_basic_expression(self):
        self.assertEqual(expression_transform("1+2#"), ['1', '2', '+'])

    def test_operator_priority(self):
        self.assertEqual(expression_transform("3+4*2#"), ['3', '4', '2', '*', '+'])

    def test_parentheses(self):
        self.assertEqual(expression_transform("(3+4)*2#"), ['3', '4', '+', '2', '*'])

    def test_multidigit_numbers(self):
        self.assertEqual(expression_transform("123+456#"), ['123', '456', '+'])


class TestRegularExpressions(unittest.TestCase):
    def test_filename_validator(self):
        valid_cases = ["image.jpg", "photo.jpeg", "test.gif"]
        invalid_cases = ["file.txt", "doc.pdf", "image.jpg.png"]

        for case in valid_cases:
            with self.subTest(case=case):
                self.assertTrue(filename_validator(case))

        for case in invalid_cases:
            with self.subTest(case=case):
                self.assertFalse(filename_validator(case))

    def test_datetime_validator(self):
        valid_dates = ["12/31/2020", "02/28/2021", "04/30/2022"]
        invalid_dates = ["13/01/2020", "02/40/2021", "00/15/2022"]

        for date in valid_dates:
            with self.subTest(date=date):
                self.assertTrue(datetime_validator(date))

        for date in invalid_dates:
            with self.subTest(date=date):
                self.assertFalse(datetime_validator(date))

    def test_phone_number_validator(self):
        valid_numbers = [
            ("(1234)56789012-3456", "1234"),
            ("(9999)00000000-1111", "9999")
        ]
        invalid_numbers = ["(123)45678901-2345", "1234567890123456"]

        for number, code in valid_numbers:
            with self.subTest(number=number):
                result, area_code = phone_number_validator(number)
                self.assertTrue(result)
                self.assertEqual(area_code, code)

        for number in invalid_numbers:
            with self.subTest(number=number):
                self.assertFalse(phone_number_validator(number)[0])


def main():
    # Unit tests
    unittest.main(argv=[''], exit=False)


if __name__ == "__main__":
    main()
