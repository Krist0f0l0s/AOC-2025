pos=50
password=0
with open('input', 'r') as file:
    while line:= file.readline():
        x = -int(line[1:]) if line[0]=="L" else int(line[1:])
        for i in range(0, x, 1 if x > 0 else -1):
            pos = (pos + (1 if x > 0 else -1)) % 100
            if pos == 0:
                password += 1
                
print(pos, password)    