def str_compress(s):
    count = 1
    if count > len(s):
        return ""
    while count < len(s) and s[count] == s[0]:
        count += 1
    return s[0] + str(count) + str_compress(s[count:])

print(str_compress(s = input("Enter string: ")))
