# BOJ 9251 LCS 

word_a = input()
word_b = input()

dp = [[0]*(len(word_a)+1) for _ in range((len(word_b)+1))]

for b_idx in range(1, len(word_b)+1):
    for a_idx in range(1, len(word_a)+1): 
        if word_a[a_idx-1] == word_b[b_idx-1]: 
            dp[b_idx][a_idx] = max(dp[b_idx-1][a_idx], dp[b_idx][a_idx-1], dp[b_idx-1][a_idx-1]+1)
        else: 
            dp[b_idx][a_idx] = max(dp[b_idx-1][a_idx], dp[b_idx][a_idx-1])

print(dp[-1][-1])