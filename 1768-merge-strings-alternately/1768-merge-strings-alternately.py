class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result = ""
        iter_int = 0
        for i, j in zip(word1, word2):
            result = result + i + j
            iter_int += 1

        result = result + word1[iter_int:] + word2[iter_int:]


        return result
