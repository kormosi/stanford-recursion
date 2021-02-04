# 2. Write a recursive function that, given a number  n,
# returns the sum of the digits of the number n.


# Possibly can be done in more elegant way,
# for now I just don't know how.
def sum_digits(n):
    if len(str(n)) == 1:
        return(int(n))
    return sum_digits(str(n)[1:]) + int(str(n)[0])


results = [
    sum_digits(15) == 6,
    sum_digits(314) == 8,
    sum_digits(1) == 1
]
assert all(results)
