doors = [False]*101
j = 1

while j <=100:
    for i in range(0, 101, j):
        doors[i] = not(doors[i])
    j += 1

for i in range(len(doors)):
    if doors[i] == True:
        print(i)
