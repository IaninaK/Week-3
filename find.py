'''
Prints out the positions of the letter "f" within a given string

    Given:
    a(str): a string
    
    Output:
    index of the letter "f" (int): if the letter appears once,
    only one index should be included in the responce. If there are
    two or more letters, the output will contain the first and last
    indexes. If "f" is not found, the outpu will be blank
'''
# fyi I could not use the count function or any loops for this exersise 

a = input()
pos = a.find('f')
if pos >= 0:  # we need to make sure that the letter was found
    b = a[::-1] # in order to find the last index, the string needs to be in reverse
    posB = b.find('f')
    realB = len(a) - 1 - posB # translating the index of the reverse string into its normal counterpart
    if posB >= 0 and realB != pos: # making sure that there isn't only one letter
        print(pos, realB)
    else:
        print(pos)
    