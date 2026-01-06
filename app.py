import streamlit as st
import pandas as pd

st.set_page_config(page_title="FG Item Search", layout="wide")

st.title("FG Item Search Tool")
st.write("Upload the FG List Excel file, then search by Item Code or Item Name.")

uploaded_file = st.file_uploader(
    "Upload Excel file (.xlsx)",
    type=["xlsx"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.success(f"File loaded successfully — {df.shape[0]} items available.")

    search_text = st.text_input(
        "Search Item Code or Item Name",
        placeholder="Start typing to search..."
    )

    if search_text:
        filtered_df = df[
            df["Item Code"].astype(str).str.contains(search_text, case=False, na=False)
            |
            df["Item Name"].astype(str).str.contains(search_text, case=False, na=False)
        ]

        if filtered_df.empty:
            st.warning("No matching item found.")
        else:
            st.write(f"Showing {filtered_df.shape[0]} result(s)")
            st.dataframe(filtered_df, use_container_width=True)

    else:
        st.info("Please type in the search box to see results.")

else:
    st.info("Please upload the FG List Excel file to begin.")
