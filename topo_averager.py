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
data = pd.DataFrame(list(zip(precisions, recalls, region, img_no)), columns=['täpsus', 'saagis', 'regioon', 'ruudu number'])
est_data = data.loc[data['regioon']=="Eesti linnadel treenitud"]
global_data = data.loc[data['regioon']=="Globaalsetel linnadel treenitud"]
print(global_data.head(10))
pre_avg_p = data.loc[data['regioon']=="Eesti linnadel treenitud", 'täpsus'].mean()
non_avg_p = data.loc[data['regioon']=="Globaalsetel linnadel treenitud", 'täpsus'].mean()
pre_avg_r = data.loc[data['regioon']=="Eesti linnadel treenitud", 'saagis'].mean()
non_avg_r = data.loc[data['regioon']=="Globaalsetel linnadel treenitud", 'saagis'].mean()


sns.set_theme(style="white")
fig, (ax1, ax2) = plt.subplots(1, 2, sharey='col')
ax1 = sns.barplot(x='ruudu number', y='täpsus', hue='regioon', data=est_data, linewidth=2.5)
ax2 = sns.barplot(x='ruudu number', y='täpsus', hue='regioon', data=global_data, linewidth=2.5)
#ax.text(1, 1,'mean precision, estonian trained model = ' + str(pre_avg_p) + '\nand global trained model = ' + str(non_avg_p), fontsize=9)
plt.show()
#sv_plot = ax.get_figure()
#sv_plot.savefig(path + 'precision_comparison.png')
print('mean precision, estonian trained model = ' + str(pre_avg_p) + '\nand global trained model = ' + str(non_avg_p))

ax2 = sns.barplot(x='ruudu number', y='saagis', hue='regioon', data=data, linewidth=2.5)
ax2.text(1, 0.7,'mean recall, estonian trained model = ' + str(pre_avg_r) + '\nand global trained model = ' + str(non_avg_r), fontsize=9)
plt.show()
print('mean recall, estonian model = ' + str(pre_avg_r) + '\nand global trained model = ' + str(non_avg_r))

#sv_plot = ax2.get_figure()
#sv_plot.savefig(path + 'recall_comparison.png')











