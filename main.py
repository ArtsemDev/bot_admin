# # n = int(input())
# # lst = [2**i for i in range(1, n + 1)]
# # print(lst)
#
# data = {i: i**2 for i in range(1, 11)}
# # print(data)
# from collections import Counter
#
# text = input()
# # res = Counter(text)
# # print(res)
# res = {letter: text.count(letter) for letter in text}
# print(res)

# text = input()
# first_space = text.find(' ')
# second_space = text.rfind(' ')
# first_word = text[:first_space]
# second_word = text[first_space+1:second_space]
# third_word = text[second_space+1:]
# print(first_word)
# print(second_word)
# print(third_word)


import collections
n = int(input())
name = input('name ')
mail = input('mail ')
dict_1 = {name, mail}
defdict = collections.defaultdict(list)
for i in range(0, n):
    defdict[i].append(dict_1)
print(defdict)