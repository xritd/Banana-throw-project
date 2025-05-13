def fizz_buzz1(n: int) -> None:
    for k in range(1, n+1):
        if (k % 3 == 0) and (k % 5 == 0):
            print("FizzBuzz")
        elif (k % 3 == 0):
            print("Fizz")
        elif (k % 5 == 0):
            print("Buzz")
        else:
            print(k)

def fizz_buzz(n: int):
    '''
    Returns a list of strings from 1 to n, where
    multiples of 3 are replaced with "Fizz", 
    multiples of 5 with "Buzz", and 
    multiples of both 3 and 5 with "FizzBuzz".
    '''
    if n < 1:
        return []
    n_lst = [None]*n
    for k in range(1, n+1):
        if (k % 3 == 0) and (k % 5 == 0):
            n_lst[k-1] = 'FizzBuzz'
        elif k % 3 == 0:
            n_lst[k-1] = 'Fizz'
        elif k % 5 == 0:
            n_lst[k-1] = 'Buzz'
        else:
            n_lst[k-1] = f'{k}'
    return n_lst

# fizz_buzz(15) 
# fizz_buzz(0)

# fizz_buzz1(15)

def is_palindrome(s: str) -> bool:
    '''
    Cleans a string by removing whitespace and punctuation, 
    converts it to lower-case only and compares it to its 
    inverse.
    '''
    s = ''.join(filter(str.isalnum, s.lower()))
    return s == s[::-1]

# my_str = "Hello World"
# my_str2 = "Racecar"
# is_palindrome(my_str)
# is_palindrome(my_str2)

def count_vowels(s: str) -> int:
    '''
    Returns the number of vowels in a string.
    '''
    vowel_lst = {"a", "e", "i", "o", "u"}
    vowel_count = 0
    s = s.lower()
    for char in s:
        if char in vowel_lst:
            vowel_count += 1
    return vowel_count

# count_vowels("")
# count_vowels("Bababooey")

def sum_of_evens(lst):
    '''
    Returns sum of all even integers in the list.
    '''
    return sum(filter(lambda num: num % 2 == 0, lst))

# sum_of_evens([]) # Output: 0
# sum_of_evens([1, 2, 3, 4, 5, 6, 7, 8, 9]) # Output: 20

def are_anagrams(a, b):
    '''
    Compares two strings, ignoring whitespace and punctuation
    as well as being case-insensitive, to see if they are 
    anagrams.
    '''
    # Clean the two strings
    a = ''.join(filter(str.isalnum, a.lower()))
    b = ''.join(filter(str.isalnum, b.lower()))
    
    # Create dictionaries for each string 
    a_dict = {u : 0 for u in a}
    b_dict = {v : 0 for v in b}
    
    # Calculate number of occurrences of each character in each string
    for char in a:
        a_dict[char] += 1
    for char in b:
        b_dict[char] += 1

    return a_dict == b_dict

# print(are_anagrams("listen", "silent"))  # Output: True
# print(are_anagrams("hello", "world"))    # Output: False
# print(are_anagrams("Astronomer", "Moon starer"))  # Output: True
# print(are_anagrams("The eyes", "They see"))  # Output: True
# print(are_anagrams("Test", "")) # Output: False
# print(are_anagrams("", "")) # Output: True

def fibonacci1(n: int) -> list:
    '''
    Returns a list of the first n Fibonacci numbers,
    starting with 0 and 1.
    '''
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_list = [0, 1]
    for k in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    return fib_list

def has_unique_characters(s: str):
    s = ''.join(filter(str.isalnum, s))
    
    seen = set()
    
    for char in s:
        if char in seen:
            return False
        seen.add(char)
        
    return True

has_unique_characters("Hello World") # Output: False
has_unique_characters("abcde") # Output: True
has_unique_characters("") # Output: True

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

def primes_to_n(n):
    primes= []
    candidate = 2
    while candidate <= n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

first_n_primes(20)
primes_to_n(20)

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]  # Step 1: Check if result is already computed
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Step 2: Calculate the result
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)  # Store the result
    return memo[n]

def generate_primes(n):
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p*p, n + 1, p):
                is_prime[multiple] = False
    
    # Collecting all prime numbers
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

def factorial1(n, memo = {}):
    if n < 0:
        raise ValueError("Must be a non-negative integer")
    if n in memo:
        return memo[n]
    elif n == 0:
        return 1
    
    memo[n] = 1
    for k in range(1, n+1):
        memo[n] = memo[n]*k
        
    return memo[n]

def factorial2(n, memo = {}):
    if n < 0:
        raise ValueError("Must be a non-negative integer")
    if n in memo:
        return memo[n]
    elif n == 0:
        return 1
    
    memo[n] = n*factorial2(n-1, memo)
    
    return memo[n]

def collatz_sequence(n: int, memo_cache=None):
    '''
    Generates Collatz sequence starting with n, along with
    length of that sequence.
    '''
    if memo_cache is None:
        memo_cache = {}
    
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Must be a positive integer")

    if n in memo_cache:
        return memo_cache[n], len(memo_cache[n])

    collatz_seq = [n]

    while collatz_seq[-1] != 1:
        if collatz_seq[-1] % 2 == 0:
            collatz_seq.append(collatz_seq[-1] // 2)
        else:
            collatz_seq.append(3 * collatz_seq[-1] + 1)

        if collatz_seq[-1] in memo_cache:
            collatz_seq += memo_cache[collatz_seq[-1]][1:]

    for index in range(len(collatz_seq)):
        if collatz_seq[index] not in memo_cache:
            memo_cache[collatz_seq[index]] = collatz_seq[index:]

    return collatz_seq, len(collatz_seq)

print(collatz_sequence(14))
    
    
    

    