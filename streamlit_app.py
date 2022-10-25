import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('😎 Just Try It! ')
st.caption('This web app use for transform data from csv file to visualize in python using streamlit :-)')

#df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/NBA_2021.csv")
#https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv

st.sidebar.subheader('Input')
url_input = st.sidebar.text_input('csv/github url', '')
#st.write('The github url of your data is', url_input)
#Player, Pos

#st.subheader('Output')
#st.info(f'This github url of your data is: {url_input}')

if url_input:
    st.subheader('Output')
    st.info(f'This github url of your data is: {url_input}')
    df = pd.read_csv(url_input)
    st.subheader('Data from your file here👇')
    st.write(df)
    column_names = df.columns

#    st.header('Please select the group')
#    st.write(list(column_names))

    st.subheader('Please select the function')
    col1, col2, col3 = st.columns(3)

    #done!
    with col1:
        st.header('Select column')
        sel_col = st.multiselect(
        'You can select multiple columns and SORT it manually!!',
        (list(column_names)),df.columns[0])

        st.write('You selected:', pd.DataFrame(sel_col).to_string(index=False, header=None))

    with col2:
        st.subheader("Aggregate")
        #https://stackoverflow.com/questions/20077651/python-pandas-sum-up-values-from-different-columns
        #select column and method ex. sum pts, avr age
        #df_agg = df.groupby(['job','source']).agg({'count':sum})

        sum_col = st.multiselect(
        'Sum column',
        (list(column_names)))
        st.write(sum_col)
        
        #.mean()
        avg_col = st.multiselect(
        'Average column',
        (list(column_names)))
        
        min_col = st.multiselect(
        'Min column',
        (list(column_names)))

        avg_col = st.multiselect(
        'Max column',
        (list(column_names)))


    #done!
    with col3:
        st.subheader('Sort')
        #sort function
        sort_option = st.radio(
        'Do you want to sort the data?',
        ('No', 'Ascending', 'Descending'))

        sort_input = st.selectbox(
        'Please select sort values:',
        (list(column_names)))


    #if sum_col: 
    #   df4 = df[sel_col].sum

    st.write('sandbox')
    df4 = df[sel_col]
    df5 = df4.groupby(df4.columns[0]).sum([sum_col])
    #หาวิธีทำ aggregate
    #df6 = df5.sort_values([sort_input], ascending=False)
    #.agg({[sum_col]:sum})
    #df5 = df4.sort_values([sort_input], ascending=False).groupby(df.columns[0]).head(3)
    #df.sort_values(['job','count'],ascending=False).groupby('job').head(3)
    #df_agg = df.groupby(['job','source']).agg({'count':sum})
    #A.groupby('Name').agg({'Missed':'sum','Credit':'sum','Grades':'mean'})
    st.write(df6)

    #dataframe
    if sort_option == 'Ascending':
        df_ft = df4.groupby(df.columns[0]).sort_values([sort_input], ascending=True)
        st.write(df_ft)
    if sort_option == 'Descending':
        df_ft = df4.groupby(df.columns[0]).sort_values([sort_input], ascending=False)
        st.write(df_ft)
    else:
        df_ft = df4.groupby(df.columns[0])
        st.write(df_ft)

#    if option == 'Ascending':
#        df2 = df.sort_values().groupby(column_names,sort=)
#        st.write(df2)



#    filter = st.radio(
#        "Select a value",
#        (1,2,3)


#    if genre == 'Comedy':
#        st.write('You selected comedy.')
#    else:
#        st.write("You didn't select comedy.")

    #df5 = df4.sort_values([sort_input], ascending=False).groupby(df.columns[0]).head(3)

    df2 = df.groupby(column_names)
    st.bar_chart(df2)
    st.write(df2)



    max

#    st.header('Please select the ')
#    genre = st.radio(
#        "Select a value",
#        (1,2,3)

#    if genre == 'Comedy':
#        st.write('You selected comedy.')
#    else:
#        st.write("You didn't select comedy.")

else:
    st.subheader('Welcome! please enter your input at the sidebar')
    st.write('sample: https://raw.githubusercontent.com/dataprofessor/data/master/NBA_2021.csv')
    image = Image.open('NBA.jpg')
    st.image(image, caption='Fly high!')
    
