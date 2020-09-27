# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def generador():
    for num in range(1, 101):
        if num <= 100:
            yield num * 2


def iterador():
    my_list = [1,2,3]
    my_iter = iter(my_list)
    print(type(my_iter))

    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    pass
    # Impelementation of Generator
    # my_first_gen = generador()
    # for num in range (1, 51):
    #     print(next(my_first_gen))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
