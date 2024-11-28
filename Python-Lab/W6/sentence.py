string = "this is the sentence"
print(string)

v = 0 
c = 0
max_len = 0
for i in string.split():
    if len(i) > max_len:
        max_len = len(i)
    for j in i:
        if j in "AEIOUaeiou":
            v += 1
        else:
            c += 1

print("number of vowels:", v)
print("number of consonants:", c)
print("longest word:", i)
print("reversed sentence:", string[::-1])
