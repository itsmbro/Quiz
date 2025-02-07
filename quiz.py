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
    {"question": "Qual è la legge di Coulomb?", "options": ["F = k * (q1 * q2) / r^2", "F = m * a", "F = G * (m1 * m2) / r^2", "F = I * R"], "answer": "F = k * (q1 * q2) / r^2"},
    {"question": "Cos'è l'effetto fotoelettrico?", "options": ["Emissione di elettroni da un materiale quando illuminato", "Emissione di luce da un materiale quando riscaldato", "Assorbimento di radiazioni da parte di un atomo", "Radiazione prodotta dalle particelle subatomiche"], "answer": "Emissione di elettroni da un materiale quando illuminato"},
    {"question": "Che cos'è la termodinamica?", "options": ["Lo studio delle leggi del calore e dell'energia", "Lo studio delle particelle subatomiche", "Lo studio del comportamento degli elettroni", "Lo studio della gravità"], "answer": "Lo studio delle leggi del calore e dell'energia"},
    {"question": "Qual è la formula dell'energia potenziale gravitazionale?", "options": ["E = m * g * h", "E = m * v^2", "E = 1/2 * m * v^2", "E = G * (m1 * m2) / r^2"], "answer": "E = m * g * h"},
    {"question": "Cosa succede durante una reazione di fissione nucleare?", "options": ["Il nucleo di un atomo si divide in due parti", "Il nucleo di un atomo si unisce con un altro", "Il numero di neutroni aumenta", "La massa di un atomo diminuisce"], "answer": "Il nucleo di un atomo si divide in due parti"},
    {"question": "Cos'è l'elasticità?", "options": ["La capacità di un materiale di tornare alla sua forma originale dopo essere stato deformato", "La capacità di un materiale di essere solido", "La capacità di un materiale di assorbire calore", "La capacità di un materiale di condurre elettricità"], "answer": "La capacità di un materiale di tornare alla sua forma originale dopo essere stato deformato"},
    {"question": "Che cos'è una supernova?", "options": ["Un'esplosione stellare alla fine della vita di una stella massiccia", "Un tipo di stella che emette solo luce rossa", "Una galassia che si avvicina alla Terra", "Un buco nero che cresce enormemente"], "answer": "Un'esplosione stellare alla fine della vita di una stella massiccia"},
    {"question": "Chi ha scoperto il principio di indeterminazione?", "options": ["Bohr", "Einstein", "Heisenberg", "Fermi"], "answer": "Heisenberg"},
    {"question": "Che cos'è un buchi neri?", "options": ["Una regione dello spazio con un campo gravitazionale così forte che nulla può sfuggirvi", "Una stella molto piccola", "Una particella subatomica", "Un fenomeno che accade solo nelle nebulose"], "answer": "Una regione dello spazio con un campo gravitazionale così forte che nulla può sfuggirvi"},
    {"question": "Chi ha proposto il modello atomico planetario?", "options": ["Einstein", "Bohr", "Rutherford", "Thomson"], "answer": "Bohr"},
    {"question": "Cos'è un acceleratore di particelle?", "options": ["Un dispositivo che accelera particelle subatomiche", "Un dispositivo che misura la velocità delle particelle", "Un dispositivo che raffredda le particelle", "Un dispositivo che genera energia"], "answer": "Un dispositivo che accelera particelle subatomiche"},
    {"question": "Quale tra questi è un esempio di energia rinnovabile?", "options": ["Energia solare", "Energia nucleare", "Energia fossile", "Energia geotermica"], "answer": "Energia solare"},
    {"question": "Cos'è un magnete?", "options": ["Un oggetto che genera un campo magnetico", "Un oggetto che genera una corrente elettrica", "Un oggetto che emette luce", "Un oggetto che attrae l'elettricità"], "answer": "Un oggetto che genera un campo magnetico"},
    {"question": "Cos'è la teoria delle stringhe?", "options": ["Una teoria che cerca di spiegare le particelle subatomiche come vibrazioni di stringhe energetiche", "Una teoria che descrive il moto delle particelle", "Una teoria che spiega la relatività", "Una teoria che descrive i buchi neri"], "answer": "Una teoria che cerca di spiegare le particelle subatomiche come vibrazioni di stringhe energetiche"},
    {"question": "Che cos'è il vuoto quantistico?", "options": ["Uno stato di energia minima in cui le particelle fluttuano", "Una zona dello spazio senza materia", "Una regione dove non esistono leggi fisiche", "Un'area priva di campi magnetici"], "answer": "Uno stato di energia minima in cui le particelle fluttuano"},
    {"question": "Cos'è la materia oscura?", "options": ["Una sostanza che non emette luce e che non possiamo vedere", "Un tipo di energia", "Una sostanza che si trova solo nel nostro corpo", "Una materia visibile ma invisibile ai nostri occhi"], "answer": "Una sostanza che non emette luce e che non possiamo vedere"},
    {"question": "Cos'è la fusione nucleare?", "options": ["Il processo in cui due nuclei leggeri si uniscono per formare un nucleo più pesante", "Il processo in cui un nucleo pesante si divide in nuclei più leggeri", "Il processo in cui un atomo rilascia elettroni", "Il processo in cui una particella viene accelerata"], "answer": "Il processo in cui due nuclei leggeri si uniscono per formare un nucleo più pesante"},
    {"question": "Qual è la particella che porta la forza elettromagnetica?", "options": ["Fotone", "Neutrino", "Elettrone", "Quark"], "answer": "Fotone"},
    {"question": "Chi ha sviluppato il principio di esclusione?", "options": ["Heisenberg", "Fermi", "Pauli", "Dirac"], "answer": "Pauli"},
    {"question": "Cos'è la teoria del Big Bang?", "options": ["Una teoria che spiega l'origine dell'universo", "Una teoria che spiega la gravitazione", "Una teoria che descrive l'evoluzione della materia", "Una teoria che spiega la velocità della luce"], "answer": "Una teoria che spiega l'origine dell'universo"},
    {"question": "Qual è la particella subatomica di carica negativa?", "options": ["Neutrino", "Protone", "Elettrone", "Neutroni"], "answer": "Elettrone"},
    {"question": "Qual è la legge di Hooke?", "options": ["F = k * x", "F = m * a", "F = P * V", "F = G * (m1 * m2) / r^2"], "answer": "F = k * x"},
    {"question": "Cos'è un'onda elettromagnetica?", "options": ["Un'onda che non ha bisogno di un mezzo per propagarsi", "Un'onda che si propaga in un fluido", "Un'onda che si propaga solo nel vuoto", "Un'onda che è generata da particelle subatomiche"], "answer": "Un'onda che non ha bisogno di un mezzo per propagarsi"},
    {"question": "Cos'è la teoria della relatività generale?", "options": ["Una teoria che descrive la gravità come una curvatura dello spazio-tempo", "Una teoria che descrive il comportamento delle particelle subatomiche", "Una teoria che spiega la fisica dei buchi neri", "Una teoria che descrive la velocità della luce"], "answer": "Una teoria che descrive la gravità come una curvatura dello spazio-tempo"},
    {"question": "Cosa accade durante la fusione nucleare?", "options": ["Due nuclei leggeri si uniscono per formare un nucleo più pesante", "Un nucleo pesante si divide in due nuclei leggeri", "Un elettrone si unisce con un protone", "Un fotone si trasforma in una particella"], "answer": "Due nuclei leggeri si uniscono per formare un nucleo più pesante"},
    {"question": "Cosa significa il termine 'quark'?", "options": ["La particella subatomica che forma protoni e neutroni", "La particella che porta la forza gravitazionale", "Una forma di energia", "Una particella che esiste solo in uno stato quantico"], "answer": "La particella subatomica che forma protoni e neutroni"},
    {"question": "Cos'è un campo gravitazionale?", "options": ["Una regione in cui una massa subisce una forza gravitazionale", "Una regione in cui si verifica la fissione nucleare", "Una regione di energia magnetica", "Una regione in cui la luce non può passare"], "answer": "Una regione in cui una massa subisce una forza gravitazionale"},
    {"question": "Cosa misura un accelerometro?", "options": ["Accelerazione", "Velocità", "Temperatura", "Energia"], "answer": "Accelerazione"},
    {"question": "Cos'è la legge di Faraday?", "options": ["La legge che descrive la relazione tra variazione del flusso magnetico e forza elettromotrice", "La legge che descrive la forza tra cariche elettriche", "La legge che descrive l'energia cinetica", "La legge che descrive la velocità della luce"], "answer": "La legge che descrive la relazione tra variazione del flusso magnetico e forza elettromotrice"},
    {"question": "Cos'è un superconduttore?", "options": ["Un materiale che ha resistenza elettrica nulla a basse temperature", "Un materiale che conduce calore velocemente", "Un materiale che emette luce", "Un materiale che assorbe energia"], "answer": "Un materiale che ha resistenza elettrica nulla a basse temperature"}
    ]

