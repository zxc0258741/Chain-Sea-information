import pyspark  
from pyspark import SparkConf, SparkContext
from pyspark.mllib.clustering import KMeans
from pyspark.mllib.clustering import KMeansModel
from numpy import array




conf = SparkConf()

conf.setMaster('yarn-client')

conf.setAppName('spark-yarn')

sc = SparkContext(conf=conf)

data=sc.textFile("hdfs:///user/cloudera/kmeans/bbbbbbb.txt")
parsedata=data.map(lambda line:array([float(x) for x in line.split(', ')]))
#print parsedata.collect()
c = KMeans.train(parsedata, 3, maxIterations=10, runs=1, initializationMode="random")

print '--------------------'
print c.clusterCenters
print '--------------------'
