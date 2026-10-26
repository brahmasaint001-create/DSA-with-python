letter = str(input("Enter the letter : "))
vowels = "aeiouAEIOU"
vowel_count = 0
index = 0
while index < len(letter):
    if letter[index] in vowels:
        vowel_count += 1
    index += 1
print("No of vowels = ", vowel_count)