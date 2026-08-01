"""
take input from the user and

Check python is exists in the sentence.
if python is exists in the sentence, 
then print the index of python in the sentence.
if not exists, then print
 "python is not found in the sentence."
"""
sentence = input("Enter a sentence: ").lower()
if "python" in sentence:
    index = sentence.index("python")
    print(f"Index of 'python' : {index}")
else:
    print("python is not found in the sentence.")
