import numpy as np
import matplotlib.pyplot as plt
 
# 円グラフを描画

x = np.array([1]*13)
plt.pie(x)
plt.savefig('test3_13.png', format="png", dpi=300)