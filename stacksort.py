stack = eval(input("Enter a stack :-"))

for i in range (len(stack)):
    for j in range(len(stack)-1):
        if stack [ j ]  > stack [ j + 1 ] :
            stack [ j ] , stack [ j + 1 ] = stack [ j + 1 ] , stack [ j ]

print(stack)
