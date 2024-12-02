# UDEMY PYTHON COURSE

# statements assessment test
# question 1
st = "print only the words that start with s in this sentence"
for word in st.split():
    if word[0] == "s":
        print(word)

# question 3
list1 = [x for x in range(1, 50) if x % 3 == 0]                     # list comprehension
print(list1)

# question 4
st1 = "print every word in this sentence that has an even number of letters"
words = (elem for elem in st1.split() if len(elem) % 2 == 0)
try:
    while True:                                          # how to write the for and if statements in 1 line???????
        print(next(words))                                                        # using next keyword
except StopIteration:
    pass

# question 5
for num in range(1, 101):
    if num % 15 == 0:
        print("FizzBuzz")                                  # check again (done)
    elif num % 3 == 0:                                     # works the same with keyword continue
        print("Fizz")                                      # nope it doesnt
    elif num % 5 == 0:                                     # checking divisibility with 15 first does the trick!
        print("Buzz")
    else:
        print(num)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for num in range(1, 101):
    if num % 3 == 0:
        print("fizz")
        continue
    elif num % 5 == 0:
        print("Buzz")
        continue
    elif num % 15 == 0:
        print("FizzBuzz")
    else:
        print(num)
    
# question 6
st2 = "create a list of the first letters of every word in this string"
list2 = []
for word in st2.split():
    list2.append(word[0])
print(list2)

# OR METHOD 2

list3 = [word[0] for word in st2.split()]
print(list3)

# Define a function called myfunc that takes in a string, and returns a
# matching string where every even letter is uppercase, and every odd
# letter is lowercase. Assume that the incoming string only contains
# letters, and don't worry about numbers, spaces or punctuation. The
# output string can start with either an uppercase or lowercase letter,
# so long as letters alternate throughout the string.


# coding exercise 10

def myfunc(x):
    out = []
    for i in range(len(x)):
        if i % 2 == 0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    print(''.join(out))


myfunc("qwerty")

# OR


def myfunc(x):
    out = ""
    for i in range(len(x)):
        if i % 2 == 0:
            out += x[i].lower()
        else:
            out += x[i].upper()
    print(out)


myfunc("qwerty")

result = 100/777
print(result)

print("the result is {r:10.6f}".format(r=result))

print(2**38)

txt = "Hi Sam!"

x = "S"
y = "J"

def twosum(nums, target):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j

print(twosum([2,7,11,15], 9))


def func9(str):
    length = len(str)
    if str[0] == str[length-1]:
        print("yes")
    else:
        print("no")

func9("starts")


def calc_reciprocal(lst):
    reciprocal = []
    for i in lst:
        try:
            reciprocal.append(1/i)
        except ZeroDivisionError:
            reciprocal.append("infinity")
    print(reciprocal)


calc_reciprocal([1, 4, 0, 5, 3])
print("-------------------------------------------------------------------------------\n")
def sum(lst):
    s = 0
    print("consecutive sum")
    for i in lst:
        s += i
        print(s)
    print("total sum")
    print(s)

sum([1,2,3,4])


def string(a,b):
    if a in b:
        print("yes")
    else:
        print("no")

string("he", "hello")

def evenodd(s):
    even = []
    odd = []
    for word in s.split():
        if len(word)%2 == 0:
            even.append(word)
        else:
            odd.append(word)
    print("even words", even)
    print("odd words", odd)

evenodd("i am pranathi")

def addmatrices(x, y):
    lst = []
    for i in range(0,9):
        lst.append(x[i] + y[i])
    print(lst)

addmatrices([1,2,3,4,5,6,7,8,9], [0,2,3,4,5,6,7,8,9])

def counts(s):
    dict1 = {}
    for char in s:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1

    ans = max(dict1, key=dict1.get)

    print(ans, dict1[ans])

counts("i am inevitable")


def remove(s, n, m):
    if n < 0 or n > len(s):
        print(s)
    else:
        s1 = s[:n-1] + s[n:]
        print(s1)

    print(s1[:m-1] + s1[m:])

remove("hello pranathi", 7, 10)

def add_matrices(matrix1, matrix2):
    result = [[0 for k in range(len(matrix1[0]))] for k in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

# example
matrix1 = [[1,1,1,2],[1,1,1,2],[1,1,1,2],[1,1,1,2]]
matrix2 = [[1,1,1,2],[1,1,1,2],[1,1,1,2],[1,1,1,2]]

result = add_matrices(matrix1, matrix2)

for row in result:
    print(row)


if True:
 print("true")