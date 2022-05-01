#!/bin/bash
scriptpath="../Sat2Graph/metrics/apls/"
filepath="../results/orto_infer/metrics/apls/apls_jsons/"
for i in $(seq 1 1 16)
do
	go run "$scriptpath"main.go ../results/orto_infer/metrics/apls/apls_jsons/gt"$i"_graph.json ../results/orto_infer/metrics/apls/apls_jsons/prop"$i"_graph.json ../results/orto_infer/metrics/apls/apls_texts/aplsresult"$i".txt
	echo "Progress : $i/16"
done
