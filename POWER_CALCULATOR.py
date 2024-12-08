# creating the algorithm
base = int(input("Enter the Base number: "))
expo = int(input("Enter the Power number: "))
ans = base
# creating the loop

for i in range (0,expo - 1):
    ans = ans * base

# printing the answer
print("The answer is",ans)