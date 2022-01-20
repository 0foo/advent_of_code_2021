with open('input.txt') as f:
    lines = f.readlines()

depth = 0
forward = 0
aim = 0

for line in lines:
    direction, quantity = line.split()
    quantity = int(quantity)

    if direction == "forward":
        forward += quantity
        depth += (quantity * aim)
    

    if direction == "up":
        aim -= quantity
    

    if direction == "down":
        aim += quantity


print(depth, forward)
print(depth * forward)
    