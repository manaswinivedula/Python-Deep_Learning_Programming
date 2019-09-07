import numpy as np
#np.zeros(2,2)

b=(np.random.randint(20, size=15))
c=(b.reshape(3,5))
print(c)
x=(np.max(c,axis=1))
l=x.reshape(-1,1)
print(l)
print(np.where(c==l,0,c))
