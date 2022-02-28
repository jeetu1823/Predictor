import mysql.connector
#mydb=mysql.connector.connect(host="localhost",user="root",passwd="root" ,database="data",auth_plugin='mysql_native_password')

mydb=mysql.connector.connect(host="mysql-70382-0.cloudclusters.net",user="admin",passwd="EL6FeiYX",database="user_data",auth_plugin='mysql_native_password',port="19716")

mycursor=mydb.cursor()
# mycursor.execute("insert into st values('sdjfgj')")
# mycursor.execute("select * from st")



# create_tb='''
# create table user_input(
# 	length int,
# 	width int,
# 	length1 int,
# 	width1 int,predicted_value int

# '''
# mycursor.execute(create_tb)

insert_stmt = (
"INSERT INTO input_data (Sepal_length,Sepal_width ,Petal_length ,Petal_width ,predicted_value) "
"VALUES (%s, %s, %s, %s,%s)"
)

 
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import json
# import sklearn

# loading in the model to predict on the data
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
	return 'welcome all'

 
def prediction(sepal_length, sepal_width, petal_length, petal_width):

	prediction1 = classifier.predict(
		[[sepal_length, sepal_width, petal_length, petal_width]])
	print(int(prediction1))
	s=int(prediction1[0])
	
	s1=["Setosa","Versicolour","Virginica"]
 
	# mycursor.execute(p, ([s]))



	data=(sepal_length, sepal_width, petal_length, petal_width ,(s1[s]))
	mycursor.execute(insert_stmt,data)

	return s1[s]
	

# this is the main function in which we define our webpage
def main():
	# giving the webpage a title
	st.title("Flower Prediction")
	
	# here we define some of the front end elements of the web page like
	# the font and background color, the padding and the text to be displayed
	html_temp = """
	 
	<h1 style ="color:black;text-align:center;">Flower Classification ML WebApp </h1>
	</div>
	"""
	
	# this line allows us to display the front end aspects we have
	# defined in the above code
	st.markdown(html_temp, unsafe_allow_html = True)
	
	# the following lines create text boxes in which the user can enter
	# the data required to make the prediction
	sepal_length = st.text_input("Sepal Length", "5")
	sepal_width = st.text_input("Sepal Width", "3.5")
	petal_length = st.text_input("Petal Length", "1.5")
	petal_width = st.text_input("Petal Width", "0.2")
	result =""
 
	if st.button("Predict"):
		result = prediction(sepal_length, sepal_width, petal_length, petal_width)
	st.success('The output is {}'.format(result))
	 
	
 



if __name__=='__main__':
	main()

	mydb.commit()
