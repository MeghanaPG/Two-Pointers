class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_of_s = len(s)
        len_of_t = len(t)

        count_dict_s = {}
        count_dict_t = {}

        if len_of_s != len_of_t: 
            return False 

        for letter in s:
            if letter in count_dict_s:
                count_dict_s[letter] += 1 
            else:
                count_dict_s[letter] = 1 

        for letter in t:
            if letter in count_dict_t:
                count_dict_t[letter] += 1 
            else:
                count_dict_t[letter] = 1 

        return count_dict_s == count_dict_t 
        