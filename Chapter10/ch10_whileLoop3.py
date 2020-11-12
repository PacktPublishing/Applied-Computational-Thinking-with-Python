while True:
    num = int(input('Please enter an integer 0 through 9. Tired? Type a number out of range. '))
    if num in range(0, 10):
        print(num)
    else:
        print('That\'s not in range. ')
        break
