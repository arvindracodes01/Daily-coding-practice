"""
Take input from the user and display the following:
Total number of characters
Total number of words
Sentence in uppercase
Sentence in lowercase
"""
sentence = input("Enter a sentence: ")
print(f"Total number of characters: {len(sentence)}")
print(f"Total number of words: {len(sentence.split())}")
print(f"Sentence in uppercase: {sentence.upper()}")
print(f"Sentence in lowercase: {sentence.lower()}")