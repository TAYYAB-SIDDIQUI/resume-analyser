import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.ensemble import RandomForestClassifier
import warnings
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding ,LSTM,Dense,Dropout,Flatten
warnings.filterwarnings("ignore")
df=pd.read_csv("Data for project level\projects_level.csv")
df.head()
df.dropna(inplace=True)
df.drop(columns=["Unnamed: 0"],inplace=True)
df.drop_duplicates(subset=["name"],inplace=True)
x=df["name"]
y=df["Level"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)
model=make_pipeline(CountVectorizer(),MultinomialNB())
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(f"accuracy :\n {accuracy_score(y_test,y_pred)} ")
model2=make_pipeline(CountVectorizer(),LogisticRegression())
model2.fit(x_train,y_train)
y_pred2=model2.predict(x_test)
print(f"accuracy :\n {accuracy_score(y_test,y_pred2)}")
model3=make_pipeline(CountVectorizer(),DecisionTreeClassifier())
model3.fit(x_train,y_train)
y_pred3=model3.predict(x_test)
print(f"accuracy :\n {accuracy_score(y_test,y_pred3)}")
model4=make_pipeline(CountVectorizer(),RandomForestClassifier())
model4.fit(x_train,y_train)
y_pred2=model4.predict(x_test)
print(f"accuracy :\n {accuracy_score(y_test,y_pred2)}")
oe=LabelBinarizer()
y=oe.fit_transform(np.array(df["Level"]).reshape(-1,1))
vector=CountVectorizer(max_features=1000)
x=vector.fit_transform(df["name"]).toarray()
model=Sequential([
    Dense(128,activation="relu",
          input_shape=(x.shape[1],)),
    Dense(64,activation="relu"),
    Dense(len(oe.classes_),activation="softmax")
])
model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])
model.fit(x,y,epochs=50)
model.save("neunetforpr.h5")
import joblib
joblib.dump(vector,"CountVector.pkl")