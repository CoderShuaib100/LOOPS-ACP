# creating the algorithm
base = int(input("Enter the Base number: "))
expo = int(input("Enter the Power number: "))
ans = 1
# creating the loop with condition

if (expo == 0):
    ans = 1
else: 
    for i in range (0,expo):
        ans = ans * base

# printing the answer
print("The answer is",ans)