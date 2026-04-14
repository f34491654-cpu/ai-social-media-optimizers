import streamlit as st 
st.title("AI Social Media Content Optimizer") 
business = st.text_input("Business Type")
audience = st.text_input("Target Audience") 
platform = st.selectbox("Platform", ["Instagram", "Facebook", "LinkedIn"]) 
if st.button("Generate Content"): 
caption = f"Grow your {business} business! Perfect for {audience}. Engage more on {platform} today!" 
hashtags = f"#{business} #{platform} #marketing #business #growth" 
timing = "Best time: 6 PM - 9 PM" 
st.subheader("Generated Content") 
st.write("Caption:", caption) 
st.write("Hashtags:", hashtags) 
st.write("Posting Time:", timing)
