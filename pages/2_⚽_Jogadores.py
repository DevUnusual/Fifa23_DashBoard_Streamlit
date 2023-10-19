import streamlit as st

st.set_page_config(page_title="Jogadores", page_icon=":soccer:", layout="wide")

df_data = st.session_state["df_fifa"]

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Selecione um clube", clubes)

df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Selecione um jogador", players)
player_stats = df_players[df_players["Name"] == player].iloc[0]

#st.write(player_stats)

col1, col2 = st.columns([0.10 , 0.90])
col1.image(player_stats["Photo"])
col2.image(player_stats["Flag"])
st.title(player_stats["Name"])

st.markdown("**Clube**: " + player_stats["Club"])
st.markdown("**Posição**: " + player_stats["Position"])
col1, col2, col3, _ = st.columns(4)
col1.markdown("**Idade**: " + str(player_stats["Age"])) 
col2.markdown(f"**Altura**: {player_stats['Height(cm.)'] / 100}cm")
col3.markdown(f"**Peso**: {player_stats['Weight(lbs.)']*0.453:0.2f} kg")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

col1, col2, col3, _ = st.columns(4)
col1.metric(label= "Valor de mercado", value=f"£: {player_stats['Value(£)']:},")
col2.metric(label= "Salário", value=f"£: {player_stats['Wage(£)']:},")
col3.metric(label= "Clausula de rescisao", value=f"£: {player_stats['Release Clause(£)']:},")
