class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # clean.lower()

        # print(clean)
        # print(clean[::-1])
        if clean == clean[::-1]:
            return True
        else:
            return False
        