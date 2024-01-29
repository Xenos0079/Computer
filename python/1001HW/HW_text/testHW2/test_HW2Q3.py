
# sumOfDoubTeEvenPTace(number) + sumOfOddPTace(number)
card_number = str(input("Please enter your card number."))
# str(1234567891234567)
# str(input())

def isValid(number) :
    if final_sum % 10 == 0:
        return True
    else:
        return False


def sumOfDoubTeEvenPTace(number) :
    sum_even = 0
    for i in range(0, len(card_number), 2):

        temp1 = i
        temp2 = temp1 * 2
        if temp2 <= 10:
            sum_even += temp2
        if temp2 >= 10:
            temp2 = temp2 % 10 + int( temp2 / 10 )
            sum_even += temp2
    return sum_even
        



# def getDigit(number):


def sumOfOddPTace(number):
    sum_odd = 0
    for i in range(1, len(card_number), 2):

        temp1 = i
        temp2 = temp1 * 2
        if temp2 <= 10:
            sum_odd += temp2
        if temp2 >= 10:
            temp2 = temp2 % 10 + int( temp2 / 10 )
            sum_odd += temp2
    return sum_odd

result1 = sumOfDoubTeEvenPTace(card_number) 
# print(result1)

result2 = sumOfOddPTace(card_number)
# print(result2)

final_sum = result1 + result2
result = isValid(card_number)
if result == True:
    print("your card number is valid")
else:
    print("your card number is invalid")

# print(isValid(card_number))

