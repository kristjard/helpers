import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

path = "../results/orto_infer/metrics/test1/"
precisions = []
recalls = []
region = []
img_no = []
for i in range(1, 17):
    filename = "../results/orto_infer/metrics/helper_files/topotexts/toporesult_" + str(i) + ".txt"
    with open(filename) as f:
        for line in f:
            pass
        region.append("Eesti linnadel treenitud")
        img_no.append(i)
        last_line = line
        last_line_split = last_line.split(sep=' ')
        for j in range(len(last_line_split)):
            value = float(last_line_split[j].split(sep='=')[1])
            if j % 2 == 0:
                precisions.append(value)
            else:
                recalls.append(value)
for i in range(1, 10):
    filename = "../results/est_infer/metrics/retrained_g300-600/helper_files/topotexts/toporesult_" + str(i) + ".txt"
    with open(filename) as f:
        for line in f:
            pass
        region.append("Globaalsetel linnadel treenitud")
        img_no.append(i)
        last_line = line
        last_line_split = last_line.split(sep=' ')
        for j in range(len(last_line_split)):
            value = float(last_line_split[j].split(sep='=')[1])
            if j % 2 == 0:
                precisions.append(value)
            else:
                recalls.append(value)
xs1 = range(1, 17)
xs2 = range(1, 10)
print(xs1, xs2)
data = pd.DataFrame(list(zip(precisions, recalls, region, img_no)), columns=['täpsus', 'saagis', 'regioon', 'ruudu number'])
est_data = data.loc[data['regioon']=="Eesti linnadel treenitud"]
global_data = data.loc[data['regioon']=="Globaalsetel linnadel treenitud"]
pre_avg_p = data.loc[data['regioon']=="Eesti linnadel treenitud", 'täpsus'].mean()
non_avg_p = data.loc[data['regioon']=="Globaalsetel linnadel treenitud", 'täpsus'].mean()
pre_avg_r = data.loc[data['regioon']=="Eesti linnadel treenitud", 'saagis'].mean()
non_avg_r = data.loc[data['regioon']=="Globaalsetel linnadel treenitud", 'saagis'].mean()

est_precisions = est_data['täpsus'].to_numpy()
global_precisions = global_data['täpsus'].to_numpy()
est_recall = est_data['saagis'].to_numpy()
global_recall = global_data['saagis'].to_numpy()

fig, (ax1, ax2) = plt.subplots(1, 2, sharex='col')
a = ax1.bar(xs1, est_precisions, color='lime', align='center', width=0.4, label='treenitud eesti linnade andmetel')
b = ax2.bar(xs2, global_precisions, color='salmon', align='center', width=0.4, label='treenitud globaalsete linnade andmetel')
fig.suptitle("TOPO mõõdik")
ax1.set_xlabel("Ruudu number")
ax2.set_xlabel("Ruudu number")
ax1.set_ylabel("täpsus")
bars_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*bars_labels)]
plt.legend(lines, labels, loc='lower right')
#plt.savefig('../results/orto_infer/metrics/apls/apls_comparison_new.png')
plt.show()
print("est topo precision mean = ", pre_avg_p)
print("global TOPO precision mean = ", non_avg_p)

print("est topo recall mean = ", pre_avg_r)
print("global TOPO recall mean = ", non_avg_r)
fig, (ax1, ax2) = plt.subplots(1, 2, sharex='col')
a = ax1.bar(xs1, est_recall, color='lime', align='center', width=0.4, label='treenitud eesti linnade andmetel')
b = ax2.bar(xs2, global_recall, color='salmon', align='center', width=0.4, label='treenitud globaalsete linnade andmetel')
fig.suptitle("TOPO mõõdik")
ax1.set_xlabel("Ruudu number")
ax2.set_xlabel("Ruudu number")
ax1.set_ylabel("saagis")
bars_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*bars_labels)]
plt.legend(lines, labels, loc='lower right')
#plt.savefig('../results/orto_infer/metrics/apls/apls_comparison_new.png')
plt.show()