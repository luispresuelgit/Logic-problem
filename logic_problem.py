import decimal
import math

states = ["R", "D", "L", "U"]

N_array = []

M_array = []

results = []

def validate_axis(axis, axis_value):
    try:
        decimal.Decimal(axis_value)
    except decimal.InvalidOperation:
        raise ValueError("value: %s is not a number for axis %s" % (axis_value, axis))
    try:
        int(axis_value)
    except:
        raise ValueError("value: %s is not an integer for axis %s" % (axis_value, axis))
    if not (1 <= int(axis_value) and int(axis_value) <= math.pow(10, 9)):
        raise ValueError("value: %s is not inside the allowed interval for axis %s" % (axis_value, axis))

def validate_times(value):
    try:
        decimal.Decimal(value)
    except decimal.InvalidOperation:
        raise ValueError("value: %s is not a number for T" % value)
    try:
        int(value)
    except:
        raise ValueError("value: %s is not an integer for T" % value)
    if not (1 <= int(value) and int(value) <= (5*math.pow(10, 3))):
        raise ValueError("value: %s is not inside the allowed interval for T" %value)


print("Please, insert only integer numbers. Make sure to follow the intervals given,")
print("else the program will fail and you'll have to start again.")
T = input("Enter T  value for the times this code will be executed (1 <= T <= 5000): ")
validate_times(T)
T = int(T)
print("Intervals for N and M: 1 <= N,M <= 10^9")
for i in range(T):

    N = input("Enter N value for matrix number %s: " % str(i+1))

    validate_axis("N", N)

    M = input("Enter M value for matrix number %s: " % str(i+1))

    validate_axis("M", M)

    N_array.append(int(N))
    M_array.append(int(M))

    print()


for i in range(T):
    full=False

    rows = M_array[i]

    columns = N_array[i]

    # Initialize matrix
    matrix = []

    # Filling with zeroes
    for x in range(rows):
        a=[]
        for y in range(columns):
            a.append(0)
        matrix.append(a)

    print()
    print("Our matrix filled with zeroes: ")
    for y in range(columns):
        for x in range(rows):
            print(matrix[x][y], end='')
        print()

    print()
    x = 0
    y = columns-1
    filling = 0
    matrix[x][y] = 1  # Initializing from top left-corner
    state = states[0]
    last_state = state

    filling += 1

    maximum_filled_movs = rows*columns

    # ------
    while(full==False):
        # are we done?
        if filling == maximum_filled_movs:
            break

        if state == "R":
            # we are advancing right →
            if x+1 == rows:
                # out of boundaries
                # turn right
                state = states[1]
            else:
                if matrix[x+1][y] == 1:
                    # filled space
                    # turn right
                    state = states[1]
                else:
                    # else we advance
                    last_state = state
                    x+=1
                    matrix[x][y] = 1
                    filling += 1
                    print("we advanced R")

        if state == "D":
            # we are advancing down ↓
            if y-1 < 0:
                # out of boundaries
                # turn right
                state = states[2]
            else:
                if matrix[x][y-1] == 1:
                    # filled space
                    # turn right
                    state = states[2]
                else:
                    # we advance
                    last_state = state
                    y-=1
                    matrix[x][y] = 1
                    filling += 1
                    print("we advanced D")

        if state == "L":
            # we are advancing left ←
            if x-1 < 0:
                # out of boundaries
                # turn right
                state = states[3]
            else:
                if matrix[x-1][y] == 1:
                    # filled space
                    # turn right
                    state = states[3]
                else:
                    # we advance
                    x-= 1
                    last_state = state
                    matrix[x][y] = 1
                    filling += 1
                    print("we advanced L")

        if state == "U":
            # we are advancing up ↑
            if y+1 == columns:
                # out of boundaries
                # turn right
                state = states[0]
            else:
                if matrix[x][y+1] == 1:
                    # filled space
                    # turn right
                    state = states[0]
                else:
                    # we advance
                    y+= 1
                    last_state = state
                    matrix[x][y] = 1
                    filling += 1
                    print("we advanced U")

    #---------


    print()
    print("filled matrix (%s): " % str(i+1))
    for y in range(columns):
        for x in range(rows):
            print(matrix[x][y], end='')
        print()
    print()
    print("Direction result for matrix %s: %s" % (str(i+1), last_state))
    print()

    results.append(last_state)

print()
print("Output:")
print()
for i in range(len(results)):
    print(results[i])
    print()
