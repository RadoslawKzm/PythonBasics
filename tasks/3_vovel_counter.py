"""Create program that counts vowel occurrences in given string
input: string = "Some test string"
output: whatever that shows count of vowels
"""

from collections import Counter


def vowel_counter(string: str) -> dict:
    vowels = "aeiouy"
    string = string.lower()  # sanitizing input
    dict_ = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "y": 0}
    for letter in string:
        if letter in dict_.keys():
            dict_[letter] = dict_[letter] + 1
    return {key: value for key, value in dict_.items() if value > 0}


def vowel_couter_upgraded(string: str) -> dict:
    return {k: v for k, v in Counter(string.lower()).items() if k in "aeiouy"}


if __name__ == "__main__":
    print(vowel_counter("Some test string"))
    print(vowel_couter_upgraded("Some test string"))
