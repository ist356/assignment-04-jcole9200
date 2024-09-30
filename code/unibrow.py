'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("unibrow")
st.caption("the universal data browser")

file = st.file_uploader("upload a file:", type=["csv", "xlsx", "json"])

if file:
    file_type = pl.get_file_extension(file.name)
    df = pl.load_file(file, file_type)
    columns = pl.get_column_names(df)
    
    selected_columns = st.multiselect("select columns to display:", columns, default = columns)
    
    if st.toggle("enable filtering"):
        stcols = st.columns(3)
        text_columns = pl.get_columns_of_type(df, 'object')
        filter_column = stcols[0].selectbox("select column to filter:", text_columns) 
        if filter_column:
            unique_values = pl.get_unique_values(df, filter_column)
            selected_value = stcols[1].selectbox("select value to filter by:", unique_values)
            df_filtered = df[df[filter_column] == selected_value][selected_columns]
        else:
            df_filtered = df[selected_columns]
    else:
        df_filtered = df[selected_columns]
    
    st.dataframe(df_filtered)
    st.dataframe(df_filtered.describe())

