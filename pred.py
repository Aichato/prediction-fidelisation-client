import streamlit as st
from PIL import Image
import pickle

model = pickle.load(open("Ml_model.pkl", "rb"))


def run():
    img1 = Image.open("BSIC.png")
    #img1 = img1.resize((162, 145))
    st.image(img1, use_column_width=False)
    st.title("Prediction de fidelisation client")

    ## Account_no
    account = st.text_input("Account_no")

    ## Credit_score
    credit_score = st.number_input("Credit_score",value=0)

    ## Age
    age =  st.number_input("Age",value=0)

    ## Tenure
    tenure = st.number_input("Tenure",value=0)

    ## Balance
    balance = st.number_input("Balance",value=0)

    ## NumOfProducts
    number_of_product = st.number_input("NumOfProducts",value=0)

    ## HasCrCard
    has_credit_card = st.number_input("HasCrCard",value=0)

    ## IsActiveMember
    is_active_number = st.number_input("IsActiveMember",value=0)

    ## EstimatedSalary
    estimated_salary = st.number_input("EstimatedSalary",value=0)

    ## Gender
    gen_display = ('Male', 'Female')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])

    ## Geography
    geo_display = ('Maradi', 'Niamey', "Tahoua")
    geo_options = list(range(len(geo_display)))
    geo = st.selectbox("Education", geo_options, format_func=lambda x: geo_display[x])

    features = [[credit_score, age, tenure, balance, number_of_product, has_credit_card, is_active_number, estimated_salary, gen, geo]]
    print(features)

    prediction = model.predict(features)
    lc = [str(i) for i in prediction]

    ans = int("".join(lc))
    if st.button("Submit"):
        if ans == 1:
            st.error(
                "Attention!!!"  
                "Account_no: "+ account +' || '
                "quittera la banque"
            )
        else:
            st.success(
                "Account_no: " + account + ' || '
                "restera fidele a la banque"
            )


run()




