import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oat Meal')
streamlit.text('🥗Kale , Spinach & Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Strawberries','Peach'])
fruits_to_show=my_fruit_list.loc[my_fruit_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

def fruityvice_data(this_fruit):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit)
  fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
from urllib.error import URLError
import requests
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    func_response = fruityvice_data(fruit_choice)
    streamlit.dataframe(func_response)
except URLError as e:
  streamlit.error()
  
  

import snowflake.connector
streamlit.header("The Fruit load list contains:")
def get_fruit_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * FROM pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()
  
if streamlit.button('Get fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows =get_fruit_list()
  streamlit.dataframe(my_data_rows)

steamlit.stop()

add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
