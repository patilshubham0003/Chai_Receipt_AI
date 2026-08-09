import streamlit as st
from google import genai


st.set_page_config(
    page_title="Chai Calculator",
    page_icon="☕"
)

st.title("☕ Chai Calculator")


def calculate(cups, price):
    return cups * price


cups = st.number_input(
    "Enter number of cups",
    min_value=1
)

price = st.number_input(
    "Enter price per cup",
    min_value=1
)

# Note: Price already includes GST as provided by the owner.
# GST is shown separately for customer reference only.

gst_rate = st.number_input(
    "Enter GST",
    value=18
)

name = st.text_input("Customer Name")


if st.button("Calculate"):

    total_price = calculate(cups, price)
    gst_amount = total_price * gst_rate / 100

    # Usage of GenAI
    api_key = st.secrets["GOOGLE_API_KEY"]

    client = genai.Client(api_key=api_key)

    try:
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            input=f"""
            Give a one-line quote for the chai customer whose name is {name},
            instead of saying 'Thank you! Visit Again'.
            Provide only the quote and no other text.
            """
        )

        quote = interaction.output_text

    except Exception:
        quote = f"Enjoy your chai and have a wonderful day!{name}"



receipt = f"""
============================================================
                     CHAI RECEIPT
============================================================

Total Cups       : {cups}
Price per Cup    : ₹{price:.2f}

------------------------------------------------------------
GST Included     : ₹{gst_amount:.2f}
------------------------------------------------------------

TOTAL AMOUNT     : ₹{total_price:.2f}

------------------------------------------------------------

"{quote}"

============================================================
"""


    # Display receipt
    st.text(receipt)

    # Download receipt
    st.download_button(
        label="🖨️ Print Receipt",
        data=receipt,
        file_name=f"{name}_receipt.txt",
        mime="text/plain"
    )
