import streamlit as st
import requests

def main():
    # Title for the app
    st.title('Welcome to Hylab')
    st.write('Hybrid Laboratory for PhD Student')
    # URL to fetch data from
    url = "https://hylab-result.pptik.id/"

    if st.button('Fetch Data'):
        # Make a GET request to the URL
        response = requests.get(url)

        if response.status_code == 200:
            # Display the fetched data
            st.write(response.text)
        else:
            st.error('Failed to fetch data')

if __name__ == "__main__":
    main()
