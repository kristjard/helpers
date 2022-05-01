#!/bin/bash
for i in $(seq 0 1 33)
do
	python3 ~/dev_kristjan/helpers/topo_plotter.py -i ~/cuda10/dev_kristjan/results/orto_infer/metrics/helper_files/toporesult_"$i".txt -o ~/cuda10/dev_kristjan/results/retrained_g300-600/test1/g"$i"_topo.png
	echo "progress $i/33"
done
