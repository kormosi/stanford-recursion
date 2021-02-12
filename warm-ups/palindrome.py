# 4. Write a recursive function that checks whether a string is a palindrome
# (a palindrome is a string that's the same when reads forwards and backwards.)

def is_palindrome(string):
    if len(string) < 2:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False


positive_results = [
    is_palindrome("tenet"),
    is_palindrome("redder"),
    is_palindrome("racecar"),
]

negative_results = [
    not is_palindrome("vim"),
    not is_palindrome("emacs"),
    not is_palindrome("linux"),
]

assert all(positive_results)
assert all(negative_results)
