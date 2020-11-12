while True:
    num = int(input('Please enter an integer 0 through 9. '))
    if num in range(0, 10):
        print(num)
    else:
        print('That\'s not in range. ')
        break
