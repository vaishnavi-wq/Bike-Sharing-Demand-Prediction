import streamlit as st
import joblib
import pandas as pd

# Load the model pkl file
model = joblib.load(r"C:\Users\sattyam\Desktop\Project\project3\BRProject\model2.pkl")

# functions to make predictions
def predict(model, input_df):
    """Make predictions using the trained model."""
    predictions = model.predict(input_df)
    return predictions

# create a form for the user input
def input_form():
    """Display the input form and receive user input."""
    # Define the input fields
    season_options = {1: 'fall', 2: 'springer', 3: 'summer', 4: 'winter'}
    season = st.selectbox('Season', options=list(season_options.values()))
    
    weekday_options = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    weekday = st.selectbox('Day of Week', options=list(weekday_options.values()))

    workingday_options = {1: 'No work', 2: 'Working Day'}
    workingday = st.selectbox('Working Day', options=list(workingday_options.values()))
    
    weather_condition_options = {1: 'Clear', 2: 'Heavy Rain', 3: 'Light Snow', 4: 'Mist'}
    weather = st.selectbox('Weather Condition', options=list(weather_condition_options.values()))

    month = st.selectbox('Month', range(1, 13))
    hour = st.slider('Hour', 0, 23, 12)
    registered = st.number_input('Registered Users', value=0)
    casual = st.number_input('Casual Users', value=0)
    date = st.slider('Date', 1, 31, 10)

    # Combine the input fields into a DataFrame
    input_dict = {'season': season,
                  'month': month,
                  'hour': hour,
                  'weekday': weekday,
                  'workingday': workingday,
                  'registered': registered,
                  'casual': casual,
                  'date': date,
                  'weather': weather}
    input_df = pd.DataFrame(input_dict, index=[0])

    return input_df


# streamlit app
def app():
    """Define the Streamlit app."""
    # Set the app title
    st.set_page_config(page_title="Bike Sharing Demand Prediction", page_icon=":bike:", layout="wide")
    #st.title('Bike Sharing Demand Prediction')


    # Add animation and color to title
    st.title('Bike Sharing Demand Prediction :bicyclist: :chart_with_upwards_trend:')
    st.markdown("<h3 style='text-align: center; color: #7E8C8D;'>Predict the number of bike rentals based on the given parameters</h3>", unsafe_allow_html=True)
    st.text("")
    st.text("")
    st.text("")

    # Add legend
    st.sidebar.markdown("<h4 style='text-align: center; color: #7E8C8D;'>Legend :mag:</h4>", unsafe_allow_html=True)
    st.sidebar.markdown("- Season :leaves:: 1: 'fall', 2: 'springer', 3: 'summer', 4: 'winter'", unsafe_allow_html=True)
    st.sidebar.markdown("- Working Day :hammer_and_wrench:: 1: 'No work', 2: 'Working Day'", unsafe_allow_html=True)
    st.sidebar.markdown("- Weather  :cloud:: 1: 'Clear', 2: 'Heavy Rain', 3: 'Light Snow', 4: 'Mist'", unsafe_allow_html=True)
    
    # Get the user input
    input_df = input_form()
# Add a predict button
    predict_button = st.button('Predict')

# If the predict button is clicked, make a prediction and display it
    if predict_button:
    # Make a prediction
        predictions = predict(model, input_df)

    # Display the prediction
        st.success(f'Predicted Bike Rentals: **{round(predictions[0]):,}**')

# Run the Streamlit app
if __name__ == '__main__':
    app()