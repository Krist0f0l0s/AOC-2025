import math
problems = []
with open("./6/input", "r") as file:
    data = file.read().split("\n")
    operations = data[-1]
    last_index = False
    for i in range(len(operations)-1, -1, -1):
        o = operations[i]
        if o in ["*", "+"]:
            problems.append([[line[i:last_index or None] for line in data[:-1]],o])
            last_index = i-1

grand_total = 0
for problem in problems:
    text = problem[0]
    operation = problem[1]
    nums = []
    k = len(text)
    l = len(text[0])
    for i in range(l-1, -1, -1):
        num = ""
        for j in range(k):
            if text[j][i]!=" ":
                num += text[j][i]
        nums.append(int(num))
    if operation == "*":
        grand_total += math.prod(nums)
    else:
        grand_total += sum(nums)
print(grand_total)