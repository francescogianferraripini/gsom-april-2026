# Scaletta lezione MBA Politecnico di Milano
## LLM e agenti: dai mattoncini semplici ai sistemi agentici

---

# 0. Inquadramento della lezione

## Audience
- Studenti MBA Politecnico di Milano
- Background eterogeneo: non si può dare per scontata alcuna conoscenza pregressa (né AI/ML, né tecnica)
- Target di ruolo futuro: manager, founder, decisori, non implementatori

## Obiettivo didattico
Formare "informed users" capaci di:
- distinguere hype da sostanza nel panorama AI agentico
- porre le domande giuste a fornitori, team tecnici, articoli di stampa
- riconoscere i pattern architetturali dietro qualunque prodotto AI che incontreranno
- prendere decisioni di adozione basate su criteri operativi, non su marketing

**Non obiettivo**: formare implementatori. Nessuna slide insegna a scrivere codice o configurare sistemi.

## Razionali di progettazione

### Razionale narrativo
La lezione è costruita come una **gerarchia di loop**:
- Loop atomico (token-per-token)
- Loop conversazionale (turno-per-turno)
- Loop agentico con tool
- Loop agentico con codice

Ogni sezione aggiunge un livello al loop precedente. Il messaggio ricorrente: *"tutto ciò che vedrete è un loop dentro un altro loop dentro un altro loop"*. Questo dà agli studenti una chiave di lettura unica per qualunque architettura agentica futura.

### Razionale del frame iniziale
Apertura provocatoria: *"Sembra complicatissimo, ma è combinazione di concetti semplici"*. Il resto della lezione mantiene questa promessa costruendo per strati. La chiusura richiama esplicitamente l'apertura, chiudendo l'arco narrativo.

### Razionale "informed user"
Ogni concetto tecnico è sempre seguito da:
- "cosa significa per te come decisore"
- "quale domanda fare al fornitore per smascherare il marketing"

Nessun concetto è presentato in modo puramente descrittivo.

### Razionale della densità delle slide
- Format: frontale denso + demo live finale (no Q&A strutturato)
- 105 minuti di concetti + 15 minuti di vetrina Claude (demo, no slide)
- ~58 slide concettuali → ~1'45'' a slide: denso ma sostenibile per un MBA

### Razionale delle posizioni forti
La lezione prende posizione esplicita su 5 tesi (elencate in chiusura):
1. Il contesto è una risorsa scarsa
2. Tutto il lavoro serio sugli agenti è lavoro sul contesto
3. Prompt senza eval è artigianato
4. La verificabilità predice l'automazione
5. L'AI è uno specchio del caos informativo aziendale

Le tesi sono seminate durante la lezione e raccolte in chiusura.

### Razionale del taglio "founder di Quantyca"
Lo speaker porta in aula credibilità di campo (non accademica). Il deck sfrutta questo in alcuni momenti specifici:
- Slide 16 (dataset delle traiettorie come moat)
- Slide 21 (closed vs open)
- Slide 38 (caos informativo — tesi Quantyca esplicita)
- Slide 52 (modellazione conoscenza come precondizione)
- Slide 56 (harness landscape — data point dal campo)

### Razionale "vetrina senza slide"
Gli ultimi 15 minuti sono live demo sull'harness Claude. Nessuna slide di preparazione: gli studenti passano direttamente dalla Slide 57 (ponte) alla demo. Motivazione: una demo vera vale più di qualunque slide di preparazione.

## Struttura complessiva
- **Sezione 1** — LLM: cosa sono, come sono addestrati, context, loop atomico (9 slide)
- **Sezione 2** — L'agente conversazionale (10 slide)
- **Sezione 3** — Closed vs open (2 slide)
- **Sezione 4** — L'agente che agisce pt.1: tool calling (10 slide)
- **Sezione 5** — Tipi di tool (6 slide)
- **Slide cerniera** — Organizzazione della conoscenza aziendale (1 slide)
- **Sezione 6** — L'agente che agisce pt.2: codice (6 slide)
- **Sezione 7** — Context engineering (13 slide)
- **Chiusura** — Mappa + tesi (1 slide)

**Totale: 58 slide concettuali + demo live finale**

## Convenzioni del documento
Per ogni slide:
- **Obiettivo della slide**: cosa deve rimanere in testa allo studente
- **Layout proposto**: struttura visiva della slide
- **Contenuto testuale**: testo pronto, da copiare sulla slide
- **Note per lo speaker**: cosa dire a voce oltre al testo slide
- **Visual / schema**: descrizione dettagliata dell'elemento grafico, con prompt per generazione quando applicabile

Le slide marcate **[VIZ]** sono slide extra interamente dedicate a un diagramma o visualizzazione complessa che richiede spazio proprio.

## Terminologia
- Nel deck si usa sempre **"context"** (non "blob"). Il termine "blob" compare una volta sola alla Slide 11 come glossa intuitiva, poi si abbandona.
- Termini tecnici EN sono mantenuti in originale: context, tool, tool call, sub-agent, harness, skill, eval, pruning, compaction, sandbox, knowledge cutoff, prompt injection, RAG, MCP.

---

# Sezione 1 — LLM

Introduce il mattoncino atomico: cos'è un LLM, come nasce, i suoi limiti strutturali, il loop di generazione token-per-token. L'arco della sezione piantona due semi che verranno sfruttati per il resto della lezione: la *compressione per astrazione* (che giustifica capacità e limiti) e il *loop atomico* (primo livello della gerarchia).

---

## Slide 1 — Apertura della lezione

**Obiettivo**: aprire con una promessa forte che orienta tutta la lezione.

**Layout**: slide centrata, frase grande, sotto una mappa sintetica delle 7 tappe.

**Contenuto testuale**:

Titolo (grande, centrato):
> Sembra complicatissimo. In realtà è combinazione di concetti semplici.

Sotto, riga più piccola:
> 2 ore per darvi i mattoncini.

Griglia delle 7 tappe (in fondo, 2 righe × 4 colonne):
- LLM
- Agente conversazionale
- Closed vs open
- Tool calling
- Tipi di tool
- Codice
- Context engineering

**Note per lo speaker**:
- La promessa è vincolante: se la lezione cade in dettagli tecnici inutili, la promessa viene tradita. Tornare spesso a "questi sono i mattoncini".
- Si può aprire con una battuta: *"fuori dall'aula leggerete titoli allarmistici. Qui dentro non esiste allarmismo né entusiasmo — esistono solo meccaniche."*

**Visual**: nessun diagramma, solo tipografia e griglia.

---

## Slide 2 — Cos'è un LLM (livello 1: meccanica)

**Obiettivo**: smontare subito l'equivalenza "LLM = chatbot". Un LLM è una funzione matematica, nient'altro.

**Layout**: due colonne. Sinistra: definizione minimale. Destra: schema visivo input→output.

**Contenuto testuale**:

Titolo: **Cos'è un LLM: la meccanica**

Colonna sinistra (testo):
- Funzione matematica
- Input: una sequenza di token (pezzi di testo)
- Output: una distribuzione di probabilità sul prossimo token
- Niente di più, niente di meno

Colonna destra (schema):
- "La gatta è sul..." → modello → probabilità: *tetto* 45%, *divano* 20%, *tavolo* 15%, ...

**Note per lo speaker**:
- Sottolineare: non conversa, non segue istruzioni, non ha intenzioni. Completa testo.
- ChatGPT = LLM + strati sopra. Quegli strati li vedremo nelle prossime sezioni.

**Visual**:
- Schema semplice a 3 blocchi orizzontali.
- Blocco 1 (sinistra): testo di input ("La gatta è sul…")
- Blocco 2 (centro): box grigio "LLM" con freccia in entrata e uscita
- Blocco 3 (destra): lista di 4-5 token candidati ciascuno con una percentuale

**Prompt per generazione SVG** (per designer/tool):
```
SVG schema 3-block horizontal flow. Light neutral palette.
Block 1 left: text bubble containing "La gatta è sul..."
Block 2 center: rounded rectangle labeled "LLM", monospace inside
Block 3 right: vertical bar chart of 5 tokens with probabilities:
  "tetto" 45%, "divano" 20%, "tavolo" 15%, "letto" 10%, "libro" 10%
Arrows from block 1 to block 2 and from block 2 to block 3.
Flat design, no shadows, no gradients.
```

---

## Slide 3 — Cos'è un LLM (livello 2: l'origine)

**Obiettivo**: spiegare da dove viene questa funzione — pre-training su corpus massivi — e lasciare un buco aperto: il modello "base" non conversa.

**Layout**: singola colonna, focus su ordine di grandezza + un bullet finale che crea tensione narrativa.

**Contenuto testuale**:

Titolo: **Come nasce un LLM: pre-training**

Bullet:
- Addestrato su enormi quantità di testo: web, libri, codice, articoli
- Ordine di grandezza: trilioni di token (equivalente di milioni di vite di lettura umana)
- Obiettivo di training: predire il prossimo token, su miliardi di esempi
- Il risultato è un modello "base" che sa completare testo

Box in evidenza (a fine slide):
> **Il modello base non conversa, non segue istruzioni. Completa testo.**
> Come si arriva da qui a ChatGPT? Lo vedremo in Sezione 2.

**Note per lo speaker**:
- Questo buco è voluto. Si chiude con la Slide 13.
- Se qualcuno chiede *"ma GPT non è un LLM base?"*, rispondere: "GPT-3 nel 2020 era il modello base. ChatGPT a novembre 2022 è GPT-3 con sopra un secondo giro di addestramento che vedremo."

**Visual**: nessun diagramma. Eventualmente un piccolo grafico a barre di confronto scale (biblioteca umana vs training corpus) se si vuole enfasi visiva.

---

## Slide 4 — Cos'è un LLM (livello 3a: la potenza)

**Obiettivo**: piantare il frame "sanno tutto della conoscenza pubblica". Calibra le aspettative verso l'alto, non verso il basso.

**Layout**: titolo forte, elenco di domini, un bullet di take-home.

**Contenuto testuale**:

Titolo: **Sanno tutto della conoscenza di dominio pubblico**

Su qualunque argomento pubblico, un LLM moderno ha visto migliaia di trattazioni:
- Medicina, diritto, ingegneria, finanza, marketing
- Storia, filosofia, scienze, letteratura
- Codice di tutti i linguaggi principali, documentazione di framework
- Manuali di prodotto, paper accademici, forum tecnici

**Conseguenza operativa**:
- La baseline informativa di qualunque loro risposta è più alta di quella di un laureato medio nella materia
- Non sono pappagalli che "ripetono": hanno integrato informazioni da fonti molteplici

**Note per lo speaker**:
- Questa slide è in tensione con la prossima (limiti). La tensione va lasciata esplicita: *"sanno tanto. Ma vediamo come lo sanno — perché il come cambia tutto."*

**Visual**: nessun diagramma necessario. Possibile "nuvola di domini" con 10-15 etichette di campi del sapere, sfondo neutro.

---

## Slide 5 — Cos'è un LLM (livello 3b: il meccanismo) — PICCO CONCETTUALE

**Obiettivo**: il punto di svolta della Sezione 1. Spiegare che la compressione avviene per astrazione, non per memorizzazione. Le capacità emergenti sono sottoprodotto necessario della compressione.

**Layout**: slide centrale con metafora JPEG, contrappunto forte, insight emergente.

**Contenuto testuale**:

Titolo: **Compressione lossy per astrazione**

Metafora (Ted Chiang, 2023):
> *"ChatGPT is a blurry JPEG of the web"*

Meccanismo:
- Trilioni di token → centinaia di miliardi di parametri
- Il rapporto di compressione è enorme — non c'è spazio per memorizzare letteralmente
- Il modello è **costretto** a costruire rappresentazioni astratte: concetti, relazioni, regolarità
- Per comprimere bene, deve "capire" cosa sta comprimendo

Box contrappunto (enfasi):
> **Non è un JPEG stupido.**
> È un JPEG che ha dovuto capire cosa comprime.
> Ragionamento, analogia, transfer tra domini: sottoprodotti necessari della compressione.

**Note per lo speaker**:
- Questo è uno dei due o tre punti che devono rimanere a lungo termine. Spendere tempo qui.
- Esempio efficace: "un LLM che vede 10.000 volte frasi come 'il gatto dorme', '2+2=4', 'il ghiaccio è freddo', è costretto a estrarre i concetti di animale, aritmetica, temperatura — altrimenti non comprime bene".

**Visual**: illustrativo. Metafora della compressione.

**Prompt per generazione SVG/illustrazione**:
```
Illustrative diagram, abstract concept.
Left side: a dense, richly detailed image (represents "the web" — many small
icons: books, documents, code snippets, images, articles).
Center: a compression funnel that forces the content through a narrow passage.
Right side: same scene but reconstructed from fewer, more "conceptual" shapes
— showing that the reconstruction captures the structure but not the literal
pixels. Annotations: left "trilioni di token", center "miliardi di parametri",
right "rappresentazioni astratte del mondo".
Flat design. Two color ramps: gray for structure, warm (coral/amber) for the
compression process.
```

---

## Slide 6 — Cos'è un LLM (livello 3c: le conseguenze in prospettiva)

**Obiettivo**: ridimensionare le allucinazioni. Non drammatizzare. Dare una regola pratica da informed user.

**Layout**: due colonne — "dove funziona bene" / "dove serve cautela" — e una regola pratica in fondo.

**Contenuto testuale**:

Titolo: **Le conseguenze, in prospettiva**

Due colonne:

**Dove funziona bene**
- Frame concettuali e sintesi
- Ragionamento qualitativo e analisi
- Trasformazioni di testo
- Spiegazioni, pattern, analogie
- Il 95% dei casi d'uso reali

**Dove serve cautela**
- Fatti puntuali: numeri, date, statistiche
- Citazioni letterali
- Riferimenti specifici (paper, autori, titoli)
- Eventi recenti
- Dettagli di nicchia poco rappresentati nel training