players=["",""]

# Inizializza lo stato della sessione
if 'game_state' not in st.session_state:
    st.session_state.game_state = 0  # 0: schermata iniziale, 1: domande giocatore 1, 2: domande giocatore 2, 3: fine gioco
    st.session_state.players = ["", ""]
    st.session_state.scores = [0, 0]
    st.session_state.current_question_index = 0
    st.session_state.questions_player1 = []
    st.session_state.questions_player2 = []



# Funzione per resettare il gioco
def reset_game():
    st.session_state.game_state = 0
    st.session_state.players = ["", ""]
    st.session_state.scores = [0, 0]
    st.session_state.current_question_index = 0
    st.session_state.questions_player1 = random.sample(questions, 5)
    st.session_state.questions_player2 = random.sample(questions, 5)

# Funzione per mostrare una domanda
def show_question(player_index):
    player = st.session_state.players[player_index]
    current_question_list = st.session_state.questions_player1 if player_index == 0 else st.session_state.questions_player2
    question = current_question_list[st.session_state.current_question_index]

    st.subheader(f"Domanda per {player}:")
    st.write(question["question"])
    answer = st.radio("Scegli la risposta:", question["options"], key=f"answer_{st.session_state.current_question_index}")

    if st.button("Conferma risposta"):
        if answer == question["answer"]:
            st.success("Risposta corretta!")
            st.session_state.scores[player_index] += 1
        else:
            st.error(f"Risposta errata. La risposta corretta era: {question['answer']}")

        st.session_state.current_question_index += 1

        # Passaggio al prossimo turno
        if st.session_state.current_question_index >= 5:
            if st.session_state.game_state == 1:
                st.session_state.game_state = 2  # Passa al giocatore 2
            else:
                st.session_state.game_state = 3  # Fine del gioco
            st.session_state.current_question_index = 0

