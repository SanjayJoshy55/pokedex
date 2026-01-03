import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Hoenn Pokedex", page_icon="📱")

st.title("📱 Hoenn Pokedex")

# Load Data
@st.cache_data
def load_data():
    path = os.path.join("data", "hoenn_pokedex.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame() # Empty if not found

df = load_data()

if df.empty:
    st.error("Data not found! Please run `scripts/fetch_pokedex_data.py` or ensure `data/hoenn_pokedex.csv` exists.")
else:
    # Sidebar filter
    st.sidebar.header("Filter")
    search = st.sidebar.text_input("Search Pokemon", "")
    
    if search:
        df = df[df['name'].str.contains(search, case=False, na=False)]

    # Main Data View
    # st.dataframe with selection is available in newer streamlit, but let's use a two-column layout 
    # where user selects from a box or clicks on the table.
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader("Database")
        st.dataframe(
            df[['id', 'name', 'types', 'location']], # Show relevant cols
            use_container_width=True,
            height=600,
            hide_index=True
        )
        
    with col2:
        st.subheader("Selected Details")
        selected_mon_name = st.selectbox("Select a Pokemon to view details:", df['name'].unique())
        
        if selected_mon_name:
            # Get the row
            row = df[df['name'] == selected_mon_name].iloc[0]
            
            # Display
            st.markdown(f"### #{row['id']} {row['name']}")
            
            # Sprite
            if 'sprite_url' in row and pd.notna(row['sprite_url']):
                st.image(row['sprite_url'], width=200)
            
            st.markdown("---")
            st.markdown(f"**Type(s):** {row['types']}")
            st.markdown(f"**Location (ORAS):**")
            st.info(row['location'])
