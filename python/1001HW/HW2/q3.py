'''
(Financial: credit card number validation) 
Credit card numbers follow certain patterns: 
It must have between 13 and 16 digits, and the number must start with:
■ 4 for Visa cards
■ 5 for MasterCard credit cards 
■ 37 for American Express cards 
■ 6 for Discover cards
In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers. 
The algorithm is useful to determine whether a card number is entered correctly or whether a credit card is scanned correctly by a scanner. 
Credit card numbers are generated following this validity check, commonly known as the Luhn check or the Mod 10 check
1. Double every second digit from right to left. If doubling of a digit results in a twodigit number, add up the two digits to get a single-digit number.
2. Now add all single-digit numbers from Step 1.
3. Add all digits in the odd places from right to left in the card number. 6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38
4. Sum the results from Steps 2 and 3.
5. If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is invalid. 
For example, the number 4388576018402626 is invalid, but the number 4388576018410707 is valid.
Write a program that prompts the user to enter a credit card number as an integer. 
Display whether the number is valid or invalid. 
Design your program to use the following functions:
'''

# sumOfDoubTeEvenPTace(number) + sumOfOddPTace(number)
card_number = str(input("Please enter your card number: ")) # let the user to enter the number
number_list0 = list(card_number) # spilt the initial list
number_list = list() # set the new list

for i in number_list0: # for the element in initial list
    i = int(i)  # change its data type
    number_list.append(i) # add the int into the new list

def isValid() : # the final check
    if final_sum % 10 == 0: # check process
        return True # vaild
    else: # if not:
        return False # invalid

def sumOfDoubTeEvenPlace() : # the even sum
    sum_even = 0 # initialize the sum_even
    for i in number_list[-2::-2]:  # select the number
        sum_even += getDigit(i) # get the sum
    return sum_even

def getDigit(number):  # def the process for double sum even
    temp = number * 2 # set temp
    if temp >= 10: # judge if bigger than 10
        sum = temp // 10 + temp % 10 # get the sum
    else: # smaller than 10
        sum = temp # directly get sum
    return sum # output

def sumOfOddPlace(): # the odd sum
    sum_odd = 0 # initialize it
    for j in number_list[-1::-2]:  # select the digit
        sum_odd += j # add to the sum
    return sum_odd # output


final_sum = sumOfDoubTeEvenPlace() + sumOfOddPlace() # get the final sum
result = isValid() # get the final check result
if result == True:  # when meet
    print("your card number is valid")  # tell the user the card number is valid
else: # when not
    print("your card number is invalid")  # tell the user the card number is invalid
