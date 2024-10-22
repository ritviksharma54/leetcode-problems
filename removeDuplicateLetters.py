class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        pos={char: i for i, char in enumerate(s)}
        stack=[]
        ans=set()  

        for i, char in enumerate(s):
            if char not in ans:
                while (stack and char<stack[-1] and i<pos[stack[-1]]):
                    ans.remove(stack.pop())
                stack.append(char)
                ans.add(char)
        
        return "".join(stack)


if __name__ == "__main__":
    solution = Solution()
    s = "bcabc"
    print(solution.removeDuplicateLetters(s))  
