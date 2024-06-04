x = 371
x_str = str(x)

# sum = 0
# for i in range(len(str(x))):
#     sum += int(str(x)[i]) ** len(str(x))

# print(sum)

for i in range(len(x_str)):
    result = sum(int(x_str[i]) ** len(x_str))

print(result)
