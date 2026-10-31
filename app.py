import streamlit as st
import datetime, random

st.set_page_config(page_title="Iam Chimaco Studio", page_icon="❤️")
st.title("❤️ Iam Chimaco - African Romance Studio")

romance_types = [
 "Village love - Chiamaka waiting",
 "City love - Lagos hustle romance", 
 "Long distance - Japa love",
 "Secondary school love",
 "Rich vs Poor love",
 "Arranged marriage turned love",
 "Facebook love - DM to wedding"
]

today_type = st.selectbox("Today's Romance Type:", romance_types)
idea = st.text_area("Story idea (leave empty for AI random):", placeholder="e.g. Obinna returns from Lagos with Benz...")

if st.button("🔥 GENERATE VIDEO SCRIPT"):
    script = f"""African Romance - {today_type}
    Scene 1: {idea or 'Chiamaka in village...'} 
    Scene 2: Conflict...
    Scene 3: Happy ending with love...
    """
    st.success("Script generated!")
    st.code(script)
    st.write("This will be saved to `daily_script.txt` for robot to post 3x")
    with open("daily_script.txt","w") as f:
        f.write(script)
