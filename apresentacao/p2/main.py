import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


type = 4
size = 20
variation = 5
shift = 3

a = np.arange(size)

if type == 0:
    b = a.copy()
    np.random.shuffle(b)
elif type == 1:
    b = a[::-1]
elif type == 2:
    b = np.argsort(a + np.random.randint(-variation, variation + 1, size))
elif type == 3:
    b = np.concatenate((a[-shift:], a[:-shift]))
elif type == 4:
    b = np.stack((a[1::2], a[::2]), axis=1).reshape(size)

kendall = stats.kendalltau(a, b)[0]
spearman = stats.spearmanr(a, b)[0]

fig = plt.figure()
ax = fig.add_subplot(111)
plt.scatter(a, b)
plt.text(0.98, 0.09, ('Kendall: %f' % kendall), horizontalalignment='right', transform=ax.transAxes)
plt.text(0.98, 0.04, ('Spearman: %f' % spearman), horizontalalignment='right', transform=ax.transAxes)
plt.show()

print(a)
print(b)

print(' Kendall: %f' % kendall)
print('Spearman: %f' % spearman)
