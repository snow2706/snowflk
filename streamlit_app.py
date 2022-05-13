import streamlit
import pandas

streamlit.title('Hello Snowflake')
streamlit.title('Learing the new things')
streamlit.header('Dataware Housing')
streamlit.text('Good data management')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Pick up list 
streamlit.multiselect('Pick some fruit',list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
