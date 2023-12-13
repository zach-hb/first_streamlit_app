import streamlit
import pandas as pd
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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# filter out selected fruits
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),key='Lime')
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display df on page
streamlit.dataframe(fruits_to_show)
