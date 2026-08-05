#print numbers from 1 to 20 using for loop
for i in range(1,11):
    print(i)

# print the multiplicaton table of any number
num=int(input("Enter a integer: "))
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")

#print even number from 1 to 50 uing a while loop
print("Even number over the range of 1-50 are:")
for i in range(1,51):
    if i%2==0:
        print(i,end=" ")