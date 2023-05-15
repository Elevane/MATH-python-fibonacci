

output = "0"
for i in range(100):
    if i == 0:
        output += f"{1}"
    else:
        output += f"{int(output[i]) +  int(output[i-1])}"

#with a and b letters
# output = "a"
# for i in range(10):
#     if i == 0:
#         output += "b"
#     else:
#         output += f"{output[i] +  output[i-1]}"

print(output)
