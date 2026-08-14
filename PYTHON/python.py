def is_palindrome(s:str) -> bool:
    s = s.lower()
    return s == s[::-1]
is_palindrome("Racecar")

def find_max(nums:list) -> int:
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
find_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

def count_vowels(s:str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
count_vowels("Hello, World!")

def fibonacci(n:int) -> list:
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence
fibonacci(10)

def sort_by_age(records:list) -> list:
    return sorted(records , key=lambda x: x['age'])
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
sort_by_age(people)

def find_duplicates(nums:list) -> list:
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
find_duplicates([1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1])

def reverse_string(s:str) -> str:
    s = list(s)
    for i in range(len(s) // 2):
        s[i], s[-(i + 1)] = s[-(i + 1)], s[i]
    return ''.join(s)
reverse_string("Hello, World!")

def is_prime(n:int) -> bool:
    if n == 1:
        return False
    for i in range(2, n - 1 ):
        if n % i == 0:
            return False
    return True
is_prime(53)

def word_count(s:str) -> dict:
    words = s.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq
word_count("the quick brown fox jumps over the lazy dog")

def flatten_list(nested_list:list) -> list:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
flatten_list([[1, 2], [3, 4], [5, 6]])

def common_elements(list1:list, list2:list) -> list:
    return list(set(list1) & set(list2))
common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])

def group_even_odd(nums:list) -> dict:
    result = {'even': [], 'odd': []}
    for num in nums:
        if num % 2 == 0:
            result['even'].append(num)
        else:
            result['odd'].append(num)
    return result
group_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])