# # # # Problem:
# # # # Write a Python function that takes a list of
# # # # integers and a target sum. The function should return
# # # # all unique pairs of numbers from the list that add up to the target sum.
# # #
# # # def find_pairs(nums, target):
# # #     seen = set()
# # #     pairs = set()
# # #
# # #     for num in nums:
# # #         complement = target - num
# # #         if complement in seen:
# # #             # Add pairs with smaller number first to avoid duplicates
# # #             pair = tuple(sorted((num, complement)))
# # #             pairs.add(pair)
# # #         seen.add(num)
# # # #
# # # #     return list(pairs)
# # # #
# # # # # Test
# # # # input_list = [1, 2, 3, 2, 4, 5, 0, -1, 4]
# # # # target_sum = 4
# # # #
# # # # result = find_pairs(input_list, target_sum)
# # # # print(result)
# # #
# # #
# # # # Problem:
# # #
# # # # Write a function that takes a sentence as input and
# # # # returns the longest word in the sentence.
# # # # If there are multiple words of the same maximum length, return the first one.
# # #
# # # def longest_word(sentence):
# # #     words = sentence.split()
# # #     max_word = ""
# # #
# # #     for word in words:
# # #         # Remove punctuation (optional, depending on the requirement)
# # #         clean_word = ''.join(char for char in word if char.isalnum())
# # #         if len(clean_word) > len(max_word):
# # #             max_word = clean_word
# # #
# # #     return max_word
# # #
# # #
# # # # Test
# # # sentence = "Artificial intelligence is revolutionizing the world"
# # # result = longest_word(sentence)
# # # print(result)
# #
# #
# # #  Problem Statement:
# # # Given an integer array nums,
# # # return all the triplets [nums[i], nums[j], nums[k]] such that:
# # #
# # # i != j, i != k, and j != k
# # #
# # # nums[i] + nums[j] + nums[k] == 0
# # #
# # # Note: The solution set must not contain duplicate triplets.
# #
# # # def three_sum(nums):
# # #     nums.sort()
# # #     result = []
# # #
# # #     for i in range(len(nums)):
# # #         if i > 0 and nums[i] == nums[i - 1]:
# # #             continue
# # #
# # #         left, right = i + 1, len(nums) - 1
# # #
# # #         while left < right:
# # #             total = nums[i] + nums[left] + nums[right]
# # #
# # #             if total < 0:
# # #                 left += 1
# # #             elif total > 0:
# # #                 right -= 1
# # #             else:
# # #                 result.append([nums[i], nums[left], nums[right]])
# # #
# # #                 while left < right and nums[left] == nums[left + 1]:
# # #                     left += 1
# # #                 while left < right and nums[right] == nums[right - 1]:
# # #                     right -= 1
# # #
# # #                 left += 1
# # #                 right -= 1
# # #
# # #     return result
# # #
# # # # Function call with output
# # # print(three_sum([-1, 0, 1, 2, -1, -4]))
# #
# #
# #
# # #  Problem:
# # # Given two strings s1 and s2, return True if s2 contains a permutation of s1, or False otherwise.
# # #
# # # In other words, one of s1's permutations is a substring of s2.
# #
# #
# # from collections import Counter
# #
# # def check_inclusion(s1, s2):
# #     len1, len2 = len(s1), len(s2)
# #     if len1 > len2:
# #         return False
# #
# #     s1_count = Counter(s1)
# #     window_count = Counter(s2[:len1])
# #
# #     if s1_count == window_count:
# #         return True
# #
# #     for i in range(len1, len2):
# #         start_char = s2[i - len1]
# #         new_char = s2[i]
# #
# #         window_count[new_char] += 1
# #         window_count[start_char] -= 1
# #
# #         if window_count[start_char] == 0:
# #             del window_count[start_char]
# #
# #         if window_count == s1_count:
# #             return True
# #
# #     return False
# #
# # #  Call the function and print the result
# # print(check_inclusion("ab", "eidbaooo"))  # Expected: True
# # # print(check_inclusion("ab", "eidboaoo"))  # Expected: False
# # Problem:
# # Given an array arr and an integer target, count the number of subarrays whose XOR is equal to targe
#
# def count_subarrays_with_xor(arr, target):
#     count = 0
#     xor_map = {0: 1}
#     xor = 0
#     for num in arr:
#         xor ^= num
#         count += xor_map.get(xor ^ target, 0)
#         xor_map[xor] = xor_map.get(xor, 0) + 1
#     return count
#
# # Add this to see output:
# if __name__ == "__main__":
#     result = count_subarrays_with_xor([4, 2, 2, 6, 4], 6)
#     print("Subarrays with XOR 6:", result)

