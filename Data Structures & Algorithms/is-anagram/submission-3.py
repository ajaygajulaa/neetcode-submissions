class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dica = {}
        dicb = {}

        for i in range(0, len(s)):
            dica[s[i]]= dica.get(s[i],0)+1
            dicb[t[i]]= dicb.get(t[i],0)+1
        if dica == dicb:
            return True
        return False
        