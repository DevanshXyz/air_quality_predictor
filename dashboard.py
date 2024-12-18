import streamlit as st
import pandas as pd
from scripts.waqi_fetch import fetch_city_data
from scripts.visualization import visualize_real_time_data

def main():
    st.title("Air Quality Monitoring Dashboard")
    
    # Input: City Name
    city = st.text_input("Enter a city name to fetch air quality data:", "")
    
    if city:
        try:
            # Fetch data for the city
            city_data = fetch_city_data(city)
            st.subheader(f"Air Quality Data for {city}")
            
            # Display the data
            if city_data is not None:
                st.write(city_data)
                st.bar_chart(city_data.drop(columns=['city', 'datetime']).set_index('datetime'))
            else:
                st.error("Failed to fetch data. Please check the city name or try again later.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    
    # Optionally visualize real-time data for multiple cities
    st.subheader("Compare AQI Across Multiple Cities")
    cities = st.text_area("Enter a list of cities (comma-separated):", "Delhi, Los Angeles, Beijing, London")
    if st.button("Fetch and Visualize"):
        city_list = [city.strip() for city in cities.split(",")]
        if city_list:
            try:
                real_time_data = pd.concat([fetch_city_data(c) for c in city_list])
                real_time_data.to_csv("data/real_time_air_quality.csv", index=False)
                visualize_real_time_data("data/real_time_air_quality.csv")
                st.success("Visualization saved as 'data/aqi_by_city.png'.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
