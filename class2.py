a=["22","33","44","55"]

# for x in range (6):
#     print(x)

# for x in a:
#     # print(x)
#     if x == "44":
#         continue# break
#     print(x)

# for x in range (6,12,2):
#      print(x)

# Number of rows
n = 5

# Loop through each row
for i in range(1, n + 1):
    # Loop to print numbers from 1 to i
    for j in range(1, i + 1):
        print("+", end=" ")
    # Print a new line after each row
    print()

for i in range(6,1, - 1):
    # Loop to print numbers from 1 to i
    for j in range(1, i - 1):
        print("+", end=" ")
    # Print a new line after each row
    print()