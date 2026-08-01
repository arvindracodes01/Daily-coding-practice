"""
take the input from the user and display the following:
Total number of characters
Total number of words
first word in the sentence
last word in the sentence
reverse the sentence
is sentence start with python
is sentence end with programming
"""
sentence = input("Enter a sentence: ")
print(f"Total characters: {len(sentence)}")
print(f"Total words: {len(sentence.split())}")
print(f"First word: {sentence.split()[0]}")
print(f"Last word: {sentence.split()[-1]}")
print(f"Reversed sentence: {sentence[::-1]}")
print(f"Starts with 'python': {sentence.startswith('python')}")
print(f"Ends with 'programming': {sentence.endswith('programming')}")