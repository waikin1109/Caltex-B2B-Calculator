import streamlit as st

st.title("Calculator-Style Ratio Output")
st.header("Chop Yew Lee Petroleum")
st.subheader("Caltex B2B Ratio Calculator")

st.write("""
This calculator divides **Total Litres** by **Ancillary Litres**, just like typing `418 ÷ 18 × 100%` 
on a calculator — which gives **23.22**, NOT a percentage.
""")

# Input fields
value1 = st.number_input("Enter Total Litres (e.g. 2 drums + 1 pail = 418):", min_value=0.0, step=0.1)
value2 = st.number_input("Enter Ancillary Litres (e.g. 1 pail = 18):", min_value=0.0, step=0.1)

# Validation and result
if value2 == 0 and value1 > 0:
    st.warning("⚠️ Ancillary litres (denominator) cannot be zero.")
elif value2 > 0:
    result = value1 / value2
    st.metric(label="Calculator-style result", value=f"{result:.2f}")


# Ancillary Range
st.write("Ancillary Range:")
st.markdown("""
            - Delo Gear 
            - ATF-J or Texamatic 1888 
            - Delo TorqForce 
            - Greases (Starplex, Multifak, Marfak) 
            - Delo XLI/XLC 
            - Brake Fluid""")



















