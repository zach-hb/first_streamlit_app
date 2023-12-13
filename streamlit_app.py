import streamlit
import pandas as pd
import requests
import snowflake.connector

# restaurant menu
streamlit.title('Our New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# import data from s3 bucket txt file
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# pick list so user can pick fruit they want
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))
# filter out selected fruits
remaining_fruits = my_fruit_list.drop(fruits_selected, errors='ignore')

# display the entire dataframe excluding selected fruits
streamlit.dataframe(remaining_fruits)

# new section for fruityvice api response
streamlit.header ('Fruityvice Fruit Advice!')
fruit = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit)

fruit_response = requests.get("https://fruityvice.com/api/fruit/"+fruit)

# normalize json response
fv_normalized = pd.json_normalize(fruit_response.json())
streamlit.dataframe(fv_normalized)


streamlit.text(fruit_response)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains")
streamlit.text(my_data_row)
