import matplotlib.pyplot as plt

pretrained_apls_list = []
retrained_apls_list = []
for i in range(1, 17):
    filename = '../results/orto_infer/metrics/apls/apls_texts/aplsresult' + str(i) + '.txt'
    with open(filename) as f:
        for line in f:
            pass
        apls = float(line.split(' ')[2])
        pretrained_apls_list.append(apls)

for i in range(1, 10):
    filename = '../results/est_infer/metrics/retrained_g300-600/helper_files/apls_texts/aplsresult' + str(i) + '.txt'
    with open(filename) as f:
        for line in f:
            pass
        apls = float(line.split(' ')[2])
        retrained_apls_list.append(apls)
fig, (ax1, ax2) = plt.subplots(1, 2, sharey='col')
xs1 = range(1, 17)
xs2 = range(1, 10)
a = ax1.bar(xs1, pretrained_apls_list, color='lime', align='center', width=0.4, label='treenitud eesti linnade andmetel')
b = ax2.bar(xs2, retrained_apls_list, color='salmon', align='center', width=0.4, label='treenitud globaalsete linnade andmetel')

fig.suptitle("Mudeli võrdlus APLS mõõdiku järgi")
ax1.set_xlabel("Ruudu number")
ax2.set_xlabel("Ruudu number")
ax1.set_ylabel("Normaliseeritud pikkuste erinevus")
bars_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
lines, labels = [sum(lol, []) for lol in zip(*bars_labels)]
plt.legend(lines, labels, loc='lower right')
#plt.savefig('../results/orto_infer/metrics/apls/apls_comparison_new.png')
plt.show()
print("est apls mean = ", sum(pretrained_apls_list) / len(pretrained_apls_list))
print("global apls mean = ", sum(retrained_apls_list) / len(retrained_apls_list))
