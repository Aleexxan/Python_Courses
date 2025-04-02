# 1.

# numbers = [5, -3, 12, 0, -8, 7, -1, 4]
#
# new_list = []
# for i in numbers:
#     if i >= 0:
#         new_list.append(i)
#
# print(new_list)
# print(len(new_list))

# 2.

# words = ["apple", "banana", "cherry", "date", "kiwi"]
#
# word = input()
#
# if word in words:
#     print('You word index is ' + str(words.index(word)))
# else:
#     print('No such word')


# 3.

# a = [1, 2, 3]
# b = [4, 5, 6]
#
# new_list = []
#
# for i in a + b:
#     new_list.append(i * 2)
#
# print(new_list)

# 4.

# phrases = ["  Hello ", "world ", " PYTHON ", " is ", " GREAT "]
# new_list = []
#
# for i in phrases:
#     new_word = i.lower().strip()
#     new_list.append(new_word)
#
# print(new_list)

#5.

# students = [
#     ["Anna", 90],
#     ["Ben", 75],
#     ["Oleg", 88]
# ]
#
#
# students.sort(key=lambda L: L[1], reverse=True)
# print(students[0])

#6.


values = [3, 5, 3, 7, 9, 5, 3, 9, 10]

st = set(values)
new_list = list(st)

print(new_list)

12345