def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def main():
    mySentence = input("Enter a sentence: ")
    num_vowels = count_vowels(mySentence)
    print("Number of vowels:", num_vowels)

main()