# problem: Group Anagrams
#
# def group_anagrams(strs):
#     from collections import defaultdict
#     anagram_map = defaultdict(list)
#
#     for s in strs:
#         key = tuple(sorted(s))
#         print(f"Processing word: '{s}' -> key: {key}")
#         anagram_map[key].append(s)
#         print(f"Current anagram groups: {dict(anagram_map)}")
#
#     result = list(anagram_map.values())
#     print(f"Final grouped anagrams: {result}")
#     return result

# problem : spiral traversal output
#
# def spiral_order(matrix):
#     res = []
#     while matrix:
#         # Take and remove the first row
#         res += matrix.pop(0)
#
#         # Take the last element of each remaining row
#         if matrix and matrix[0]:
#             for row in matrix:
#                 res.append(row.pop())
#
#         # Take and remove the last row in reverse order
#         if matrix:
#             res += matrix.pop()[::-1]
#
#         # Take the first element of each remaining row, bottom to top
#         if matrix and matrix[0]:
#             for row in matrix[::-1]:
#                 res.append(row.pop(0))
#     return res
#
# if __name__ == "__main__":
#     matrix = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
#     result = spiral_order(matrix)
#     print("Spiral order traversal:", result)

# Given a string s containing just the
# characters ()[]{}, determine if the input is valid.
# def is_valid_parentheses(s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}
#     for char in s:
#         if char in mapping.values():
#             stack.append(char)
#         elif char in mapping:
#             if not stack or stack.pop() != mapping[char]:
#                 return False
#     return not stack
#
# print("Valid Parentheses:", is_valid_parentheses("({[]})"))  # True
#

#Given an array of size n, find the majority element (appears more than n/2 times).
# def majority_element(nums):
#     count = 0
#     candidate = None
#     for num in nums:
#         if count == 0:
#             candidate = num
#         count += (1 if num == candidate else -1)
#     return candidate
#
# print("Majority Element:", majority_element([2,2,1,1,1,2,2]))  # 2


# A peak element is one that is greater than its neighbors. Return the index of any pe

# def find_peak_element(nums):
#     left, right = 0, len(nums) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] < nums[mid + 1]:
#             left = mid + 1
#         else:
#             right = mid
#     return left
#
# print("Peak Element Index:", find_peak_element([1, 2, 3, 1]))  # 2
# Top K Frequent Elements
# from collections import Counter
#
# def top_k_frequent(nums, k):
#     count = Counter(nums)
#     return [item for item, freq in count.most_common(k)]
#
# print("Top K Frequent:", top_k_frequent([1,1,1,2,2,3], 2))  # [1, 2]

# Rotate Matrix (90 degrees)
# def rotate(matrix):
#     return [list(row)[::-1] for row in zip(*matrix)]
#
# print("Rotated Matrix:", rotate([[1,2,3],[4,5,6],[7,8,9]]))

# Longest Substring Without Repeating Characters

# def length_of_longest_substring(s):
#     char_index = {}
#     left = max_len = 0
#     for right, char in enumerate(s):
#         if char in char_index and char_index[char] >= left:
#             left = char_index[char] + 1
#         char_index[char] = right
#         max_len = max(max_len, right - left + 1)
#     return max_len
#
# print("Longest Substring:", length_of_longest_substring("abcabcbb"))  # 3
#

# Climbing Stairs
# def climb_stairs(n):
#     a, b = 1, 1
#     for _ in range(n-1):
#         a, b = b, a + b
#     return b
#
# print("Climb Stairs (n=5):", climb_stairs(5))  # 8


# Isomorphic Strings

# def is_isomorphic(s, t):
#     mapping_s_t = {}
#     mapping_t_s = {}
#     for a, b in zip(s, t):
#         if mapping_s_t.get(a, b) != b or mapping_t_s.get(b, a) != a:
#             return False
#         mapping_s_t[a] = b
#         mapping_t_s[b] = a
#     return True
#
# print("Isomorphic:", is_isomorphic("egg", "add"))  # True

