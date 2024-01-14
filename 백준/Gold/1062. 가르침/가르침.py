# BOJ 1062 가르침 

# cnt: 재귀 횟수, learned: 배운 알파벳 체크 
def sol(cnt, start):

    global max_learned_words 
    
    if cnt == K - 5:
        learned_words = 0 
        for word in words: 
            for c in word: 
                if learned[ord(c)-97] == 0: 
                    break 
            else: 
                learned_words += 1
        max_learned_words = max(max_learned_words, learned_words) 

        return

    for i in range(start, 26): 
        if not learned[i]: 
            learned[i] = 1
            sol(cnt+1, i+1)
            learned[i] = 0

N, K = map(int, input().split())
words = [set(input()) for _ in range(N)]

# a, n, t, i, c 를 모르면 어떤 글자도 읽을 수 없다 
if K < 5: 
    print(0)
elif K == 26: 
    print(N)
else:
    learned = [0] * 26
    for ch in 'antic':
        learned[ord(ch)-97] = 1
    max_learned_words = 0
    
    sol(0, 0)
    print(max_learned_words)