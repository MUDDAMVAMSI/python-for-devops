text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")


text = "Python is easy"
print("easy" in text)      # True if found
print("hard" not in text)  # True if not found
