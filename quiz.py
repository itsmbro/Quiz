import streamlit as st
import random
import time






# Inizializzazione dello stato della sessione
if 'players' not in st.session_state:
    st.session_state.players = ["", ""]
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'current_player' not in st.session_state:
    st.session_state.current_player = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'scores' not in st.session_state:
    st.session_state.scores = [0, 0]
if 'questions_p1' not in st.session_state:
    st.session_state.questions_p1 = []
if 'questions_p2' not in st.session_state:
    st.session_state.questions_p2 = []


# Lista di domande e risposte (inserisci le tue domande e risposte)
questions = [
    {"question": "Qual è la velocità della luce?", "options": ["150.000 km/s", "300.000 km/s", "400.000 km/s", "200.000 km/s"], "answer": "300.000 km/s"},
    {"question": "Chi ha formulato la teoria della relatività?", "options": ["Galileo", "Tesla", "Einstein", "Newton"], "answer": "Einstein"},
    {"question": "Qual è l'elemento chimico con simbolo H?", "options": ["Elio", "Hafnio", "Ero", "Idrogeno"], "answer": "Idrogeno"},
    {"question": "Cosa misura un barometro?", "options": ["Velocità", "Densità", "Temperatura", "Pressione atmosferica"], "answer": "Pressione atmosferica"},
    {"question": "Chi ha scoperto la legge della gravitazione universale?", "options": ["Galileo", "Newton", "Keplero", "Einstein"], "answer": "Newton"},
    {"question": "Che tipo di onda è la luce?", "options": ["Sonora", "Gravitazionale", "Meccanica", "Elettromagnetica"], "answer": "Elettromagnetica"},
    {"question": "Cosa misura il termometro?", "options": ["Pressione", "Velocità", "Temperatura", "Densità"], "answer": "Temperatura"},
    {"question": "Qual è il più grande pianeta del nostro sistema solare?", "options": ["Saturno", "Giove", "Urano", "Terra"], "answer": "Giove"},
    {"question": "Cos'è l'energia cinetica?", "options": ["Energia immagazzinata", "Energia da luce", "Energia prodotta dal calore", "Energia associata al movimento"], "answer": "Energia associata al movimento"},
    {"question": "Che cos'è un isotopo?", "options": ["Un atomo con lo stesso numero di neutroni ma diversi protoni", "Un atomo con lo stesso numero di protoni ma diversi neutroni", "Un elemento chimico", "Una molecola"], "answer": "Un atomo con lo stesso numero di protoni ma diversi neutroni"},
    {"question": "Quante leggi del moto ha formulato Newton?", "options": ["2", "1", "4", "3"], "answer": "3"},
    {"question": "Qual è la formula dell'energia cinetica?", "options": ["E = 1/2 * m * v^2", "E = m * v", "E = m * g", "E = m * h"], "answer": "E = 1/2 * m * v^2"},
    {"question": "Cos'è la materia oscura?", "options": ["Una forma di energia", "Un tipo di luce", "Un elemento chimico", "Una sostanza invisibile"], "answer": "Una sostanza invisibile"},
    {"question": "Quanti protoni ci sono nell'atomo di idrogeno?", "options": ["0", "3", "2", "1"], "answer": "1"},
    {"question": "In quale unità si misura l'intensità della corrente elettrica?", "options": ["Ampere", "Volt", "Coulomb", "Watt"], "answer": "Ampere"},
    {"question": "Qual è la legge di Ohm?", "options": ["P = I * R", "V = I * T", "V = P * I", "V = I * R"], "answer": "V = I * R"},
    {"question": "Che cos'è la radioattività?", "options": ["Emissione di energia", "Emissione di particelle da un nucleo instabile", "Emissione di suono", "Emissione di luce visibile"], "answer": "Emissione di particelle da un nucleo instabile"},
    {"question": "Quale tra questi è un combustibile fossile?", "options": ["Solare", "Petrolio", "Eolico", "Geotermico"], "answer": "Petrolio"},
    {"question": "Qual è la formula della legge di Gravitazione Universale?", "options": ["F = G * (m1 * m2) / r^2", "F = m * v", "F = k * q1 * q2 / r^2", "F = m * a"], "answer": "F = G * (m1 * m2) / r^2"},
    {"question": "Quante ore ci sono in un giorno?", "options": ["48", "12", "72", "24"], "answer": "24"},
    {"question": "Chi ha sviluppato il concetto di relatività speciale?", "options": ["Newton", "Maxwell", "Galileo", "Einstein"], "answer": "Einstein"},
    {"question": "Cos'è un atomo?", "options": ["Una molecola", "Una particella subatomica", "La parte più piccola di un elemento chimico", "Una forma di energia"], "answer": "La parte più piccola di un elemento chimico"},
    {"question": "Come si chiama l'effetto che spiega il cambiamento della luce in movimento?", "options": ["Effetto Hall", "Effetto Doppler", "Effetto Compton", "Effetto fotoelettrico"], "answer": "Effetto Doppler"},
    {"question": "Cosa rappresenta la costante di Planck?", "options": ["La carica di un protone", "La massa di un elettrone", "La velocità della luce", "La quantità minima di energia"], "answer": "La quantità minima di energia"},
    {"question": "In quale unità si misura la temperatura?", "options": ["Kelvin", "Ampere", "Watt", "Joule"], "answer": "Kelvin"},
    {"question": "Chi ha scoperto l'elettrone?", "options": ["Bohr", "Thomson", "Rutherford", "Einstein"], "answer": "Thomson"},
    {"question": "Cos'è un acceleratore di particelle?", "options": ["Un dispositivo che genera energia", "Un dispositivo che misura la velocità delle particelle", "Un dispositivo che accelera particelle subatomiche", "Un dispositivo che raffredda le particelle"], "answer": "Un dispositivo che accelera particelle subatomiche"},
    {"question": "Che tipo di particelle sono i neutrini?", "options": ["Elettroni", "Fotoni", "Particelle cariche", "Particelle subatomiche senza carica"], "answer": "Particelle subatomiche senza carica"},
    {"question": "Cosa succede quando un oggetto supera la velocità della luce?", "options": ["Non è possibile secondo la relatività", "Diventa invisibile", "Scompare", "Diventa rosso"], "answer": "Non è possibile secondo la relatività"},
    {"question": "Cos'è il modello atomico di Bohr?", "options": ["Un modello che rappresenta gli atomi come una nuvola di particelle", "Un modello che rappresenta gli elettroni in orbite circolari attorno al nucleo", "Un modello che rappresenta solo protoni e neutroni", "Un modello che rappresenta gli atomi come un insieme di sfere"], "answer": "Un modello che rappresenta gli elettroni in orbite circolari attorno al nucleo"},
    {"question": "Quale fenomeno fisico descrive la rifrazione?", "options": ["Il cambiamento di direzione della luce quando passa da un mezzo a un altro", "L'emissione di radiazioni", "La riflessione della luce", "La propagazione del suono"], "answer": "Il cambiamento di direzione della luce quando passa da un mezzo a un altro"},
    {"question": "Qual è la legge di Coulomb?", "options": ["F = k * (q1 * q2) / r^2", "F = I * R", "F = m * a", "F = G * (m1 * m2) / r^2"], "answer": "F = k * (q1 * q2) / r^2"},
    {"question": "Cos'è l'effetto fotoelettrico?", "options": ["Emissione di elettroni da un materiale quando illuminato", "Emissione di luce da un materiale quando riscaldato", "Assorbimento di radiazioni da parte di un atomo", "Radiazione prodotta dalle particelle subatomiche"], "answer": "Emissione di elettroni da un materiale quando illuminato"},
    {"question": "Che cos'è la termodinamica?", "options": ["Lo studio delle particelle subatomiche", "Lo studio delle leggi del calore e dell'energia", "Lo studio del comportamento degli elettroni", "Lo studio della gravità"], "answer": "Lo studio delle leggi del calore e dell'energia"},
    {"question": "Qual è la formula per calcolare la densità?", "options": ["m / V", "F * d", "V / m", "P * A"], "answer": "m / V"},
    {"question": "Quale unità di misura rappresenta il Joule?", "options": ["Forza", "Energia", "Temperatura", "Pressione"], "answer": "Energia"},
    {"question": "Cosa rappresenta la seconda legge di Newton?", "options": ["F = m * a", "E = mc²", "p = m * v", "V = I * R"], "answer": "F = m * a"},
    {"question": "Quale grandezza fisica si misura in Pascal?", "options": ["Velocità", "Pressione", "Energia", "Temperatura"], "answer": "Pressione"},
    {"question": "Qual è la velocità del suono nell’aria a temperatura ambiente?", "options": ["1500 m/s", "343 m/s", "1200 m/s", "299.792 m/s"], "answer": "343 m/s"},
    {"question": "Qual è la costante di gravità universale (G)?", "options": ["9.8 m/s²", "6.67 × 10⁻¹¹ N·m²/kg²", "3 × 10⁸ m/s", "1.6 × 10⁻¹⁹ C"], "answer": "6.67 × 10⁻¹¹ N·m²/kg²"},
    {"question": "Cosa rappresenta la quantità di moto?", "options": ["Il prodotto tra massa e velocità", "Il rapporto tra forza e accelerazione", "L’energia totale di un corpo", "La resistenza di un materiale"], "answer": "Il prodotto tra massa e velocità"},
    {"question": "Quale tra questi fenomeni è dovuto all’effetto Doppler?", "options": ["Cambiamento di colore delle stelle in movimento", "Propagazione della luce attraverso un prisma", "Curvatura della luce vicino a un buco nero", "Polarizzazione della luce"], "answer": "Cambiamento di colore delle stelle in movimento"},
    {"question": "In un circuito elettrico, cosa misura un voltmetro?", "options": ["Corrente elettrica", "Differenza di potenziale", "Resistenza elettrica", "Potenza dissipata"], "answer": "Differenza di potenziale"},
    {"question": "Qual è la formula per la legge di conservazione dell’energia meccanica?", "options": ["E = K + U", "F = m * a", "P = V * I", "W = F * d"], "answer": "E = K + U"},
    {"question": "Cos'è un’onda longitudinale?", "options": ["Un'onda in cui la direzione di propagazione coincide con la direzione di oscillazione", "Un'onda che si propaga solo nel vuoto", "Un'onda elettromagnetica", "Un'onda visibile a occhio nudo"], "answer": "Un'onda in cui la direzione di propagazione coincide con la direzione di oscillazione"},
    {"question": "Cosa rappresenta il principio di Archimede?", "options": ["Un corpo immerso in un fluido riceve una spinta verso l'alto pari al peso del fluido spostato", "L’energia totale di un sistema isolato resta costante", "La velocità della luce è costante in tutti i sistemi di riferimento", "La forza è uguale al prodotto tra massa e accelerazione"], "answer": "Un corpo immerso in un fluido riceve una spinta verso l'alto pari al peso del fluido spostato"},
    {"question": "Qual è la formula della legge di Hooke?", "options": ["F = -k * x", "F = m * a", "P = V * I", "E = m * c²"], "answer": "F = -k * x"},
    {"question": "Quale particella subatomica ha carica negativa?", "options": ["Protone", "Neutrone", "Elettrone", "Fotone"], "answer": "Elettrone"},
    {"question": "Cosa descrive il principio di conservazione della quantità di moto?", "options": ["La quantità di moto totale di un sistema isolato rimane costante", "L’energia può essere creata o distrutta", "La forza è sempre perpendicolare alla velocità", "La massa di un corpo può variare in condizioni normali"], "answer": "La quantità di moto totale di un sistema isolato rimane costante"}
]






