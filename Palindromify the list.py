'''
Author: Niel
Date: 24 March 2021
Purpose: Python Practice
'''


# if the number is not a palindrome it will continue to add up
def nxt_palindrome(n):
    n = n+1
    while not palindrome(n):
        n+=1
    return n
# function stating when the number is plaindrome
def palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == '__main__':
    # take an input from the user
    n = int(input("enter limit:"))

    # make an empty list
    lst = []

    # loop to iterate and insert the user given numbers in
    # the empty list
    for i in range(n):
        ele = int(input("Enter your numbers:\n"))
        lst.append(ele)
    print(f"Input list {lst}")

    # loop to iterate each element from the list to check
    # the given condition
    new_lst = []
    for i in lst:
        if i>=10:
            a = nxt_palindrome(i)
            new_lst.append(a)
        else:
            new_lst.append(i)
    print(f"Output list {new_lst}")

    # using list comprehension
    # print(f"Output list"
    #       f"{[lst[i] if lst[i]<=10 else nxt_palindrome(lst[i]) for i in range(n)]}")