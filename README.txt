Sukhum Boondecharak
S3940976

Instructions:

1. Go to the local directory where all the files are
2. From your local directory: scp -r task-* jumphost:~/
3. ssh jumphost
4. From jumphost: scp -r task-* hadoop:~/
5. ssh hadoop
6. Make sure you have hadoop-streaming-3.1.4.jar in hadoop:~/
7. chmod +x *.sh
8. ls to check if .sh files are executable
9. ./run.sh: run.sh = shell script name

The above instruction are with the expectation that you have created an EMR master node in hadoop.
If it is not the case, from your jump host: ./create_cluster.sh and wait about 15 minutes.