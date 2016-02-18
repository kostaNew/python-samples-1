import numpy as np

d_type = np.dtype([('x', float), ('y', float),('z', float)])

# For text data
# np.loadtxt('data.data', dtype=d_type)

# For binary data
# np.fromfile('data.data', dtype=d_type)

data = np.loadtxt('data.data', dtype=d_type)

print data
print ""
print data['x']
print ""
print data['x'][2]
print ""
print data[2]
print ""
print data[2]['x']
print data[2][0]
