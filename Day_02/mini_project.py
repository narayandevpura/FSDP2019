# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:24:52 2019

@author: Narayan Devpura
"""
shopping_list = []
def instruction():
    print("Enter items for shopping.")
    print('Enter Done to stop adding to the list.')
    print('Enter Show to see what is currently in list')
    print('Enter Help to see special commands.')

def display(shopping_list):
    print('Shopping List: ')
    for i in range(len(shopping_list)):
        print('{0}. {1}'.format(i+1,shopping_list[i]))

def add_item():
    count = 0
    item = None
    while item != 'DONE' or item != 'Done' or item != 'done':
        if count > 0:
            item = input('Add more item: ')
            if item == 'Show' or item == 'SHOW' or item == 'show':
                display(shopping_list)
            elif item == 'HELP' or item == 'help' or item == 'Help':
                instruction()
            else:
                shopping_list.append(item)
                count -=1
                    
        item = input('Add item: ')
        if item == 'Show' or item == 'SHOW' or item == 'show':
            display(shopping_list)
        elif item == 'HELP' or item == 'help' or item == 'Help':
                instruction()
        else:
            shopping_list.append(item)
            count += 1

instruction()
add_item()
display(shopping_list)

    
    
    