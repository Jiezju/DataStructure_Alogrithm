'''
Plus one
'''


def plusOne(digits):
    n = len(digits)
    index = n - 1
    while index >= 0:
        digits[index] += 1
        if digits[index] < 10:
            return digits
        digits[index] = 0
        index -= 1
    if digits[0] == 0:
        return [1] + digits

def plusOne2(digits):
    if len(digits) == 0:
        return -1
    
    for i in range(len(digits)-1,-1,-1):
        digits[i] += 1
        if digits[i] == 10:
            digits[i] = 0
            if i == 0:
                digits.insert(0,1)
        else:
            break

    return digits


if __name__ == '__main__':
    digits = [1, 2, 3]
    print(plusOne2(digits))
