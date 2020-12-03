# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return "Hello World"

    def concatenate(self, value_to_be_added_to, value_to_add):
        return str(value_to_be_added_to) + str(value_to_add)

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index:ending_index+1]

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index+1:ending_index]

    def compare(self, first_value, second_value):
        if(first_value == None and second_value == 0 ):
            return True
        elif(first_value == False and second_value == 0 ):
            return True
        elif(first_value == True and second_value == 1 ):
            return True
        elif str(first_value) == str(second_value):
            return True
        else:
            return False

    def get_middle_character(self, string_to_fetch_from):
        len(string_to_fetch_from)//2
        return None # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
        chopped=string_to_fetch_from.split()[0]
        return chopped

    def get_second_word(self, string_to_fetch_from):
        chopped=string_to_fetch_from.split()[1]
        return chopped

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed[::-1]