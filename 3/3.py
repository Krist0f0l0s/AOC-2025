jolts = 0
k = 12
with open('./3/input', 'r') as file:
    while line := file.readline().strip():
        digits = [int(char) for i,char in enumerate(line)]
        sum = ""
        biggest_index = 0
        for i in range(0, k):
            biggest = digits[biggest_index]
            looking = digits[biggest_index+1:-(k-1-i) or None]
            for j, v in enumerate(digits[biggest_index+1:-(k-1-i) or None], start=biggest_index+1):
                if v > biggest:
                    biggest = v
                    biggest_index = j
            biggest_index += 1
            sum += str(biggest)
        jolts += int(sum)
print(jolts)