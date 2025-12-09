with open("./5/input", "r") as file:
    data = file.read().strip().split("\n\n")
ranges = [tuple(map(int, line.split("-"))) for line in data[0].split("\n")]
items = [int(x) for x in data[1].split("\n")]
fresh_count = 0
for item in items:
    for r in ranges:
        if r[0] <= item <= r[1]:
            fresh_count += 1
            break
print(fresh_count)