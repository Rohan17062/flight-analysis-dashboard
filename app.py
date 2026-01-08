import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px
db=DB()
st.sidebar.title('analysis options')

choice=st.sidebar.selectbox("menu",['select one option','flight details','analytics'])
if choice=='flight details':
    st.title('Flight details')
    col1,col2,col3=st.columns(3)
    city=db.extract_city_name()
    with col1:
        sourc=st.selectbox('source',sorted(city))
    with col2:
        destin=st.selectbox('destination',sorted(city))
    with col3:
        dat=db.extract_date()
        jour=st.selectbox('select date',sorted(dat))
    if st.button('search'):
        if sourc==destin:
            st.warning('source and destination cannot be same')
        else:
             with st.spinner("Searching flights..."):
              detail = db.extract_flight_details(sourc, destin, jour)

             if len(detail) == 0:
               st.warning("Sorry, no flight details found")
             else:
              st.success(f"{len(detail)} flights found")
              st.dataframe(detail)






elif choice=='analytics':
    st.title('Analytics')
    name,frequency=db.extract_pie_details()
    fig = go.Figure(
        go.Pie(
            labels=name,
            values=frequency,
            hoverinfo='label+percent',
            textinfo='value'
        )
    )

    st.header("Airline Distribution")
    st.plotly_chart(fig, use_container_width=True)

    source,frequency1=db.extract_busy_details()
    fig = go.Figure(
        data=[
            go.Bar(
                x=source,
                y=frequency1
            )
        ]
    )

    fig.update_layout(
        title='total flights arriving and leaving a airport',
        xaxis_title='Source',
        yaxis_title='Count'
    )

    st.plotly_chart(fig, use_container_width=True)

    name,price=db.expense()
    fig = go.Figure(
        data=[
            go.Bar(
                x=name,
                y=price
            )
        ]
    )

    fig.update_layout(
        title='comparison of avg price of airlines',
        xaxis_title='name of airline',
        yaxis_title='avg price'
    )

    st.plotly_chart(fig, use_container_width=True)


else:
    st.title('flight dataset analysis')



