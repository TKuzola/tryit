'''
Created on May 2, 2018

@author: Anthony Local
'''
import random


def items_list(items, bin_string):
    inventory = []
    for i, c in enumerate(bin_string):
        if c == '1':
            inventory.append(items[i])
    return(inventory)

# generate all combinations of N items


def powerSet(items):
    N = len(items)
    bin_format = '0{0}b'.format(N)
    print(bin_format)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        print("i = ", format(i, bin_format))
        print(items_list(items, format(i, bin_format)))
        combo = []
        for j in range(N):
            # print("j = ", j)
            # test bit jth of integer i
            # print("i >> j = ", (i >> j))
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        # print('exiting')
        yield combo


def yieldBag2Combos(items):
    N = len(items)
    bin_format = '0{0}b'.format(N)
    print(bin_format)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        print("bag 2 i = ", format(i, bin_format))
        bag2 = items_list(items, format(i, bin_format))
        yield bag2


def yieldAllCombos(items):
    N = len(items)
    bit_format = '0{0}b'.format(N)
    bit_all_items = (2**N) - 1
    print(bit_format)
    print(format(bit_all_items, bit_format))
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        print("bag 1 i = ", format(i, bit_format))
        print(format(i ^ bit_all_items, bit_format))
        bag1 = items_list(items, format(i, bit_format))
        items_bag2 = items, format(i, bit_format)
        bit_format_bag2 = '0{0}b'.format(len(items_bag2))
        for j in range(2**len(items_bag2)):
            bag2 = items_list(items, format(j, bit_format_bag2))
            print('bag1')
            print(bag1)
            yield bag2


peeps = ['fred', 'bryan', 'mark', 'joe']

# look = items_list(peeps,'1001')
# print(look)
first = yieldAllCombos(peeps)
for x in first:
    print('bag2')
    print(x)

horses = [7, 7, 7, 11, 11, 11, 14, 14, 14, 5, 5, 6, 6, 6, 16, 16, 16, 18, 18, 9, 10, 8, 20]

for x in range(20):
    print(random.choice(horses), random.choice(horses), random.choice(horses), random.choice(horses))

for x in range(20):
    print(random.choice(horses), random.choice(horses), random.choice(horses))
