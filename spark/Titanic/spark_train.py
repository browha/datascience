import pandas as pd
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.mllib.regression import LabeledPoint
import array

sc=SparkContext("local","titanic_test")
sqlContext = SQLContext(sc)
df=pd.read_csv('Titanic_train.csv')

df['Sex']=df['Sex'].replace('female',1)
df['Sex']=df['Sex'].replace('male',0)
df['Age']=df['Age'].replace('NaN',-1)

traindf=pd.DataFrame(df,columns=['Survived','Pclass','Age','Sex','Fare'])

sdf=sqlContext.createDataFrame(traindf)
import pyspark.mllib.classification as sparkclass
temp = sdf.map(lambda x:LabeledPoint(x[0],[x[1:]]))
#Spark uses LabeledPoints. That is to say, for a particular set of features (x[1:]), we have a classification x[0]

from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
lrm=DecisionTree.trainClassifier(temp,numClasses=2, categoricalFeaturesInfo={}, impurity='gini', maxDepth=5, maxBins=32)

df=pd.read_csv('Titanic_test.csv')

df['Sex']=df['Sex'].replace('female',1)
df['Sex']=df['Sex'].replace('male',0)
df['Age']=df['Age'].replace('NaN',-1)

testdf=pd.DataFrame(df,columns=['Pclass','Age','Sex','Fare'])
testsdf=sqlContext.createDataFrame(testdf)
testtemp = testsdf.map(lambda x:x[0:])
test_predictions=lrm.predict(testtemp).collect()
print(test_predictions)
