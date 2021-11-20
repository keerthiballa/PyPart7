from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import multilingual_greeter
import multilingual_greeter_v2

class MultilingualGreeterTest(TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_language_options(self, stdout_mock):
        languages = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
        }

        expected = "Please choose a language: \n" \
                   "1: English\n" \
                   "2: Spanish\n" \
                   "3: Portuguese\n"

        multilingual_greeter.print_language_options(languages)
        self.assertEqual(expected, stdout_mock.getvalue())

    @patch('builtins.input', return_value="1")
    def test_language_input(self, user_input):
        actual = multilingual_greeter.language_input()
        self.assertEqual(1, actual)

    def test_language_choice_is_valid(self):
        languages = {
            1: "English",
            2: "Spanish",
            3: "Portuguese"
        }

        test_cases = [
            (1, True),
            (2, True),
            (3, True),
            (4, False),
            (5, False),
            (10, False),
            ('PIG LATIN', False)
        ]

        for key, expected in test_cases:
            with self.subTest(f"{key}, {expected}"):
                self.assertEqual(expected, multilingual_greeter.language_choice_is_valid(languages, key))

    def test_get_name_input(self):
        name_prompt_dict = {
            1: 'What is your name?',
            2: '¿Cómo te llamas?',
            3: 'Qual é o seu nome?'
        }

        for key, expected in name_prompt_dict.items():
            with self.subTest(f"{key} -> {expected}"):
                self.assertEqual(expected, multilingual_greeter.get_name_input(name_prompt_dict, key))

    @patch('builtins.input', return_value="Harry Potter")
    def test_name_input(self, user_input):
        self.assertEqual("Harry Potter", multilingual_greeter.name_input("What is your name?"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_greet(self, stdout_mock):
        greetings_dict = {
            1: 'Hello',
            2: 'Hola',
            3: 'Olá'
        }

        multilingual_greeter.greet("Winston Wolfe", greetings_dict, 1)
        self.assertEqual("Hello Winston Wolfe\n", stdout_mock.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test2_greet(self, stdout_mock):
        greetings_dict = {
            1: 'Hello',
            2: 'Hola',
            3: 'Olá'
        }
        multilingual_greeter.greet("Vincent Vega", greetings_dict, 2)
        self.assertEqual("Hola Vincent Vega\n", stdout_mock.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test3_greet(self, stdout_mock):
        greetings_dict = {
            1: 'Hello',
            2: 'Hola',
            3: 'Olá'
        }
        multilingual_greeter.greet("Jules Winnfield", greetings_dict, 3)
        self.assertEqual("Olá Jules Winnfield\n", stdout_mock.getvalue())

class MultilingualGreeterTest_V2(TestCase):
    """
    @patch('sys.stdout', new_callable=StringIO)
    def test_mode_input(self, stdout_mock):
        actual = multilingual_greeter_v2.mode_input()
        self.assertEqual(1, actual)


    @patch('builtins.input', return_value="1")
    def test_language_input(self, user_input):
        actual = multilingual_greeter.language_input()
        self.assertEqual(1, actual)"""

    #@patch('')
    #def test_add_to_all_dicts(self, stdout_mock):
     #   actual=multilingual_greeter_v2.add_to_all_dicts()

    @patch('builtins.input', side_effect=['Spanish', 'Como te llamas', 'Hola'])
    def test_add_to_all_dicts(self, mock_input):
        actual = multilingual_greeter_v2.add_to_all_dicts()
        expected = ({1: 'English',
          2: 'Hindi',
          3: 'Telugu',
          4: 'Spanish'},
         {1: 'What is your name?',
          2: 'Aap ka naam kya hain?',
          3: 'Mee perenti?',
          4: 'Como te llamas'},
         {1: 'Hello', 2: 'Namaste', 3: 'Namaste', 4: 'Hola'})
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['English'])
    def test_add_to_all_dicts_lang_already_exist(self, mock_input):
        actual = multilingual_greeter_v2.add_to_all_dicts()
        expected = ({1: 'English',
                     2: 'Hindi',
                     3: 'Telugu'
                     },
                    {1: 'What is your name?',
                     2: 'Aap ka naam kya hain?',
                     3: 'Mee perenti?'
                     },
                    {1: 'Hello', 2: 'Namaste', 3: 'Namaste'})
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['1','English', 'What is your name ?', 'Greetings'])
    def test_modify_in_all_dicts(self, mock_input):
        actual = multilingual_greeter_v2.modify_in_all_dicts()
        expected = ({1: 'English',
          2: 'Hindi',
          3: 'Telugu'
          },
         {1: 'What is your name ?',
          2: 'Aap ka naam kya hain?',
          3: 'Mee perenti?'},
         {1: 'Greetings', 2: 'Namaste', 3: 'Namaste'})
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['5'])
    def test_modify_in_all_dicts_invalid_key(self, mock_input):
        actual = multilingual_greeter_v2.modify_in_all_dicts()
        expected = ({1: 'English',
          2: 'Hindi',
          3: 'Telugu'
          },
         {1: 'What is your name?',
          2: 'Aap ka naam kya hain?',
          3: 'Mee perenti?'},
         {1: 'Hello', 2: 'Namaste', 3: 'Namaste'})
        self.assertEqual(actual, expected)

    def test_view_from_all_dicts(self):
        actual = multilingual_greeter_v2.view_from_all_dicts()
        expected = ({1: 'English',
          2: 'Hindi',
          3: 'Telugu'
          },
         {1: 'What is your name?',
          2: 'Aap ka naam kya hain?',
          3: 'Mee perenti?'},
         {1: 'Hello', 2: 'Namaste', 3: 'Namaste'})
        self.assertEqual(actual, expected)