import streamlit as st

st.title("Chop Yew Lee Petroleum")
st.header("Caltex B2B Calculator")
st.write("Check if Ancillary Range is ≥ 15% of Total Litres")

# Input fields
ancillary_litres = st.number_input("Enter Ancillary Litres: ", min_value=0.0, step=0.1)
total_litres = st.number_input("Enter Total Litres: ", min_value=0.0, step=0.1)

# Calculation
if ancillary_litres == 0 and total_litres > 0:
    st.warning("⚠️ Ancillary litres cannot be zero.")
elif ancillary_litres > 0:
    # Matches: 418 / 18 * 100% (i.e., *1), then format as percent
    percentage = total_litres / ancillary_litres
    st.metric(label="Calculator Style Output", value=f"{percentage:.2f}%")

    if percentage >= 15:
        st.success("✅ Total litres are ≥ 15x ancillary litres.")
    else:
        st.error("❌ Total litres are < 15x ancillary litres.")

# Ancillary Range
st.write("Ancillary Range:")
st.markdown("""
            - Delo Gear 
            - ATF-J or Texamatic 1888 
            - Delo TorqForce 
            - Greases (Starplex, Multifak, Marfak) 
            - Delo XLI/XLC 
            - Brake Fluid""")














