def factorial(n):
    """
    Returns the factorial of a number using recursion.
    """
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


def sum_to(n):
    """
    Returns the sum of numbers from 1 to n using recursion.
    """
    if n == 1:
        return n
    return n + sum_to(n - 1)


def digit_count(n):
    """
    Returns the number of digits in a number using recursion.
    """
    if n < 9:
        return 1
    return 1 + digit_count(n // 10)


def sum_digits(n):
    """
    Returns the sum of all digits in a number using recursion.
    """
    if n < 10:
        return n 
    return n % 10 + sum_digits(n // 10)


def reverse_string(s):
    """
    Returns the reversed string using recursion.
    """
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


def sum_even_digits(n):
    """
    Returns the sum of even digits in a number using recursion.
    """
    sum = 0
    if n == 0:
        return 0
    
    digit = n % 10
    if digit % 2 == 0:
        sum = digit
    
    return sum + sum_even_digits(n // 10)


def power(base, exponent):
    """
    Returns the result of base raised to the power of exponent using recursion.
    """
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    return base * power(base, exponent - 1)


def is_palindrome(s):
    """
    Returns True if the string is a palindrome using recursion.
    """
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])



def count_occurrences(word, cha):
    """
    Returns the number of times a character appears in a string using recursion.
    """
    if len(word) == 0:
        return 0
    count = 0
    if cha == word[0]:
        count += 1
    return count + count_occurrences(word[1:], cha)


def max_digit(n):
    """
    Returns the largest digit in a number using recursion.
    """
    digit = n % 10
    if n < 10:
        return digit
    return max(digit, max_digit(n // 10))


def multiply(a, b):
    """
    Returns the product of two numbers using recursion.
    """
    if b == 0:
        return 0
    return a + multiply(a, b - 1)


def sum_list(lst):
    """
    Returns the sum of all elements in a list using recursion.
    """
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])


def max_in_list(lst):
    """
    Returns the maximum element in a list using recursion.
    """
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], max_in_list(lst[1:]))


def is_sorted(lst):
    """
    Returns True if the list is sorted in ascending order using recursion.
    """
    if len(lst) <= 1:
        return True
    if lst[0] > lst[1]:
        return False
    return is_sorted(lst[1:])


