import streamlit as st

st.title("Chop Yew Lee Petroleum")
st.title("Caltex B2B Calculator")
st.write("Check if Ancillary Range is ≥ 15% of Total Litres")

# Input fields
ancillary_litres = st.number_input("Enter Ancillary Litres: ", min_value=0.0, step=0.1)
total_litres = st.number_input("Enter Total Litres: ", min_value=0.0, step=0.1)

# Calculation
if total_litres > 0:
    percentage = (ancillary_litres / total_litres) * 100
    st.metric(label="Ancillary Percentage", value=f"{percentage:.2f}%")

    if percentage >= 15:
        st.success("✅ Ancillary range is ≥ 15% of total litres.")
    else:
        st.error("❌ Ancillary range is < 15% of total litres.")
elif total_litres == 0 and (ancillary_litres > 0):
    st.warning("⚠️ Total litres cannot be zero.")

# Ancillary Range
st.write("Ancillary Range:")
st.write("""Delo Gear\n ATF-J or Texamatic 1888\n Delo TorqForce\n Greases\n Delo XLI/XLC\n Brake Fluid""")






