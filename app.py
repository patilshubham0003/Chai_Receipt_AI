import streamlit as st

st.set_page_config(
    page_title="Chai Calculator",
    page_icon="☕"
)
st.title("☕ Chai Calculator")



def calculate(cups, price):
    return cups * price


cups = st.number_input("Enter number of cups",min_value=1)
price = st.number_input("Enter price per cup",min_value=1)

# Note: Price already includes GST as provided by the owner.
# GST is shown separately for customer reference only.
gst = st.number_input("Enter GST",value=18)
name = st.text_input("Customer Name", value="Customer")


if st.button("Calculate"):

    total_price = calculate(cups, price)
    gst = total_price * gst



    receipt = f"""
==============================
        ☕ COFFEE SHOP
==============================

Total Cups       : {cups}
Price per Cup    : ₹{price:.2f}
GST Included     : ₹{gst:.2f}

------------------------------
Total Price      : ₹{total_price:.2f}
------------------------------

      Thank you! {name}
      Visit Again 😊

==============================
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