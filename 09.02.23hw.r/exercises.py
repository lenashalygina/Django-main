# скобочки
def is_balanced(string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False

            last_opening = stack.pop()
            if opening_brackets.index(last_opening) != closing_brackets.index(char):
                return False

    return len(stack) == 0


# пересечение
from collections import defaultdict


def intersection(nums1, nums2):
    count_dict = defaultdict(int)
    for num in nums1:
        count_dict[num] += 1

    intersection_list = []
    for num in nums2:
        if count_dict[num] > 0:
            intersection_list.append(num)
            count_dict[num] -= 1

    return intersection_list
