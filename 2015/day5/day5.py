VOWELS = set(['a', 'e', 'i', 'o', 'u'])

BANNED_SUBSTRINGS = set(['ab', 'cd', 'pq', 'xy'])

def at_least_three_vowels(word):
    global VOWELS
    
    count = 0

    for character in word:
        if character in VOWELS:
            count += 1
            if count == 3:
                return True

    return False

def two_in_a_row(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True

    return False

def no_banned_substring(word):
    global BANNED_SUBSTRINGS
    
    for i in range(len(word) - 1):
        if word[i:i+2] in BANNED_SUBSTRINGS:
            return False

    return True


def is_nice_word(word):
    return at_least_three_vowels(word) and two_in_a_row(word) and no_banned_substring(word)

def pair_of_same_two_letter_substring(word):
    two_letter_substrings = set()

    for i in range(1, len(word) - 1):
        if word[i:i+2] in two_letter_substrings:
            return True
        two_letter_substrings.add(word[i-1:i+1])

    return False

def one_letter_between_same_letter(word):
    for i in range(len(word) - 2):
        if word[i] == word[i+2]:
            return True

    return False

def is_new_nice_word(word):
    return pair_of_same_two_letter_substring(word) and one_letter_between_same_letter(word)

def count_of_nice_words(words):
    count = 0

    for word in words:
        if is_nice_word(word):
            count += 1

    return count

def count_of_new_nice_words(words):
    count = 0

    for word in words:
        if is_new_nice_word(word):
            count += 1

    return count

def get_words(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def main():
    words = get_words("day5input.txt")
    
    result = count_of_nice_words(words)
    #part 1
    print(result)

    result = count_of_new_nice_words(words)
    #part 2
    print(result)


if __name__ == "__main__":
    main()
