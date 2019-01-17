#Given a list of strings, make a list of all palindromes in the original list using filter.

list_string=["apple", "dad", "yay", "huuh", "orange", "cat"]

filter_obj=filter(lambda x: True if x==x[::-1] else False, list_string)
print(list_string)
print(list(filter_obj))
