import streamlit  as st



numt = st.text_input('Enter the number of rows to display')
num = int(numt)
a=18
if a == num:
    st.write(True)
else:
    st.write(False)

# a = 18
# ju = st.text_input("Enter a value")
::::::::::::Input 


if ju == str(a):  # Convert to string because text_input returns string
 
 st.success('true')

else: 

    st.error('false')


:::::::::::::::::::::::::::::: Import input box 

import streamlit as st

a = 18
ju = st.text_input("Enter a value")
si = st.button("Check")
if si:
    if ju == str(a):
        st.success('True')
    else:
        st.error('False')







#Column
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    st.write("Column 1")

with col2:
    st.write("Column 2")

with col3:
    st.write("Column 3")



#Slider Bar important

a = st.sidebar.radio("Select one:", [1, 2])

tab1 = st.sidebar
with tab1:
    # Add a radio button
    selected_option = st.radio("Select one:", [1, 2])


# Download image ------------------

st.image("all.jpg", width=200)
# Function to download the image
def download_image(image_data):
    with open("all.jpg", "rb") as file:
        image_bytes = file.read()
    st.download_button(label="Download Image", data=image_bytes, file_name="all.jpg", mime="image/jpeg")

# Call the function to download the image
download_image("all.jpg")


# go the gallery  ----------------<><><><<>
url="http://google.com"
st.link_button("Go to gallery", url)


# Nav bar  --------------------------<><><><><>
st.page_link("one.py", label="Home")


#Check Box logic  --------------------<><><>
agree = st.checkbox("I agree")
if agree:
    st.write("You have agreed.")
else:
    st.write("You have not agreed.")

# Radio button
st.radio("Pick one", ["cats", "dogs"])

# select box
st.selectbox("Pick one", ["cats", "dogs"])

st.multiselect("Buy", ["milk", "apples", "potatoes"])

# slider
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])


# Inpute Box

st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.camera_input("Take a picture")
st.color_picker("Pick a color")  


################### Display Processing Function

st.balloons()
st.snow()
st.toast("Warming up...")
st.error("Error message")
st.warning("Warning message")
st.info("Info message")
st.success("Success message")


bar = st.progress(50)  #Prohess bar
time.sleep(3)
bar.progress(100)

with st.spinner(text="In progress"):
  time.sleep(3)
  st.success("Done")


with st.status("Authenticating...") as s:
  time.sleep(2)
  st.write("Some long response.")
  s.update(label="Response")