# Schermata iniziale
if st.session_state.game_state == 0:
    st.title("🎯 Gioco di Quiz Multiplayer")
    st.write("Inserisci i nomi dei due giocatori per iniziare:")
    
    players[0] = st.text_input("Nome Giocatore 1", key="player1")
    players[1] = st.text_input("Nome Giocatore 2", key="player2")
    
    if st.button("Avvia Gioco"):
        if players[0] and players[1]:
            reset_game()  # Resetta e mescola le domande
            st.session_state.game_state = 1  # Inizia con il giocatore 1
        else:
            st.warning("Inserisci entrambi i nomi per continuare.")

# Domande per il Giocatore 1
elif st.session_state.game_state == 1:
    st.header(f"🎮 Turno di {players[0]}")
    show_question(0)

# Domande per il Giocatore 2
elif st.session_state.game_state == 2:
    st.header(f"🎮 Turno di {players[1]}")
    show_question(1)

# Schermata finale con i punteggi
elif st.session_state.game_state == 3:
    st.title("🏆 Risultati Finali")
    st.write(f"**{st.session_state.players[0]}:** {st.session_state.scores[0]} punti")
    st.write(f"**{st.session_state.players[1]}:** {st.session_state.scores[1]} punti")
    
    if st.session_state.scores[0] > st.session_state.scores[1]:
        st.success(f"🎉 Il vincitore è {st.session_state.players[0]}!")
    elif st.session_state.scores[0] < st.session_state.scores[1]:
        st.success(f"🎉 Il vincitore è {st.session_state.players[1]}!")
    else:
        st.info("🤝 È un pareggio!")

    if st.button("Gioca di nuovo"):
        reset_game()
