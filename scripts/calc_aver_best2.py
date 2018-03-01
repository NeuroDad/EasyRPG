import numpy as np
import pylab as plt

sum1 = 0
sum2 = 0
sum3 = 0
s = 0
array_3 = np.zeros((25,))
array_2 = np.zeros((25,))
array_1 = np.zeros((25,))
for i in range(1,7):
  for j in range(1,7):
    for k in range(1,7):
        a = np.array([i,j,k])
        a = np.sort(a)

        erg = a[-3:].sum()
        sum3 += erg
        array_3[erg] += 1

        erg = a[-2:].sum()
        sum2 += erg
        array_2[erg] += 1

        erg = a[-1:].sum()
        sum1 += erg
        array_1[erg] += 1

        s += 1
print float(sum1)/float(s)
print float(sum2)/float(s)
print float(sum3)/float(s)
plt.subplot(311)
plt.plot(array_1)
plt.subplot(312)
plt.plot(array_2)
plt.subplot(313)
plt.plot(array_3)
plt.show()