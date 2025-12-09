import numpy as np
with open("./4/input") as file:
    data = file.read().strip()
    data = data.replace(".", "0").replace("@", "1")
    data = [list(map(int, line)) for line in data.split("\n")]
data = np.pad(np.array(data), pad_width=1, mode="constant", constant_values=0)
steps = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
overall = 0
result = 1
while result != 0:
    result = 0
    for i in range(1, data.shape[0] - 1):
        for j in range(1, data.shape[1] - 1):
            aviable = 0
            if data[i, j] == 0:
                continue
            for step in steps:
                x, y = i + step[0], j + step[1]
                aviable += data[x, y]
            if aviable < 4:
                data[i, j] = 0
                result += 1
    overall += result
print(overall)