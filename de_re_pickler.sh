#!/bin/bash
echo "run"
for i in $(seq 0 1 33)
do
    echo "on image nr $i rn"
    python3 pickle_protocol_changer.py -i ../../cuda10/dev_kristjan/results/orto_infer/raw/graph_"$i"graph.p -o ../../cuda10/dev_kristjan/results/orto_infer/raw/graph_"$i"graph.p
done
