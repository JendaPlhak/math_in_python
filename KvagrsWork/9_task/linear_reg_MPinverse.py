import matplotlib.pyplot as plt
from numpy import array, transpose, dot
from numpy.linalg import inv, pinv

with open('linreg.txt', 'r') as f:
    data = f.read()

data = data.split('\n')
data.pop()

x = []
y = []
for point in data:
    point = point.split(' ')
    x.append( float(point[0]) )
    y.append( float(point[1]) )

plt.plot(x, y,'ko')
plt.axis('equal')
A_t = array( [ x, [1] * len(x) ] )
A   = transpose( A_t )

A_plus = dot( inv( dot( A_t, A) ), A_t )
a, b   = dot(A_plus, y)
print a, b
plt.plot( [-8, 8], [b - 8 * a, b + 8 * a])


#B_plus  = pinv( A )
#Ba, Bb,  = dot( B_plus, y )
#print Ba, Bb
#plt.plot( [-2, 2], [Bb - 2 * Ba, Bb + 2 * Ba])
plt.savefig('linereg',format='png')