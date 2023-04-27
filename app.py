import streamlit as st
st.set_option('server.enableCORS', True)
headline = st.text_input('Enter news headline (Hindi/English):')
# Population size input
pop_size = st.number_input('Enter population size:')
# Population growth rate input
pop_growth = st.number_input('Enter population growth rate:')
# Number of interventions input
num_interventions = st.number_input('Enter number of interventions to be added:', min_value=1, max_value=10, step=1)
# Position of interventions input
intervention_positions = ['Random', 'Max degree', 'Max centrality']
selected_position = st.selectbox('Choose position of interventions:', options=intervention_positions)
