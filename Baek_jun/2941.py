croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

input_string = input()

for idx, alpha in enumerate(croatia):
    input_string = input_string.replace(alpha, str(idx) )

length = len(input_string)

print(length)