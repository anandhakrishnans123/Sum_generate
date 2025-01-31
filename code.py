import streamlit as st
import pandas as pd
import numpy as np

def generate_csv(num_rows, target_sum):
    values = np.random.dirichlet(np.ones(num_rows), size=1)[0] * target_sum
    df = pd.DataFrame({"Values": values})
    return df

# Streamlit App
st.title("CSV Generator App")

# User Inputs
num_rows = st.number_input("Enter number of rows:", min_value=1, value=491, step=1)
target_sum = st.number_input("Enter target sum:", min_value=1, value=900, step=1)

if st.button("Generate CSV"):
    df = generate_csv(num_rows, target_sum)
    st.write("Preview of Generated Data:")
    st.dataframe(df.head())  # Show preview of first few rows

    # Convert DataFrame to CSV for download
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", data=csv, file_name="generated_values.csv", mime="text/csv")

