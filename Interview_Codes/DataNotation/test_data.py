import numpy as np

File = np.genfromtxt('test.txt',
                     delimiter=',',
                     names=True,
                     encoding='utf-8',
                     filling_values=np.nan)

print(File)
