import streamlit as st 
import pandas as pd 
import joblib 
import numpy as np 

st.title("Using a model to predict")

@st.cache_resource
def load_model(file):
    model_file = open(file,'rb')
    loaded_model = joblib.load(model_file)
    model_file.close()
    return loaded_model

penguin_model = load_model('penguin_dt.pkl')

st.sidebar.title('forms')
form1 = st.sidebar.form(key='inputs')

form1.subheader('Bill Length')
bill_length = form1.number_input(
    'Enter Bill Length (mm)',
    min_value=0.01
)

form1.subheader('Bill Depth')
bill_depth = form1.number_input(
    'Enter Bill Depth (mm)',
    min_value=0.01
)

form1.subheader('Flipper Length')
flipper_length = form1.number_input(
    'Enter Flipper Length (mm)',
    min_value=0.01
)

form1.subheader('Body Mass')
body_mass = form1.number_input(
    'Enter Body Mass (g)',
    min_value=0.01
)

form1.subheader('Sex')
sex = form1.radio(
    'Enter Sex',
    ['Male','Female']
)

form1.subheader('Island')
island = form1.selectbox(
    'Select Island',
    ['Torgersen','Biscoe','Dream']
)

form_button = form1.form_submit_button("Submit Features")

st.header("New Penguin Stats")
new_input = np.array([
    island,bill_length,bill_depth,flipper_length,body_mass,sex
    ]).reshape(1,-1)
# new_input = np.array([island, bill_length, bill_depth, flipper_length, body_mass, sex]).reshape(1,-1)
predict_in = pd.DataFrame(new_input,columns=penguin_model.feature_names_in_)
expander_df = st.expander('Show new penguin stats')
expander_df.table(predict_in)

predict_button = st.button("Predict the penguin species")

if predict_button:
    if float(bill_length) == 0.0:
        st.write("This is invalid")
    else:
        prediction = penguin_model.predict(predict_in)
        st.write(f'According to our model, the species is **{prediction[0]}**')