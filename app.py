import streamlit as st


st.markdown("""# This is a header
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used in order to select the displayed lines
head_df = df.head(line_count)

head_df

col1, col2, col3 = st.columns(3)
col1.metric("SPDR S&P 500", "$437.8", "-$1.25")
col2.metric("FTEC", "$121.10", "0.46%")
col3.metric("BTC", "$46,583.91", "+4.87%")


@st.cache
def get_line_chart_data():
    return pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])


df = get_line_chart_data()

st.line_chart(df)
