def reverse_string(text):
    return text[::-1]

def to_upper(text):
    return text.upper()

def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in 'aeiou':
            count += 1
    return count

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def word_count(text):
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