Box regola pratica (in evidenza):
> **Fidati del frame, verifica i fatti.**
> Usa un LLM come un consulente senior che ha letto tutto ma potrebbe ricordare male un numero.

**Note per lo speaker**:
- Esempio concreto: *"'Cosa pensi della mia strategia go-to-market?' — ottima domanda. 'Quanto ha fatturato Ferrari nel Q3 2023?' — pessima domanda senza verifica."*
- Le allucinazioni non sono un bug morale del modello: sono un comportamento strutturale. Come leggere lettere sbiadite — a volte riempi gli spazi.

**Visual**: due colonne a specchio. Palette cool (blue) per "funziona bene", warm (amber) per "cautela".

---

## Slide 7 — Il limite della context size

**Obiettivo**: piantare il concetto che *il contesto è una risorsa scarsa*. Peso narrativo sul vincolo economico/qualitativo, non solo tecnico.

**Layout**: metafora breve in cima + 3 ragioni sotto + domanda operativa in fondo.

**Contenuto testuale**:

Titolo: **Il context è una risorsa scarsa**

Metafora (breve, 1 riga):
> Il context è come la RAM di un computer: tutto ciò che vuoi che il modello "consideri adesso" deve starci dentro.

Ma non tutta la RAM è uguale. Tre ragioni:

**1. Costo quadratico**
- L'attention meccanism ha costo O(n²) sulla lunghezza
- Raddoppiare il context non raddoppia il costo: lo quadruplica

**2. Latenza crescente**
- Più context → più lento
- Non in modo trascurabile: secondi, a volte decine

**3. Degrado qualitativo**
- Anche quando "ci sta", il modello non usa bene tutto
- Tende a ricordare meglio inizio e fine (*lost in the middle*)
- Si distrae, perde focus

Box in fondo (domanda da informed user):
> *"1M di token di context!" — ok, ma quanto costa per chiamata? E la qualità regge davvero a 800k, o degrada?*

**Note per lo speaker**:
- Questa slide è il primo seme del *context rot* (Slide 18).
- Nota tecnica: "O(n²)" va menzionato a voce solo se l'audience è a suo agio; altrimenti dire "cresce molto più che proporzionalmente".

**Visual**: opzionale. Se usato, un mini-grafico a 3 curve sovrapposte (costo, latenza, qualità) al crescere del context. Ma molto schematico, non numerico.

---

## Slide 8 — Il loop di generazione (meccanica)

**Obiettivo**: mostrare visivamente il loop atomico. Nessuna pianificazione, solo token-per-token.

**Layout**: diagramma centrale grande, minimo testo.

**Contenuto testuale**:

Titolo: **Il loop atomico: token per token**

Sotto il diagramma, testo breve:
- Non c'è pianificazione
- Non c'è "prima penso, poi scrivo"
- Solo un token alla volta che riconfigura l'intero context

**Visual**: diagramma di loop.

**Prompt per generazione SVG**:
```
SVG cyclic flow diagram, 4 nodes in a loop, left-to-right then back.
Node 1: "Context" (rounded rect, light gray)
Node 2: "LLM" (rounded rect, purple)
Node 3: "Distribuzione di probabilità" (rounded rect, amber)
Node 4: "Sampling → nuovo token" (rounded rect, teal)
Node 4 loops back to Node 1 with an arrow annotated "token appeso al context".
Below: small text "Fino a un token di stop".
Flat design, one clean stroke, no gradients.
```

**Note per lo speaker**:
- Insistere: il modello **non sa dove andrà a parare**. Ogni token è una decisione singola.
- Paragone utile: come scrivere un testo una parola alla volta, senza poter tornare indietro.

---

## Slide 9 — Il loop di generazione (implicazioni + mappa)

**Obiettivo**: chiudere la Sezione 1 con due osservazioni operative + il seme della gerarchia di loop.

**Layout**: 3 blocchi testo + frase finale grande.

**Contenuto testuale**:

Titolo: **Implicazioni operative**

**1. Streaming non è UX, è meccanica**
- Le parole che compaiono una alla volta su ChatGPT non sono un effetto grafico
- Il modello sta davvero generando token-per-token, in tempo reale

