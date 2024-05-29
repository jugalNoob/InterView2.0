import streamlit  as st
import time

 ######################################
st.write("jugal sharma karan")
one=["jugal" , "karan"]
st.write(one)
st.error("i am error")
st.text("Fixed width text")
st.title("My title")
st.header("My header")
st.subheader("My sub")
st.code("for i in range(8): foo()")
st.code(["1" , "2" , "3"])

st.json({"foo":"bar","fu":"ba"})
st.metric("My metric", 42, 2)


st.image("all.jpg", width=200)


st.html("<h1>Hi!</h1>")



tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")


tab1, tab2 = st.tabs(['one' , 'two'])

with tab1:
    # if st.button("Check CSV"):
        df = pd.read_csv("earth.csv")
        st.write(df)

with tab2:
    st.write("This is tab 1")
    st.write("This is tab 2")



tab1, tab2 = st.tabs(['one' , 'two'])

with tab1:
    # if st.button("Check CSV"):
        df = pd.read_csv("earth.csv")
        st.write(df)

with tab2:
    st.write("This is tab 1")
    st.write("This is tab 2")
