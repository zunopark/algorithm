import sys

words_num = int(sys.stdin.readline().strip())
li = []

for i in range(words_num):
    word = str(input())
    word_count = len(word)
    li.append((word, word_count))

#중복 삭제
words_list = list(set(li))
print(words_list)

#단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[1], word[0]))

print(words_list)