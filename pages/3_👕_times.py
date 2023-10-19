import streamlit as st

st.set_page_config(page_title="Time", page_icon="👕", layout="wide")

df_data = st.session_state["df_fifa"]

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Selecione um clube", clubes)

df_filtered = df_data[df_data["Club"] == club].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age" , "Photo", "Flag" , "Overall", "Value(£)", "Wage(£)","Joined", "Height(cm.)","Weight(lbs.)","Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filtered[columns].sort_values(by="Overall", ascending=False), column_config={
  "Overall": st.column_config.ProgressColumn(
    "Overall",format="%d", min_value=0, max_value=100
  ),
  "Wage(£)": st.column_config.ProgressColumn('Weekly Wage',format="£%f", min_value=0, max_value=df_filtered["Wage(£)"].max()),
  "Photo": st.column_config.ImageColumn(),
  "Flag": st.column_config.ImageColumn(),
})