# Write a recursive function that, given two strings, returns whether the
# first string is asubsequence of the second. For example, given hac and
# cathartic, you should return true, but given bat and table,
# you should return false.


def is_subsequence(str1: str, str2: str) -> bool:
    # ohandlovat error
    if not str1:
        return True
    if str1[0] in str2:
        return is_subsequence(str1[1:], str2[str2.index(str1[0])+1:])
    return False


assert is_subsequence("xvr", "xavier")
assert is_subsequence("hac", "cathartic")

assert not is_subsequence("bat", "table")
assert not is_subsequence("frh", "fighter")
