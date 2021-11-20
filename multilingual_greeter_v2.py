from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1:'English', 2:'Hindi', 3: 'Telugu'}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {1:'What is your name?', 2:'Aap ka naam kya hain?', 3:'Mee perenti?'}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {1:'Hello', 2:'Namaste', 3:'Namaste'}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print('Please choose a language: ')
    for key, value in lang_options.items():
        print(f'{key}:',value)



def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    lang_choice = int(input())
    return lang_choice


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    return lang_choice in lang_options


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    return name_prompt_options.get(lang_choice)


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """

    #name = int(input('What is your name?'))


    return input(name_prompt)
    #keys_list=list(name_prompt_dict.keys())
    #vals_list=list(name_prompt_dict.values())
    #position = vals_list.index(name_prompt)
    #return keys_list[position]

def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    print(greetings_options.get(lang_choice), name)

def mode_input():
    return input('Please select a mode - 1-Admin mode 2-User mode 0-Exit:')

def add_mod_fn():
    return input('Please select an option - 1-add 2-modify 3-view 0-go back:')

def add_to_all_dicts():
    input_lang = input('Enter the new language name:')
    if(input_lang not in lang_dict.values()):
        new_key = max(lang_dict.keys()) + 1
        lang_dict[new_key] = input_lang
        input_name_prompt = input('Enter name prompt in the new language:')
        name_prompt_dict[new_key] = input_name_prompt
        input_greetings_dict = input('Enter greetings in the new language:')
        greetings_dict[new_key] = input_greetings_dict
        return lang_dict, name_prompt_dict, greetings_dict
    else:
        print('The language already exists!')
        return lang_dict, name_prompt_dict, greetings_dict

def modify_in_all_dicts():
    input_lang_key = int(input('Enter the existing language key to modify:'))
    if input_lang_key in lang_dict:
        lang_dict[input_lang_key] = input('Enter the existing language:')
        name_prompt_dict[input_lang_key] = input('Enter name prompt in the existing language:')
        greetings_dict[input_lang_key] = input('Enter greetings in the new language:')
        print('Entries have been updated')
    else:
        print('Invalid input')
    return lang_dict, name_prompt_dict, greetings_dict

def view_from_all_dicts():
    for key, value in lang_dict.items():
        print(key, value, end=" ")
    print('\n')
    for key, value in name_prompt_dict.items():
        print(key, value, end=" ")
    print('\n')
    for key, value in greetings_dict.items():
        print(key, value, end=" ")
    print('\n')
    return lang_dict, name_prompt_dict, greetings_dict

if __name__ == '__main__':

    while True:
        mode_opt = mode_input()
        if mode_opt == '1':#1-admin 2-user
            add_mod_view = add_mod_fn()
            while add_mod_view == '1' or add_mod_view == '2' or add_mod_view == '0' or add_mod_view == '3':
                if add_mod_view == '1':#1-add 2-modify 3-view
                    lang_dict, name_prompt_dict, greetings_dict = add_to_all_dicts()
                    break
                elif add_mod_view == '2':#1-add 2-modify 3-view
                    lang_dict, name_prompt_dict, greetings_dict = modify_in_all_dicts()
                    break
                elif add_mod_view == '3':#1-add 2-modify 3-view
                    lang_dict, name_prompt_dict, greetings_dict = view_from_all_dicts()
                    break
                elif add_mod_view == '0':
                    break
                else:
                    print('Invalid input, try again')
                    break
        elif mode_opt == '2':#1-admin 2-user
            print_language_options(lang_dict)
            chosen_lang = language_input()
            while language_choice_is_valid(lang_dict, chosen_lang) is False:
                print("Invalid selection. Try again.")
                chosen_lang = language_input()

            selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
            chosen_name = name_input(selected_prompt)
            greet(chosen_name, greetings_dict, chosen_lang)
        elif mode_opt == '0':
            print('Thank you! Visit again!')
            break
        else:
            print('Invalid input for mode! Try again!')