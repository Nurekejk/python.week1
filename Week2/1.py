class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = 0
        ans = str("")
        for x in range(0, len(address)):
            if address[a]==".":
                ans = ans + "[" + address[a] + "]"
            else: ans += address[a]
            a += 1 
        return ans