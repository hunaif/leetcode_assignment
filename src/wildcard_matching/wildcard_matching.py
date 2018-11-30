class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if len(p) == 0:
            return len(s) == 0


        p = self.remove_redundant_asterisks(p)

        str_len = len(s)
        pattern_len = len(p)


        lookup_table = [[False]*(pattern_len + 1) for x in range(0,str_len + 1)]

        lookup_table[0][0] = True  #Empty string and empty pattern

        for j in range(1, pattern_len+1):  #Hanndling empty string and * pattern combinations
            if p[j-1] == '*':
                lookup_table[0][j] = lookup_table[0][j-1]

        for i in range(1,str_len + 1):
            for j in range(1, pattern_len + 1):

                if p[j-1] == '*':
                    lookup_table[i][j] = lookup_table[i-1][j] or lookup_table[i][j-1]    ##Look left or top and see if any of them is True

                elif p[j-1] == '?' or p[j-1] == s[i-1] :
                    lookup_table[i][j] = lookup_table[i-1][j-1]   ##Look diagonally up and fetch its value

                else:
                    lookup_table[i][j] = False

        return lookup_table[str_len][pattern_len]


    def remove_redundant_asterisks(self,p):
        """
        :type p: str
        :rtype: str

        """

        """To convert a****b to a*b"""
        """Remove redundant asterisks to save execution time and memory"""
        updated_pattern = ""
        is_first_asterisk = True
        for i in range(0,len(p)):
            if p[i] == '*':
                if is_first_asterisk:
                    updated_pattern += p[i]
                    is_first_asterisk = False
            else:
                updated_pattern += p[i]
                is_first_asterisk = True
        return updated_pattern