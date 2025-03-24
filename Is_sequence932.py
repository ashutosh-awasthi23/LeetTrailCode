def isSubsequence(s, t):
    main_list = list(t)
    second_list = list(s)
    p = 0
    c = 0
    for i in range(0, len(second_list)):
        for j in range(p, len(main_list)):
            if second_list[i] == main_list[j]:
                p = j + 1
                c = c + 1
                break
    if len(s) == c:
        return True
    else:
        return False


print(isSubsequence("abc","ahbgdc"))