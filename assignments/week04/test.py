name = input("What is your name?: ")
 
vowels = 0
 
for letter in name:
    print(f"ตัวอักษร : {letter}")
 
    if letter == 'a' or letter == 'A':
        vowels = vowels + 1
 
    if letter == 'e' or letter == 'E':
        vowels = vowels + 1
 
print("Your name have", vowels, "vowels")