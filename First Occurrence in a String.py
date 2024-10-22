class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        
        if len(haystack)<len(needle):
            return -1
        

        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j]!=needle[j]:
                    break  
            else:
                return i  

        return -1

if __name__ == "__main__":
    solution = Solution()
    haystack = "hello"
    needle = "ll"
    print(solution.strStr(haystack, needle))  
