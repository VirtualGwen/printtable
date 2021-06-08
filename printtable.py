user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

x = 0
for rows in mult_table:
    for columns in rows:
        if (x + 1) < len(mult_table) : 
            print('{}'.format(columns), end = ' | ')
        else:
            print('{}'.format(columns))
            x = -1
        x += 1
