def isPalindrome(s) :
    def check(s, si, ei):
        if si >= ei:
            return True
        if s[si] != s[ei]:
            return False
        return check(s, si + 1, ei - 1)

    p = []
    for i in s:
        if i.isalnum():
            p.append(i.lower())
    p = "".join(p)
    return check(p, 0, len(p) - 1)


print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(isPalindrome("race a car"))  # Output: False
