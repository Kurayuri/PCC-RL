import os
import numpy as np
import matplotlib.pyplot as plt

# plt.rcParams["font.family"]=['sans-serif']
# plt.rcParams["font.sans-serif"]=['dengxian']

with open("./model/ans/reward_log.log") as f:
    txt=f.readlines()

rewards=[]
emwa_rewards=[]
for line in txt:
    line=line.split(",")
    rewards.append(float(line[1]))
    emwa_rewards.append(float(line[2]))

fig,axes = plt.subplots(1)
axes=axes
fig=fig
# axes.set_xlabel("训练回合",fontsize=14)
# axes.set_ylabel("训练奖励",fontsize=14)
axes.set_xlabel("Training Episode",fontsize=14)
axes.set_ylabel("Training Reward",fontsize=14)
axes.set_xscale("log")
axes.plot(emwa_rewards,label="Aurora")


try:
    with open("./origin/ans/reward_log.log") as f:
        txt=f.readlines()   
    rewards=[]
    emwa_rewards=[]
    for line in txt:
        line=line.split(",")
        rewards.append(float(line[1]))
        emwa_rewards.append(float(line[2]))
    axes.plot(emwa_rewards,label="Origin")
except:
    pass

axes.legend(fontsize=14)
# plt.show()
plt.savefig("reward.pdf", format="pdf")
