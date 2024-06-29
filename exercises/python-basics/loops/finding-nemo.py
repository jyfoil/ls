# Loop over the elements of the fish_list list below, logging each one. 
# Terminate the loop immediately after printing the string 'Nemo'.



fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    if fish == 'Nemo':
        break

    print(fish)


index = 0
while index < len(fish_list):
    if fish_list[index] == 'Nemo':
        break

    print(fish_list[index])
    index += 1