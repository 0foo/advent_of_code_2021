with open('input.txt') as f:
    lines = f.readlines()

cur_max = int(lines[0])
inc = 0

for i in lines:
    i = int(i)

    if i > cur_max:
        inc += 1
        cur_max = i
    
    if i <= cur_max:
        cur_max = i


print(inc)