**2. Stesso prompt ≠ stessa risposta**
- Il sampling è probabilistico (c'è un parametro "temperatura")
- Due chiamate identiche producono output diversi — è strutturale, non un bug

**Frase finale (grande, enfasi)**:
> Questo è il loop atomico.
> Tutto il resto della lezione è solo mettere loop più grandi intorno a questo.

**Note per lo speaker**:
- Questa frase è l'anticipazione della gerarchia di loop che userai fino alla chiusura. Ripeterla.
- Transizione: *"ora mettiamo il primo loop sopra: quello conversazionale."*

**Visual**: testo tipografico. Nessun diagramma.

---

# Sezione 2 — L'agente conversazionale

Introduce il secondo loop della gerarchia: turno-per-turno. Spiega come si è passati da "modello che completa testo" a "modello che conversa". Pianta i concetti cardine di stateless, context che cresce, context rot — che saranno riutilizzati per il resto della lezione.

---

## Slide 10 — Apertura: novembre 2022

**Obiettivo**: gancio storico. Piantare la domanda: "cosa è cambiato davvero quel giorno?"

**Layout**: titolo-data grande + 3 bullet.

**Contenuto testuale**:

Titolo: **Novembre 2022 — cosa è cambiato davvero?**

Bullet:
- Non è stato inventato un nuovo modello: GPT-3 esisteva dal 2020
- È stato inventato **un nuovo modo di addestrare il modello a conversare**
- Interfaccia + post-training: la rivoluzione è qui, non nella capacità grezza

Box finale:
> La domanda che ci accompagnerà per la sezione:
> come si passa da "completatore di testo" a "assistente che risponde"?

**Note per lo speaker**:
- Questa è una correzione di senso comune: molti pensano che ChatGPT = modello più potente. In realtà ChatGPT = stesso modello di base + RLHF + UI.
- È anche un'anticipazione del business: il valore non è solo nei pesi, è in come vengono rifiniti.

**Visual**: nessun diagramma. Eventualmente screenshot-icona dell'interfaccia ChatGPT di lancio.

---

## Slide 11 — Meccanica della conversazione [VIZ]

**Obiettivo**: mostrare visivamente che la conversazione è un'illusione dell'interfaccia. Piantare stateless.

**Layout**: slide a due viste affiancate, tutta visuale.

**Contenuto testuale**:

Titolo: **La conversazione è un'illusione dell'interfaccia**

Nessun bullet. Il diagramma parla.

Una nota piccola in fondo:
> Il context è un blob di testo strutturato che cresce. Ogni turno, tutto viene rispedito al modello.
> **L'API è stateless: il modello non ricorda, riceve tutto ogni volta.**

**Visual**: diagramma a due colonne.

**Prompt per generazione SVG**:
```
SVG split diagram, two vertical columns.
LEFT COLUMN — "Cosa vede l'utente":
Chat bubbles alternating user/assistant, 4-5 turns.
Examples: "Ciao chi sei?" (user blue) / "Sono un assistente AI..." (assistant
purple) / "Spiegami i transformer" (user) / "I transformer sono..." (assistant)
/ "E l'attention?" (user, cursor blinking).

RIGHT COLUMN — "Cosa riceve l'API ad ogni turno":
A single long structured text blob with role tags:
[system] Sei un assistente utile...
[user] Ciao chi sei?
[assistant] Sono un assistente AI...
[user] Spiegami i transformer
[assistant] I transformer sono...
[user] E l'attention?
[assistant] ▌

Highlight the entire blob with a dashed amber rectangle, annotated
"Rispedito integralmente ad ogni turno".

Arrow from left column to right column labeled "inviato".
Flat design, no shadows.
```

**Note per lo speaker**:
- Qui introduci "blob" come glossa intuitiva una volta sola. Da qui in avanti, solo "context".
- Martellare: la conversazione non esiste per il modello. Per lui c'è solo testo che cresce.
- Questo è il fondamento di tutto ciò che verrà: se il context è tutto, gestirlo bene è tutto.

---

## Slide 12 — Il system prompt

**Obiettivo**: spiegare il meccanismo più frainteso dai non-tecnici. Aprire la dimensione strategica: l'identità di un prodotto AI vive qui.

**Layout**: tre blocchi (cos'è / come si comporta / perché conta).

**Contenuto testuale**:

Titolo: **Il system prompt**

**Cos'è**
- Turno zero invisibile all'utente
- Messo in cima al context da chi costruisce l'applicazione
- Definisce ruolo, tono, vincoli, capacità dell'assistente

**Come si comporta**
- Il modello **tende** a seguirlo
- Non è un comando hard: può essere aggirato (prompt injection)
- Può essere "eroso" in conversazioni lunghe
- Istruzioni user successive molto forti possono pesare di più

**Perché conta strategicamente**
- ChatGPT, Claude, Gemini hanno "personalità" diverse anche perché hanno system prompt diversi
- L'identità di un prodotto AI vive qui
- Per chi costruisce: il differenziale iniziale del vostro prodotto AI sta nel system prompt — poi si alza con tool e skill

**Note per lo speaker**:
- Qui puoi condividere esperienza: un system prompt ben scritto è un artefatto che un'azienda cura come cura un brand book.
- Esempio: il system prompt pubblico di Claude è lungo migliaia di parole.

**Visual**: nessun diagramma. Layout a 3 colonne testo.

---

## Slide 13 — Il problema del modello base

**Obiettivo**: chiudere il buco aperto alla Slide 3. Un modello base non sa cosa vuoi — serve un secondo giro di addestramento.

**Layout**: esempio concreto in cima + bullet di conseguenze.

**Contenuto testuale**:

Titolo: **Il modello base non sa cosa vuoi**

Esempio:

Prompt dato a un modello solo pre-trained:
> *"Come faccio a perdere peso?"*

Possibili completamenti plausibili (perché vengono tutti dal web):
- Una ricetta dietetica
- Un articolo di Vogue su influencer
- Una lista di link sponsorizzati
- Un rifiuto ("non sono un medico")
- Un'altra domanda ("in quanto tempo?")
- Uno scherzo

**Il modello non sa quale sia quello "giusto" — statisticamente sono tutti plausibili.**

Conseguenza: serve un **secondo giro di addestramento** per insegnargli a comportarsi come un assistente. Lo vediamo nella prossima slide.

**Note per lo speaker**:
- Il punto non è "il modello è stupido". È "il modello fa quello per cui è stato addestrato — completare testo plausibile". Il cambio di compito richiede un cambio di training.

**Visual**: nessun diagramma. Eventualmente un layout "prompt" in mono + lista di completamenti plausibili sotto.

---

## Slide 14 — RLHF e conseguenze strategiche

**Obiettivo**: spiegare RLHF a livello concettuale + 3 insight portabili per un MBA.

**Layout**: 2 sezioni — meccanica (breve) + insight (prevalente).

**Contenuto testuale**:

Titolo: **Dal completamento all'assistenza: RLHF**

**La meccanica (in breve)**
- RLHF = Reinforcement Learning from Human Feedback
- Umani (o altri AI) giudicano le risposte del modello
- Il modello viene ri-addestrato per massimizzare il giudizio
- Non "cosa è probabile" ma "cosa è desiderabile"

**3 insight da portare via**

**1. La personalità è scolpita, non emergente**
- Claude, GPT, Gemini hanno caratteri diversi per **scelta** di addestramento
- Anthropic ha costruito un approccio proprio ("Constitutional AI") dove le regole di comportamento sono esplicite
- È un elemento di differenziazione di prodotto

**2. I limiti sono spesso scelte, non capacità**
- Quando un modello rifiuta, nella maggior parte dei casi "è stato addestrato a rifiutare", non "non può"
- Il confine tra capability e policy è sottile e cambia per ogni provider

**3. Chi fornisce il feedback plasma l'AI**
- Cambi i valutatori → cambi il modello
- Implicazioni etiche, geopolitiche, di business enormi
- Poco discusse fuori dall'industria

Box finale:
> **Il modello che usate non è "l'AI". È una particolare AI addestrata con particolari valori da particolari persone.**

**Note per lo speaker**:
- Questo è un punto che spesso spiazza: non esiste "l'AI neutrale". Ogni modello riflette le scelte del team che l'ha post-trained.
- Rilevanza geopolitica: un modello cinese ha policy diverse da uno americano. Un modello europeo (se esistesse) avrebbe policy diverse ancora.

**Visual**: nessun diagramma. Layout testuale a blocchi.

---

## Slide 15 — Tipi di task (mappa leggera)

**Obiettivo**: piantare una tassonomia che verrà richiamata nelle sezioni successive.

**Layout**: tabella compatta 6×2 (tipo + forza/cautela).

**Contenuto testuale**:

Titolo: **Che task stai dando al modello?**

Tabella:

| Tipo di task | Dove l'LLM brilla | Dove serve cautela |
|---|---|---|
| **Trasformazione** (traduci, riassumi, riformatta) | Qualità alta e affidabile | — |
| **Generazione** (scrivi email, brief, storia) | Frame eccellente | Fatti puntuali |
| **Q&A / recupero conoscenza** | Sintesi concettuale | Fatti precisi (allucinazioni) |
| **Ragionamento** (matematica, logica, planning) | Migliora rapidamente | Catene lunghe, verifiche numeriche |
| **Classificazione / giudizio** (sentiment, routing) | Affidabile | Bias potenziali |
| **Conversazione stateful** | Sintesi delle sopra | Context rot |

Box finale:
> **Primo skill da informed user: classificare il task prima di delegarlo.**
> Non esiste "l'LLM fa X". Esiste "questo task è più o meno adatto a un LLM".

**Note per lo speaker**:
- Questa mappa verrà richiamata: il RAG serve a rinforzare il Q&A, i tool a rinforzare il ragionamento con fatti, il codice a rinforzare il ragionamento deterministico.
- Non approfondire qui ogni riga — presentarla velocemente, è una mappa di riferimento.

**Visual**: tabella. Nessun diagramma aggiuntivo.

---

## Slide 16 — Dataset delle traiettorie (posizione forte da founder)

**Obiettivo**: far capire l'asimmetria del valore delle conversazioni. Piantare il concetto di moat che verrà richiamato alle Slide 21 e 38.

**Layout**: due colonne a specchio + 3 domande in fondo.

**Contenuto testuale**:

Titolo: **Chi vince davvero: tu o il provider?**

Ogni volta che usi un LLM, produci una **traiettoria di conversazione**: sequenza reale, su problema reale, con correzioni, re-prompt, soddisfazione/insoddisfazione.

Due colonne:

**Per te (utente/azienda)**
- Valore: hai risolto un problema oggi
- Domani la conversazione è dimenticata (stateless)
- Valore medio, localizzato, non cumulativo

**Per il provider**
- Valore: carburante del prossimo training
- Scopre: dove sbaglia, cosa vogliono davvero gli utenti, quali pattern emergono
- Valore enorme, cumulativo, compounding

Box (posizione forte):
> **Il vero moat dei big player non sono i modelli (si replicano) né i dati pubblici (sono condivisi). Sono le traiettorie reali di milioni di utenti.**

**3 domande da informed user**

1. **Nel vostro contratto, i dati entrano nel training del provider?**
   - Piani consumer: spesso sì, con opt-out sepolti
   - Piani enterprise: tipicamente no (ma leggere il contratto)

2. **Se costruite un prodotto AI, dove si accumula il vostro flywheel?**
   - Non batterete OpenAI sul general-purpose
   - Vertical-specific: Harvey (legale), Hippocratic (medicina) hanno senso perché accumulano traiettorie in un dominio

3. **Oggi pagate il modello. Domani il valore sarà nei dati d'uso proprietari.**
   - Il modello diventa commodity
   - I dati di come il vostro team usa l'AI sono un asset nuovo da costruire

**Note per lo speaker**:
- Qui prendi posizione. Non paternalistica, ma chiara.
- Esperienza da Quantyca: "quando un cliente mi chiede 'quale modello comprare', rispondo 'prima decidiamo dove volete che si accumuli il vostro valore'".

**Visual**: due colonne a specchio. Palette contrastante — blu (te) vs amber (provider).

---

## Slide 17 — Stateless e crescita del context

**Obiettivo**: esplicitare meccanicamente perché il context cresce e ha un costo non lineare.

**Layout**: 2 colonne — meccanica (sinistra) + conseguenze (destra).

**Contenuto testuale**:

Titolo: **Il context cresce — e non gratis**

**La meccanica**
- L'API è stateless
- Ogni turno, tutto il context viene rispedito integralmente al modello
- System prompt + tool definition + cronologia completa + nuovo messaggio
- Niente viene "ricordato lato server": è sempre reinviato

**Le conseguenze**
- Costo O(n²) — vedi Slide 7
- Latenza crescente
- *Lost in the middle*: il modello usa peggio la parte centrale di context lunghi
- Dispersione dell'attenzione, minor aderenza al system prompt
- **Qualità che degrada, non solo costo che sale**

Box finale:
> Le conversazioni non sono gratuite.
> Ogni turno costa più del precedente.
> E mantenere la qualità diventa più difficile, non più facile.

**Note per lo speaker**:
- Controintuitivo: molti pensano "più parlo con l'AI, più mi conosce, meglio risponde". È vero in senso sociale, ma meccanicamente è l'opposto.
- Transizione alla prossima: "diamo un nome a questo fenomeno: context rot."

**Visual**: nessun diagramma. 2 colonne testuali.

---

## Slide 18 — Context rot (con mini-grafico) [VIZ]

**Obiettivo**: dare un nome al fenomeno + mostrarlo visivamente + regole pratiche.

**Layout**: grafico centrale grande + 3 take-home sotto.

**Contenuto testuale**:

Titolo: **Context rot: quando la conversazione peggiora**

(Sopra il grafico, 1 riga:)
> 3 curve, stesso asse x = lunghezza del context.

**3 take-home**

1. **Regola pratica**: nuovo compito = nuova chat. Non estendere conversazioni esistenti.
2. **Il context è una risorsa scarsa**, non un cassetto infinito.
3. **Tutto ciò che vedremo dopo** (sub-agent, context engineering, compaction, skill, memoria) **è una risposta a questo.**

**Note per lo speaker**:
- Questo è il *seed narrativo* più importante della Sezione 2. Le prossime 5 sezioni si agganciano qui.
- Frase da ripetere: "tutto ciò che vedete dopo risolve context rot in modi diversi".

**Visual**: grafico a 3 curve sovrapposte.

**Prompt per generazione SVG**:
```
SVG line chart. X-axis: "lunghezza del context (token)", from 0 to 200k.
Y-axis: unitless (normalized), label "relativo a valori iniziali".
Three curves:
1. "Costo" — quadratic growth, starts slow, accelerates (label color: amber)
2. "Latenza" — linear growth (label color: coral)
3. "Qualità effettiva" — rises quickly, plateaus around 30-50k, then
    gently declines past 100k (label color: teal)
Legend on the top-right.
Highlight with a vertical dashed line at "200k" annotated "degrado evidente".
Flat design, no shadows. Clean grid, minimal.
```

---

## Slide 19 — Il loop conversazionale (chiusura Sezione 2) [VIZ]

**Obiettivo**: sintesi visiva del secondo loop. Focus sul context che cresce.

**Layout**: diagramma di loop + frase messaggio.

**Contenuto testuale**:

Titolo: **Il loop conversazionale**

Sotto il diagramma:
> Il loop turno-per-turno. Il context cresce ad ogni giro.
> **Il vero problema da risolvere è il context che cresce.**
> Tutto ciò che viene dopo è una risposta a questo.

**Visual**: loop a 4-5 step con accumulo visuale del context.

**Prompt per generazione SVG**:
```
SVG cyclic flow, 4 nodes arranged in a rectangle, arrows clockwise.
Node 1 (top-left): "User scrive messaggio" (blue)
Node 2 (top-right): "Client costruisce context (system + storico + nuovo)" (gray)
Node 3 (bottom-right): "Modello genera risposta" (purple)
Node 4 (bottom-left): "Client riceve e appende" (gray)
Arrow from 4 back to 1 labeled "ogni giro il context cresce".

CRITICAL VISUAL ELEMENT: along the return arrow (from 4 to 1),
show a progressively thickening accumulation bar — a stacked block
that grows with each visualized turn, colored amber/coral,
showing the context size compound accumulation.

Flat design. No extra text on the slide itself beyond the nodes and arrow.
```

**Note per lo speaker**:
- Fare una pausa dopo questa slide. È un punto di riposo prima di cambiare tema.
- Transizione: "ma prima di vedere come risolvere il context rot, una digressione importante: che modello stiamo usando?"

---

# Sezione 3 — Modelli closed vs open

Due slide. Introduce una scelta di architettura, costo, rischio e vendor lock-in. Richiama esplicitamente la Slide 16 (moat) per mostrare che la scelta closed/open è anche una scelta di a chi si regala dati.

---

## Slide 20 — Mappa tecnica: chi è chi

**Obiettivo**: dare vocabolario e classificazione dei provider.

**Layout**: 3 categorie in griglia con esempi.

**Contenuto testuale**:

Titolo: **Closed, open weight, open source "vero"**

**Closed / API-only**
- Pesi mai rilasciati, si accede solo via API del provider
- Esempi: GPT (OpenAI), Claude (Anthropic), Gemini (Google)

**Open weight**
- Pesi scaricabili, training code e dataset tipicamente no
- Si possono eseguire, modificare, fine-tunare
- Esempi: Llama (Meta), Mistral (francese), DeepSeek/Qwen (cinesi), Gemma (Google)

**Open source "vero"**
- Pesi + training code + dataset
- Rari, tipicamente dietro la frontiera di capacità
- Esempi: OLMo (AllenAI)

Box finale:
> **"Open" è una parola scivolosa.**
> Quasi tutto ciò che viene chiamato open è **open weight**, non veramente open source.
> La distinzione conta se vi servono auditing completo o reproducibility.

**Note per lo speaker**:
- Per un MBA: questa è la slide di vocabolario. Poco emotiva, molto informativa.
- Non attardarsi: serve per la slide successiva, che è quella operativa.

**Visual**: 3 colonne/box. Nessun diagramma.

---

## Slide 21 — Trade-off decisionale (economico + geopolitico + moat)

**Obiettivo**: dare un framework decisionale + prendere posizione forte sul moat + inserire l'update 2025.

**Layout**: tabella comparativa + riquadro centrale forte + riquadro update 2025.

**Contenuto testuale**:

Titolo: **Closed vs open: il trade-off reale**

Tabella comparativa:

| Dimensione | Closed | Open |
|---|---|---|
| Qualità di frontiera | In testa oggi | A 6-12 mesi, ma il gap si chiude |
| Costo a scala | Pay-per-token, cresce con l'uso | Costo infra fisso, marginale ~zero |
| Privacy / data residency | Dati al provider (salvo enterprise tier) | Totalmente in casa, sovrano |
| Customization | Fine-tuning limitato, no accesso pesi | Fine-tuning totale, quantizzazione |
| Effort | Zero infra, usi subito | Servono GPU, MLOps, competenze |
| Geopolitica / compliance | Dipendenza vendor USA (o Cina) | Sovranità, AI Act-friendly |

**Box centrale (posizione forte, richiama Slide 16)**:
> Quando usate un modello closed, state consolidando il moat del provider.
> Ogni vostra conversazione è dato di training per lui.
> Ogni vostro workflow gli insegna cosa vogliono gli utenti.
> **Open non è solo più economico o più sovrano.**
> **È l'unica opzione dove il vostro uso NON alimenta il competitivo di qualcun altro.**

**Box update 2025** (in fondo):
> **Update 2025 — il gap si chiude più in fretta del previsto**
> Esempio: Gemma 4 (~31B parametri) raggiunge qualità comparabile a Sonnet 4.5 su molti task concreti, ed è eseguibile in inferenza su singola GPU consumer (NVIDIA 4090).
> Un modello open weight di quasi-frontiera, in casa, con costo marginale vicino a zero.
> La scelta "closed perché sono gli unici seri" non regge più come prima.

**Take-home (1 bullet)**:
- Regola pratica: **closed per sperimentare, open per scalare**. E oggi open è anche un'opzione di qualità.

**Note per lo speaker**:
- Verificare il data point Gemma 4 / Sonnet 4.5 alla data della lezione. Se superato, sostituire con il modello open-weight di riferimento al momento.
- Richiamo esplicito alla Slide 16: "ricordate il moat delle traiettorie? Closed consolida quel moat — ma non vostro, del provider."

**Visual**: tabella pulita. Due box evidenziati (centrale e in fondo) in colore distinto.

---

# Sezione 4 — L'agente che agisce pt.1: tool calling

Introduce il terzo loop della gerarchia: il loop con tool. È dove il modello smette di essere solo un'interfaccia di linguaggio e diventa un organo decisionale che sceglie azioni.

---

## Slide 22 — Apertura Sezione 4 (provocatoria)

**Obiettivo**: riattivare l'attenzione a metà lezione. Piantare la distinzione "decide vs esegue".

**Layout**: frase a tutto schermo.

**Contenuto testuale**:

(Titolo grande, centrato)
> Fino a qui: un modello che parla.
> Da qui in avanti: un modello che agisce.

(Sottotitolo più piccolo, sotto)
> Non eseguendo codice.
> Scegliendo cosa far eseguire.

**Note per lo speaker**:
- Lunga pausa prima di leggere il sottotitolo. La distinzione "decide vs esegue" è uno dei punti fondamentali della sezione.
- Sei a ~45-50 minuti di lezione: attivatore giusto prima di entrare in materia densa.

**Visual**: testo centrato. Opzionale: due piccoli pittogrammi ai lati (bocca/parola vs mano/azione) molto minimali.

---

## Slide 23 — L'intuizione: cosa succede da fuori

**Obiettivo**: porre la domanda. Creare tensione narrativa per la slide successiva.

**Layout**: chat mockup + domanda aperta.

**Contenuto testuale**:

Titolo: **Osservate questo scambio**

Chat mockup (2 turni):
- User: *"Che tempo fa a Milano?"*
- Assistant: *"A Milano ora ci sono 19°C e il cielo è nuvoloso, con 65% di umidità."*

Sotto la chat (grande):
> L'LLM non ha questi dati nel training.
> Il suo knowledge cutoff è mesi fa.
> Eppure la risposta è corretta e aggiornata.
>
> **Come?**

**Note per lo speaker**:
- Chiedere a voce all'aula: "secondo voi come?". 10-15 secondi di silenzio. Raccoglie ipotesi.
- Poi transizione alla slide seguente: "vediamo esattamente cosa è successo".

**Visual**: chat bubbles stilizzate. Nessun altro elemento.

---

## Slide 24 — La meccanica: cosa è successo davvero [VIZ]

**Obiettivo**: mostrare il loop con tool nella sua forma completa a 4 attori.

**Layout**: diagramma grande centrale + 3 bullet didattici sotto.

**Contenuto testuale**:

Titolo: **Il tool call: meccanica**

(Diagramma centrale, vedi visual)

Sotto il diagramma, 3 bullet:

1. **Il modello non esegue, decide.** L'esecuzione la fa l'harness. Questo dà controllo totale su cosa l'agente può fare, definendo quali tool esporre.
2. **Ogni tool call aggiunge turni al context.** Tool call + tool result vengono appesi al context e restano.
3. **Il modello sceglie il tool giusto dalla sua descrizione.** Descrizioni ambigue = agente che sbaglia. Scrivere bene le descrizioni dei tool è metà del lavoro.

**Visual**: diagramma a 4 swim-lane.

**Prompt per generazione SVG**:
```
SVG sequence diagram, 4 vertical lanes.
Lanes from left to right: "User", "Harness", "Model", "External API".
Each lane is a vertical timeline.
Arrows labeled with step numbers 1-8:

1. User → Harness: "Che tempo fa a Milano?"
2. Harness → Model: context (system + tool definitions + history + user msg)
3. Model → Harness: tool call `get_weather(city="Milano")` [HIGHLIGHT AMBER]
4. Harness → External API: HTTP call to weather service
5. External API → Harness: `{temp: 19, sky: "cloudy", humidity: 0.65}` [HIGHLIGHT AMBER]
6. Harness → Model: context updated with tool result appended
7. Model → Harness: natural language response
8. Harness → User: "A Milano ci sono 19°C..."

Highlight arrows 3 and 5 in amber color (the two "tool" moments).
All other arrows in neutral gray.
Flat design.
```

**Note per lo speaker**:
- L'insight da portare a casa è il punto 1: il modello **decide** ma non **esegue**. Questa distinzione elimina un sacco di fraintendimenti ("ma se ChatGPT fa un bonifico, chi è responsabile?").
- Il controllo di sicurezza vive nell'harness: se non gli esponi il tool "fai bonifico", non può farlo, anche se decidesse.

---

## Slide 25 — Persistenza: cosa si accumula nel context

**Obiettivo**: mostrare chirurgicamente cosa entra nel context quando attivi i tool.

**Layout**: tabella 4 righe × 4 colonne.

**Contenuto testuale**:

Titolo: **Cosa persiste nel context con i tool**

Tabella:

| Componente | Quando entra | Dimensione tipica | Persistenza |
|---|---|---|---|
| **Tool definition** | Una volta, in cima | 100-300 token × numero tool | Tutta la conversazione |
| **Tool call** (richiesta modello) | Ogni volta che l'agente usa un tool | Piccola (nome + args) | Tutta la conversazione |
| **Tool result** (payload di ritorno) | Ogni volta che un tool esegue | **Variabilissima: decine → decine di migliaia di token** | Tutta la conversazione |
| **Turni naturali user/assistant** | Come prima | Piccola | Tutta la conversazione |

Box in fondo:
> **Il context non contiene solo quello che dite voi e risponde l'agente.**
> Contiene anche tutto quello che i tool hanno tirato fuori dal mondo esterno.
> **Niente viene pulito automaticamente.** L'API è stateless: tutto questo viene rispedito al modello ad ogni turno successivo.

**Note per lo speaker**:
- Scenario concreto da usare a voce: "un tool di query SQL può facilmente tornare 10k righe. Se il modello ha sbagliato query e ne fa un'altra, avete 20k righe nel context. A fine conversazione avete bruciato il budget di context in raw data."

**Visual**: tabella. Nessun diagramma aggiuntivo.

---

## Slide 26 — Il paradosso: context rot accelerato [VIZ]

**Obiettivo**: esplicitare il paradosso — i tool risolvono un problema e ne creano un altro. Seme per le sezioni successive.

**Layout**: due mini-grafici affiancati + paradosso in forma di frase.

**Contenuto testuale**:

Titolo: **Il paradosso: i tool accelerano il context rot**

(Due mini-grafici affiancati, vedi visual)

Sotto i grafici, una sola frase enfatizzata:
> I tool risolvono un problema — l'LLM non sa tutto e non può agire.
> Ma ne creano un altro — accelerano il context rot.
> **Tutto ciò che vedremo dopo** (sub-agent, context engineering, compaction, skill, memoria) **è una risposta a questo nuovo problema.**

**2 take-home operativi**:

1. **Quanti tool servono davvero?** Più tool esposti = più context bruciato prima di parlare. Minimizza, non massimizzare.
2. **I tool result vanno dimensionati.** Un tool che torna 50k token non è un tool, è una bomba. Un buon tool filtra/sintetizza prima di restituire.

**Visual**: due mini-grafici affiancati.

**Prompt per generazione SVG**:
```
SVG two-panel chart, side by side.

LEFT PANEL — "Conversazione pura":
Line chart. X: turno (1-20). Y: token nel context (0-15k).
Single curve, smooth linear growth, reaches ~5k by turn 20.
Title on top: "Conversazione pura".

RIGHT PANEL — "Conversazione con tool":
Line chart. Same axes.
Stepped curve with large jumps at turns where tool calls happen.
Jumps approximate: +5k at turn 2, +8k at turn 4, +12k at turn 6, +10k at turn 9.
By turn 15 reaches ~45k.
Title on top: "Conversazione con tool".

Both charts use teal line color. The right chart has amber vertical
highlights where tool calls cause the jumps.
Flat design, minimal grid, clean axes.
```

**Note per lo speaker**:
- Frase chiave da ripetere: "tutto il resto della lezione risolve questo."
- Transizione: "la prima soluzione architetturale al context rot indotto dai tool: i sub-agent."

---

## Slide 27 — Sub-agent: analogia del manager che delega

**Obiettivo**: introdurre il pattern architetturale con un'analogia forte, intuitivamente.

**Layout**: analogia centrale + traduzione in AI.

**Contenuto testuale**:

Titolo: **Sub-agent: il manager che delega**

**L'analogia**
- Il partner di una consulting firm non legge 5000 pagine di raw data
- Chiede a un associate di leggerle, analizzarle, e tornare con una slide sintetica
- Il partner lavora su un context pulito — quello strategico
- L'associate lavora sul context sporco — quello operativo

**Traduzione in AI**
- L'agente principale ("padre") riceve un task complesso
- Invece di fare tutto nel suo context, **delega** a un agente figlio
- Il figlio ha il suo context pulito, i suoi tool, il suo system prompt
- Il figlio esegue il lavoro sporco (cerca, legge, prova, fallisce, riprova)
- Torna al padre **solo con il risultato sintetico**
- Il context del padre **non viene mai contaminato** dal processo

Box:
> **Il padre non si sporca le mani.**
> **Resta nel suo context strategico.**

**Note per lo speaker**:
- Analogia efficace perché la maggior parte degli MBA ha esperienza con gerarchie o con consulting firm.
- Transizione: "vediamo meccanica, benefici, e chi lo usa davvero oggi."

**Visual**: opzionale. Se inserito, schema a 2 livelli (padre → figlio) con context separati.

---

## Slide 28 — Sub-agent: meccanica, benefici, esempi [VIZ]

**Obiettivo**: meccanica visiva + 4 benefici + 3 esempi reali.

**Layout**: diagramma a sinistra + bullet a destra.

**Contenuto testuale**:

Titolo: **Come funziona (e chi lo usa già oggi)**

(Diagramma a sinistra)

A destra, **4 benefici**:

1. **Isolamento del context**: ogni sub-agent ha la sua finestra. Il context rot viene contenuto.
2. **Parallelizzazione**: più sub-agent possono lavorare in parallelo. Un agente researcher può lanciare 10 ricerche simultanee, sintetizzare, tornare al padre.
3. **Specializzazione**: ogni sub-agent può avere il suo system prompt e i suoi tool. Un "researcher" con web, un "coder" con bash, un "verifier" che rilegge.
4. **Affidabilità**: un errore nel figlio non corrompe il padre. Il padre lo sa, riassegna.

**3 esempi reali**:
- **Claude Code**: sub-agent per esplorare grandi codebase senza inquinare il context principale
- **Deep Research (Claude, Perplexity, ChatGPT)**: sub-agent per ricerche parallele su decine di fonti
- **Devin**: sub-agent specializzati per task di implementazione

**Visual**: diagramma padre-figlio con context separati.

**Prompt per generazione SVG**:
```
SVG hierarchical diagram.
Top: large rounded rect labeled "Agente padre" (purple).
Inside: small text "context strategico, pulito".
Below the padre, 3 smaller rounded rects labeled "Sub-agent 1",
"Sub-agent 2", "Sub-agent 3" (teal).
Each sub-agent has its own context bubble next to it labeled
"context isolato" with a dashed border.
Arrows: padre to each sub-agent (label "spawn + task").
Return arrows: sub-agent to padre (label "sintesi", amber color).

Below the sub-agents, tool icons (small rectangles) representing
different tool sets per sub-agent — visually showing specialization.

Flat design, clean hierarchy.
```

**Note per lo speaker**:
- Gli esempi sono fondamentali: "avete usato Deep Research? Ecco cosa succede dietro."
- Collegamento a Sezione 6: "Claude Code lo approfondiamo nella prossima sezione sul codice".

---

## Slide 29 — Sub-agent: ma non sono gratis

**Obiettivo**: raffreddare l'entusiasmo. 4 effetti collaterali onesti. Take-home equilibrato.

**Layout**: 4 blocchi + take-home finale.

**Contenuto testuale**:

Titolo: **Ma attenzione: i sub-agent non sono gratis**

**1. Perdita di informazione nella sintesi**
- Il figlio sintetizza al padre — la sintesi è per definizione lossy
- Il padre non sa cosa il figlio ha visto e scartato
- Il "tono dei dati grezzi" si perde
- Il padre non può "fare domande follow-up" al lavoro del figlio (il context del figlio è morto)

**2. Debugging e osservabilità esplodono**
- In un sistema monolitico: leggi una cronologia, capisci dove ha sbagliato
- In un multi-agent: tracce ad albero, figli che muoiono senza log completi
- Debugging in produzione diventa un problema industriale serio

**3. Errori composti silenziosi**
- Se il padre dà istruzioni ambigue → figlio fa quello che capisce (non quello che serve)
- Il figlio torna un risultato che sembra corretto
- Il padre ci costruisce sopra altre decisioni
- L'errore **si propaga silenziosamente** — nascosto negli handoff

**4. Nuova superficie di prompt injection**
- Un sub-agent con accesso al web può essere manipolato da una pagina
- Istruzioni maliziose possono contaminare la sintesi che torna al padre
- Il padre si fida di un report manomesso
- Superficie d'attacco nuova e sottovalutata

**Box take-home (onesto)**:
> Sub-agent sono un pattern potente, non una pillola magica.
> - **Vincono** su task esplorativi, parallelizzabili, o con contesti specializzati
> - **Perdono** su task lineari o dove la tracciabilità è critica
> - **Sul costo**: dipende dalla natura del task — non date per scontato né risparmio né spreco, misurate.

**Note per lo speaker**:
- Onestà nota: è un'opinione raffinata. Molti corsi/conferenze vendono multi-agent come soluzione universale. Prendere posizione equilibrata è un valore.
- Richiamo Slide 38 (caos informativo): "il pattern fallisce peggio se sotto c'è caos informativo. Tenetelo in mente per più avanti."

**Visual**: nessun diagramma. 4 blocchi testuali.

---

## Slide 30 — Il loop agentico con tool (chiusura meccanica) [VIZ]

**Obiettivo**: sintesi visiva del terzo loop + take-home operativi sui limiti.

**Layout**: diagramma di loop + due bullet di limiti.

**Contenuto testuale**:

Titolo: **Il loop agentico con tool**

(Diagramma centrale)

Sotto, messaggio chiave:
> Il modello decide quando agire e quando rispondere.
> Questo è il cuore dell'**agentività**.

**In produzione, sempre questi limiti**:
- Max numero di tool call per turno (evita loop infiniti)
- Timeout su ogni esecuzione
- Budget di token complessivo per sessione

Un agente senza questi limiti può entrare in loop infiniti o bruciare soldi a vuoto.

**Visual**: diagramma di loop con biforcazione.

**Prompt per generazione SVG**:
```
SVG flowchart with a decision diamond.
1. Top: "User invia messaggio" (blue rect)
2. Arrow down to: "Modello decide" (purple diamond)
3. Diamond has two branches:
   - Left branch: "Tool call" → leads to "Harness esegue" (gray rect)
     → "Tool result nel context" (amber rect) → arrow back UP to "Modello decide"
   - Right branch: "Risposta" → "User riceve" (blue rect) → END

Show the left loop clearly (the agent can iterate through multiple tool calls
before responding). Add a small annotation on the left branch: "può ripetere
N volte".

Flat design, single clean palette.
```

**Note per lo speaker**:
- L'insight chiave è che il numero di iterazioni non è fisso — lo decide il modello, entro i limiti che imponi.
- I limiti sono pratica operativa, non teoria. Chi li omette scopre il problema con la fattura del provider.

---

## Slide 31 — Eval: la domanda che smaschera i dilettanti

**Obiettivo**: introdurre il concetto di eval + prendere posizione forte.

**Layout**: titolo forte + 3 blocchi + chiusura.

**Contenuto testuale**:

Titolo: **Eval: la domanda che smaschera i dilettanti**

**Cos'è un eval**
- Suite di test per agenti AI
- Concettualmente simile ai test del software, con 3 differenze chiave

**3 peculiarità**

1. **Risultati non binari**: "giusto/sbagliato" raramente basta. Serve valutare qualità, tono, aderenza, sicurezza. Spesso si usa **LLM-as-judge** (un modello che giudica altri modelli).
2. **N run statistici**: stesso input può dare output diversi (sampling probabilistico). Ogni test va fatto girare N volte, si misura una distribuzione.
3. **Dataset curato**: servono casi reali, edge case, prompt injection, ambiguità. Costa lavoro umano di qualità.

**3 perché conta (informed user)**

- **Distingue professionisti da dilettanti**: prompt senza eval = software non testato
- **È il modo per ottimizzare sistematicamente**: ogni modifica al system prompt, ogni tool aggiunto, dovrebbe essere validato contro eval
- **È il vero lavoro nascosto dell'AI engineering**: i progetti seri spendono più tempo a curare eval che a scrivere prompt

**Box posizione forte (chiusura)**:
> **Se state valutando un fornitore AI: la domanda fondamentale non è "che modello usate". È "mostratemi il vostro eval harness".**
> Se non ce l'hanno, o è banale, state comprando una demo.
>
> **Prompt senza eval è artigianato. Prompt con eval è ingegneria.**

**Note per lo speaker**:
- Questo è uno dei momenti più portable della lezione: una domanda concreta da usare nel lavoro.
- Esperienza da Quantyca: "quando vediamo un progetto AI che naviga a vista, la prima cosa che introduciamo non è un modello migliore. È una suite di eval."

**Visual**: nessun diagramma. Testo con box evidenziato in chiusura.

---

# Slide cerniera

## Slide 32 — Organizzazione della conoscenza aziendale (cerniera)

**Obiettivo**: piantare la tesi strategica di Quantyca prima di entrare in Sezione 5/6/7. Stacco narrativo voluto.

**Layout**: titolo forte + frame + sintomi + tesi forte + chiusura operativa.

**Contenuto testuale**:

Titolo: **Un interludio scomodo**

Sottotitolo:
> L'AI non risolve il caos informativo — lo amplifica.

**Il frame**
- Tutto ciò che abbiamo visto (RAG, MCP, Deep Research, agenti, tool — vedremo ancora skill, memoria) presuppone **qualcosa di coerente da interrogare**
- Nella maggior parte delle aziende, questo qualcosa **non esiste ancora**

**5 sintomi del caos informativo che emergono con l'AI**

1. **Stesso concetto, definizioni diverse**: "cliente attivo" secondo marketing ≠ sales ≠ finance. L'agente sintetizza risposte incoerenti.
2. **Dati duplicati con versioni contraddittorie**: l'agente cita la versione sbagliata, nessuno se ne accorge finché non esplode.
3. **Conoscenza tacita in teste umane, non in sistemi**: l'agente non la trova e allucina plausibilmente.
4. **Ownership e policy di accesso confuse**: l'agente pesca da dove non dovrebbe, o non pesca da dove dovrebbe.
5. **Documentazione obsoleta o assente**: l'agente si ancora a info vecchie ed è più convincente del dovuto proprio perché "cita le fonti aziendali".

**Tesi forte**:
> Il valore dell'AI agentica in azienda è **proporzionale** alla qualità della vostra organizzazione della conoscenza.
> Molti progetti AI non falliscono per problemi di AI.
> Falliscono perché hanno scoperto in diretta il caos informativo che nessuno voleva affrontare.
>
> **L'AI è uno specchio: vi mostra con spietatezza come siete organizzati davvero.**

**Chiusura operativa**:
- Prima di investire in agenti sofisticati, investite in:
  - un semantic layer condiviso
  - ownership chiara dei dati
  - una knowledge base viva e mantenuta
- L'agente viene dopo — e senza questi non funziona

(Opzionale — nota speaker da Quantyca):
> È anche il motivo per cui in Quantyca ci occupiamo sia di dato sia di AI. Non sono due business: sono due facce della stessa cosa.

**Note per lo speaker**:
- Questa è una slide che rallenta volutamente il ritmo. Va lasciata respirare.
- La tesi è una delle 5 finali (Slide 58): richiamarla qui e piantarla come "la sentirete di nuovo".
- Se il pubblico annuisce, bene. Se qualcuno pensa "non è il mio problema": perfetto, è il suo problema.

**Visual**: nessun diagramma. Solo testo con box tesi fortemente evidenziato.

---

# Sezione 5 — Tipi di tool

Panoramica degli archetipi di tool che contano nel panorama attuale. Ogni tipo ha pesi uguali per indicazione dello speaker. La sezione costruisce anche il ponte verso Sezione 6 (via bash) e Sezione 7 (via skill/MCP).

---

## Slide 33 — API tools

**Obiettivo**: archetipo base. Qualunque endpoint HTTP = capacità.

**Layout**: titolo + 2 blocchi + bullet sicurezza.

**Contenuto testuale**:

Titolo: **API tools**

**L'archetipo**
- Qualunque endpoint HTTP diventa una capacità dell'agente
- Schema standard: nome + descrizione + parametri + auth
- Il connettore universale tra LLM e sistemi aziendali

**Esempi in ambito aziendale**
- Lookup su CRM, query su DB
- Creazione ticket, invio email transazionale
- Pagamento, aggiornamento inventario
- Interrogazione ERP, API di notifica

**Nodo di sicurezza**:
- Non tutti i tool sono sicuri da esporre
- Tool read-only su CRM ≠ tool che esegue bonifico
- **Principio di minimo privilegio**: si applica agli agenti come agli umani, forse di più

**Box take-home**:
> Ogni sistema aziendale che ha un'API è già potenzialmente un tool.
> La vera domanda non è "possiamo connetterlo all'AI".
> È "**quali connessioni hanno senso e quali sono troppo rischiose da dare a un agente**".

**Visual**: nessun diagramma. Possibile mini-schema di "tool definition" in mono (nome, descrizione, args).

---

## Slide 34 — Search + RAG + Deep Research (famiglia conoscenza)

**Obiettivo**: 3 livelli di sofisticazione. Posizionarli come una scala di complessità.

**Layout**: 3 blocchi a scala crescente + domanda da informed user.

**Contenuto testuale**:

Titolo: **Search, RAG, Deep Research: la famiglia della conoscenza**

Tre livelli di sofisticazione per dare all'agente accesso a conoscenza fuori dal training:

**Livello 1 — Search-as-a-tool**
- Il modello può fare una query (web o indice privato) quando serve
- Risolve il problema del knowledge cutoff
- Tool atomico, semplice

**Livello 2 — RAG (Retrieval-Augmented Generation)**
- Pattern architetturale, non un tool singolo
- Prima della generazione: recupero dai vostri dati dei chunk rilevanti, iniezione nel context
- Il modello risponde **ancorato** alla vostra conoscenza proprietaria
- Su vector DB, search engine, DB aziendali

**Livello 3 — Deep Research**
- Sistema agentico multi-fase — non un tool
- La slide successiva lo approfondisce

**Domanda chiave da informed user**:
> Quando un fornitore vi propone un prodotto AI per la vostra azienda:
> - Come fa a conoscere i vostri dati?
> - Fa RAG? Su quale base di conoscenza?
> - Come la tiene aggiornata?
> - Che policy di accesso applica?

**Note per lo speaker**:
- RAG è il pattern più diffuso in assoluto per integrare AI in azienda. Un MBA deve conoscerlo.
- Collegamento Slide 32: "il RAG funziona bene **se** la knowledge base sotto è modellata bene. Altrimenti è spazzatura in, spazzatura out."

**Visual**: 3 livelli in scala crescente (opzionale), o 3 colonne.

---

## Slide 35 — Deep Research come architettura agentica [VIZ]

**Obiettivo**: scomporre Deep Research nei suoi 4 step e far vedere che usa tutti i pattern visti in Sezione 4.

**Layout**: diagramma a 4 fasi + 4 domande finali.

**Contenuto testuale**:

Titolo: **Deep Research: un'architettura, non un tool**

(Diagramma a 4 fasi)

**Fase 1 — Elicitation del piano**
- L'agente principale analizza la domanda
- Produce un piano strutturato: sotto-domande, fonti probabili, sintesi attesa
- Spesso chiede chiarimenti all'utente (focus, orizzonte temporale)

**Fase 2 — Spawn di micro-agenti di retrieve**
- Per ogni sotto-domanda → sub-agent in parallelo
- Ogni sub-agent ha context isolato
- Cerca, legge, sintetizza, torna con un mini-report

**Fase 3 — Loop esterno di steering**
- L'agente principale riceve i mini-report
- Confronta con il piano originale
- Identifica gap ("dati su UE ma non US")
- Lancia nuovi sub-agent mirati
- Auto-correzione

**Fase 4 — Sintesi finale**
- Integrazione dei mini-report in un documento strutturato
- Citazioni ancorate alle fonti
- **Unico output visibile all'utente**

Box:
> Deep Research è il primo prodotto multi-agent mainstream che gli utenti usano senza rendersene conto come sistema multi-agente.
> Usa tutti i pattern visti in Sezione 4: sub-agent, context isolato, loop di decisione, tool.

**4 domande da informed user per smascherare**:
1. Chi fa il planning iniziale?
2. Quanti sub-agent in parallelo?
3. C'è un loop di steering o è one-shot?
4. Come sono citate le fonti?

**Nota onesta**:
- Deep Research è potente ma costoso e lento (minuti, non secondi)
- Non è il pattern giusto per ogni domanda
- È il pattern giusto per domande di ricerca complesse con ampiezza e struttura

**Visual**: diagramma 4 fasi, con parallelismo visibile in fase 2.

**Prompt per generazione SVG**:
```
SVG horizontal flow with 4 phases.

Phase 1 (left): box "Elicitation piano" (purple). Below: "sotto-domande,
fonti, piano sintesi".

Phase 2: box "Spawn sub-agent" (teal). Below: 4-5 small circles representing
parallel sub-agents, connected by arrows from the top box.

Phase 3: box "Steering loop" (amber). Below: "valuta, identifica gap,
riassegna". Arrow back to Phase 2 showing the loop.

Phase 4: box "Sintesi finale" (purple). Below: "output con citazioni".

Arrows connecting phases 1→2→3 (with loop)→4. Phase 3 has a return
arrow up to Phase 2.

Flat design. Use different colors per phase to emphasize structure.
```

**Note per lo speaker**:
- Esperimento: chiedi quanti hanno usato Claude Research o Perplexity Deep Research. Poi spiega che hanno usato un multi-agent senza saperlo.
- Punto didattico: i concetti di Sezione 4 (sub-agent) si vedono "all'opera" in un prodotto che usano già.

---

## Slide 36 — MCP (Model Context Protocol)

**Obiettivo**: demistificare. MCP è un protocollo di discovery/invocazione, non una nuova capacità. + caveat contesto.

**Layout**: demistificazione + analogia + perché conta + caveat forte.

**Contenuto testuale**:

Titolo: **MCP — Model Context Protocol**

**Cos'è davvero (demistificazione)**:
- **Non è un nuovo tipo di tool**
- **Non è una nuova capacità dell'agente**
- È un **protocollo standard** per discovery e invocazione dei tool
- Sotto il cofano, il tool call funziona esattamente come in Slide 24

**Cosa standardizza**
- **Discovery**: un agente chiede a un server MCP "quali tool offri?" e riceve lo schema completo, senza configurazione manuale
- **Invocazione**: il formato con cui l'agente chiama un tool e riceve un result è lo stesso, indipendentemente dal server

**Analogia**:
> Prima di USB, ogni dispositivo aveva il suo cavo proprietario.
> MCP è l'USB dei tool per agenti.

**Perché conta strategicamente**
- **Riduce vendor lock-in**: integrazione al vostro CRM funziona con qualunque agente MCP-compatibile
- **Accelera l'ecosistema**: centinaia di server MCP pubblici già disponibili (GitHub, Linear, Notion, Gmail, DB)
- **È il layer degli "app store" degli agenti**: preparatevi

**Caveat operativo (forte)**:
> ⚠ **Gli MCP non sono gratis in termini di context.**
> Ogni server MCP connesso pubblica le definizioni dei suoi tool nel context.
> 10 server con 20 tool ciascuno = 3-6k token **prima ancora di parlare**.
> Connetterli "nel caso servano" satura il context.
>
> **Regola pratica**: connetti solo gli MCP che servono per il task in corso.

**Posizione finale (doppia lama)**:
> - Se vi vendono un'integrazione AI senza MCP → state comprando vendor lock-in
> - Se vi vendono "supporto per 50 MCP" → chiedete quali si attivano di default e come
>
> La differenza tra "disponibili" e "sempre in context" è la differenza tra un prodotto serio e uno che vi brucia token.

**Note per lo speaker**:
- Questa slide è da ~3 minuti. Densa, con posizioni forti.
- Il caveat è un ponte esplicito verso Sezione 7 (skill come soluzione di progressive disclosure): "ricordatevelo, tra poco vediamo come si risolve".

**Visual**: nessun diagramma. Layout testuale con box evidenziati.

---

## Slide 37 — Browser use

**Obiettivo**: pattern "agente pilota un browser". Presentarlo come ultima istanza, non prima scelta.

**Layout**: cos'è + esempi + limiti onesti + take-home.

**Contenuto testuale**:

Titolo: **Browser use**

**Il pattern**
- L'agente pilota un browser come farebbe un essere umano
- Vede screenshot, produce azioni (click, scroll, scrittura in form, navigazione)
- Esempi di prodotto: Claude Computer Use (Anthropic), Browser Use (open source), OpenAI Operator

**Quando serve**
- Quando il sistema esterno **non ha API né MCP**
- Unico modo di interagirci è come umano
- Sblocca il "long tail" delle automazioni aziendali su sistemi legacy

**Limiti onesti**
- **Lento**: ogni azione è un round-trip con screenshot
- **Costoso**: molti token per screenshot in input
- **Fragile**: cambia l'UI → si rompe
- **Difficile da auditare**: cosa ha visto/cliccato?

**Box take-home**:
> Ultima istanza, non prima scelta.
> Ma sblocca casi che altrimenti non si farebbero affatto.

**Note per lo speaker**:
- Caso d'uso tipico: SaaS proprietario legacy (tipicamente aziendale) senza API moderne. L'unico modo di automatizzare è "far usare il SaaS a un agente".
- Demo possibile: tra gli harness moderni (Claude Computer Use), è impressionante visivamente.

**Visual**: nessun diagramma. Opzionale: screenshot stilizzato di browser con puntatore/highlight.

---

## Slide 38 — Bash / code execution come tool

**Obiettivo**: posizionare bash come tool *architetturalmente fondamentale* — substrato di coding agent (Sez 6) e skill (Sez 7).

**Layout**: cos'è + 3 ragioni "perché è fondamentale" + nodo sicurezza.

**Contenuto testuale**:

Titolo: **Bash / code execution: il tool più potente**

**Cos'è**
- L'agente esegue comandi shell o codice (Python, Node, …) in un ambiente sandboxato
- Filesystem accessibile, esegue programmi, installa librerie
- Può fare qualunque cosa sia possibile in una shell

**Perché è architetturalmente fondamentale** (3 punti)

**1. È il tool più generale di tutti**
- Non sblocca una capacità specifica
- **Sblocca lo spazio delle capacità**
- Se hai bash, hai accesso a tutto l'universo software

**2. Abilita l'agente a scriversi i tool**
- Anziché avere 20 tool predefiniti...
- ...un agente con bash può scrivere uno script al volo, eseguirlo, interpretare il risultato
- Cuore dei coding agent (Sezione 6)

**3. È il substrato delle skill**
- Una skill = directory di file + istruzioni su come usarli, eseguita in ambiente bash
- Senza bash come tool, **non esistono le skill** (Sezione 7)

**Nodo sicurezza (forte)**:
- Bash è il tool più potente e più pericoloso
- **Sempre sandboxato**: container isolato, no accesso a rete privata, no credenziali sensibili nell'environment
- Un bash non sandboxato = chiave dell'ufficio allo stagista al primo giorno

Box:
> Quando vedrete le skill nella Sezione 7, il meccanismo che le fa funzionare è **proprio** il tool bash.
> Tenetelo in mente.

**Note per lo speaker**:
- Questa è una slide di ponte: chiude Sezione 5 ma anticipa esplicitamente 6 e 7.
- "Se dovete ricordare un solo tool di tutti quelli visti: bash. Non perché lo userete — perché è quello che fa funzionare tutto il resto."

**Visual**: nessun diagramma. Testo con nodo sicurezza evidenziato.

---

# Sezione 6 — L'agente che scrive ed esegue codice

Quarto loop della gerarchia: il loop con scrittura ed esecuzione di codice. Introduce la distinzione fondamentale code-as-tool vs code-as-product, il ruolo del TDD, e chiude con il framework "verificabilità → automazione" — una delle slide più portable della lezione.

---

## Slide 39 — Apertura: il codice come tool definitivo

**Obiettivo**: framing iniziale. Richiamare bash di Sezione 5. Anticipare la distinzione (a)/(b).

**Layout**: frase forte + 3 bullet.

**Contenuto testuale**:

Titolo: **Il codice come tool definitivo**

Frase (grande):
> Il codice è il tool di ultima istanza.
> Sblocca capacità arbitrarie senza doverle pre-definire.

Bullet:
- Richiamo: **bash è il substrato** (Slide 38)
- Un agente con bash può scriversi i tool a runtime
- Ma il codice negli agenti ha **due anime profondamente diverse**, che vengono spesso confuse

Transizione:
> Vediamole — e vediamo perché la distinzione è strategica, non accademica.

**Note per lo speaker**:
- Slide breve, di transizione. Non attardarsi.
- Tensione narrativa: "quali sono queste due anime?"

**Visual**: nessun diagramma. Testo centrato.

---

## Slide 40 — Le due anime del codice negli agenti

**Obiettivo**: piantare la distinzione strategica come pietra angolare della sezione.

**Layout**: tabella a 2 colonne (a) vs (b).

**Contenuto testuale**:

Titolo: **Code as tool vs Code as product**

Tabella:

| | **(a) Code as tool** | **(b) Code as product** |
|---|---|---|
| **Cosa fa** | L'agente scrive codice per risolvere il suo task | L'agente scrive software che qualcuno userà e manterrà |
| **Vita del codice** | Usa-e-getta (utente spesso non lo vede) | Persistente (è il deliverable) |
| **Esempi di prodotto** | ChatGPT Advanced Data Analysis, Claude code execution | Claude Code, Cursor, Devin, Copilot |
| **Beneficiari in azienda** | Knowledge worker (analisi, report, calcoli) | Team R&D / engineering |
| **Metrica ROI** | Produttività del singolo | Velocità e qualità dello sviluppo |

Box:
> Un fornitore che vi dice *"la nostra AI scrive codice"* può vendervi **una di queste due cose**.
> Sono due mondi con requisiti, vincoli di sicurezza, e team beneficiari completamente diversi.
> **Chiedete sempre quale dei due.**

**Note per lo speaker**:
- Dato concreto da portare: un'azienda può adottare (a) senza che il team R&D ne sia coinvolto. È data science / knowledge work, non engineering.
- Inversamente, un'adozione di (b) senza una policy di review del codice generato è pericolosa.

**Visual**: tabella. Nessun diagramma.

---

## Slide 41 — Code as tool: il loop scrivi-esegui-interpreta

**Obiettivo**: meccanica del pattern (a). Cambio di paradigma per data analysis.

**Layout**: diagramma del loop + 3 punti chiave.

**Contenuto testuale**:

Titolo: **(a) Code as tool: il loop**

(Diagramma del loop)

**Meccanica**
- L'agente riceve un task analitico (*"fatturato medio per trimestre 2023?"*)
- Decide che serve codice
- Scrive uno script (Python, SQL, JS…)
- Lo esegue in sandbox
- Legge l'output, lo interpreta, risponde in linguaggio naturale all'utente

**3 punti chiave**

1. **L'utente vede la risposta, non il codice** (spesso). Il codice è plumbing interno dell'agente.
2. **Sblocca task che il modello non farebbe "a mano"**: un LLM sbaglia la media di 50 numeri. Con Python la calcola perfettamente.
3. **Cambio di paradigma per data analysis**: il business user non chiede più "fammi la query SQL" — chiede *"dimmi il fatturato medio"* e l'agente costruisce da sé il mezzo.

**Implicazione strategica**
- Rende obsoleto il "dashboarding predefinito" per molti casi d'uso
- La domanda si fa in linguaggio naturale, il codice viene scritto on-the-fly, la risposta torna in linguaggio naturale
- Il dato resta il dato. Cambia il modo di interrogarlo.

**Visual**: diagramma di loop semplice scrivi→esegui→interpreta.

**Prompt per generazione SVG**:
```
SVG small cyclic flow, 3 steps.
Step 1: "Scrivi codice" (purple, rounded rect, with small `<>` icon)
Step 2: "Esegui in sandbox" (gray, rounded rect)
Step 3: "Interpreta output" (teal, rounded rect)
Arrows clockwise: 1→2→3→1.
Step 1 has an additional input arrow from above labeled "task utente".
Step 3 has an additional output arrow going down labeled "risposta in linguaggio naturale".
Flat design.
```

---

## Slide 42 — Code as product: coding agent + TDD

**Obiettivo**: meccanica pattern (b) + TDD come chiave per affidabilità + implicazione strategica.

**Layout**: 3 blocchi + frase strategica finale.

**Contenuto testuale**:

Titolo: **(b) Code as product: coding agent e TDD**

**I prodotti**
- Claude Code, Cursor, Devin, Copilot
- Il pattern è simile a (a) — scrivi, esegui, valuta — ma **scalato** a progetti reali
- Molti file, dipendenze, test suite, git, pull request

**Pattern delle sezioni precedenti all'opera**
- Sub-agent per esplorare grandi codebase senza inquinare il context principale (Sezione 4)
- Skill per codificare convenzioni di progetto e stile (Sezione 7)

**Come si ottiene codice affidabile: TDD come prerequisito**
- **Test-Driven Development**: specificare il comportamento atteso come test **prima**, far scrivere all'agente il codice che li fa passare
- La test suite diventa:
  - il **contratto** con cui l'agente sa quando ha finito
  - il **feedback loop** deterministico che gli dice se è sulla strada giusta
  - l'**ancora di affidabilità** che previene regressioni quando l'agente cambia cose

Box:
> Con gli agenti il TDD diventa un prerequisito, non una best practice opzionale.
> Un agente che scrive codice senza test è un agente che lavora al buio.
> Un agente con test è un agente che impara dai propri errori automaticamente.

**Implicazione strategica (frase finale forte)**:
> Il software engineering sta diventando un mestiere di **direzione**, non di esecuzione.
> Il differenziale non è chi digita più velocemente.
> È chi sa definire meglio il contratto (test, spec, architettura) e orchestrare agenti che lo realizzano.

**Note per lo speaker**:
- Questa slide cambia come molti studenti vedono il software engineering.
- Caveat onesto: questo è vero oggi per coding task ben delimitati. Per decisioni architetturali complesse, il ruolo umano di direzione resta centrale.

**Visual**: nessun diagramma obbligatorio. Opzionale: mini-schema "test suite come contratto".

---

## Slide 43 — Il loop agentico con codice (chiusura meccanica) [VIZ]

**Obiettivo**: quarto loop della gerarchia. Focus su "verify as signal".

**Layout**: diagramma di loop + take-home.

**Contenuto testuale**:

Titolo: **Il loop agentico con codice**

(Diagramma di loop)

Sotto, take-home:
> **Perché gli agenti stanno migliorando così rapidamente nel codice?**
> **Perché possono testare se stessi.**
> Il loop ha qualcosa che gli altri loop non avevano: un giudizio automatico e deterministico della qualità di ciascun passo.

**Visual**: loop scrivi-esegui-valuta-correggi con enfasi sul "valuta".

**Prompt per generazione SVG**:
```
SVG cyclic flow, 4 nodes in a square layout.
Node 1 (top-left): "Scrivi codice" (purple)
Node 2 (top-right): "Esegui" (gray)
Node 3 (bottom-right): "Valuta output" (amber, EMPHASIZED — slightly larger, brighter border)
Node 4 (bottom-left): "Correggi" (coral)
Arrows clockwise: 1→2→3→4→1.

Near node 3, add a small badge or call-out: "Signal: test passed? / compile ok? / output as expected?"

Below the diagram, a subtle label: "Deterministic verify loop".

Flat design. Emphasize node 3 as the key differentiator.
```

**Note per lo speaker**:
- Collegamento al ragionamento della prossima slide: il fatto che il codice sia verificabile è ciò che rende l'RL così efficace in questo dominio.

---

## Slide 44 — La verificabilità come predittore di automazione

**Obiettivo**: slide-framework portable. Una delle più importanti dell'intera lezione.

**Layout**: 3 passi di ragionamento + tesi generalizzata + esempi contrastivi + caveat.

**Contenuto testuale**:

Titolo: **Verificabilità → automazione**

**Il ragionamento in 3 passi**

**Passo 1 — Perché il codice è lo sweet spot dell'AI**
- Il codice ha una proprietà rara: la sua verifica è **immediata e binaria**
- Un programma gira o non gira
- Un test passa o non passa
- Una compilazione riesce o fallisce
- Segnale netto, deterministico, automatico

**Passo 2 — Perché questo accende il Reinforcement Learning**
- L'RL funziona magnificamente quando il segnale di correttezza è netto
- Lento quando è ambiguo
- Impossibile quando manca
- Non è solo il codice: anche matematica, scacchi, calcolo numerico, problemi di ottimizzazione

**Passo 3 — La regola generalizzata**

Box tesi (enfasi):
> **Se una professione intellettuale ha un output la cui verificabilità è immediata e binaria, è ad altissimo rischio di automazione da parte dell'AI.**
>
> **Se l'output richiede giudizio qualitativo, negoziazione, contesto sociale, o ha criteri di successo ambigui, il rischio è più basso — per ora.**

**Esempi contrastivi** (come spunti, non verità assolute):

| Alta verificabilità → alta pressione | Bassa verificabilità → pressione più lenta |
|---|---|
| Scrittura di codice (con test) | Strategia aziendale |
| Calcoli ingegneristici | Negoziazione |
| Validazione contabile automatica | Terapia |
| Conformità normativa codificata | Leadership |
| Traduzioni tecniche | Vendita consulenziale complessa |
| Debugging | Decisioni etiche |

**Caveat onesto**:
- Verificabilità ≠ sostituibilità totale
- Anche in campi ad alta verificabilità, resta il ruolo umano:
  - di definire il contratto (cosa va verificato)
  - di gestire i casi che escono dal pattern
  - di rispondere delle conseguenze
- Il pattern **sposta** il lavoro, non lo **cancella** sempre

**Chiusura (posizione)**:
> Questa non è una previsione sul *"se"*. È un framework per capire il *"quando"* e il *"dove"*.
> Guardate il vostro lavoro e quello dei vostri team.
> Quanto è verificabile l'output? Quanto binario è il giudizio di "ben fatto"?
> Quella risposta vi dice molto più di mille articoli su "l'AI ruberà i lavori".

**Note per lo speaker**:
- Questa è una delle slide più portable della lezione. Se gli studenti si portano via una cosa, portino via questa.
- Essere cauti con gli esempi: non sono verità assolute, sono spunti. Dirlo esplicitamente.
- Silenzio dopo la chiusura. Far respirare.

**Visual**: nessun diagramma obbligatorio. Tabella 2 colonne per gli esempi.

---

# Sezione 7 — Context engineering

Sezione di sintesi. Tutto il lavoro serio sugli agenti è lavoro sul context. Tratta: harness, compaction/pruning, skill (progressive disclosure), modellazione della conoscenza (3 slide), sandbox, memoria (2 slide), harness landscape, chiusura.

---

## Slide 45 — Apertura Sezione 7 (provocatoria)

**Obiettivo**: aprire con la tesi della sezione + richiamare tutto ciò che era già context engineering senza nome.

**Layout**: frase grande + elenco di "richiami".

**Contenuto testuale**:

Titolo (grande):
> Tutto il lavoro serio sugli agenti è lavoro sul context.

Sotto:
**Fin qui abbiamo fatto context engineering senza chiamarlo così:**
- Il **system prompt** che definisce l'agente (Slide 12) → context engineering
- La scelta di **quali tool esporre** (Slide 25-26) → context engineering
- I **sub-agent** per isolare lavoro sporco (Slide 27-28) → context engineering
- Il caveat MCP *"non connetterli tutti"* (Slide 36) → context engineering
- La **modellazione della conoscenza** (Slide 32) → context engineering

**In questa sezione lo facciamo esplicito, e vediamo le tecniche di frontiera.**

**Note per lo speaker**:
- Effetto psicologico: gli studenti si rendono conto di aver già imparato metà della sezione senza saperlo. Consolidamento senza fatica.
- "Non c'è niente di nuovo nella prima metà di questa sezione. Ridiamogli un nome, e vedrete le cose diversamente."

**Visual**: nessun diagramma. Testo con richiami.

---

## Slide 46 — Harness: chi fa davvero le cose

**Obiettivo**: demistificare il ruolo dell'harness. Il modello decide, l'harness esegue.

**Layout**: definizione + cosa fa + frase chiave.

**Contenuto testuale**:

Titolo: **Harness: il lavoro invisibile**

**Cos'è**
- Software "muto" intorno all'LLM, non è il modello
- È l'applicazione che orchestra tutto

**Cosa fa davvero (nessuna di queste cose la fa l'LLM)**
- Gestisce il context (costruzione, compaction, pruning)
- Esegue i tool call e raccoglie i result
- Applica policy di sicurezza (cosa l'agente può/non può fare)
- Orchestra sub-agent, gestisce parallelismo
- Persiste stato (conversazioni, memoria, skill)
- Gestisce retry, timeout, budget
- Audita cosa è successo

**Frase chiave**:
> Quando dite *"Claude ha fatto X"*, in realtà:
> - **Claude ha deciso X**
> - **L'harness ha eseguito X**
>
> Il confine tra i due è sottile ma cruciale.
> Quasi tutta la sicurezza, l'affidabilità e la qualità di un agente in produzione **vive nell'harness**.

**Box take-home**:
> L'harness è diventato il livello dove si gioca la competizione.
> L'LLM è commodity.
> **L'harness è dove si differenzia il prodotto.**

**Note per lo speaker**:
- Questa slide smonta un fraintendimento diffuso: "abbiamo comprato l'LLM X, funziona come Y". No, avete comprato un LLM dentro un harness. Cambiare harness = cambiare prodotto.
- Anticipa Slide 56 (harness landscape).

**Visual**: opzionale. Schema a 2 livelli (LLM dentro Harness) con l'harness come "shell" che contiene il modello.

---

## Slide 47 — Compaction e pruning

**Obiettivo**: tecniche "difensive" di gestione del context quando cresce troppo.

**Layout**: 2 tecniche in 2 blocchi + osservazione chiusura.

**Contenuto testuale**:

Titolo: **Compaction e pruning: gestire il context che cresce**

Due tecniche opposte per lo stesso problema.

**Pruning — tagliare**
- Elimina parti del context non più rilevanti:
  - tool result vecchi
  - turni obsoleti
  - informazioni superate
- Politica: **"quali informazioni sono sicure da dimenticare?"**
- Semplice da implementare, potente se le policy sono sensate

**Compaction — condensare**
- Sostituisce parti del context con una loro versione sintetizzata
- Tipicamente un sub-agent riassume gli ultimi N turni
- La sintesi **rimpiazza** gli originali nel context
- Politica: **"se devo dimenticare, prima condenso"**

**Box osservazione**:
> Entrambe le tecniche sono **lossy**: perdi informazione in cambio di spazio.
> La scelta di *cosa* comprimere o buttare via è una delle decisioni di design più delicate di un agente in produzione.
>
> Domanda da informed user: *"come gestite il context quando diventa troppo grande? Pruning, compaction, o niente?"*
> Risposta *"niente"* = prodotto fragile oltre una certa soglia di uso.

**Note per lo speaker**:
- Nota pratica: ChatGPT fa compaction in conversazioni lunghe. Se avete visto "mi sembra di aver dimenticato cose precedenti", è compaction.

**Visual**: schema semplice opzionale. Due freccette: una taglia una parte del context (pruning), l'altra sostituisce un blocco con un blocco più piccolo (compaction).

---

## Slide 48 — Progressive disclosure: da MCP a skill

**Obiettivo**: introdurre la tecnica "offensiva": non caricare ciò che non serve. Ponte da caveat MCP a skill.

**Layout**: problema + pattern.

**Contenuto testuale**:

Titolo: **Progressive disclosure**

**Il problema (richiamo Slide 36)**
- Connettere molti MCP satura il context
- Tutte le tool definition stanno sempre lì — usate o no
- È il **modello opposto** di un'organizzazione sana della conoscenza

**Il pattern**
- La conoscenza/capacità sta **fuori dal context**
- Viene caricata **on demand**, solo quando serve
- Quando non serve, non entra mai nel context

**L'analogia**:
> **Skill sta a MCP come "libro sullo scaffale" sta a "libro aperto sulla scrivania".**
> MCP paga il costo del libro aperto sempre.
> Skill paga solo quando apre il libro.

Transizione:
> Vediamo cosa sono le skill.

**Note per lo speaker**:
- Questa slide è breve — è un setup per la prossima.
- Concetto memorabile: il principio di "caricare all'occorrenza" si applica bene a qualsiasi conoscenza aziendale. Non è un dettaglio tecnico, è un principio organizzativo.

**Visual**: opzionale. Due icone a confronto: scaffale (libri chiusi) vs scrivania affollata (molti libri aperti).

---

## Slide 49 — Cosa sono le skill

**Obiettivo**: meccanica delle skill + richiamo esplicito bash come substrato.

**Layout**: meccanica + messaggio forte + richiamo.

**Contenuto testuale**:

Titolo: **Skill: conoscenza on-demand**

**Il pattern**
- Una skill è una **directory** sul filesystem
- Contiene: documentazione, istruzioni, esempi, eventualmente script
- File radice: `SKILL.md` — spiega al modello come usarla

**Cosa vede il modello inizialmente**
- Solo una **brevissima descrizione** della skill:
  *"disponibile: skill per gestire file Excel, caricala quando serve"*
- Poche decine di token

**Quando decide che serve**
- Il modello la carica tutta in context
- Esplora la directory (legge `SKILL.md`, file di supporto, esempi)
- Usa le istruzioni e gli script contenuti per eseguire il task

**Quando non serve**
- Il materiale **non entra mai nel context**
- Costo: zero

**Richiamo esplicito**:
> **È il tool bash che rende tutto questo possibile** (Slide 38).
> Una skill è letteralmente una cartella navigabile via bash.
> Ve lo avevo detto: bash è il substrato.

**Box messaggio**:
> La skill trasforma il problema della saturazione del context in un problema di **discovery navigabile**.
> Avere 100 skill non costa nulla in context — finché non le apri.
> Avere 100 MCP connessi costa tutto, subito, sempre.

**Note per lo speaker**:
- Le skill sono state introdotte da Anthropic come pattern. La demo finale ne mostrerà alcune all'opera.
- "Se un prodotto vi dice 'supporta skill', chiedete come sono organizzate, chi le scrive, come si versionano. È il nuovo terreno di lavoro."

**Visual**: schema directory + navigazione a richiesta.

**Prompt per generazione SVG**:
```
SVG two-panel.

LEFT panel — "MCP": the model's context box (purple outline) with many
tool definitions stacked inside — filling most of the box. Label: "sempre
in context".

RIGHT panel — "Skill": small context box (purple outline) with just one
tiny line inside labeled "skill descriptor: Excel handler — 20 token".
Above or beside, a folder icon labeled "SKILL directory" containing
multiple files. Dashed arrow from folder to context, labeled
"caricata solo quando serve".

Highlight the dramatic difference in context usage.
Flat design.
```

---

## Slide 50 — Modellazione della conoscenza (1/3): perché "dare i documenti all'agente" non basta

**Obiettivo**: sfatare l'intuizione naïve "metto i PDF in un vector DB e via".

**Layout**: 4 problemi pratici + analogia.

**Contenuto testuale**:

Titolo: **Modellazione della conoscenza (1/3)**

Sottotitolo:
> Perché "dare i documenti all'agente" è un punto di partenza, non una destinazione.

**L'intuizione sbagliata**
> *"Metto i miei documenti in una base di conoscenza, l'agente ci accede via RAG, funziona."*

**Corretta in teoria. Insufficiente in pratica.**

**4 problemi pratici**

1. **Gergo interno non interpretabile**
   - Documenti parlano di "SKU_v3", "CDP", "cliente Gold", "ramo Hermes"
   - L'agente non sa cosa significano senza contesto esplicito

2. **Scritti per umani con conoscenza implicita**
   - "Seguire il processo standard" — quale?
   - "Contattare il referente" — chi è?
   - Ogni documento presuppone informazioni che non cita

3. **Contraddizioni silenziose**
   - Documento 2022: procedura X
   - Documento 2024: procedura Y
   - Nessuno ha ritirato il primo
   - L'agente cita entrambi con pari autorità

4. **Granularità sbagliata**
   - Troppo lunghi per stare nel context
   - Troppo sconnessi per essere utili in frammenti
   - Il RAG restituisce pezzi fuori dal loro senso originale

**Box analogia**:
> Dare i documenti all'agente senza modellazione è come assumere un dipendente e dargli l'archivio senza fargli onboarding.
> Tecnicamente tutte le informazioni ci sono.
> **Praticamente è inutilizzabile.**

**Note per lo speaker**:
- Esperienza dal campo da citare: "la maggior parte dei progetti RAG che vediamo fallire in produzione, falliscono qui — non sui modelli, non sul vector DB, non sul prompt. Falliscono perché la conoscenza sottostante non era pronta."
- Richiamo Slide 32 (caos informativo): "è lo stesso problema visto prima, ma operativizzato. Qui vediamo cosa serve costruire."

**Visual**: nessun diagramma. 4 blocchi testuali.

---

## Slide 51 — Modellazione della conoscenza (2/3): cosa serve davvero

**Obiettivo**: cosa costruire a monte dell'adozione AI. Lista strutturata e operativa.

**Layout**: 5 pilastri + messaggio strategico.

**Contenuto testuale**:

Titolo: **Modellazione della conoscenza (2/3)**

Sottotitolo:
> Cosa va costruito affinché l'agente usi bene la conoscenza aziendale.

**I 5 pilastri**

**1. Semantic layer condiviso**
- Definizioni esplicite e univoche dei concetti chiave
- "Cliente attivo", "fatturato", "chiuso vinto" = **contratto semantico**
- Non è un glossario: è un contratto che vale per tutti gli agenti **e** tutti gli umani

**2. Ontologia delle entità e relazioni**
- Quali sono le entità del vostro dominio
- Come si relazionano
- Chi ha autorità su cosa
- È la mappa con cui l'agente navigherà

**3. Documentazione pensata per agenti**
- **Non** i PDF prodotti per umani
- Versioni **strutturate**, **granulari**, **pulite di riferimenti impliciti**
- A volte lavoro di riscrittura
- A volte lavoro di creazione ex novo

**4. Freschezza e ownership**
- Ogni pezzo di conoscenza ha:
  - un responsabile
  - una data di ultimo aggiornamento
  - un criterio di obsolescenza
- Senza questo, l'agente cita fonti morte

**5. Policy di accesso**
- Chi (quale agente, per quale utente) può vedere cosa
- **Non è un dettaglio tecnico**: è un requisito di compliance

**Box messaggio strategico**:
> Costruire la knowledge base per agenti è un progetto a sé.
> Di data & information architecture, **non di AI**.
> Precede logicamente l'adozione dell'AI.
> (Anche se in pratica si fa in parallelo — perché l'AI stessa è l'occasione per farlo finalmente.)

**Note per lo speaker**:
- Questa è la slide più operativa della tesi Quantyca. Si può prendere il tempo di elaborare.
- Se il pubblico è senior: "quante delle vostre aziende hanno già queste 5 cose? Se la risposta è <4, l'AI sarà uno specchio".

**Visual**: nessun diagramma. 5 blocchi testuali.

---

## Slide 52 — Modellazione della conoscenza (3/3): dai documenti alle skill

**Obiettivo**: ponte operativo. Come si passa dalla teoria (semantic layer, ontologia) al meccanismo (skill).

**Layout**: pattern + esempi concreti + take-home.

**Contenuto testuale**:

Titolo: **Modellazione della conoscenza (3/3)**

Sottotitolo:
> Dai documenti alle skill.

**Il pattern emergente**
- Ogni **dominio di conoscenza** dell'azienda → **skill navigabile**
- La skill contiene:
  - istruzioni di navigazione ("quando cerchi info su X, consulta il file Y")
  - esempi d'uso
  - riferimenti ai tool specifici (query DB, search su KB)
- La skill **non è la conoscenza**: è la **mappa alla conoscenza**
- La conoscenza vera sta nei sistemi (DB, wiki, documenti)

**Esempi pratici di skill aziendali**

- **Skill "politiche HR"**: come sono organizzate le policy, come si cercano, come si citano
- **Skill "prodotti e pricing"**: indice dei prodotti, tariffe, regole di sconto
- **Skill "architettura tecnologica"**: stack, convenzioni, pattern adottati
- **Skill "clienti strategici"**: chi sono, chi li segue, cosa ci comprano
- **Skill "processo di onboarding nuovi dipendenti"**: passi, owner, scadenze

**Box take-home**:
> Se il vostro prossimo progetto AI parte con:
> *"prendiamo i nostri PDF e mettiamoli in un vector store"* → fermatevi.
>
> Partite invece da:
> - quali sono i domini di conoscenza della vostra azienda
> - chi ne è owner
> - qual è il semantic layer
> - come descriveremmo a un nuovo dipendente "dove si trova cosa"
>
> **Quella descrizione è la vostra prima skill.**

(Opzionale — nota speaker da Quantyca):
> È il lavoro che facciamo con le aziende quando ci chiamano "per fare l'AI".
> Quasi sempre, il 70% del progetto è qui. L'AI è il 30%.

**Note per lo speaker**:
- Slide conclusiva del "tris" sulla conoscenza. Tono pratico.
- Se la demo finale mostra skill di Claude, richiamo: "tra 10 minuti ve le faccio vedere all'opera."

**Visual**: schema opzionale con "dominio di conoscenza" al centro e "skill" come interfaccia verso i sistemi veri.

---

## Slide 53 — Sandboxes

**Obiettivo**: sicurezza operativa. Cosa significa dare tool potenti a un agente senza rovinarsi.

**Layout**: cosa limita + analogia.

**Contenuto testuale**:

Titolo: **Sandbox: i confini dell'agente**

**L'agente esegue codice, usa bash, manipola file. A cosa gli date accesso?**

Una sandbox è un ambiente isolato con confini espliciti:

- **Filesystem limitato**: solo cartelle di lavoro, non l'intero sistema
- **Rete limitata**: solo endpoint autorizzati
- **Credenziali limitate**: principio di minimo privilegio
- **Tempo limitato**: ogni esecuzione scade (timeout)
- **Risorse limitate**: CPU/memoria cap

**Analogia**:
> Sandbox è alla sicurezza degli agenti cosa il container è al deployment del software.
> **Nessun agente serio gira senza.**

**Domanda da informed user**:
> Quando un fornitore vi propone un agente che "esegue codice":
> - In che sandbox gira?
> - A cosa ha accesso di default?
> - Come si audita?
> - Cosa succede se l'agente prova a fare qualcosa fuori perimetro?

**Note per lo speaker**:
- Breve richiamo a Slide 38 (bash come tool): "il bash che vi dicevo di sandboxare? È questo".

**Visual**: nessun diagramma obbligatorio. Opzionale: icona di box con "confini" marcati.

---

## Slide 54 — Memoria (1/2): cos'è e cosa NON è

**Obiettivo**: demistificare. Memoria non è il modello che "ricorda". È un sistema esterno gestito dall'harness.

**Layout**: demistificazione forte + realtà tecnica.

**Contenuto testuale**:

Titolo: **Memoria (1/2): cosa NON è**

**Il fraintendimento**
- "Memoria" suggerisce che il modello "ricorda" come un umano
- **Non è così.**

**La realtà**
- Il modello è stateless (richiamo Slide 17)
- La "memoria" è un sistema **esterno** gestito dall'harness
- Fa tre cose:
  1. **Decide cosa salvare** fuori dal context corrente (fatti sull'utente, preferenze, sintesi di conversazioni)
  2. **Archivia in modo persistente** (DB, vector store, file)
  3. **Al turno successivo, recupera e inietta** i fatti rilevanti nel context

**Frase chiave**:
> **Memoria dell'agente = RAG sulle sue stesse conversazioni passate.**
> Non è che Claude "si ricorda di voi".
> È che l'harness ha archiviato fatti su di voi e ve li ri-inietta nel context quando parlate di nuovo.

**Box**:
> Il modello resta stateless.
> La memoria è plumbing dell'harness.

**Note per lo speaker**:
- Se nel vostro harness "la memoria non funziona", il problema non è il modello. È come avete implementato lo storage, l'estrazione, il recupero.
- Questo è un punto dove molti prodotti venduti come "AI con memoria" sono in realtà "harness con RAG sulla storia conversazionale".

**Visual**: nessun diagramma obbligatorio. Schema opzionale: conversazione ↔ archivio esterno ↔ inject nel prossimo context.

---

## Slide 55 — Memoria (2/2): estrazione, gestione, rischi

**Obiettivo**: come funziona operativamente + rischi da conoscere.

**Layout**: meccanica + 4 rischi + take-home.

**Contenuto testuale**:

Titolo: **Memoria (2/2): operativa e rischi**

**Come funziona operativamente**

- **Estrazione**: un sub-agent scorre la conversazione ed estrae "fatti memorizzabili"
  - *"l'utente si chiama Mario"*
  - *"preferisce risposte brevi"*
  - *"lavora sul progetto X"*
- **Gestione**: organizzazione, deduplicazione, aggiornamento quando cambiano
- **Recupero**: al turno successivo, i fatti rilevanti vanno nel system prompt o inizio del context

**4 rischi da conoscere**

1. **Memoria obsoleta**
   - "Preferisce riunioni il lunedì" — ma Mario ha cambiato lavoro 6 mesi fa
   - Nessun meccanismo automatico di invalidazione
2. **Privacy e compliance**
   - Cosa viene salvato, per quanto, con quale consenso?
   - GDPR molto rilevante
3. **Cross-contamination**
   - Memoria di una conversazione che influenza un'altra dove non dovrebbe
   - Tra utenti diversi (grave), o tra contesti diversi dello stesso utente (confuso)
4. **Gaslight da memoria**
   - L'agente "ricorda" cose false iniettate in passato
   - Da utente (distrazione) o da attaccante (deliberato)

**Box take-home**:
> La memoria è potente, ma da maneggiare con cura.
>
> **Domande da informed user quando un prodotto "ha memoria"**:
> - Cosa salva?
> - Per quanto?
> - Come si pulisce?
> - Chi ne è owner?
> - Come si audita?
>
> *"Non è una magia — è un sistema, con policy, bug, e conseguenze."*

**Note per lo speaker**:
- La privacy è spesso sottovalutata. Se il prodotto salva "fatti estratti" sugli utenti, quei fatti sono dati personali nuovi che non esistevano prima — e rientrano in GDPR.
- "La memoria non è un feature. È una responsabilità."

**Visual**: nessun diagramma. Layout testuale.

---

## Slide 56 — Harness landscape (placeholder — da Deep Research)

**Obiettivo**: panoramica del mercato degli harness oggi. Chiusura "panoramica" della sezione.

**Layout**: griglia compatta di harness.

**Contenuto testuale**:

Titolo: **Il landscape degli harness oggi**

**Premessa**:
> L'LLM è commodity. L'harness è dove si gioca la competizione di prodotto.

Griglia (da riempire con i risultati della Deep Research dello speaker):

| Harness | Cosa fa | Per chi | Dove brilla |
|---|---|---|---|
| Claude web | (da riempire) | (da riempire) | (da riempire) |
| Claude Code | (da riempire) | (da riempire) | (da riempire) |
| OpenClaw | (da riempire) | (da riempire) | (da riempire) |
| Hermes Agent | (da riempire) | (da riempire) | (da riempire) |
| Pi | (da riempire) | (da riempire) | (da riempire) |
| Agno | (da riempire) | (da riempire) | (da riempire) |

**Note per lo speaker**:
- Questa slide va completata dopo la Deep Research separata che farà lo speaker.
- I nomi citati (OpenClaw, Hermes Agent, Pi, Agno) potrebbero essere prodotti specifici del suo ecosistema o emersi dopo il knowledge cutoff del modello.
- Alla lezione, verificare che tutti i nomi siano ancora attivi e aggiornati.

**Box take-home**:
> Quando valutate un prodotto AI: non chiedete solo "che modello usa".
> Chiedete "che harness usa" e "cosa fa l'harness".
> Il valore aggiunto vive lì.

**Visual**: griglia 6 righe × 4 colonne. Righe distinte per leggibilità.

---

## Slide 57 — Chiusura Sezione 7 + ponte alla demo

**Obiettivo**: recap visivo + transizione pulita alla demo live.

**Layout**: mappa dei temi della Sezione 7 + ponte.

**Contenuto testuale**:

Titolo: **Context engineering: la mappa**

**Le tecniche viste in questa sezione**

| Categoria | Tecniche |
|---|---|
| **Identificare chi fa cosa** | Harness vs LLM |
| **Tecniche difensive** | Compaction, pruning |
| **Tecniche offensive** | Progressive disclosure (skill vs MCP) |
| **Conoscenza** | Semantic layer, ontologia, skill come mappa |
| **Sicurezza** | Sandbox |
| **Persistenza** | Memoria come sistema esterno |
| **Ecosistema** | Harness landscape |

**Ora vedete perché dicevamo all'inizio:**
> **Tutto il lavoro serio è lavoro sul context.**
> Questo è il luogo dove un prodotto AI diventa serio o resta demo.

**Ponte (alla demo)**:
> Tutto quello che ho raccontato non è teoria.
> Lo vediamo nell'harness che ho qui aperto. →

**Note per lo speaker**:
- Alla transizione, chiudere la slide in secondo piano e passare al live. Non lasciare la slide sullo schermo durante la demo — ruba attenzione.
- Tempo previsto demo: 15 minuti. Preparare 3-4 scenari, non di più.

**Visual**: tabella di riepilogo. Eventualmente una piccola freccia "→ demo" in basso a destra.

---

# Chiusura della lezione

## Slide 58 — Chiusura (mappa dei loop + tesi finale) [VIZ]

**Obiettivo**: chiudere l'arco narrativo aperto alla Slide 1. Consolidare con la mappa. Lasciare un messaggio emotivo.

**Layout**: mappa visiva nella parte alta + frase finale grande nella parte bassa.

**Contenuto testuale**:

Titolo: **I mattoncini**

(Parte alta — mappa visiva dei 4 loop + context engineering trasversale)

(Parte bassa — frase finale grande, centrata)

> Da domani, quando sentirete parlare di AI agentica,
> sentirete suonare dei concetti.
>
> **Quelli sono i mattoncini.**
>
> Buona adozione.

**Visual**: diagramma stratificato + titoli.

**Prompt per generazione SVG**:
```
SVG layered diagram, 4 horizontal levels stacked bottom-to-top.

Level 1 (bottom, smallest width): "Loop atomico" (purple)
  Subtext: "token per token"

Level 2 (wider): "Loop conversazionale" (blue)
  Subtext: "turno per turno"

Level 3 (wider still): "Loop agentico con tool" (teal)
  Subtext: "decide → agisci → osserva"

Level 4 (top, widest): "Loop agentico con codice" (amber)
  Subtext: "scrivi → esegui → verifica"

Each level VISUALLY CONTAINS the level below (nested), like Russian dolls
in 2D — concentric rectangles or stacked trapezoids that clearly show
hierarchy.

Diagonally across all 4 levels, a transparent vertical bar labeled
"CONTEXT ENGINEERING" with sub-labels alongside:
- compaction, pruning
- progressive disclosure (skill)
- modellazione della conoscenza
- memoria, harness, sandbox

Flat design, single consistent palette. The nesting metaphor must be
immediately obvious.

Below the diagram, leave space for the closing text.
```

**Note per lo speaker**:
- Dopo la demo. La slide è l'ultimo sguardo che gli studenti hanno.
- La pausa dopo "buona adozione" è parte della chiusura. Non parlare subito. Se sembra che applaudano, lasciarli applaudire.
- Il richiamo all'apertura è deliberato: "sembra complicatissimo → ecco, i mattoncini". Arco narrativo chiuso.

---

# Appendice A — Note di produzione

## Rendering dei diagrammi
Le slide marcate `[VIZ]` richiedono diagrammi costruiti ad hoc. Per ciascuna il documento contiene un prompt testuale che può essere passato a:
- tool di generazione SVG (Claude con skill artifact, Excalidraw AI, Lucid AI)
- designer per costruzione manuale

Lo stile richiesto è uniforme: flat design, palette consistente, no shadows/gradients.

## Palette suggerita
- Gray (neutro, strutturale)
- Blue (utente, input)
- Purple (modello, LLM)
- Teal (sub-agent, tool, output utile)
- Amber (attenzione, highlight, tool calls, elementi critici)
- Coral (errori, warning)

## Template slide
- Titolo: sentence case, non title case
- Corpo: bullet points preferiti a prosa
- Box evidenziati per messaggi chiave o take-home
- Massimo 7-8 bullet per slide (oltre, spezzare in 2 slide)
- Nessun emoji nelle slide (il documento li usa per marcatori editoriali, ma non devono finire sulle slide vere)

## Densità e tempistica
- 58 slide in 105 minuti → ~1'45'' per slide media
- Slide leggere (apertura, transizioni): 30-60''
- Slide dense (meccanica, diagrammi complessi): 2-3'
- Slide forti con posizione (16, 21, 29, 31, 32, 44): 2-3' ciascuna, lasciare respirare

## Demo finale (~15 minuti, no slide)
Preparazione consigliata:
- 3-4 scenari pronti, non di più
- Ambiente Claude desktop/code preconfigurato con skill
- Evitare demo che dipendono da internet veloce o API esterne che possono failare
- Avere un "piano B" narrativo se la demo fallisce (cosa raccontare se il tool non risponde)

## Harness landscape (Slide 56)
La slide è un **placeholder**. Va completata dopo la Deep Research separata. Verificare in particolare:
- L'esistenza e il posizionamento di OpenClaw, Hermes Agent, Pi, Agno
- Eventuali nuovi harness rilevanti emersi dopo il knowledge cutoff del modello
- Dati di mercato aggiornati (adozione, finanziamenti, ecc.)

---

# Appendice B — Checklist pre-lezione

- [ ] Aver verificato che i dati numerici siano attuali (Gemma 4 / Sonnet 4.5 su Slide 21)
- [ ] Aver completato la Slide 56 con risultati Deep Research
- [ ] Aver preparato 3-4 scenari demo e testato la connettività dell'ambiente
- [ ] Aver deciso quali "war stories" Quantyca inserire a voce (non sulle slide) in particolare su: Slide 16, 21, 32, 51
- [ ] Aver allineato il vocabolario: **context** ovunque (non "blob"), **tool** (non "strumenti")
- [ ] Aver generato i diagrammi `[VIZ]` (slide 11, 18, 19, 24, 26, 28, 30, 35, 43, 58)
- [ ] Aver previsto un buffer temporale: se la lezione rallenta, sono sacrificabili Slide 15 (tipi di task) e Slide 56 (harness landscape) senza danni narrativi

---
