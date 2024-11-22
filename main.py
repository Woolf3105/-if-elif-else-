first = int(input(339))
second = int(input(74))
third = int(input(339))

if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)