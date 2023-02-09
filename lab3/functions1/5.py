import itertools

def permutation(s=str(input())):
    perm_set=itertools.permutations(s)
    for i in perm_set:
        print(i)
        
permutation()