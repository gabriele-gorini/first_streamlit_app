import streamlit
import pandas

streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🍵 Omega 3 & Bluberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.header("🍌🥭 Build your own Fruit Smoothie 🥝🍇")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#This is a pick list the user can use to select the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#Display the list on the page
streamlit.dataframe(my_fruit_list)