# Fase 1: Inserimento dei nickname
if st.session_state.current_step == 0:
    st.title("🎯 Gioco di Quiz Multiplayer")
    st.session_state.players[0] = st.text_input("Nome Giocatore 1", key="player1")
    st.session_state.players[1] = st.text_input("Nome Giocatore 2", key="player2")

    if st.button("Avvia Gioco") and st.session_state.players[0] and st.session_state.players[1]:
        st.session_state.current_step = 1
        st.session_state.questions_p1 = random.sample(questions, 5)
        st.session_state.questions_p2 = random.sample(questions, 5)

# Fase 2: Turno di gioco
elif st.session_state.current_step == 1:
    player = st.session_state.players[st.session_state.current_player]
    st.header(f"🎮 Turno di {player}")

    current_questions = st.session_state.questions_p1 if st.session_state.current_player == 0 else st.session_state.questions_p2
    question_data = current_questions[st.session_state.current_question]

    with st.form(key=f"form_{st.session_state.current_player}_{st.session_state.current_question}"):
        st.write(f"Domanda {st.session_state.current_question + 1}: {question_data['question']}")
        selected_option = st.radio("Scegli la risposta:", question_data['options'])
        submit = st.form_submit_button("Prossima Domanda")

        if submit:
            if selected_option == question_data['answer']:
                st.session_state.scores[st.session_state.current_player] += 1

            st.session_state.current_question += 1

            if st.session_state.current_question >= 5:
                st.session_state.current_question = 0
                st.session_state.current_player += 1

            if st.session_state.current_player >= 2:
                st.session_state.current_step = 2

# Fase 3: Risultati finali
elif st.session_state.current_step == 2:
    st.title("🏆 Risultati Finali")
    st.write(f"{st.session_state.players[0]}: {st.session_state.scores[0]} punti")
    st.write(f"{st.session_state.players[1]}: {st.session_state.scores[1]} punti")

    if st.session_state.scores[0] > st.session_state.scores[1]:
        winner = st.session_state.players[0]
    elif st.session_state.scores[1] > st.session_state.scores[0]:
        winner = st.session_state.players[1]
    else:
        winner = "Pareggio!"

    st.subheader(f"🎉 Vincitore: {winner}")
    st.success("GRANDE BROOO")
    st.balloons()

    if st.button("Ricomincia Gioco"):
        for key in st.session_state.keys():
            del st.session_state[key]





