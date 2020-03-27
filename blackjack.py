def blackjack(num1, num2, num3):
    sum1 = num1 + num2 + num3
    if sum1 <= 21:
        return sum1
    elif sum1 <= 31 and 11 in (num1, num2, num3):
        return sum1-10
    else:
        return 'BUST'

print(blackjack(11, 9, 5))
