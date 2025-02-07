import streamlit as st
import random
import time

# Lista di domande e risposte (inserisci le tue domande e risposte)
questions = [
    {"question": "Qual è la velocità della luce?", "options": ["300.000 km/s", "150.000 km/s", "400.000 km/s", "200.000 km/s"], "answer": "300.000 km/s"},
    {"question": "Chi ha formulato la teoria della relatività?", "options": ["Newton", "Einstein", "Galileo", "Tesla"], "answer": "Einstein"},
    # Aggiungi altre 98 domande qui
]

# Funzione per mostrare la schermata iniziale
def show_intro():
    st.title("Quiz sulla Scienza e sulla Fisica")
    st.write("Benvenuto! Imposta il numero di giocatori e i loro nickname.")
    
    num_players = st.slider("Seleziona il numero di giocatori", 1, 4, 1)
    players = {}
    
    for i in range(num_players):
        players[f"Player {i+1}"] = st.text_input(f"Nome del giocatore {i+1}", f"Giocatore {i+1}")
    
    return players

# Funzione per giocare
def play_game(players):
    scores = {player: 0 for player in players}
    rounds = 5
    
    for round_num in range(1, rounds + 1):
        st.subheader(f"Round {round_num}")
        random.shuffle(questions)
        
        for player in players:
            st.write(f"{player}'s turn!")
            question = questions[round_num - 1]  # Assicurati che le domande siano selezionate correttamente
            
            st.write(question["question"])
            answer = st.radio("Scegli una risposta", question["options"])
            
            if answer == question["answer"]:
                st.write("Risposta corretta!")
                scores[player] += 1
            else:
                st.write(f"Risposta sbagliata. La risposta corretta era: {question['answer']}")
            
            time.sleep(1)  # Pausa di 1 secondo tra le risposte
    
    return scores

# Funzione per mostrare il vincitore con animazione
def show_winner(scores):
    winner = max(scores, key=scores.get)
    st.write(f"Il vincitore è {winner} con {scores[winner]} punti!")
    
    # Animazione finale (per esempio, un effetto di scrittura del nome vincitore)
    for char in winner:
        st.markdown(f"<h1 style='color: red;'>{char}</h1>", unsafe_allow_html=True)
        time.sleep(0.2)
        st.experimental_rerun()

# Funzione principale che esegue il gioco
def main():
    players = show_intro()
    if st.button("Inizia il quiz"):
        scores = play_game(players)
        show_winner(scores)

# Avvio del gioco
if __name__ == "__main__":
    main()
