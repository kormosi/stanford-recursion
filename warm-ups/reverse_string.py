# 3. Write a recursive function that, given a string s,
# prints the characters of s in reverse order.

# Using index
def reverse_string_recursively(str, index):
    if index+1 == len(str):
        return str[index]
    return reverse_string_recursively(str, index+1) + str[index]


# Assert correctness and print.
if (result := reverse_string_recursively("recursion", 0)) == "recursion"[::-1]:
    print(result)


# Not using index
def _reverse_string_recursively(str):
    if len(str) == 1:
        return(str)
    return _reverse_string_recursively(str[1:]) + str[0]


# Assert correctness and print.
if (result := _reverse_string_recursively("recursion")) == "recursion"[::-1]:
    print(result)
