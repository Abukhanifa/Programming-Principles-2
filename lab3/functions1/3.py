def solve(numheads, numlegs):
    
    x = 0
    y = 0

    if (numheads >= numlegs):
        print("No solution")
    elif (numlegs % 2 != 0):
        print("No solution")
    else:
        y = (numlegs - 2 * numheads) / 2
        x = numheads - y
        print(int(x), int(y))

head = int(input())
leg = int(input())
solve(head,leg)
