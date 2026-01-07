import streamlit as st

st.title("My First Streamlit App 🚀")
st.write("Hello, Streamlit!")

#Showing text & data
st.header("Text examples")
st.text("Plain text")
st.markdown("**Bold**, *italic*, `code`")

st.header("Data")
st.write({"name": "Alex", "age": 15})
st.write([1, 2, 3, 4])

#User input (buttons, sliders, text)
#button
if st.button("Click me"):
    st.success("Button clicked!")

#Slider
age = st.slider("Select your age", 5, 18, 15)
st.write("Your age is:", age)

#Text input
name = st.text_input("Enter your name")
if name:
    st.write(f"Hello {name} 👋")

#Layout (columns & sidebar)
#Sidebar
st.sidebar.title("Menu")
choice = st.sidebar.selectbox("Choose", ["Home", "About"])
st.write("You chose:", choice)

#Columns
col1, col2 = st.columns(2)

with col1:
    st.button("Left")

with col2:
    st.button("Right")

#Display images & charts
#images
from PIL import Image

img = Image.open("image.png")
st.image(img, caption="My image")

# uploading text file
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.text(content)

#text area
text = st.text_area(placeholder="Type here...",
    height=150)

st.write("You typed:")
st.write(text)
