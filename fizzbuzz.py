for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print('fizzbuzz')
    elif i%3 == 0:
        print('fizz!')
    elif i%5 == 0:
        print('buzz!')
    else:
        num = int(input("What's the next number? " ))
        if num == i:
            print(num)
        else:
            print('Wrong answer, you shall die!')
            break
