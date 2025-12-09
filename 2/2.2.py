with open('./2/input', 'r') as file:
    lines = file.read()
ranges = [tuple(map(int, x.split("-"))) for x in lines.split(",")]
# print(ranges)
invalid_sum = 0
for start, end in ranges:
    for num in range(start, end + 1):
        str_num = str(num)
        l = len(str_num)
        for i in range(1, l//2 + 1):
            if l%i == 0 and all(str_num[j:j+i] == str_num[0:i] for j in range(0, l, i)):
                invalid_sum += num
                break

print(invalid_sum)