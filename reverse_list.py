"""
Given a list of strings, write a function that prints a reverse version of each string:

For example:
>A = [ "Hello World", "Hello Python", "1 2 3 4 5 6 7 8"]
>magic_function(A)
['dlroW olleH', 'nohtyP olleH', '8 7 6 5 4 3 2 1']
"""

# one way
def magic_function(A):
    reverse_list = []
    for a in A:
        reverse_list.append(a[::-1])
    return reverse_list


# better way
def magic_function_2(A):
    reverse_list = [a[::-1] for a in A]
    return reverse_list


if __name__ == '__main__':
    A = [ "Hello World", "Hello Python", "1 2 3 4 5 6 7 8"]
    
    print(magic_function(A))
    print(magic_function_2(A))
