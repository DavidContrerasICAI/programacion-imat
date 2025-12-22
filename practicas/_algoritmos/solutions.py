'''
MISSING NUMBER
Write a function to find the missing number in a given integer array of 1 to n. 
The function takes to parameter the array and the number of elements that needs to be in array.  
For example if we want to find missing number from 1 to 6 the second parameter will be 6. The array might not be sorted!
Note: There are no duplicates in the list.
'''

#BEST SOLUTION:
def missing_number(arr:list, n:int) -> int:
    total = n * (n + 1) // 2
    
    sum_arr = sum(arr)
    
    missing = total - sum_arr
    
    return missing

#NOT SO GOOD SOLUTION:
def missing_number_less_efficient(arr:list, n:int) -> int:
    correct_sum = 0
    our_sum = 0
    for i in range(len(arr)):
        correct_sum += i + 1
        our_sum += arr[i]
    correct_sum += n

    return correct_sum - our_sum

    
# Example
print(missing_number([6, 1, 2, 3, 4], 6))  # Output: 5
print(missing_number([1, 3, 4, 5, 6, 7, 8], 8))  # Output: 2
print(missing_number_less_efficient([1, 3, 4, 5, 6, 7, 8], 8))  # Output: 2
print(missing_number_less_efficient([6, 1, 2, 3, 4], 6))  # Output: 5



'''
TWO SUM
Given an array of integers nums and an integer target, return the indices of the two numbers that add up to the target.
Each input would have exactly one solution, and you may not use the same element twice.
'''

#INNEFICIENT SOLUTION:
def two_sum_less_efficient(nums:list, target:int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

#MORE OPTIMAL SOLUTION:
def two_sum(nums:list, target:int) -> list:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []
    
nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
indices2 = two_sum_less_efficient(nums, target)
print(f"Indices of the two numbers are: {indices}")
print(f"Indices of the two numbers are: {indices2}")


'''
MAX PRODUCT

Find the maximum product of two integers in an array where all elements are positive.
'''

#SOLUTION:
def max_product(arr:list) -> int:
    max1, max2 = 0, 0  
    
    for num in arr:
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  
            max2 = max1  
            max1 = num  
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  
            max2 = num  
    
    return max1 * max2  #
    
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)


'''
REMOVE DUPLICATES:
Write a function to remove the duplicate numbers on given integer array/list.
'''

# SOLUTION
def remove_duplicates(lst: list) -> list:
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst
    
my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]


'''
PAIR_SUM: Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs. 
'''
# SOLUTION
def pair_sum(arr: list, target_sum: int) -> list:
    result = []
    seen = set()  

    for elem in arr:
        elem2 = target_sum - elem
        if elem2 in seen:
            result.append(f"{elem2}+{elem}")
        seen.add(elem)  

    return result

# SOLUTION (not so efficient)
def pair_sum_less_efficient(arr:list, target_sum: int) -> list:
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result


arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
print(pair_sum(arr, target_sum))  
print(pair_sum_less_efficient(arr, target_sum)) # Output: ['2+5', '4+3', '3+4', '-2+9']

'''
CONTAINS_DUPLICATE:

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

    Input: nums = [1,2,3,1]
    Output: true

Hint: Use sets
'''

#SOLUTION:
def contains_duplicates(nums:list) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
    
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

'''
def rotate(matrix:list[list]) -> list[list]:
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row

# Example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix) #-> [[7,4,1],[8,5,2],[9,6,3]]

'''
Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum.
'''
def largest_sum_contiguous_sub_array(a:list, size:int):
    # MAIN IDEA: for each element, store de maximum sum among all the subarrays until that element. For each element, we have 2 choices:
    # CHOICE 1: add the current element (extend the array) and see if the maximum is > 0. If it is, add it (we extend the array),
    # CHOICE 2: start a new array from the current element. If the maximum subarray sum ending in the preovious element. It is better to start a new one.
    
    res = a[0]
    max_ending_here = a[0]

    for i in range(1, size):

        max_ending_here = max(max_ending_here + a[i], a[i])
        
        res = max(res, max_ending_here)
    
    return res

def largest_sum_contiguous_sub_array_v2(a:list, size:int):
    max_so_far = a[0] 
    max_ending_here = a[0]
    # Same idea as before. Max so far will contain the best sum. Max_ending here, the maximum until element n.
    # An array with negative sum is always better to start in the next position

    for i in range(1, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

def largest_sum_contiguous_sub_array_less_efficient(a:list, size:int):
    res = a[0]
  
    # Considering from i, to the rest
    for i in range(size):
        current_sum = 0
      
        # Considering each element from i in that iteraction
        for j in range(i, size):
            current_sum = current_sum + a[j]
          
            res = max(res, current_sum)
          
    return res



# Example
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is", largest_sum_contiguous_sub_array(a, len(a)))
print("Maximum contiguous sum is", largest_sum_contiguous_sub_array_v2(a, len(a)))
print("Maximum contiguous sum is", largest_sum_contiguous_sub_array_less_efficient(a, len(a)))


"""
FIND SINGULAR NUMBERS
Write a function called find_singular_nums that identifies and returns the indices of "singular numbers" in a list of integers.
A "singular number" is an element in a vector whose value is equal to the arithmetic mean of all previous elements in the vector. 
The first element of the vector cannot be singular since there are no previous elements to compute the average.
"""


def find_singular_nums(vec: list[int]) -> list[int]:
    singular = []
    for k in range(1, len(vec)):
        if vec[k] == sum(vec[:k]) / k:
            singular.append(k)
    return singular

print("Singular values ", find_singular_nums([8, 9, 4, 7, 20, 10, 5, 9, 2])) #Ouput 3 and 7. Index 3 contains a 7 ((8+9+4/3) = 7). Index 7 contains 9 ((8+9+4+7+20+10+5/7=9)) 