from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = min(len(s) for s in strs)
        for i in range(minlen):
            for j in range(1, len(strs)):
                if strs[j][i]!=strs[0][i]:
                    return strs[0][0:i]
        return strs[0][0:minlen]

if __name__ == "__main__":
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    print(solution.longestCommonPrefix(strs))  