#
# def knapsack(n, capacity, weights, profits):
#     # Create DP table
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
#
#     # Fill DP table
#     for i in range(1, n + 1):
#         for w in range(capacity + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
#             else:
#                 dp[i][w] = dp[i - 1][w]
#
#     # Find selected items
#     selected_items = []
#     w = capacity
#     for i in range(n, 0, -1):
#         if dp[i][w] != dp[i - 1][w]:
#             selected_items.append(i - 1)
#             w -= weights[i - 1]
#
#     return dp[n][capacity], selected_items
#
#
# def main():
#     # Get input from user
#     n = int(input("Enter the number of items: "))
#     capacity = int(input("Enter the knapsack capacity: "))
#
#     weights = []
#     profits = []
#     print("Enter weight and profit for each item:")
#     for i in range(n):
#         w, p = map(int, input(f"Item {i + 1} (weight profit): ").split())
#         weights.append(w)
#         profits.append(p)
#
#     # Solve knapsack problem
#     max_profit, selected = knapsack(n, capacity, weights, profits)
#
#     # Display results
#     print("\nMaximum profit:", max_profit)
#     print("Selected items (index, weight, profit):")
#     for idx in reversed(selected):  # Reverse to show items in ascending order
#         print(f"Item {idx + 1}: weight = {weights[idx]}, profit = {profits[idx]}")
#
#
# if __name__ == "__main__":
#     main()


# 0/1 Knapsack Problem Solver
#
# def knapsack_01():
#     print("""
#     Solves the 0/1 Knapsack Problem using dynamic programming.
#     Calculates and displays the maximum achievable profit and the set of selected items.
#     """)
#
#     while True:
#         try:
#             num_items = int(input("Enter the number of items: "))
#             if num_items <= 0:
#                 print("Number of items must be positive. Please try again.")
#             else:
#                 break
#         except ValueError:
#             print("Invalid input. Please enter an integer.")
#
#     weights = []
#     profits = []
#
#     for i in range(num_items):
#         while True:
#             try:
#                 weight = int(input(f"Enter weight for item {i+1}: "))
#                 if weight <= 0:
#                     print("Weight must be positive. Please try again.")
#                 else:
#                     weights.append(weight)
#                     break
#             except ValueError:
#                 print("Invalid input. Please enter an integer.")
#
#         while True:
#             try:
#                 profit = int(input(f"Enter profit for item {i+1}: "))
#                 if profit < 0:
#                     print("Profit cannot be negative. Please try again.")
#                 else:
#                     profits.append(profit)
#                     break
#             except ValueError:
#                 print("Invalid input. Please enter an integer.")
#
#     while True:
#         try:
#             capacity = int(input("Enter the knapsack capacity: "))
#             if capacity <= 0:
#                 print("Capacity must be positive. Please try again.")
#             else:
#                 break
#         except ValueError:
#             print("Invalid input. Please enter an integer.")
#
#     dp_table = [[0 for _ in range(capacity + 1)] for _ in range(num_items + 1)]
#
#     for i in range(1, num_items + 1):
#         for w in range(1, capacity + 1):
#             if weights[i-1] <= w:
#                 include_item_profit = profits[i-1] + dp_table[i-1][w - weights[i-1]]
#                 exclude_item_profit = dp_table[i-1][w]
#                 dp_table[i][w] = max(include_item_profit, exclude_item_profit)
#             else:
#                 dp_table[i][w] = dp_table[i-1][w]
#
#     max_profit = dp_table[num_items][capacity]
#
#     selected_items = []
#     i = num_items
#     w = capacity
#     while i > 0 and w > 0:
#         if dp_table[i][w] != dp_table[i-1][w]:
#             selected_items.append(f"Item {i} (Weight: {weights[i-1]}, Profit: {profits[i-1]})")
#             w -= weights[i-1]
#         i -= 1
#
#     selected_items.reverse()
#
#     print(f"\nMaximum achievable profit: {max_profit}")
#     if selected_items:
#         print("Selected items:")
#         for item in selected_items:
#             print(f"- {item}")
#     else:
#         print("No items were selected.")
#
# if __name__ == "__main__":
#     knapsack_01()

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that:
# def threeSum(nums):
#     nums.sort()
#     res = []
#
#     for i in range(len(nums) - 2):
#         # Skip duplicates
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#
#         left, right = i + 1, len(nums) - 1
#
#         while left < right:
#             s = nums[i] + nums[left] + nums[right]
#
#             if s < 0:
#                 left += 1
#             elif s > 0:
#                 right -= 1
#             else:
#                 res.append([nums[i], nums[left], nums[right]])
#
#                 # Skip duplicates
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
#
#                 left += 1
#                 right -= 1
#
#     return res
#
# # Now this is outside the function
# print(threeSum([-1, 0, 1, 2, -1, -4]))

