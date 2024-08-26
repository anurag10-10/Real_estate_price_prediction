import streamlit as st
import pickle
import numpy as np
import pandas as pd
import json

# Load the trained model and columns
model = pickle.load(open('banglore_home_prices_model.pickle', 'rb'))

# Load the column names from the JSON file
with open('columns.json', 'r') as file:
    model_columns = json.load(file)

# Title of the app
st.title('Real Estate Price Prediction')

# Area input
area = st.number_input('Area (Sq. ft)', min_value=100, max_value=10000, step=1)

# BHK input with selectable boxes
bhk = st.radio('BHK', [1, 2, 3, 4, 5], horizontal=True)

# Bathrooms input with selectable boxes
bathrooms = st.radio('Bathrooms', [1, 2, 3, 4, 5], horizontal=True)

# Location input with a dropdown and search functionality
locations = ["1st Block Jayanagar", "1st Phase Jp Nagar", "2nd Phase Judicial Layout", "2nd Stage Nagarbhavi", "5th Block Hbr Layout", "5th Phase Jp Nagar", "6th Phase Jp Nagar", "7th Phase Jp Nagar", "8th Phase Jp Nagar", "9th Phase Jp Nagar", "Aecs Layout", "Abbigere", "Akshaya Nagar", "Ambalipura", "Ambedkar Nagar", "Amruthahalli", "Anandapura", "Ananth Nagar", "Anekal", "Anjanapura", "Ardendale", "Arekere", "Attibele", "Beml Layout", "Btm 2nd Stage", "Btm Layout", "Babusapalaya", "Badavala Nagar", "Balagere", "Banashankari", "Banashankari Stage Ii", "Banashankari Stage Iii", "Banashankari Stage V", "Banashankari Stage Vi", "Banaswadi", "Banjara Layout", "Bannerghatta", "Bannerghatta Road", "Basavangudi", "Basaveshwara Nagar", "Battarahalli", "Begur", "Begur Road", "Bellandur", "Benson Town", "Bharathi Nagar", "Bhoganhalli", "Billekahalli", "Binny Pete", "Bisuvanahalli", "Bommanahalli", "Bommasandra", "Bommasandra Industrial Area", "Bommenahalli", "Brookefield", "Budigere", "Cv Raman Nagar", "Chamrajpet", "Chandapura", "Channasandra", "Chikka Tirupathi", "Chikkabanavar", "Chikkalasandra", "Choodasandra", "Cooke Town", "Cox Town", "Cunningham Road", "Dasanapura", "Dasarahalli", "Devanahalli", "Devarachikkanahalli", "Dodda Nekkundi", "Doddaballapur", "Doddakallasandra", "Doddathoguru", "Domlur", "Dommasandra", "Epip Zone", "Electronic City", "Electronic City Phase Ii", "Electronics City Phase 1", "Frazer Town", "Gm Palaya", "Garudachar Palya", "Giri Nagar", "Gollarapalya Hosahalli", "Gottigere", "Green Glen Layout", "Gubbalala", "Gunjur", "Hal 2nd Stage", "Hbr Layout", "Hrbr Layout", "Hsr Layout", "Haralur Road", "Harlur", "Hebbal", "Hebbal Kempapura", "Hegde Nagar", "Hennur", "Hennur Road", "Hoodi", "Horamavu Agara", "Horamavu Banaswadi", "Hormavu", "Hosa Road", "Hosakerehalli", "Hoskote", "Hosur Road", "Hulimavu", "Isro Layout", "Itpl", "Iblur Village", "Indira Nagar", "Jp Nagar", "Jakkur", "Jalahalli", "Jalahalli East", "Jigani", "Judicial Layout", "Kr Puram", "Kadubeesanahalli", "Kadugodi", "Kaggadasapura", "Kaggalipura", "Kaikondrahalli", "Kalena Agrahara", "Kalyan Nagar", "Kambipura", "Kammanahalli", "Kammasandra", "Kanakapura", "Kanakpura Road", "Kannamangala", "Karuna Nagar", "Kasavanhalli", "Kasturi Nagar", "Kathriguppe", "Kaval Byrasandra", "Kenchenahalli", "Kengeri", "Kengeri Satellite Town", "Kereguddadahalli", "Kodichikkanahalli", "Kodigehaali", "Kodigehalli", "Kodihalli", "Kogilu", "Konanakunte", "Koramangala", "Kothannur", "Kothanur", "Kudlu", "Kudlu Gate", "Kumaraswami Layout", "Kundalahalli", "Lb Shastri Nagar", "Laggere", "Lakshminarayana Pura", "Lingadheeranahalli", "Magadi Road", "Mahadevpura", "Mahalakshmi Layout", "Mallasandra", "Malleshpalya", "Malleshwaram", "Marathahalli", "Margondanahalli", "Marsur", "Mico Layout", "Munnekollal", "Murugeshpalya", "Mysore Road", "Ngr Layout", "Nri Layout", "Nagarbhavi", "Nagasandra", "Nagavara", "Nagavarapalya", "Narayanapura", "Neeladri Nagar", "Nehru Nagar", "Ombr Layout", "Old Airport Road", "Old Madras Road", "Padmanabhanagar", "Pai Layout", "Panathur", "Parappana Agrahara", "Pattandur Agrahara", "Poorna Pragna Layout", "Prithvi Layout", "R.T. Nagar", "Rachenahalli", "Raja Rajeshwari Nagar", "Rajaji Nagar", "Rajiv Nagar", "Ramagondanahalli", "Ramamurthy Nagar", "Rayasandra", "Sahakara Nagar", "Sanjay Nagar", "Sarakki Nagar", "Sarjapur", "Sarjapur Road", "Sarjapura - Attibele Road", "Sector 2 Hsr Layout", "Sector 7 Hsr Layout", "Seegehalli", "Shampura", "Shivaji Nagar", "Singasandra", "Somasundara Palya", "Sompura", "Sonnenahalli", "Subramanyapura", "Sultan Palaya", "Tc Palaya", "Talaghattapura", "Thanisandra", "Thigalarapalya", "Thubarahalli", "Thyagaraja Nagar", "Tindlu", "Tumkur Road", "Ulsoor", "Uttarahalli", "Varthur", "Varthur Road", "Vasanthapura", "Vidyaranyapura", "Vijayanagar", "Vishveshwarya Layout", "Vishwapriya Layout", "Vittasandra", "Whitefield", "Yelachenahalli", "Yelahanka", "Yelahanka New Town", "Yelenahalli", "Yeshwanthpur"] 
 # Replace with actual locations
location = st.selectbox('Location', locations)

# Estimate Price button
if st.button('Estimate Price'):
    # Create a DataFrame from the input
    input_df = pd.DataFrame([[area, bathrooms, bhk, location]], 
                            columns=['total_sqft', 'bath', 'bhk', 'location'])
    
    # Generate dummy variables for the location
    input_df = pd.get_dummies(input_df, columns=['location'], drop_first=True)
    
    # Reindex to ensure the same structure as training data
    input_df = input_df.reindex(columns=model_columns, fill_value=0)
    
    # Debugging: Print the DataFrame and types
    st.write("Input DataFrame:")
    st.write(input_df)
    st.write("Data Types:")
    st.write(input_df.dtypes)
    
    # Predict using the model
    try:
        estimated_price = model.predict(input_df)[0]
        # Display the result
        st.success(f'The estimated price is ₹{estimated_price:,.2f}')
    except Exception as e:
        st.error(f"Error during prediction: {e}")
