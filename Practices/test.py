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
# #
# #     return list(pairs)
# #
# # # Test
# # input_list = [1, 2, 3, 2, 4, 5, 0, -1, 4]
# # target_sum = 4
# #
# # result = find_pairs(input_list, target_sum)
# # print(result)
#
#
# # Problem:
#
# # Write a function that takes a sentence as input and
# # returns the longest word in the sentence.
# # If there are multiple words of the same maximum length, return the first one.
#
# def longest_word(sentence):
#     words = sentence.split()
#     max_word = ""
#
#     for word in words:
#         # Remove punctuation (optional, depending on the requirement)
#         clean_word = ''.join(char for char in word if char.isalnum())
#         if len(clean_word) > len(max_word):
#             max_word = clean_word
#
#     return max_word
#
#
# # Test
# sentence = "Artificial intelligence is revolutionizing the world"
# result = longest_word(sentence)
# print(result)


#  Problem Statement:
# Given an integer array nums,
# return all the triplets [nums[i], nums[j], nums[k]] such that:
#
# i != j, i != k, and j != k
#
# nums[i] + nums[j] + nums[k] == 0
#
# Note: The solution set must not contain duplicate triplets.

# def three_sum(nums):
#     nums.sort()
#     result = []
#
#     for i in range(len(nums)):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#
#         left, right = i + 1, len(nums) - 1
#
#         while left < right:
#             total = nums[i] + nums[left] + nums[right]
#
#             if total < 0:
#                 left += 1
#             elif total > 0:
#                 right -= 1
#             else:
#                 result.append([nums[i], nums[left], nums[right]])
#
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
#
#                 left += 1
#                 right -= 1
#
#     return result
#
# # Function call with output
# print(three_sum([-1, 0, 1, 2, -1, -4]))



#  Problem:
# Given two strings s1 and s2, return True if s2 contains a permutation of s1, or False otherwise.
#
# In other words, one of s1's permutations is a substring of s2.


from collections import Counter

def check_inclusion(s1, s2):
    len1, len2 = len(s1), len(s2)
    if len1 > len2:
        return False

    s1_count = Counter(s1)
    window_count = Counter(s2[:len1])

    if s1_count == window_count:
        return True

    for i in range(len1, len2):
        start_char = s2[i - len1]
        new_char = s2[i]

        window_count[new_char] += 1
        window_count[start_char] -= 1

        if window_count[start_char] == 0:
            del window_count[start_char]

        if window_count == s1_count:
            return True

    return False

#  Call the function and print the result
print(check_inclusion("ab", "eidbaooo"))  # Expected: True
print(check_inclusion("ab", "eidboaoo"))  # Expected: False
