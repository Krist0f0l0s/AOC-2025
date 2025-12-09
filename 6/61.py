with open("./6/input", "r") as file:
    data = [x.split() for x in file.read().strip().split("\n")]
    data[0]=[int(x) for x in data[0]]
    data[1]=[int(x) for x in data[1]]
    data[2]=[int(x) for x in data[2]]
    data[3]=[int(x) for x in data[3]]
grand_total = sum([x*y*z*t if o=="*" else x+y+z+t for x,y,z,t,o in zip(*data)])
print(grand_total)
