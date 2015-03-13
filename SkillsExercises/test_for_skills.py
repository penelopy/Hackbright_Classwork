import unittest

from skills import *

class TestSkillsExercise(unittest.TestCase):

    def setUp(self):
        self.number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
        self.word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

    ### Tests ###

    def test_1_all_odd(self):
        self.assertEqual(all_odd(self.number_list), [-5, 15, 23, 7])

    # test failing - return None 
    def test_2_all_even(self):
        self.assertEqual(all_even(self.number_list), [6, 4, 8, 16, 42, 2])

    def test_3_long_words(self):
        self.assertEqual(long_words(self.word_list), ['What', 'about', 'Spam', 'sausage', 'spam', 'spam', 'bacon', 'spam', 'tomato', 'spam'])

    # test failing - return 0     
    def test_4_smallest(self):
        self.assertEqual(smallest(self.word_list), -5)
    
    def test_5_largest(self):
        self.assertEqual(largest(self.number_list), 42)

    def test_6_halvesies(self):
        self.assertEqual(halvesies(self.number_list), [-2.5, 3.0, 2.0, 4.0, 7.5, 8.0, 11.5, 21.0, 1.0, 3.5])

    def test_7_word_lengths(self):
        self.assertEqual(word_lengths(self.word_list), [4, 5, 3, 4, 7, 4, 4, 5, 4, 6, 3, 4])

    def test_8_sum_numbers(self): 
        self.assertEqual(sum_numbers(self.number_list), 118)

    def test_9_mult_numbers(self):
        self.assertEqual(mult_numbers(self.number_list), -3115929600)

    def test_10_join_strings(self):
        self.assertEqual(join_strings(self.word_list), "WhatabouttheSpamsausagespamspambaconspamtomatoandspam")

    # test failing - return None     
    def test_11_average(self):
        self.assertEqual(average(self.number_list), 11.8)



    

if __name__ == '__main__':
    unittest.main()