'''
MISSING NUMBER
Write a function to find the missing number in a given integer array of 1 to n. 
The function takes to parameter the array and the number of elements that needs to be in array.  
For example if we want to find missing number from 1 to 6 the second parameter will be 6. The array might not be sorted!
Note: There are no duplicates in the list.
'''

def missing_number(arr:list, n:int) -> int:
    pass

# Example
print(missing_number([6, 1, 2, 3, 4], 6))  # Output: 5
print(missing_number([1, 3, 4, 5, 6, 7, 8], 8))  # Output: 2


'''
TWO SUM
Given an array of integers nums and an integer target, return the indices of the two numbers that add up to the target.
Each input would have exactly one solution, and you may not use the same element twice.
'''

def two_sum(nums:list, target:int) -> list:
    pass

# Example
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}") #Output: 0, 1 (Index 0 is 2 and index 1 is 7)


'''
MAX PRODUCT

Find the maximum product of two integers in an array where all elements are positive.
'''
def max_product(arr:list) -> int:
    pass

#Example
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)


'''
REMOVE DUPLICATES:
Write a function to remove the duplicate numbers on given integer array/list.
'''
def remove_duplicates(lst: list) -> list:
    pass

#Example
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]


'''
PAIR_SUM: Write a function to find all pairs of an integer array whose sum is equal to a given number.
Do not consider commutative pairs.
'''
def pair_sum(arr:list, target_sum: int) -> list:
    pass

#Example
arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
print(pair_sum(arr, target_sum))  # Output: ['2+5', '4+3', '3+4', '-2+9']


'''
CONTAINS_DUPLICATE:

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

    Input: nums = [1,2,3,1]
    Output: True

'''

def contains_duplicates(nums:list) -> bool:
    pass

# Example
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(contains_duplicates(nums))  # Output: True


#ROTATE_MATRIX
'''
Rotate Matrix/ Image - LeetCode 48

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.

This envolves transpose the matrix and then reverse each row


Example:

'''
def rotate(matrix:list[list]) -> list[list]:
    pass

# Example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix) #-> [[7,4,1],[8,5,2],[9,6,3]]


# Largest Sum Contiguous Subarray

'''
Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum.
'''

def largest_sum_contiguous_sub_array(a:list, size:int):
    pass

# Example
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is", largest_sum_contiguous_sub_array(a, len(a)))


"""
FIND SINGULAR NUMBERS
Write a function called find_singular_nums that identifies and returns the indices of "singular numbers" in a list of integers.
A "singular number" is an element in a vector whose value is equal to the arithmetic mean of all previous elements in the vector. 
The first element of the vector cannot be singular since there are no previous elements to compute the average.
"""
def find_singular_nums(vec: list[int]) -> list[int]:
    pass

# Example
print("Singular values ", find_singular_nums([8, 9, 4, 7, 20, 10, 5, 9, 2])) #Ouput 3 and 7. Index 3 contains a 7 ((8+9+4/3) = 7). Index 7 contains 9 ((8+9+4+7+20+10+5/7=9)) 