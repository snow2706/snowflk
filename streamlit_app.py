import streamlit
import pandas
import requests


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
streamlit.header('Fruit vice Advice')
fruit_choice = streamlit.text_input('What fruit you like','Kiwi')
streamlit.write('User enter Choice',fruit_choice)

fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

# take json response 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text("Fruit load list contain")
streamlit.text(my_data_row)
