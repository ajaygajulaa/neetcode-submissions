class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l = len(clean)
        # print(l)
        for i in range(l//2):
            print(clean[i], clean[l-1])
            if clean[i]== clean[l-1]:
                # print(clean[i], clean[l-1])
                l=l-1
            else:
                return False
        return True
        