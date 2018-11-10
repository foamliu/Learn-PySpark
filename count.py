from pyspark import SparkContext
sc=SparkContext("local", "count app")
words=sc.parallelize(
["scala",
"java",
"hadoop",
"spark",
"akka",
"spark vs hadoop",
"pyspark",
"pyspark and spark"]
)
count=words.count()
print("Number of elements in RDD -> %i" % (count))
