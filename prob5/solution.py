import sys
import numpy as np
sys.path.append('..')
import biblioteca as bib

test=[[2, 3, 5], [3, 27, 9], range(1, 11), range(1, 21) ]

for valores in test:
    mmc=bib.mmc(np.array(valores))
    print('{} -> {}'.format(valores, mmc))