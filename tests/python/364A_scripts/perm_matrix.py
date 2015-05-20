# Data file for graph isomorphism problem. A and B are adjacency matrices
# of two isomorphic graphs

import numpy as np
from cvxpy import *
A = np.array(np.mat(
'0  1  0  0  0  0  1  0  0  0  1  1  1  0  0  1  0  1  1  0  1  1  0  1  0  1  1  1  0  1;\
 1  0  0  0  0  0  1  1  0  0  1  0  1  0  0  1  1  0  0  0  0  0  0  0  1  0  0  1  1  0;\
 0  0  0  1  1  1  0  0  0  0  1  1  0  1  0  1  0  0  0  1  1  0  1  0  1  1  0  1  1  0;\
 0  0  1  0  0  1  0  0  1  0  0  0  1  1  0  0  0  1  1  1  1  0  0  1  0  0  0  1  0  1;\
 0  0  1  0  0  1  0  0  1  1  0  0  0  0  0  1  0  0  1  0  0  0  0  1  1  0  1  0  0  1;\
 0  0  1  1  1  0  0  1  0  1  1  1  1  0  1  0  1  1  1  1  1  1  1  1  1  1  0  1  1  1;\
 1  1  0  0  0  0  0  1  1  0  0  1  0  0  0  1  0  0  1  0  0  1  0  0  0  0  1  0  1  1;\
 0  1  0  0  0  1  1  0  0  1  1  0  0  1  0  1  0  0  1  0  0  1  1  1  0  1  0  1  0  0;\
 0  0  0  1  1  0  1  0  0  1  1  0  0  1  1  1  1  1  1  0  1  0  0  1  0  0  0  1  0  1;\
 0  0  0  0  1  1  0  1  1  0  0  0  1  1  0  1  0  0  0  0  0  1  0  1  0  0  0  0  0  0;\
 1  1  1  0  0  1  0  1  1  0  0  1  0  0  0  0  1  0  0  0  1  1  0  1  0  1  1  1  0  1;\
 1  0  1  0  0  1  1  0  0  0  1  0  0  0  0  0  1  1  0  0  0  0  0  0  1  0  0  1  1  0;\
 1  1  0  1  0  1  0  0  0  1  0  0  0  1  1  1  0  0  0  0  1  0  1  0  1  1  0  1  1  0;\
 0  0  1  1  0  0  0  1  1  1  0  0  1  0  0  1  0  0  1  0  1  0  0  1  0  0  0  1  0  1;\
 0  0  0  0  0  1  0  0  1  0  0  0  1  0  0  1  0  0  1  1  0  0  0  1  1  0  1  0  0  1;\
 1  1  1  0  1  0  1  1  1  1  0  0  1  1  1  0  0  1  0  1  1  1  1  1  1  1  0  1  1  1;\
 0  1  0  0  0  1  0  0  1  0  1  1  0  0  0  0  0  1  1  0  0  1  0  0  0  0  1  0  1  1;\
 1  0  0  1  0  1  0  0  1  0  0  1  0  0  0  1  1  0  0  1  0  1  1  1  0  1  0  1  0  0;\
 1  0  0  1  1  1  1  1  1  0  0  0  0  1  1  0  1  0  0  1  1  0  0  1  0  0  0  1  0  1;\
 0  0  1  1  0  1  0  0  0  0  0  0  0  0  1  1  0  1  1  0  0  1  0  1  0  0  0  0  0  0;\
 1  0  1  1  0  1  0  0  1  0  1  0  1  1  0  1  0  0  1  0  0  1  0  0  0  0  1  0  0  0;\
 1  0  0  0  0  1  1  1  0  1  1  0  0  0  0  1  1  1  0  1  1  0  0  0  0  0  1  1  0  0;\
 0  0  1  0  0  1  0  1  0  0  0  0  1  0  0  1  0  1  0  0  0  0  0  1  1  1  0  0  0  0;\
 1  0  0  1  1  1  0  1  1  1  1  0  0  1  1  1  0  1  1  1  0  0  1  0  0  1  0  0  1  0;\
 0  1  1  0  1  1  0  0  0  0  0  1  1  0  1  1  0  0  0  0  0  0  1  0  0  1  0  0  1  1;\
 1  0  1  0  0  1  0  1  0  0  1  0  1  0  0  1  0  1  0  0  0  0  1  1  1  0  0  1  0  1;\
 1  0  0  0  1  0  1  0  0  0  1  0  0  0  1  0  1  0  0  0  1  1  0  0  0  0  0  1  1  0;\
 1  1  1  1  0  1  0  1  1  0  1  1  1  1  0  1  0  1  1  0  0  1  0  0  0  1  1  0  0  1;\
 0  1  1  0  0  1  1  0  0  0  0  1  1  0  0  1  1  0  0  0  0  0  0  1  1  0  1  0  0  1;\
 1  0  0  1  1  1  1  0  1  0  1  0  0  1  1  1  1  0  1  0  0  0  0  0  1  1  0  1  1  0'))

