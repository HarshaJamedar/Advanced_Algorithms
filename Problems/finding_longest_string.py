def longestStringChain(strings):
    # Sort the strings by length in ascending order
    strings.sort(key=lambda x: len(x))

    # Create a dictionary to store the chain length for each string
    chain_length = {}

    # Initialize the maximum chain length and the corresponding string
    max_chain_length = 0
    max_chain_string = ""

    # Iterate through the sorted list of strings
    for string in strings:
        chain_length[string] = 1

        # Try to form a longer chain by removing a character from the string
        for i in range(len(string)):
            current = string[:i] + string[i+1:]

            if current in chain_length and chain_length[current] + 1 > chain_length[string]:
                chain_length[string] = chain_length[current] + 1

        # Update the maximum chain length and corresponding string
        if chain_length[string] > max_chain_length:
            max_chain_length = chain_length[string]
            max_chain_string = string

    # Reconstruct the longest chain in descending order
    longest_chain = []
    current_length = max_chain_length
    current_string = max_chain_string

    while current_length > 0:
        longest_chain.append(current_string)
        current_length -= 1

        for i in range(len(current_string)):
            current = current_string[:i] + current_string[i+1:]

            if current in chain_length and chain_length[current] == current_length:
                current_string = current
                break

    return longest_chain

# Sample Input
strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

# Find and print the longest string chain
result = longestStringChain(strings)
print(result)
