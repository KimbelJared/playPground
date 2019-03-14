def isPrime(num):
    if num == 0:
        return False
    if num == 1:
        return False
    if num == 2:
        return True
    if num %  2 == 0:
        return False

    edge = num**0.5+1
    c = 3
    while c <= edge:
        if num % c == 0:
            return False
        c+=2
    return True





userIn = int(input("please enter an integer: "))

print(isPrime(userIn))
