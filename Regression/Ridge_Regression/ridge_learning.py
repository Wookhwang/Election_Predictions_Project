"""
Regression_program

- train_data = 21대 총선 자료,

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from pandas import Series
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge, ElasticNet

# Make graph font English to Korean
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


# Training & Test Data Load
train_data = pd.read_csv('/KoNLPY_M&D_train_CSV_2.csv')

#Train = train_data.sample(n=4000)
#Test = train_data.sample(n=2500)
# Na Data dop
train_data.dropna()
'''
# Arrange Data Set
#x = train_data.drop(['d'], axis=1)
x = Train.drop(['d'], axis=1)
x_2 = x.drop(['m'], axis=1)
#y = train_data.loc[:, ['d']]
y = Train.loc[:, ['d']]

xt = Test.drop(['d'], axis=1)
x_2t = xt.drop(['m'], axis=1)
#y = train_data.loc[:, ['d']]
yt = Test.loc[:, ['d']]
'''

#

#x = train_data.drop(['d'], axis=1)
x = train_data.drop(['d'], axis=1)
x_2 = x.drop(['m'], axis=1)
#y = train_data.loc[:, ['d']]
y = train_data.loc[:, ['d']]


# 내가 한 태깅 789까지임
'''
x_train = x_2.loc[:, :]
y_train = y.loc[:, :]

x_test = x_2t.loc[3500:6200, :]
y_test = yt.loc[3500:6200, :]
'''

x_train = x_2.loc[1000:6000, :]
y_train = y.loc[1000:6000, :]

x_test = x_2.loc[2000:5000, :]
y_test = y.loc[2000:5000, :]

#x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1)    # Split Data Set
predictors = x_train.columns                                                # Save tarin_X attributes

"""
Lasso Regression
lassoReg   = Coefficient List
predictors = Attributes List
coef       = DataFrame with Attributes & Coefficient
pre_coef   = Except Zero Coefficient Value List
"""

'''
ridgeReg = Ridge(alpha=0.001)                                           # Call Lasso Regression Function
ridgeReg.fit(x_train, y_train)                                              # Fit Data in Lasso function

ridgeData = np.array(ridgeReg.coef_).flatten().tolist() # 데어터 전처리

coef = Series(ridgeData, predictors).sort_values()                          # Save Coefficient
print(np.sum(ridgeReg.coef_ != 0))                                          # Check the number of valid Coefficient
coef_pre = coef[coef != 0.0][coef != -0.0]                                  # Except Zero Coefficient


coef_pre.plot(kind='bar')                                                   # Show Graph Coefficient formed by Bar
plt.show()
'''
alpha_set = [0.00001, 0.0001, 0.001, 0.01, 0.1, 1]
max_inter_set = [100000000, 10000000, 1000000, 100000, 10000, 1000]

train_score = []
test_score = []
used_feature = []

for a, m in zip(alpha_set, max_inter_set):

    lasso = Ridge(alpha=a, max_iter=m).fit(x_train, y_train)

    la_tr_score = round(lasso.score(x_train, y_train), 3)

    la_te_score = round(lasso.score(x_test, y_test), 3)

    number_used = np.sum(lasso.coef_ != 0)



    train_score.append(la_tr_score)

    test_score.append(la_te_score)

    used_feature.append(number_used)



index = np.arange(len(alpha_set))

bar_width = 0.35

plt.bar(index, train_score, width=bar_width, label='train')

plt.bar(index+bar_width, test_score, width=bar_width, label='test')

plt.xticks(index+bar_width/2, alpha_set) # bar그래프 dodge를 하기 위해 기준값에 보정치를 더해줍니다.



for i, (ts, te) in enumerate(zip(train_score, test_score)):

    plt.text(i, ts+0.01, str(ts), horizontalalignment='center')

    plt.text(i+bar_width, te+0.01, str(te), horizontalalignment='center')



plt.legend(loc=1)

plt.xlabel('alpha')

plt.ylabel('score')

plt.show()