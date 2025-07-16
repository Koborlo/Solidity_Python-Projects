largest_so_far = -1
print('Before', largest_so_far)
for the_numb in  [34, 43, 2,9,4,30,20,78,90,35,88,99]:
    if the_numb > largest_so_far:
        largest_so_far = the_numb
    print(largest_so_far, the_numb)
print('After:', largest_so_far)