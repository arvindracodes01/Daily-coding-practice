"""
Take input from the user and display the following:
replace python with java in the sentence.
print new sentence after replacing python with java.
"""
sentence = input("Enter a sentence: ")

if "python" in sentence.lower():
    new_sentence = sentence.replace("python", "Java")
    print(f"New sentence: {new_sentence}")
else:
    print("Python word not found.")