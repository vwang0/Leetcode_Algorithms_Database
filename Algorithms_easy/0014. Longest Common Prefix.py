"""
0014. Longest Common Prefix
Write a function to find the longest common prefix string 
amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:
All given inputs are in lowercase letters a-z.
"""
# Solution 1
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = min(strs, key = len) if strs else ''
        while True:           
            if all(str.startswith(prefix) for str in strs):               
                return prefix
            prefix = prefix[:-1]

a = Solution()
strs = ["flower","flow","flight"]
a.longestCommonPrefix(strs)

# Solution 2
class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        if not strs: return ""
        res = min(strs, key = len)
        for s in strs:
            for j in range(len(res)):
                if s[j]!=res[j]:
                    res = res[:j]
                    break
        return res