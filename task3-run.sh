#!/bin/bash    

hadoop fs -rm -r /input
hadoop fs -rm -r /task3
hadoop fs -rm -r /output/task3

hadoop fs -mkdir /input
hadoop fs -put ./Taxis.txt /input/Taxis.txt
hadoop fs -put ./Trips.txt /input/Trips.txt


# Use taxi number and company as keys
# use -k1 as partitioner key which is taxi number
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D stream.num.map.output.key.fields=2 \
-D map.output.key.field.separator=, \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.reduce.tasks=3 \
-file ./task3-1-mapper.py \
-mapper ./task3-1-mapper.py \
-file ./task3-1-reducer.py \
-reducer ./task3-1-reducer.py \
-input /input/Trips.txt \
-input /input/Taxis.txt \
-output /task3 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop fs -getmerge /task3/part-* ./task3-join-output.txt
hadoop fs -put ./task3-join-output.txt /input/task3-join-output.txt
hadoop fs -rm -r /task3

# Use company as a key, and it is also a partition key
# To sort key values in the reducer according to company
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D stream.num.map.output.key.fields=1 \
-D map.output.key.field.separator=, \
-D mapred.text.key.partitioner.options=-k1,1 \
-D mapred.reduce.tasks=3 \
-file ./task3-2-mapper.py \
-mapper ./task3-2-mapper.py \
-file ./task3-2-reducer.py \
-reducer ./task3-2-reducer.py \
-input /input/task3-join-output.txt \
-output /output/task3 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop fs -getmerge /output/task3/part* ./task3-output.txt
hadoop fs -put ./task3-output.txt /output/task3/task3-output.txt
hadoop fs -cat /output/task3/task3-output.txt