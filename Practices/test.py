# # Problem:
# # Write a Python function that takes a list of
# # integers and a target sum. The function should return
# # all unique pairs of numbers from the list that add up to the target sum.
#
# def find_pairs(nums, target):
#     seen = set()
#     pairs = set()
#
#     for num in nums:
#         complement = target - num
#         if complement in seen:
#             # Add pairs with smaller number first to avoid duplicates
#             pair = tuple(sorted((num, complement)))
#             pairs.add(pair)
#         seen.add(num)
#
#     return list(pairs)
#
# # Test
# input_list = [1, 2, 3, 2, 4, 5, 0, -1, 4]
# target_sum = 4
#
# result = find_pairs(input_list, target_sum)
# print(result)


# Problem:

# Write a function that takes a sentence as input and
# returns the longest word in the sentence.
# If there are multiple words of the same maximum length, return the first one.

def longest_word(sentence):
    words = sentence.split()
    max_word = ""

    for word in words:
        # Remove punctuation (optional, depending on the requirement)
        clean_word = ''.join(char for char in word if char.isalnum())
        if len(clean_word) > len(max_word):
            max_word = clean_word

    return max_word


# Test
sentence = "Artificial intelligence is revolutionizing the world"
result = longest_word(sentence)
print(result)
