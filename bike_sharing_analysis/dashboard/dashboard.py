import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


days_df = pd.read_csv('./data/day.csv')
hours_df = pd.read_csv('./data/hour.csv')

st.title('Dashboard Bike Sharing :bike:')

def count_by_day_df(day_df):
    day_df_count_2011 = day_df.query(str('dteday >= "2011-01-01" and dteday < "2012-12-31"'))
    return day_df_count_2011


def total_registered_df(day_df):
   regis_df =  day_df.groupby(by="dteday").agg({
      "registered": "sum"
    })
   regis_df = regis_df.reset_index()
   regis_df.rename(columns={
        "registered": "register_sum"
    }, inplace=True)
   return regis_df

def total_casual_df(day_df):
   casual_df =  day_df.groupby(by="dteday").agg({
      "casual": ["sum"]
    })
   casual_df = casual_df.reset_index()
   casual_df.rename(columns={
        "casual": "casual_sum"
    }, inplace=True)
   return casual_df

datetime_columns = ["dteday"]
days_df.sort_values(by="dteday", inplace=True)
days_df.reset_index(inplace=True)   

for column in datetime_columns:
    days_df[column] = pd.to_datetime(days_df[column])

min_date_days = days_df["dteday"].min()
max_date_days = days_df["dteday"].max()


with st.sidebar:
    st.image("https://i.ibb.co/M7GyVpb/Screenshot-2024-02-20-142959.jpg")
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days])
    
main_df_days = days_df[(days_df["dteday"] >= str(start_date)) &  (days_df["dteday"] <= str(end_date))]

casual_df = total_casual_df(main_df_days)
regis_df = total_registered_df(main_df_days)
day_df_count_2011 = count_by_day_df(main_df_days)


col1, col2, col3 = st.columns(3)
 
with col1:
    total_orders = day_df_count_2011.cnt.sum()
    st.metric("Total Users Sharing Bike", value=total_orders)

with col2:
    total_sum = regis_df.register_sum.sum()
    st.metric("Total Registered Users", value=total_sum)

with col3:
    total_sum = casual_df.casual_sum.sum()
    st.metric("Total Casual Users", value=total_sum)

monthly_count = days_df.groupby("mnth")["cnt"].sum().reset_index()

# Visualisasi Line Chart
st.line_chart(monthly_count.set_index("mnth"))

# create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Bike Share Count - Season")

    # Mapping dari angka ke label musim
    season_mapping = {1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'}
    days_df["season_label"] = days_df["season"].map(season_mapping)

    season_count = days_df.groupby("season_label")["cnt"].sum().reset_index()

    # Visualisasi dengan st.bar_chart
    st.bar_chart(season_count.set_index("season_label"), use_container_width=True)

with col2:
    st.subheader("Bike Share Count - Weathers")

    weather_count = days_df.groupby("weathersit")["cnt"].sum().reset_index()

    # Visualisasi dengan st.bar_chart
    st.bar_chart(weather_count.set_index("weathersit"))

total_casual = days_df['casual'].sum()
total_registered = days_df['registered'].sum()

label = ['Casual', 'Registered']
fig1, ax1 = plt.subplots()
ax1.pie([total_casual,total_registered],labels=label, explode=(0, 0.1), autopct='%1.1f%%',colors=['orange','blue'],
        shadow=False)
ax1.axis('equal')

plt.legend(title = "User Bike Sharing", loc='upper right')

st.pyplot(fig1)
