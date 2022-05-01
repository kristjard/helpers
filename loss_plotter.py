import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../Sat2Graph/model/losses.csv')

steps = data.iloc[20:, 0]
sum_loss = data.iloc[20:, 1]
sum_loss = sum_loss.clip(0, 1)
test_loss = data.iloc[20:, 2]
prob_loss = data.iloc[20:, 3]
vector_loss = data.iloc[20:, 4]
vector_loss = vector_loss.clip(0, 1)
seg_loss = data.iloc[20:, 5]


fig = plt.figure(figsize=(20, 2)) 
ax = fig.add_subplot(111)
ax.set(xlabel='steps', ylabel='loss', title='This is the LOSS')
ax.grid()
ax.plot(steps, sum_loss, 'b', label='sum loss')
ax.plot(steps, test_loss, 'g', label='test loss')
ax.plot(steps, prob_loss, 'y', label='prob loss')
ax.plot(steps, vector_loss, 'pink', label='vector loss')
ax.plot(steps, seg_loss, 'cyan', label='seg loss')
plt.legend()
# plt.show()
fig.savefig(str(steps.iloc[-1]) + '_latest_figures.png')
