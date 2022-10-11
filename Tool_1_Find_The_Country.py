import re

class Word_Searcher:

    def __init__(self, list_to_seek):
        self.list_to_seek = list_to_seek

    def change_list_to_seek(self, new_list_to_seek):
        self.list_to_seek = new_list_to_seek

    def get_list_to_seek(self):
        return self.list_to_seek

    def find_the_patter(self, string_chain, pattern):
        return bool(re.search(pattern, string_chain))

    def find_inside_list(self, word_to_seek):
        result = [self.find_the_patter(p, word_to_seek) for p in sorted(self.list_to_seek)]
        value = any(result)
        return value

    def find_entire_list(self, new_list_to_seek):
        return list(map(self.find_inside_list, new_list_to_seek))




