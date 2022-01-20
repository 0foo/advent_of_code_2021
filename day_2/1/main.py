with open('input.txt') as f:
    lines = f.readlines()

depth = 0
forward = 0

for line in lines:
    direction, quantity = line.split()
    quantity = int(quantity)

    if direction == "forward":
        forward += quantity
    

    if direction == "up":
        depth -= quantity
    

    if direction == "down":
        depth += quantity


print(depth, forward)
print(depth * forward)
    