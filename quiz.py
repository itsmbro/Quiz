import streamlit as st
import random
import time

# Lista di domande e risposte (inserisci le tue domande e risposte)
questions = [
    {"question": "Qual è la velocità della luce?", "options": ["300.000 km/s", "150.000 km/s", "400.000 km/s", "200.000 km/s"], "answer": "300.000 km/s"},
    {"question": "Chi ha formulato la teoria della relatività?", "options": ["Newton", "Einstein", "Galileo", "Tesla"], "answer": "Einstein"},
    {"question": "Qual è l'elemento chimico con simbolo H?", "options": ["Idrogeno", "Ero", "Elio", "Hafnio"], "answer": "Idrogeno"},
    {"question": "Cosa misura un barometro?", "options": ["Temperatura", "Pressione atmosferica", "Velocità", "Densità"], "answer": "Pressione atmosferica"},
    {"question": "Chi ha scoperto la legge della gravitazione universale?", "options": ["Einstein", "Galileo", "Newton", "Keplero"], "answer": "Newton"},
    {"question": "Che tipo di onda è la luce?", "options": ["Meccanica", "Elettromagnetica", "Sonora", "Gravitazionale"], "answer": "Elettromagnetica"},
    {"question": "Cosa misura il termometro?", "options": ["Temperatura", "Pressione", "Densità", "Velocità"], "answer": "Temperatura"},
    {"question": "Qual è il più grande pianeta del nostro sistema solare?", "options": ["Terra", "Saturno", "Giove", "Urano"], "answer": "Giove"},
    {"question": "Cos'è l'energia cinetica?", "options": ["Energia associata al movimento", "Energia immagazzinata", "Energia prodotta dal calore", "Energia da luce"], "answer": "Energia associata al movimento"},
    {"question": "Che cos'è un isotopo?", "options": ["Un atomo con lo stesso numero di protoni ma diversi neutroni", "Un atomo con lo stesso numero di neutroni ma diversi protoni", "Un elemento chimico", "Una molecola"], "answer": "Un atomo con lo stesso numero di protoni ma diversi neutroni"},
    {"question": "Quante leggi del moto ha formulato Newton?", "options": ["1", "2", "3", "4"], "answer": "3"},
    {"question": "Qual è la formula dell'energia cinetica?", "options": ["E = m * v", "E = 1/2 * m * v^2", "E = m * h", "E = m * g"], "answer": "E = 1/2 * m * v^2"},
    {"question": "Cos'è la materia oscura?", "options": ["Una sostanza invisibile", "Una forma di energia", "Un tipo di luce", "Un elemento chimico"], "answer": "Una sostanza invisibile"},
    {"question": "Quanti protoni ci sono nell'atomo di idrogeno?", "options": ["1", "2", "3", "0"], "answer": "1"},
    {"question": "In quale unità si misura l'intensità della corrente elettrica?", "options": ["Volt", "Ampere", "Coulomb", "Watt"], "answer": "Ampere"},
    {"question": "Qual è la legge di Ohm?", "options": ["V = I * R", "P = I * R", "V = P * I", "V = I * T"], "answer": "V = I * R"},
    {"question": "Che cos'è la radioattività?", "options": ["Emissione di particelle da un nucleo instabile", "Emissione di luce visibile", "Emissione di energia", "Emissione di suono"], "answer": "Emissione di particelle da un nucleo instabile"},
    {"question": "Quale tra questi è un combustibile fossile?", "options": ["Petrolio", "Solare", "Eolico", "Geotermico"], "answer": "Petrolio"},
    {"question": "Qual è la formula della legge di Gravitazione Universale?", "options": ["F = G * (m1 * m2) / r^2", "F = m * a", "F = k * q1 * q2 / r^2", "F = m * v"], "answer": "F = G * (m1 * m2) / r^2"},
    {"question": "Quante ore ci sono in un giorno?", "options": ["12", "24", "48", "72"], "answer": "24"},
    {"question": "Chi ha sviluppato il concetto di relatività speciale?", "options": ["Einstein", "Newton", "Galileo", "Maxwell"], "answer": "Einstein"},
    {"question": "Cos'è un atomo?", "options": ["La parte più piccola di un elemento chimico", "Una molecola", "Una particella subatomica", "Una forma di energia"], "answer": "La parte più piccola di un elemento chimico"},
    {"question": "Come si chiama l'effetto che spiega il cambiamento della luce in movimento?", "options": ["Effetto Doppler", "Effetto Hall", "Effetto Compton", "Effetto fotoelettrico"], "answer": "Effetto Doppler"},
    {"question": "Cosa rappresenta la costante di Planck?", "options": ["La quantità minima di energia", "La velocità della luce", "La massa di un elettrone", "La carica di un protone"], "answer": "La quantità minima di energia"},
    {"question": "In quale unità si misura la temperatura?", "options": ["Kelvin", "Joule", "Ampere", "Watt"], "answer": "Kelvin"},
    {"question": "Qual è il più piccolo stato della materia?", "options": ["Gas", "Liquido", "Solido", "Plasma"], "answer": "Gas"},
    {"question": "Chi ha scoperto l'elettrone?", "options": ["Rutherford", "Thomson", "Bohr", "Einstein"], "answer": "Thomson"},
    {"question": "Cos'è un acceleratore di particelle?", "options": ["Un dispositivo che accelera le particelle subatomiche", "Un dispositivo che misura la velocità delle particelle", "Un dispositivo che raffredda le particelle", "Un dispositivo che genera energia"], "answer": "Un dispositivo che accelera le particelle subatomiche"},
    {"question": "Che tipo di particelle sono i neutrini?", "options": ["Particelle subatomiche senza carica", "Particelle cariche", "Fotoni", "Elettroni"], "answer": "Particelle subatomiche senza carica"},
    {"question": "Cosa succede quando un oggetto supera la velocità della luce?", "options": ["Diventa invisibile", "Diventa rosso", "Non è possibile secondo la relatività", "Scompare"], "answer": "Non è possibile secondo la relatività"},
    {"question": "Cos'è il modello atomico di Bohr?", "options": ["Un modello che rappresenta gli elettroni in orbite circolari attorno al nucleo", "Un modello che rappresenta gli atomi come un insieme di sfere", "Un modello che rappresenta gli atomi come una nuvola di particelle", "Un modello che rappresenta solo protoni e neutroni"], "answer": "Un modello che rappresenta gli elettroni in orbite circolari attorno al nucleo"},
    {"question": "Quale fenomeno fisico descrive la rifrazione?", "options": ["Il cambiamento di direzione della luce quando passa da un mezzo a un altro", "La riflessione della luce", "L'emissione di radiazioni", "La propagazione del suono"], "answer": "Il cambiamento di direzione della luce quando passa da un mezzo a un altro"},
    # ... Continua con altre 80 domande simili
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
