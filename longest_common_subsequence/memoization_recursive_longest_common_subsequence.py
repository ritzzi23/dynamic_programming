class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(text1,text2,m,n,dp):
            if  dp[m][n] != -1:
                return dp[m][n]
            if  m == 0 or n == 0:
                return 0
            if (text1[m-1] == text2[n-1]):
                dp[m][n] = 1 + lcs(text1,text2,m-1,n-1,dp)
            else:
                dp[m][n] = max(lcs(text1,text2,m-1,n,dp), lcs(text1,text2,m,n-1,dp))
            return dp[m][n] 

        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        return lcs(text1,text2,m,n,dp)
        