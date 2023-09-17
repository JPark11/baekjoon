# BOJ 1181 단어정렬 

N = int(input())
words = [input() for _ in range(N)]
words = list(set(words))
words.sort(key=lambda x: (len(x), x))
for word in words:
    print(word)