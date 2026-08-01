"""
take a sentence input from user and print the following:
how many times 'a' appeared in the sentence.
how many times 'e' appeared in the sentence.
how many times 'i' appeared in the sentence.
how many times 'o' appeared in the sentence.
how many times 'u' appeared in the sentence.
"""

sentence = input("Enter a sentence: ")
count_a = sentence.count('a')
count_e = sentence.count('e')
count_i = sentence.count('i')
count_o = sentence.count('o')
count_u = sentence.count('u')

print(f"a in the sentence: {count_a}")
print(f"e in the sentence: {count_e}")
print(f"i in the sentence: {count_i}")
print(f"o in the sentence: {count_o}")
print(f"u in the sentence: {count_u}")