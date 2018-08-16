output = []
prime = [2,3,5,7,11,13,17,19,23,27,29,31,37,41,43,47]
x = int(input("Insert number: "))
for i in prime:
    while x%i == 0:
        output.append(i)
        x /= i

print(output)


'''

        elif i == 4:
            output.append(2)
            output.append(2)
        else:
            while i%2 == 0:
                i = i/2
        output.append(i)
        x = x/i
if x != 1:
    output.append(int(x))

if 1.0 in output:
    output.remove(1.0)
print(output)
'''
