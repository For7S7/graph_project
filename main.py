from matplotlib import pyplot as plt

def graph():
    graph_name = input('Enter a name for your graph: ')

    x_name = input('Enter a name for the axis(X): ')
    y_name = input('Enter a name for the axis(Y): ')

    type_x = input(f'Your {x_name} type is a number?(Y/N): ')
    x_input = input(f'Your {x_name} values: ').split()

    type_y = input(f'Your {y_name} type it a number?(Y/N): ')
    y_input = input(f'Your {y_name} values: ').split()


    if type_x == 'N' or 'No':
        print('Ok')
    elif type_x == 'Y':
        x = []
        for el in x_input:
            el = int(el)
            x.append(el)
            x_input = x
    else:
        print('Enter correct type')
    

    if type_y == 'Y' or 'Yes':
        y = []
        for el in y_input:
            el = int(el)
            y.append(el)
            y_input = y 
    elif type_y == 'N' or 'No':
        print('Ok')
    else:
        print('Enter correct type')

    plt.plot(x_input, y_input, marker='o')
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title(graph_name)
    plt.grid(True)
    plt.show()

graph()