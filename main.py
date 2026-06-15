import streamlit as st

st.set_page_config(page_title="Margin Visibility Portal")

st.title("Margin Visibility Portal")

# Simulated CRM + ATS data
products = {
    "Software Engineer": {
        "price": 100,
        "cost": 70
    },
    "Data Engineer": {
        "price": 120,
        "cost": 85
    },
    "Project Manager": {
        "price": 140,
        "cost": 95
    }
}

selected_product = st.selectbox(
    "Select Deal",
    list(products.keys())
)

price = products[selected_product]["price"]
cost = products[selected_product]["cost"]

st.write(f"Current Bill Rate: ${price}")
st.write(f"Labor Cost: ${cost}")

discount = st.number_input(
    "Proposed Discount ($)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

if st.button("Evaluate Deal"):

    profit = price - cost - discount
    margin = (profit / price) * 100

    st.metric(
        "Estimated Margin",
        f"{margin:.2f}%"
    )

    if margin >= 25:
        st.success("Healthy Margin")
    elif margin >= 15:
        st.warning("Medium Risk")
    else:
        st.error("High Risk")

    st.write("---")
    st.write(f"Profit: ${profit:.2f}")
