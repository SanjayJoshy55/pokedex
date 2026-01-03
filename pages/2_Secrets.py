import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Secrets & Guides", page_icon="🗝️")

st.title("🗝️ Secrets & Guides")

tab1, tab2, tab3 = st.tabs(["🗿 Regi Puzzles", "✨ Mirage Spots", "🐟 Feebas Calculator"])

with tab1:
    st.header("Unlocking the Regis")
    st.write("To unlock the Regi chambers, you need Relicanth (first slot) and Wailord (last slot).")
    
    with st.expander("Sealed Chamber Guide"):
        st.write("Dive on Route 134. Go to the Braille inscription at the end and use **Dig**.")
    
    st.subheader("Braille Decoder")
    # Quick ASCII representation or just text mapping for common phrases 
    st.text("""
    ABC: .  :  ..
         .. .  .. 
         .. .. ..
         
    (Simplified: Refer to online charts for full translation)
    """)
    st.info("Tip: Use Braille to read the inscriptions in the desert ruins, island cave, and ancient tomb.")

with tab2:
    st.header("Mirage Spot Schedule")
    # Simple logic: Some mirage spots appear daily or randomly. 
    # Let's mock a schedule based on day of week for "Daily" spots or just show the logic.
    
    today = datetime.now()
    day_name = today.strftime("%A")
    
    st.metric("Today is", day_name)
    
    # Hardcoded schedule example (Common mechanic in ORAS is daily rotation)
    schedule = {
        "Monday": "Nameless Cavern (Mesprit)",
        "Tuesday": "Pathless Plain (Cobalion)",
        "Wednesday": "Fabled Cave (Reshiram/Zekrom requirements)",
        "Thursday": "Gnarled Den (Kyurem requirement)",
        "Friday": "Crescent Isle (Random/Cresselia)",
        "Saturday": "Trackless Forest (Raikou/Entei/Suicune)",
        "Sunday": "Dimensional Rift (Deoxys/Story)"
    }
    # Note: Real ORAS schedule is complex/random for some, specific for others. This is a simplified companion guide.
    
    spot = schedule.get(day_name, "Check your BuzzNav for random spots!")
    st.success(f"Potential Legendaries today: **{spot}**")

with tab3:
    st.header("Feebas Tile Calculator")
    st.caption("In Original R/S/E, Feebas was on 6 random tiles. In ORAS, it's easier, but here's a helper for the 'Dewford Phrase' mechanic if playing legacy.")
    
    phrase = st.text_input("Enter the Trendy Phrase from Dewford Town:")
    
    if phrase:
        # Dummy calculation logic for demonstration
        # Real algorithm is complex bitwise op on string hash
        st.warning("Calculated Tile Area: **Route 119 - North Bridge (Approximation)**")
        st.write("Just kidding! In ORAS, Feebas can be found in Route 119 by fishing under the bridge during the day with 100% rate, or randomly elsewhere.")
