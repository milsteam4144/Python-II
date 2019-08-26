# CSC221
# M2T1_Milstead
# Goal: Gold

"""
Author: Mallory Milstead
Using pytest to test functions that use strings and lists
"""

import M2T1
import pytest

#To run from command prompt, cd into folder containing test_M2T1.py file
#run command: py.test -v

'''
THIS IS FOR MY REFERENCE ONLY
The decorator allows for using variables as parameters to the test function
in order to test multiple values at once

@pytest.mark.parametrize("test_input, expected_output",[
        ("abcdefghijklmnopqrstuvwxyz", ['a','e','i','o','u'] ), #Contains all vowels
        ("Mallory", ['a','o']), #Contains some vowels
        ("bcg", []),#Contains no vowels
        ("", [])#Empty String
        ])
def test_has_which_vowels(test_input, expected_output):
    assert M2T1.has_which_vowels(test_input) == expected_output
    '''
    
def test_has_which_vowels_all_vowels():
    '''Test against a string containing all the vowels'''
    assert M2T1.has_which_vowels("abcdefghijklmnopqrstuvwxyz") == ['a','e','i','o','u']
    
def test_has_which_vowels_some_vowels():
    '''Tests against a string containing some vowels'''
    assert M2T1.has_which_vowels("Mallory") == ['a','o']
    
def test_has_which_vowels_no_vowels():
    '''Tests against a string containing no vowels'''
    assert M2T1.has_which_vowels("bcg") == []
    
def test_has_which_vowels_empty_string():
    '''Tests against an empty string'''
    assert M2T1.has_which_vowels("") == []
    
def test_has_which_letters_normal_use():
    '''Tests against a 'normal' use case'''
    assert M2T1.has_which_letters("This is a string", ['h', 's', 'b']) == ['h', 's']
    
def test_has_which_letters_using_vowels():
    '''Tests a string against a list of vowels'''
    assert M2T1.has_which_letters("This is a string", ['a', 'e', 'i', 'o', 'u']) == ['a', 'i']
    #On this test, I learned that the order of the letters in the expected value matter, as I originally had ['i', 'a'] and it did not pass
    
def test_has_which_letters_empty_list():
    '''Tests a string against an empty list of letters'''
    assert M2T1.has_which_letters("This is a string", []) == []
    