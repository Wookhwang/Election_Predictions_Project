import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np
import pandas as pd

# Make graph font English to Korean
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
R_app = [0.34, 0.34, 0.34]
L_app = [0.57, 0.66, 0.25]
Ri_app = [0.40, 0.65, 0.77]
E_app = [0.55, 0.66, 0.35]

label = ['Naver', 'Youtube', 'Twitter']

plt.figure()

x = np.arange(len(label))

plt.bar(x-0.8, R_app, label='실제 지지율', width=0.2)
plt.bar(x-0.6, L_app, label='Lasso', width=0.2)

plt.bar(x-0.4, Ri_app, label='Ridge', width=0.2)
plt.bar(x-0.2, E_app, label='Elastic Net', width=0.2)
plt.xticks(x-0.5, label)

plt.legend()
plt.xlabel('플렛폼')
plt.ylabel('지지율')
plt.ylim(0, 0.9)
plt.title('21대 총선 미래 통합당 예측 지지율')

plt.savefig('M.png')
plt.show()

"""

plt.bar('실제 지지율', 0.60,  label='실제 지지율',color='blue',)
plt.bar('Lasso', 0.42,  label='실제 지지율',color='red',)
plt.bar('Ridge', 0.54,  label='실제 지지율',color='red',)
plt.bar('Elastic Net', 0.44, label='실제 지지율',color='red',)

plt.xlabel('모델')
plt.ylabel('지지율')
#plt.show()


df = pd.read_csv('C:/Users/khw08/Desktop/graph.csv', encoding='utf-8-sig')
print(df)
df.plot(kind='bar')
label = ['Thur', 'Fri', 'Sat']
index = np.arange(len(label))
plt.show()
"""