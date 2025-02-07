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


import streamlit as st
import random

# Lista di domande e risposte
questions = [
    {"question": "Qual è la capitale della Francia?", "options": ["Roma", "Londra", "Parigi", "Berlino"], "answer": "Parigi"},
    {"question": "Qual è il simbolo chimico dell'acqua?", "options": ["O2", "H2O", "CO2", "N2"], "answer": "H2O"},
    {"question": "Chi ha scritto 'Il Principe'?", "options": ["Machiavelli", "Dante", "Shakespeare", "Goethe"], "answer": "Machiavelli"},
    {"question": "Qual è la montagna più alta del mondo?", "options": ["K2", "Everest", "Kangchenjunga", "Lhotse"], "answer": "Everest"},
    {"question": "In quale anno è stato lanciato il primo uomo sulla luna?", "options": ["1965", "1969", "1971", "1975"], "answer": "1969"},
    {"question": "Qual è il pianeta più vicino al Sole?", "options": ["Venere", "Marte", "Mercurio", "Terra"], "answer": "Mercurio"},
    {"question": "Quante ossa ha il corpo umano adulto?", "options": ["206", "207", "208", "209"], "answer": "206"},
    {"question": "Chi è il fondatore di Microsoft?", "options": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Larry Page"], "answer": "Bill Gates"},
    {"question": "Che tipo di animale è il delfino?", "options": ["Pesce", "Mammifero", "Rettili", "Uccello"], "answer": "Mammifero"},
    {"question": "Qual è la lingua ufficiale del Brasile?", "options": ["Portoghese", "Spagnolo", "Inglese", "Francese"], "answer": "Portoghese"},
]

# Funzione per selezionare domande random
def get_random_questions():
    return random.sample(questions, 5)

# Inizializzazione dello stato del gioco
if 'players' not in st.session_state:
    st.session_state.players = {}  # Dizionario per i punteggi dei giocatori
    st.session_state.current_player_index = 0  # Indice del giocatore corrente
    st.session_state.current_question = 0  # Indice della domanda corrente
    st.session_state.game_state = 0  # Stato iniziale della macchina a stati (0 = attesa)
    st.session_state.questions = {}  # Domande random per ogni giocatore
    st.session_state.num_players = 0  # Numero di giocatori
    st.session_state.game_over = False  # Flag per segnare la fine del gioco

# Funzione per avanzare al prossimo stato
def next_state():
    if st.session_state.game_state == 1:  # Se siamo nello stato 1 (in attesa di risposta)
        st.session_state.game_state = 2  # Passa allo stato 2 (aggiorna il punteggio e mostra la prossima domanda)
    elif st.session_state.game_state == 2:  # Se siamo nello stato 2 (prossima domanda)
        st.session_state.current_question += 1
        if st.session_state.current_question >= 5:  # Se tutte le domande sono state fatte
            st.session_state.game_state = 3  # Passa allo stato 3 (fine del gioco)
        else:
            st.session_state.game_state = 1  # Torna allo stato 1 per la risposta della prossima domanda

# Funzione per il controllo della risposta e aggiornamento punteggio
def check_answer(answer, correct_answer):
    if answer == correct_answer:
        st.session_state.players[st.session_state.current_player] += 1
        st.write("Risposta corretta!")
    else:
        st.write("Risposta sbagliata!")

# Funzione per determinare il vincitore
def get_winner():
    winner = max(st.session_state.players, key=st.session_state.players.get)
    return winner, st.session_state.players[winner]

# Interfaccia del gioco
st.title('Quiz Game')

# Aggiungi il numero di giocatori
if st.session_state.game_state == 0:  # Se siamo nello stato di attesa
    num_players = st.number_input("Inserisci il numero di giocatori", min_value=1, max_value=10, value=1)
    if st.button("Inizia gioco"):
        st.session_state.num_players = num_players
        # Crea il dizionario di punteggio per ogni giocatore
        for i in range(num_players):
            player_name = f"Giocatore {i + 1}"
            st.session_state.players[player_name] = 0  # Imposta il punteggio iniziale a 0
            st.session_state.questions[player_name] = get_random_questions()  # Assegna le domande random
        st.session_state.game_state = 1  # Passa al primo stato di gioco

# Se il gioco è in corso
if st.session_state.game_state == 1:
    # Ottieni il nome del giocatore corrente
    current_player = list(st.session_state.players.keys())[st.session_state.current_player_index]
    st.session_state.current_player = current_player

    # Mostra il nome del giocatore e la domanda
    st.write(f"È il turno di: {current_player}")
    question = st.session_state.questions[current_player][st.session_state.current_question]
    st.write(question["question"])
    answer = st.radio("Scegli una risposta:", question["options"])

    if st.button("Invia risposta"):
        check_answer(answer, question["answer"])
        next_state()

# Se il gioco è in fase di avanzamento alla prossima domanda
if st.session_state.game_state == 2:
    # Visualizza il punteggio del giocatore corrente
    st.write(f"Punteggio di {st.session_state.current_player}: {st.session_state.players[st.session_state.current_player]}")
    if st.button("Prossima domanda"):
        # Passa al prossimo giocatore
        st.session_state.current_player_index = (st.session_state.current_player_index + 1) % st.session_state.num_players
        next_state()

# Se il gioco è finito
if st.session_state.game_state == 3:
    winner, score = get_winner()
    st.write(f"Il gioco è finito! Il vincitore è {winner} con {score} punti!")
    st.session_state.game_over = True  # Setta il flag del gioco finito

# Messaggio di fine gioco
if st.session_state.game_over:
    st.write("Ricarica la pagina per una nuova partita!")

