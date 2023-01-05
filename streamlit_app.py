import streamlit as st
import requests

st.title('Package Tracker')

# Get tracking number from user
tracking_number = st.text_input('Enter tracking number:')

# Make request to tracking API
response = requests.get(f'https://mytrackingapi.com/track?number={tracking_number}')

# Check if package has been delivered
if response.status_code == 200:
    data = response.json()
    if data['status'] == 'delivered':
        st.success('Package has been delivered!')
    else:
        st.warning('Package has not been delivered yet.')
else:
    st.error('Unable to track package')
