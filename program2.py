def decode_message(s: str, p: str) -> bool:
    # Initialize the dimensions of the DP table
    m, n = len(s), len(p)
    
    # Create a DP table with (m+1) x (n+1) dimensions
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty pattern matches empty string
    dp[0][0] = True
    
    # Handle the case where pattern has leading '*' which can match an empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' can match zero or more characters
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                # '?' matches any single character or exact character match
                dp[i][j] = dp[i - 1][j - 1]
    
    # The answer is in the bottom-right corner of the table
    return dp[m][n]

# Test cases
print(decode_message("aa", "a"))     # False
print(decode_message("aa", "*"))     # True
print(decode_message("cb", "?a"))    # False
