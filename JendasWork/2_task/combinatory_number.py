#!/usr/bin/env python

def permutation(l):
    if len(l) == 1:
        return [l]
    else:
        perm_list = []
        for e in l:
            tmp_l = list(l)
            tmp_l.remove(e)
            for perm in permutation(tmp_l):
                perm.insert(0, e)
                perm_list.append(perm)
    return perm_list


def combination(l, k, repete = False):
    if k == 1:
        return [[i] for i in l]
    else:
        ret_list = []
        for i, e in enumerate(l[:]):
            if not repete:
                i = 0
                l.remove(e)
            for comb in combination(l[i:], k-1, repete=repete):
                comb.insert(0, e)
                ret_list.append(sorted(comb))
        return sorted(ret_list)


def variation(l, k, repete = False):
    if k == 1:
        return [[i] for i in l]
    else:
        perm_list = []
        for e in l:
            tmp_l = list(l)
            if not repete:
                tmp_l.remove(e)
            for var in variation(tmp_l, k-1, repete=repete):
                var.insert(0, e)
                perm_list.append(var)
    return sorted(perm_list)


def nice_print(l):
    for comb in l:
        print "    " + "".join(comb)
    print

if __name__ == "__main__":
    print "Permutations"
    nice_print(permutation(["a", "b"]))
    print "Combinations"
    nice_print(combination(["a", "b"], 3, repete=1))
    print "Variations"
    nice_print(variation(  ["a", "b"], 4, repete=1))