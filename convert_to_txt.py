import pickle
import os

path = '/home/kristjan/Documents/schola/loputoo_artiklid/graphs/'

for filename in os.listdir(path):
    try:
        text = pickle.load(open(path + filename, 'rb'))
        with open(path + filename.strip('.p') + '.txt', 'w') as f:
            f.write('{')
            for k, v in text.items():
                f.write(str(k) + ': ' + str(v) + ', ')
            f.write('}')
    except EOFError:
        break




