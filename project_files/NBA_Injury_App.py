import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. Load the saved models and scaler
logistic_regression_model = joblib.load('logistic_regression_model.joblib')
random_forest_model = joblib.load('random_forest_model.joblib')
scaler = joblib.load('scaler.joblib')

# 2. Define the selected_features list (must match training data)
selected_features = [
    'GamesPlayed',
    'BMI',
    'AvgMins',
    'assists_mean',
    'blocks_mean',
    'steals_mean',
    'fieldGoalsAttempted_mean',
    'threePointersAttempted_mean',
    'freeThrowsAttempted_mean',
    'foulsPersonal_mean',
    'turnovers_mean',
    'total_back_to_backs',
    'avg_rest_days',
    'LeagueTenure',
    'Age',
]

# Defining proper names for the features that are being represented.

feature_names = {
            'GamesPlayed': 'Total Played Games',
            'BMI': 'BMI',
            'AvgMins': 'Average Minutes',
            'assists_mean': 'Average Number of Assists',
            'blocks_mean': 'Average Number of Blocks',
            'steals_mean': 'Average Number of Steals',
            'fieldGoalsAttempted_mean': 'Average Field Goal Attempts',
            'threePointersAttempted_mean': 'Average 3 Pointers Attempted',
            'freeThrowsAttempted_mean': 'Average Free Throws Attempted',
            'foulsPersonal_mean': 'Average Personal Fouls',
            'turnovers_mean': 'Average Number of Turnovers',
            'total_back_to_backs': 'Total Back to Back Games Played',
            'avg_rest_days': 'Average Number of Rest Days',
            'LeagueTenure': 'Years played in the NBA',
            'Age': 'Age'
}

# 3. Define feature_ranges for Streamlit widgets (must match ipywidgets)
feature_ranges = {
    'GamesPlayed': {'min': 0, 'max': 82, 'step': 1, 'type': 'int', 'default': 57},
    'BMI': {'min': 18.0, 'max': 35.0, 'step': 0.1, 'type': 'float', 'default': 24.8},
    'AvgMins': {'min': 0.0, 'max': 48.0, 'step': 0.1, 'type': 'float', 'default': 18.9},
    'assists_mean': {'min': 0.0, 'max': 15.0, 'step': 0.1, 'type': 'float', 'default': 1.03},
    'blocks_mean': {'min': 0.0, 'max': 5.0, 'step': 0.01, 'type': 'float', 'default': 0.21},
    'steals_mean': {'min': 0.0, 'max': 5.0, 'step': 0.01, 'type': 'float', 'default': 0.48},
    'fieldGoalsAttempted_mean': {'min': 0.0, 'max': 30.0, 'step': 0.1, 'type': 'float', 'default': 4.91},
    'threePointersAttempted_mean': {'min': 0.0, 'max': 20.0, 'step': 0.1, 'type': 'float', 'default': 0.87},
    'freeThrowsAttempted_mean': {'min': 0.0, 'max': 20.0, 'step': 0.1, 'type': 'float', 'default': 1.20},
    'foulsPersonal_mean': {'min': 0.0, 'max': 6.0, 'step': 0.1, 'type': 'float', 'default': 1.57},
    'turnovers_mean': {'min': 0.0, 'max': 6.0, 'step': 0.1, 'type': 'float', 'default': 0.84},
    'total_back_to_backs': {'min': 0, 'max': 20, 'step': 1, 'type': 'int', 'default': 15},
    'avg_rest_days': {'min': 0.0, 'max': 10.0, 'step': 0.1, 'type': 'float', 'default': 2.33},
    'LeagueTenure': {'min': 0, 'max': 20, 'step': 1, 'type': 'int', 'default': 4},
    'Age': {'min': 18, 'max': 45, 'step': 1, 'type': 'int', 'default': 26}
}

# 4. Streamlit UI
st.set_page_config(layout="wide")
st.title("NBA Player Injury Prediction Dashboard")
st.markdown("Adjust the player's attributes below to see the predicted injury risk from two different models.")

# Create input widgets
input_data = {}
cols = st.columns(3)

for i, feature in enumerate(selected_features):
    range_info = feature_ranges[feature]
    with cols[i % 3]:
        if range_info['type'] == 'int':
            input_data[feature] = st.slider(
                feature_names.get(feature,feature),
                min_value=range_info['min'],
                max_value=range_info['max'],
                value=range_info['default'],
                step=range_info['step']
            )
        else:
            input_data[feature] = st.slider(
                feature_names.get(feature,feature),
                min_value=float(range_info['min']),
                max_value=float(range_info['max']),
                value=float(range_info['default']),
                step=float(range_info['step']),
                format=f"%.{str(range_info['step'])[::-1].find('.') if '.' in str(range_info['step']) else 0}f"
            )

st.markdown("---")

if st.button("Predict Injury Risk"):
    # Convert input to DataFrame
    player_df = pd.DataFrame([input_data])

    # --- Logistic Regression Prediction ---
    scaled_player_lr = scaler.transform(player_df)
    lr_prob_injury = logistic_regression_model.predict_proba(scaled_player_lr)[0][1]
    lr_predicted_class = logistic_regression_model.predict(scaled_player_lr)[0]

    # --- Random Forest Prediction ---
    # RF does not require scaled data for prediction (assuming it was trained on unscaled 'selected_features')
    rf_prob_injury = random_forest_model.predict_proba(player_df)[0][1]
    rf_predicted_class = random_forest_model.predict(player_df)[0]

    st.subheader("Prediction Results:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Logistic Regression")
        st.metric("Injury Probability", f"{lr_prob_injury:.2%}")
        st.metric("Predicted Outcome", "Injury" if lr_predicted_class == 1 else "No Injury")

    with col2:
        st.markdown("### Random Forest")
        st.metric("Injury Probability", f"{rf_prob_injury:.2%}")
        st.metric("Predicted Outcome", "Injury" if rf_predicted_class == 1 else "No Injury")

    st.write("\n--- Notes ---")
    st.write("- Injury Probability close to 100% means high likelihood of injury.")
    st.write("- Injury Probability close to 0% means low likelihood of injury.")
