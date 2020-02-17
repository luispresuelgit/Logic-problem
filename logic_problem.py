
states = ["R", "D", "L", "U"]

N = input("Enter N value for matrix : ")

M = input("Enter M value for matrix : ")

full=False

rows = int(M)

columns = int(N)

# Initialize matrix
matrix = []

# Filling with zeroes
for x in range(rows):
    a=[]
    for y in range(columns):
        a.append(0)
        print("x:%s y:%s" % (x, y))
    matrix.append(a)


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
print("max: %s" % maximum_filled_movs)
print("--state: %s" % state)
# ------
while(full==False):
    # are we done?
    print("state: %s" % state)
    print("filling: %s" %  filling)
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

    print("state: %s" % state)

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

    print("state: %s" % state)

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

    print("state: %s" % state)

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

    print("state: %s" % state)
#---------


print()
print("filled matrix: ")
for y in range(columns):
    for x in range(rows):
        print(matrix[x][y], end='')
    print()
print()
print("Direction result: %s" % last_state)
