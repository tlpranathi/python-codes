# UDEMY PYTHON COURSE

# FUNCTION PRACTISE EXERCISES
# WARMUP

# Q1
def func(a, b):
    if a % 2 == 0 and b % 2 == 0:
        print(min(a, b))
    else:
        print(max(a, b))


func(2, 5)

# Q2


def func2(x):
    y = x.split()
    first = y[0]
    second = y[1]
    if first[0] == second[0]:
        print(True)
    else:
        print(False)


func2("pranathi pranathi")

# Q3


def func3(a, b):
    if a + b == 20 or a == 20 or b == 20:
        print(True)
    else:
        print(False)


func3(1, 19)

# LEVEL 1

# Q1


def func4(x):
    one = x[0]
    two = x[1:3]
    three = x[3]
    four = x[4:]
    print(one.upper() + two + three.upper() + four)


func4("wxecrvtybunim")

# Q2


def func5(y):
    list1 = y.split()
    list2 = list1[::-1]
    print(" ".join(list2))


func5("am i doing this correctly?")
func5("yay i am correct")

# Q3


def func6(z):
    if z in range(90, 111):
        print(True)
    elif z in range(190, 211):
        print(True)
    else:
        print(False)


func6(2)

# LEVEL 2

# Q1


def func7(list2):
    check = [3, 3]
    if check in list2:
        print("it worked")                         # why is this wrong???????
    else:                                          # check my notes, point 25
        print("nope")


# ANSWER


def func8(list3):
    for i in range(0, len(list3)-1):
        if list3[i] == 3 and list3[i+1] == 3:      # OR if nums[i:i+2] == [3,3]:
            return True
    return False


print(func8([2, 3, 3, 4]))

# Q2


def func9(word):
    for i in range(0, len(word)):
        print(word[i] * 3, end = "")          # all by myself lessgoooo
        i =+ 1                      # check what the error is!!!!!!!!!!!!!! found it >>>>range is not (0, len(word) + 1)
# CHANGED PRINT TO RETURN AND EVERYTHING IS WRONG NOW CHECK!!!!!!!!!!!!!!
# return keyword breaks out a function loop!!!

func9("ben")


work_hours = [("a", 10), ("b", 15), ("c", 20), ("d", 20)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ""
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass                                # DOES'NT WORK WHEN 2 EMPLOYEES HAVE SAME MAX WORK HOURS!! WHAT SHIT
    return (employee_of_month, current_max)


print(employee_check(work_hours))

###############################################################################################################
def pattern(list):
    check = False
    number = 0
    for n in range(2, len(list)):
        for i in range(0, len(list)):
            for j in range(i + (n-1), len(list)):
                if list[i:i + n] == list[j:j + n]:                      # doesn't work if 2 repeated patterns are present
                    check = True
                    ans = list[i:i+n]
                    number += 1
                    print(ans)
    if check == True:
        print("this pattern", ans, "repeats", number, "number of times")
    else:
        print("no pattern")

pattern([1,2,3,4,1,2,3,4,2,3,4,5,6,1,2,3])


def secondlargest(list):
    maxvalue = max(list)
    index1 = list.index(maxvalue)                                     # only works when max value isn't repeated!!!
    list.pop(index1)                                                  # not the best code
    secondmax = max(list)
    print("the secondmax is ", secondmax, "and the max is", maxvalue)


secondlargest([0,-2,-1])


def second(lst):
    list1 = list(set(lst))
    list1.sort()
    print("max value is ", list1[-1])
    print("second max value is ", list1[-2])
    print("third max value is ", list1[-3])
    print("fourth max value is ", list1[-4])

second([9,10,1,2,3,4,4,5,5,6,7,8])
