with open('./2/input', 'r') as file:
    lines = file.read()
ranges = [tuple(map(int, x.split("-"))) for x in lines.split(",")]
# print(ranges)
invalid_sum = 0
for start, end in ranges:
    for num in range(start, end + 1):
        str_num = str(num)
        if len(str_num)%2 == 0 and str_num[:len(str_num)//2] == str_num[len(str_num)//2:]:
            invalid_sum += num

print(invalid_sum)