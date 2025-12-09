with open("./5/input", "r") as file:
    data = file.read().strip().split("\n\n")
ranges = [list(map(int, line.split("-"))) for line in data[0].split("\n")]
i=0
while i<len(ranges):
    changed = False
    r=ranges[i]
    j=i+1
    while j<len(ranges):
        p=ranges[j]
        if (r[1]>=p[0] and r[0]<=p[1]) or (p[1]>=r[0] and p[0]<=r[1]):
            ranges[i][0], ranges[i][1] = min(r[0],p[0]), max(r[1], p[1])
            ranges.pop(j)
            j-=1
            changed = True
        j+=1
    if not changed:
        i+=1

length = sum([j+1-i for i,j in ranges])
print(length)