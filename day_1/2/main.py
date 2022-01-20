with open('input.txt') as f:
    lines = f.readlines()

# note: adds n complexity, can change to a -inf if run into time complexity issues
cur_max = None
inc = 0


for i in range(len(lines)):

    if ( len(lines) - i ) < 3:
        break
    
    summees = [ 
            int(lines[i]), 
            int(lines[i + 1]), 
            int(lines[i + 2])
    ]

    new_sum = sum( summees )


    if cur_max == None:
        cur_max = new_sum
        continue

    if new_sum > cur_max:
        inc += 1
    
    cur_max = new_sum
    



print(inc)
    
