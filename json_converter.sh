#!/bin/bash
for i in $(seq 1 1 16)
do
	python2 ../Sat2Graph/metrics/apls/convert.py ../results/orto_infer/raw/infered_"$i"_graph.p ../results/orto_infer/metrics/apls/apls_jsons/prop"$i"_graph.json
	python2 ../Sat2Graph/metrics/apls/convert.py ../results/orto_infer/raw/graph_"$i"graph.p ../results/orto_infer/metrics/apls/apls_jsons/gt"$i"_graph.json
	echo "Progress: $i/16"
done
