def are_anagrams(word1, word2):
    # Remove spaces and convert both words to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Check if the lengths of the two words are the same
    if len(word1) != len(word2):
        return False

    # Create dictionaries to store character frequencies
    char_count1 = {}
    char_count2 = {}

    # Count the frequencies of characters in the first word
    for char in word1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    # Count the frequencies of characters in the second word
    for char in word2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    # Compare the character frequencies of both words
    return char_count1 == char_count2

# # Example usage
# word1 = "tea"
# word2 = "eat"

# Input two words from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
result = are_anagrams(word1, word2)
if result:
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