B = np.array(np.mat(
'0  1  0  1  1  1  1  1  1  1  0  1  1  0  1  1  1  0  1  0  1  1  1  1  1  1  0  1  0  1;\
 1  0  1  0  0  0  1  0  1  0  0  0  0  1  0  1  0  1  1  1  0  0  1  1  1  0  0  1  0  0;\
 0  1  0  0  1  0  1  0  1  0  0  0  0  0  0  1  0  1  0  1  1  0  0  0  0  0  0  1  0  1;\
 1  0  0  0  1  0  0  0  1  0  1  1  0  0  0  1  1  1  1  1  1  1  0  1  0  0  0  1  1  0;\
 1  0  1  1  0  0  0  1  0  0  1  0  0  1  0  0  1  0  1  0  0  1  0  0  0  1  0  0  0  0;\
 1  0  0  0  0  0  1  1  1  1  0  1  1  1  1  0  0  0  1  0  1  0  0  0  0  0  0  1  1  1;\
 1  1  1  0  0  1  0  0  1  0  1  0  1  0  1  1  1  1  0  0  0  1  0  1  0  0  1  1  0  0;\
 1  0  0  0  1  1  0  0  0  1  0  0  1  1  1  0  1  0  0  0  1  0  0  0  0  1  1  0  0  1;\
 1  1  1  1  0  1  1  0  0  0  1  1  0  1  0  0  0  1  0  0  0  0  0  0  0  1  0  0  1  0;\
 1  0  0  0  0  1  0  1  0  0  0  0  1  1  0  0  0  0  0  0  0  1  1  1  0  1  0  0  0  0;\
 0  0  0  1  1  0  1  0  1  0  0  1  0  1  0  1  1  0  0  1  1  1  1  0  1  0  0  1  1  0;\
 1  0  0  1  0  1  0  0  1  0  1  0  0  0  0  0  1  0  1  0  0  1  1  0  0  1  0  1  1  0;\
 1  0  0  0  0  1  1  1  0  1  0  0  0  1  0  0  1  1  0  0  0  1  1  1  0  1  0  1  0  0;\
 0  1  0  0  1  1  0  1  1  1  1  0  1  0  0  0  1  1  1  1  1  1  1  1  1  1  1  1  1  1;\
 1  0  0  0  0  1  1  1  0  0  0  0  0  0  0  1  0  1  0  1  0  0  1  0  0  0  0  1  0  1;\
 1  1  1  1  0  0  1  0  0  0  1  0  0  0  1  0  1  0  0  0  0  0  1  0  0  0  1  0  0  1;\
 1  0  0  1  1  0  1  1  0  0  1  1  1  1  0  1  0  1  0  1  1  0  0  0  0  0  0  1  1  1;\
 0  1  1  1  0  0  1  0  1  0  0  0  1  1  1  0  1  0  0  1  0  1  1  0  0  1  1  1  0  0;\
 1  1  0  1  1  1  0  0  0  0  0  1  0  1  0  0  0  0  0  0  0  1  1  0  0  0  0  0  0  0;\
 0  1  1  1  0  0  0  0  0  0  1  0  0  1  1  0  1  1  0  0  0  0  0  1  0  0  1  0  0  1;\
 1  0  1  1  0  1  0  1  0  0  1  0  0  1  0  0  1  0  0  0  0  1  0  0  1  0  0  0  0  0;\
 1  0  0  1  1  0  1  0  0  1  1  1  1  1  0  0  0  1  1  0  1  0  1  1  1  0  0  0  1  1;\
 1  1  0  0  0  0  0  0  0  1  1  1  1  1  1  1  0  1  1  0  0  1  0  0  0  0  0  1  0  0;\
 1  1  0  1  0  0  1  0  0  1  0  0  1  1  0  0  0  0  0  1  0  1  0  0  1  0  1  1  1  0;\
 1  1  0  0  0  0  0  0  0  0  1  0  0  1  0  0  0  0  0  0  1  1  0  1  0  1  0  0  1  0;\
 1  0  0  0  1  0  0  1  1  1  0  1  1  1  0  0  0  1  0  0  0  0  0  0  1  0  1  1  1  1;\
 0  0  0  0  0  0  1  1  0  0  0  0  0  1  0  1  0  1  0  1  0  0  0  1  0  1  0  1  0  1;\
 1  1  1  1  0  1  1  0  0  0  1  1  1  1  1  0  1  1  0  0  0  0  1  1  0  1  1  0  1  0;\
 0  0  0  1  0  1  0  0  1  0  1  1  0  1  0  0  1  0  0  0  0  1  0  1  1  1  0  1  0  0;\
 1  0  1  0  0  1  0  1  0  0  0  0  0  1  1  1  1  0  0  1  0  1  0  0  0  1  1  0  0  0'))

n = len(A)
P = Variable(n,n)
constraints = [A*P.T == P.T * A]
one = np.ones((n,1))


W = np.random.rand(n,n)

for i in range(n):
	constraints.append(one.T * P[:,i] == 1)
	constraints.append( P[i,:] * one == 1)
	for j in range(n):
		constraints.append(0 <= P[i,j] )
		constraints.append(P[i,j] <=1 )


obj = Minimize(trace(W.T * P))

prob = Problem(obj, constraints)
prob.solve()

deviations = [P.value[i,j] * (1 - P.value[i,j]) for i in range(n) for j in range(n)]

print max(deviations)

v = np.asmatrix([i+1 for i in range(n)])
print P.value * v.T