# Given a string s, find the length of the longest substring without repeating characters.


# def lengthOfLongestSubstring(s):
#     char_set = set()
#     left = 0
#     max_len = 0
#
#     for right in range(len(s)):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#
#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)
#
#     return max_len
#
# # Example test
# print(lengthOfLongestSubstring("abcabcbb"))
#

# 7. Course Schedule
# from typing import List
# from collections import defaultdict, deque
#
# def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
#     graph = defaultdict(list)
#     indegree = [0] * numCourses
#     for dest, src in prerequisites:
#         graph[src].append(dest)
#         indegree[dest] += 1
#
#     queue = deque([i for i in range(numCourses) if indegree[i] == 0])
#     visited = 0
#
#     while queue:
#         node = queue.popleft()
#         visited += 1
#         for neighbor in graph[node]:
#             indegree[neighbor] -= 1
#             if indegree[neighbor] == 0:
#                 queue.append(neighbor)
#
#     return visited == numCourses
#
# print("7. Can Finish Courses:", canFinish(2, [[1, 0]]))


# 9. Word Break
# from typing import List
#
# def wordBreak(s: str, wordDict: List[str]) -> bool:
#     word_set = set(wordDict)
#     dp = [False] * (len(s) + 1)
#     dp[0] = True  # base case: empty string can be segmented
#
#     for i in range(1, len(s) + 1):
#         for j in range(i):
#             if dp[j] and s[j:i] in word_set:
#                 dp[i] = True
#                 break
#
#     return dp[-1]
#
# print("9. Word Break:", wordBreak("leetcode", ["leet", "code"]))

# 8. Subarray Sum Equals K
# from typing import List
# from collections import defaultdict
#
# def subarraySum(nums: List[int], k: int) -> int:
#     count = 0
#     curr_sum = 0
#     prefix_sums = defaultdict(int)
#     prefix_sums[0] = 1
#     for num in nums:
#         curr_sum += num
#         count += prefix_sums.get(curr_sum - k, 0)
#         prefix_sums[curr_sum] += 1
#     return count
#
# # Example usage
# print("8. Subarray Sum Equals K:", subarraySum([1, 2, 3], 3))  # Output should be 2


# Helper to print linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
#     dummy = ListNode()
#     current = dummy
#     carry = 0
#
#     while l1 or l2 or carry:
#         val1 = l1.val if l1 else 0
#         val2 = l2.val if l2 else 0
#
#         total = val1 + val2 + carry
#         carry = total // 10
#         current.next = ListNode(total % 10)
#
#         current = current.next
#         if l1: l1 = l1.next
#         if l2: l2 = l2.next
#
#     return dummy.next
#
# def print_linked_list(node):
#     res = []
#     while node:
#         res.append(node.val)
#         node = node.next
#     return res
#
# # Test
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
# print("3. Add Two Numbers:", print_linked_list(addTwoNumbers(l1, l2)))  # Output: [7, 0, 8]

# 1. 3Sum
# from typing import List
#
#
# def threeSum(nums: List[int]) -> List[List[int]]:
#     nums.sort()
#     res = []
#     for i in range(len(nums) - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         left, right = i + 1, len(nums) - 1
#         while left < right:
#             s = nums[i] + nums[left] + nums[right]
#             if s < 0:
#                 left += 1
#             elif s > 0:
#                 right -= 1
#             else:
#                 res.append([nums[i], nums[left], nums[right]])
#                 while left < right and nums[left] == nums[left + 1]:
#                     left += 1
#                 while left < right and nums[right] == nums[right - 1]:
#                     right -= 1
#                 left += 1
#                 right -= 1
#     return res
#
#
# print("1. 3Sum:", threeSum([-1, 0, 1, 2, -1, -4]))

