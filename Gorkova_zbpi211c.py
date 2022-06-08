


def fact(x):
  if x == 0:
    return 1
  else:
    return (x * fact(x-1))
# print(f'Факториал =', x)
# x = int(input('Число = '))
# print(f'Факториал =', fact(x))




def filter_even(li):
  return filter(lambda x : x % 2 == 0, li)
#   li = list(map(int, input('Введите список чисел: ').split()))

# print(list(filter_even(li)))




def square(li):
  total_list = list(map(lambda x: x*x, li))
  return total_list
# li = list(map(int, input('Введите список чисел: ').split()))
# print(list(square(li)))



def bin_search(li, element):
    i = 0
    l = len(li)
    while i <= l:
        sr = (i + l) // 2
        if li[sr] == element:
            return sr
        if element < li[sr]:
            l = sr - 1
        else:
          continue
  

# print(bin_search([2, 5, 7, 9, 11, 17, 222], 11))
# print(bin_search([6, 45, 78, 89, 90, 101], 101))




def is_palindrome(string):
    string = string.lower().replace(' ', '')
    for i in range(len(string) // 2):
        if string[i] != string[-1 - i]:
            return 'No'
    return 'Yes'


# string = input('Введите строку: ')
# print(is_palindrome(string))





class MyError(Exception):
  def __init__(self, msg):
    self.msg = msg
 