def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    """
    Returns the greatest common divisor (GCD) of two numbers using Euclid's algorithm.
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def decimal_to_binary(n):
    """
    Returns the binary representation of a decimal number using recursion.
    """
    if n == 0 or n == 1:
        return str(n)
    return decimal_to_binary(n // 2) + str(n % 2)


def sum_2d_array(matrix):
    """
    Returns the total sum of all elements in a 2D array using recursion.
    """
    if len(matrix) == 0:
        return 0
    return sum(matrix[0]) + sum_2d_array(matrix[1:])


def min_in_list(lst):
    """
    Returns the minimum element in a list using recursion.
    """
    if len(lst) == 1:
        return lst[0]
    return min(lst[0], min_in_list(lst[1:]))


def reverse_list(lst):
    """
    Returns the reversed list using recursion.
    """
    if len(lst) <= 1:
        return lst
    return reverse_list(lst[1:]) + [lst[0]]


def search_in_list(lst, n):
    """
    Returns True if the element exists in the list using recursion.
    """
    if len(lst) == 0:
        return False
    if lst[0] == n:
        return True
    return search_in_list(lst[1:], n)


def count_occurrences_in_list(lst, n):
    """
    Returns the number of times an element appears in a list using recursion.
    """
    if len(lst) == 0:
        return 0
    count = 0
    if lst[0] == n:
        count += 1
    return count + count_occurrences_in_list(lst[1:], n)


def remove_duplicates(lst):
    """
    Returns a new list with duplicates removed using recursion.
    """
    if len(lst) <= 1:
        return lst
    rest = remove_duplicates(lst[1:])
    if lst[0] in rest:
        return rest
    return [lst[0]] + rest


def is_substring(s, sub):
    """
    Returns True if 'sub' is a substring of 's' using recursion.
    """
    if len(sub) == 0:
        return True
    if len(s) < len(sub):
        return False
    if s[:len(sub)] == sub:
        return True
    return is_substring(s[1:], sub)




# print(is_substring("hello world", "ello"))  # True
# print(is_substring("hello world", "xyz"))    # False
# print(is_substring("test", "testing"))       # False

#################################################
# print(remove_duplicates([1, 2, 2, 3, 1, 4]))  # [1, 2, 3, 4]
# print(remove_duplicates([2, 2, 2]))           # [2]
# print(remove_duplicates([]))                  # []

#################################################3
# print(count_occurrences_in_list([1, 2, 1, 3, 1], 1))  # 3
# print(count_occurrences_in_list([2, 3, 4], 5))        # 0
# print(count_occurrences_in_list([2, 2, 2], 2))        # 3

###################################33

# print(search_in_list([1, 2, 3, 4], 3))  # True
# print(search_in_list([1, 2, 4], 5))     # False
# print(search_in_list([], 1))            # False

##################################
# print(reverse_list([1, 2, 3, 4]))  # [4, 3, 2, 1]
# print(reverse_list([1]))           # [1]
# print(reverse_list([]))            # []


##########################################3
# print(min_in_list([3, 1, 5, 2]))  # 1
# print(min_in_list([7]))           # 7
# print(min_in_list([4, 2, 9, 1]))  # 1    

#####################################
# print(f"sum_2d_array([[1, 2], [3, 4]]) = {sum_2d_array(
#     [
#     [1, 2],
#     [3, 4]
#     ])}")  # يجب أن تطبع 10

##################################
# print("اختبار decimal_to_binary:")
# print(f"decimal_to_binary(0) = {decimal_to_binary(0)}")    # يجب أن تطبع 0
# print(f"decimal_to_binary(1) = {decimal_to_binary(1)}")    # يجب أن تطبع 1
# print(f"decimal_to_binary(5) = {decimal_to_binary(5)}")    # يجب أن تطبع 101
# print(f"decimal_to_binary(10) = {decimal_to_binary(10)}")  # يجب أن تطبع 1010
# print(f"decimal_to_binary(42) = {decimal_to_binary(42)}")  # يجب أن تطبع 101010
    
#############################################################33
# print(f"gcd(48, 18) = {gcd(48, 18)}")  # يجب أن تطبع 6
# print(f"gcd(24, 36) = {gcd(24, 36)}")  # يجب أن تطبع 12
# print(f"gcd(17, 5) = {gcd(17, 5)}")    # يجب أن تطبع 1
# print(f"gcd(0, 5) = {gcd(0, 5)}")      # يجب أن تطبع 5
# print(f"gcd(5, 0) = {gcd(5, 0)}")      # يجب أن تطبع 5
    

#################################################
# print(fibonacci(0))  # 0
# print(fibonacci(1))  # 1
# print(fibonacci(5))  # 5
# print(fibonacci(6))  # 8

###############################################3


# print(is_sorted([1, 2, 3]))     # True
# print(is_sorted([1, 3, 2]))     # False

#####################################################
# print(max_in_list([3, 1, 5, 2]))  # 5

###############################################3 
# print(sum_list([1, 2, 3, 4]))  # 10
# print(sum_list([]))           # 0

##################################3
# print(multiply(3, 4))  # 12
# print(multiply(5, 0))  # 0
# print(multiply(7, 1))  # 7

   
############################33 
# print(max_digit(5273))   # 7
# print(max_digit(9001))   # 9
# print(max_digit(345))    # 5
# print(max_digit(8))      # 8
    
#################################3    

# print(factorial(0))  # 1
# print(factorial(1))  # 1
# print(factorial(3))  # 6
# print(factorial(5))  # 120
# print(factorial(7))  # 5040
##########################################

# print(sum_to(1))  # 1
# print(sum_to(3))  # 6
# print(sum_to(5))  # 15
# print(sum_to(10)) # 55

#####################################

# print(digit_count(7))   
# print(digit_count(42))    
# print(digit_count(12345))  


########################################
# print(sum_digits(0))       # 0
# print(sum_digits(7))       # 7
# print(sum_digits(49))      # 13
# print(sum_digits(123))     # 6
# print(sum_digits(9876))    # 30


##########################
# print(reverse_string("a"))          # "a"
# print(reverse_string("ab"))         # "ba"
# print(reverse_string("hello"))      # "olleh"
# print(reverse_string("recursion"))  # "noisrucer"


###############################
# print(sum_even_digits(123456))


#########################3
# print(power(2, 3))


########################
# print(is_palindrome("radar"))   # True
# print(is_palindrome("level"))   # True
# print(is_palindrome("hello"))   # False
# print(is_palindrome("a"))       # True
# print(is_palindrome(""))        # True


#################################
# print(count_occurrences("helllodo", "l"))


##################################





        
 
        
