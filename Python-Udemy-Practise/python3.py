# UDEMY PYTHON COURSE

# Q3
def func10(a, b, c):
    if a+b+c <= 21:
        print(a+b+c)
    elif a+b+c > 21 and a == 11 or b == 11 or c == 11:
        print(a+b+c - 10)
    else:
        print("BUST")


func10(9, 9, 9)


def spygame(num2):
    check = False
    number = 0
    for i in range(0, len(num2)):
        if num2[i:i+3] == [0, 0, 7]:
            check = True
            number += 1
        else:                                                    # DOESNT PRINT FALSE IF 007 IS NOT THERE!!!
            continue                                             # fixed using check!!
    if check == False:
        print("007 not found")
    else:
        print("caught 007")
        print("number of times = ", number)


spygame([1, 2, 0, 0, 7, 1, 0, 0, 7])

# BETTER CODE


def spy_game(num1):
    zero_counter = 0
    check = False
    for number in num1:
        if number == 0:
            zero_counter += 1
        elif number == 7 and zero_counter >= 2:                      # PRINTS TRUE AND FALSE!!!!!!!!!!!!!!!!!!!!!!!!!
            check = True
    if check == False:
        print("007 not found")
    else:
        print("caught 007")




spy_game([1, 2, 0, 7])


# MASTER CODE


def spy_games(num3):
    code = [0, 0, 7, "x"]
    # [0,7,"x"]
    # [7,"x"]
    # ["x"] length = 1
    for num1 in num3:
        if num1 == code[0]:
            code.pop(0)

    if len(code) == 1:
        print("007")
    else:
        print("no")


spy_games([0, 1, 2, 3, 0, 8, 7])


def primes(num2):
    if num2 < 2:
        print(None)
    prime_num = [2]
    x = 3
    while x <= num2:
        for y in prime_num:
            if x % y == 0:
                x += 2
                break
        else:
            prime_num.append(x)
            x += 2
    print(prime_num)
    print(len(prime_num))


primes(80)


list1 = []
for num in range(1000):
    if num % 3 == 0 or num % 5 == 0:
        list1.append(num)


print(sum(list1))

# LAMBDA FUNCTIONS, MAP AND FILTER FUNCTIONS
# MAP FUNCTION


names = ["harry", "styles", "tom", "holland"]


def splicer(mystring):
    if len(mystring) % 2 != 0:
        return mystring[0]                 # PRINTS None AFTER EACH ITERATION IF PRINT IS USED INSTEAD OF RETURN
    else:
        return "even"


for item in map(splicer, names):
    print(item)

print(list(map(splicer, names)))

# FILTER FUNCTION


def even(m):
    return m % 2 == 0


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(even, nums)))

# LAMBDA EXPRESSION

print(list(map(lambda n: n**2, nums)))

print(list(filter(lambda m: m % 2 == 0, nums)))


def palindrome(x):
    if x == x[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")


palindrome("pranathi")


def prime(n):
    code = True
    if n == 2:
        print("prime")
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                code = False
    else:
        print("neither prime nor composite")
    if code == False:
        print("not a prime")
    else:
        print("prime")


prime(7)


def anagram():
    input1 = list(input("word1? "))
    input2 = list(input("word2? "))
    if len(input1) == len(input2):
        input1.sort()
        input2.sort()                      # SORT FUNCTION ON A LIST DOESN'T RETURN THE SORTED LIST!!!!
        if input1 == input2:               # CONVERT STR TO SET TO DIRECTLY CHECK FOR EQUALITY SKIPPING THE NEED TO SORT
            print("anagrams")              # SET CANNOT CONTAIN MULTIPLE MUTABLE ELEMENTS AND DUPLICATE ENTRIES
        else:
            print("not anagrams")
    else:
        print("not anagrams")


anagram()

l1 = [1, 3, 5, 4, 2]
l2 = [2, 4, 3, 5, 1]
l1.sort()
l2.sort()
if l1 == l2:
    print(True)