# from typing import List
#
# def spiralOrder(matrix: List[List[int]]) -> List[int]:
#     res = []
#     while matrix:
#         res += matrix.pop(0)
#         if matrix and matrix[0]:
#             for row in matrix:
#                 res.append(row.pop())
#         if matrix:
#             res += matrix.pop()[::-1]
#         if matrix and matrix[0]:
#             for row in matrix[::-1]:
#                 res.append(row.pop(0))
#     return res
#
# print("1. Spiral Matrix:", spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# from typing import List
# def canJump(nums: List[int]) -> bool:
#     max_reach = 0
#     for i, num in enumerate(nums):
#         if i > max_reach:
#             return False
#         max_reach = max(max_reach, i + num)
#     return True
#
# print("5. Jump Game:", canJump([2,3,1,1,4]))

# def numDecodings(s: str) -> int:
#     if not s or s[0] == '0':
#         return 0
#     dp = [1, 1]
#     for i in range(1, len(s)):
#         count = 0
#         if s[i] != '0':
#             count += dp[-1]
#         if 10 <= int(s[i-1:i+1]) <= 26:
#             count += dp[-2]
#         dp.append(count)
#     return dp[-1]
#
# print("4. Decode Ways:", numDecodings("226"))
# from typing import List
# def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
#     result = []
#
#     def backtrack(remaining, combo, start):
#         if remaining == 0:
#             result.append(list(combo))
#             return
#         elif remaining < 0:
#             return
#         for i in range(start, len(candidates)):
#             combo.append(candidates[i])
#             backtrack(remaining - candidates[i], combo, i)
#             combo.pop()
#
#     backtrack(target, [], 0)
#     return result
#
# print("Combination Sum:", combinationSum([2, 3, 6, 7], 7))

# from typing import List
# def permute(nums: List[int]) -> List[List[int]]:
#     result = []
#
#     def backtrack(start):
#         if start == len(nums):
#             result.append(nums[:])
#             return
#         for i in range(start, len(nums)):
#             nums[start], nums[i] = nums[i], nums[start]
#             backtrack(start + 1)
#             nums[start], nums[i] = nums[i], nums[start]
#
#     backtrack(0)
#     return result
#
# print("Permutations:", permute([1, 2, 3]))


# def find_maximum(a, b, c):
#     print(f"Comparing values: {a}, {b}, {c}")
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
#
# # Example
# print("Maximum is:", find_maximum(3, 7, 5))

#
# def is_palindrome_number(num):
#     print(f"Checking if {num} is a palindrome.")
#     original = str(num)
#     reversed_num = original[::-1]
#     print(f"Original: {original}, Reversed: {reversed_num}")
#
#     if original == reversed_num:
#         return True
#     else:
#         return False
#
#
# # Example usage
# number = 12321
# if is_palindrome_number(number):
#     print(f"{number} is a palindrome.")
# else:
#     print(f"{number} is not a palindrome.")


# def count_vowels(text):
#     print(f"Input text: '{text}'")
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#             print(f"Found vowel: {char}")
#     return count
#
# # Example usage
# text = "Hello, Python is Awesome!"
# print(f"Vowel count: {count_vowels(text)}")

# def convert_seconds(seconds):
#     print(f"Total seconds: {seconds}")
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     remaining_seconds = seconds % 60
#     print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {remaining_seconds}")
#     return f"{hours:02}:{minutes:02}:{remaining_seconds:02}"
#
# # Example usage
# seconds_input = 3665
# print(f"Time: {convert_seconds(seconds_input)}")

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# # Example usage
# num = 29
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


# def reverse_words(sentence):
#     words = sentence.split()
#     reversed_sentence = " ".join(reversed(words))
#     return reversed_sentence
#
# # Example usage
# text = "Python is fun"
# print(reverse_words(text))

# def remove_duplicates(lst):
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result
#
# # Example usage
# nums = [1, 2, 2, 3, 4, 3, 5]
# print(remove_duplicates(nums))

# def fibonacci(n):
#     sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence
#
# # Example usage
# print(fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8]


def find_divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]

# Example usage
print(find_divisors(12))  # [1, 2, 3, 4, 6, 12]
