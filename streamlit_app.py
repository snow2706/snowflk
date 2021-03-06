import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Hello Snowflake')
streamlit.title('Learing the new things')
streamlit.header('Dataware Housing')
streamlit.text('Good data management')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Pick up list 
my_fruit_list=my_fruit_list.set_index('Fruit')
fruit_selected = streamlit.multiselect('Pick some fruit',list(my_fruit_list.index),['Avocado','Banana'])
fruit_to_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)
# NEW Section for request

#streamlit.text(fruityvice_response.json())


def get_frutvice_data(this_fruit_chioce):
	fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+this_fruit_chioce)
	fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
	return fruityvice_normalized

streamlit.header('Fruit vice Advice')
try: 
  fruit_choice = streamlit.text_input('What fruit you like')
  if not fruit_choice:
    streamlit.error('Please select correct Fruit')
  else:
    back_from_fun=get_frutvice_data(fruit_choice)
    streamlit.dataframe(back_from_fun)
except URLError as e:
  streamlit.error()
  
#----------------------------------------------------------------------------------------
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.text("Fruit load list contain")
streamlit.dataframe(my_data_row)

#snowflake related function Snow flake function to get fruit list from table 
def get_fruit_load_data():
	with my_cnx.cursor() as my_cur:
		my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
	return my_cur.fetchall()

#add button 
try:
	if streamlit.button('Get fruit list'):
		my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
		my_data_row=get_fruit_load_data()
		streamlit.dataframe(my_data_row)
	else:
		streamlit.header('You are not select any list')
except URLError as e:
	streamlit.error()
	
########## insert function 	
def Insert_fruit_load_data(new_fruit):
	with my_cnx.cursor() as my_cur:
		my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('"+new_fruit+"')")
	return 'Thanks for adding fruit'

my_fruit_addition = streamlit.text_input('What fruit you like to add one more fruit','Kiwi')

if streamlit.button('add fruit to list'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	from_function=Insert_fruit_load_data(my_fruit_addition)
	
streamlit.write('Thank for addting ',my_fruit_addition)

	
streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.text("Fruit load list contain")
streamlit.dataframe(my_data_row)

#################Chanllage tab 
streamlit.header('Challange tab Input box')
my_fruit_addition = streamlit.text_input('What fruit you like to add one more fruit','Kiwi')
streamlit.write('Thank for addting ',my_fruit_addition)

my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('From Streamlit')")
