import pprint
import scipy
import scipy.linalg   

A = scipy.array([ [1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12] ])
P, L, U = scipy.linalg.lu(A)

print "A:"
pprint.pprint(A)

print "P:"
pprint.pprint(P)

print "L:"
pprint.pprint(L)

print "U:"
pprint.pprint(U)