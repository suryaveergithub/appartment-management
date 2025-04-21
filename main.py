import streamlit as st
import pandas as pd

# Load data
def load_data():
    return pd.read_csv("data.csv")

# Save data
def save_data(df):
    df.to_csv("data.csv", index=False)

# UI
st.title("🏢 Apartment Management System")

menu = ["View Residents", "Add Resident", "Update Rent Status", "Delete Resident"]
choice = st.sidebar.selectbox("Menu", menu)

df = load_data()

# View Data
if choice == "View Residents":
    st.subheader("All Residents")
    st.dataframe(df)

# Add Resident
elif choice == "Add Resident":
    st.subheader("Add New Resident")
    apartment = st.text_input("Apartment Number")
    name = st.text_input("Resident Name")
    contact = st.text_input("Contact Number")
    rent_paid = st.selectbox("Rent Paid", ["Yes", "No"])

    if st.button("Add"):
        new_data = {"Apartment": apartment, "Resident": name, "Contact": contact, "Rent Paid": rent_paid}
        df = df.append(new_data, ignore_index=True)
        save_data(df)
        st.success("Resident added successfully!")

# Update Rent Status
elif choice == "Update Rent Status":
    st.subheader("Update Rent Paid Status")
    selected_apartment = st.selectbox("Select Apartment", df["Apartment"].tolist())

    new_status = st.selectbox("New Rent Status", ["Yes", "No"])
    if st.button("Update"):
        df.loc[df["Apartment"] == selected_apartment, "Rent Paid"] = new_status
        save_data(df)
        st.success("Rent status updated!")

# Delete Resident
elif choice == "Delete Resident":
    st.subheader("Delete a Resident")
    selected_apartment = st.selectbox("Select Apartment to Delete", df["Apartment"].tolist())

    if st.button("Delete"):
        df = df[df["Apartment"] != selected_apartment]
        save_data(df)
        st.success("Resident deleted successfully!")
