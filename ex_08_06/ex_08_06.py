

num_list = list()

while True:
    input_num = input('Input number: ')
    if input_num == 'done':
        break
    try:
        num = float(input_num)
    except:
        print('Input must be a number')
        continue
    num_list.append(num)

print('Max:', max(num_list))
print('Min:', min(num_list))

