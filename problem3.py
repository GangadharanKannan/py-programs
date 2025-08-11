# count vowels in string

str1 = "hello"
vowel = "aeiou"

print(sum(1 for ch in str1.lower() if ch in vowel))