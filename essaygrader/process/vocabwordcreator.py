import numpy as np
import re

data = np.array([])
with open("VW.csv", "r", encoding="utf8") as f:
    for line in f:
        line = line.split(sep = "   ")
        line1=line[0]

        line1 = line1.split()
        line1 = line1[0]
        if bool(re.search('[^a-zA-Z]',line1)):
            continue

        line1=np.array(line1)
        data=np.append(line1, data)

np.save('vocabularywords.npy',data,allow_pickle=True)
