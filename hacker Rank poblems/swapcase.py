
'''
# input
HackerRank.com presents "Pythonist 2".
# output
hACKERrANK.COM PRESENTS "pYTHONIST 2".
'''

# my soution

def swap_case(s):
    value = ("".join(map(str.swapcase, s)))
    return value

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)