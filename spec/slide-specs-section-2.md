# Specifica Sezione 2 — L'agente conversazionale
## Lezione MBA Politecnico di Milano — "Agents in action"
### Francesco Gianferrari Pini, Quantyca

**Stato**: slide 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 consolidate. Separatore sezione 2 aggiunto.
**Prossima slide da definire**: Slide 19 (Sezione 3 — Closed vs Open).

---

## Separatore — Sezione 2: Conversazionale

**File**: `slides/slide-div-sec2.html`
**Layout**: section-divider centrato. Titolo "Conversazionale", sottotitolo "Dalla funzione all'agente", roadmap 7 tappe con sezione 2 evidenziata e le altre attenuate.

---

## ✅ Slide 9 — Il primo agente: la chat

**Layout**: titolo in alto, frase centrale in evidenza, contrasto a 2 paradigmi (Prima / Dopo) al centro, nota storica in basso piccola.

**Testo**:
- Titolo: *Il primo agente: la chat*
- Frase centrale (in evidenza): *Dalla next token prediction alla conversazione*
- **Contrasto a 2 paradigmi**:
  - **Prima — modello base (dopo il solo pre-training)**: completa testo plausibile. Data una sequenza, produce la continuazione statisticamente più probabile. Non sa di parlare con qualcuno, non distingue una domanda da un frammento di articolo, non segue istruzioni.
  - **Dopo — agente conversazionale**: risponde a un interlocutore, segue istruzioni, mantiene un ruolo, rispetta vincoli di tono e comportamento.
- **Come si ottiene (accenno)**: un secondo giro di addestramento sopra il pre-training — *instruction tuning* e *RLHF* — che insegna al modello non *cosa è probabile*, ma *cosa è utile* rispondere. Più un'interfaccia che struttura lo scambio in turni. *Approfondimento nelle prossime slide.*
- Nota storica in basso (piccola): *Novembre 2022, ChatGPT. Non un nuovo modello — GPT-3 esisteva dal 2020. Un nuovo modo di addestrarlo a conversare.*

**Visual**: nessuno. Il contrasto Prima/Dopo è l'elemento visivo.

---

## ✅ Slide 10 — La meccanica della conversazione

**Layout**: titolo in alto, grande visual al centro (occupa ~70% della slide) che verrà sostituito progressivamente da 3 SVG in sequenza, didascalia sotto.

**Testo**:
- Titolo: *La meccanica della conversazione*
- Didascalia (sotto il diagramma): *La conversazione è un artefatto dell'interfaccia. Per il modello è un unico testo strutturato con tag di ruolo, che viene rispedito integralmente ad ogni turno. L'API è stateless — nessuna memoria tra chiamate.*

**Visual**: sequenza di 3 SVG mostrati progressivamente (sostituzione, non animazione — 3 step della stessa slide). Ogni SVG ha la stessa struttura a 2 colonne; cambia solo il contenuto per mostrare l'avanzare della conversazione.

**Scenario esemplificativo comune ai 3 SVG**:
- Turno 1 — User: *"Ciao, chi sei?"* → Assistant: *"Sono un assistente AI. In cosa posso aiutarti?"*
- Turno 2 — User: *"Spiegami cosa sono i transformer"* → Assistant: *"I transformer sono un'architettura di rete neurale introdotta nel 2017…"*
- Turno 3 — User: *"E l'attention come funziona?"* → Assistant: *"L'attention è il meccanismo con cui il modello pesa le relazioni tra token…"*

**Struttura comune dei 3 SVG**:
> Layout orizzontale a 2 colonne con separatore verticale centrale.
>
> **Colonna sinistra — "Cosa vede l'utente"**: interfaccia chat tipica, bolle alternate (user a destra, assistant a sinistra), font sans-serif pulito, fondo chiaro.
>
> **Colonna destra — "Cosa riceve l'API a questo turno"**: blocco di testo in font monospace, ogni riga preceduta da un tag di ruolo in stile `[system]`, `[user]`, `[assistant]`. Il blocco ha un bordo tratteggiato che lo racchiude interamente, con etichetta laterale a destra in verticale: *"rispedito integralmente ogni turno"*.
>
> Freccia orizzontale dal centro della colonna sinistra al centro della colonna destra, con etichetta *"trasformazione nascosta"*.
>
> Stile minimale, monocromatico con un colore accento solo sul bordo tratteggiato e sulla label laterale.

### Prompt SVG 1 — dopo il 1° turno

> Struttura comune (vedi sopra). Contenuto specifico:
>
> **Colonna sinistra — chat**:
>   - Bolla user: "Ciao, chi sei?"
>   - Bolla assistant: "Sono un assistente AI. In cosa posso aiutarti?"
>   - Campo di input vuoto in basso con cursore lampeggiante.
>
> **Colonna destra — testo API**:
> ```
> [system] Sei un assistente utile…
> [user] Ciao, chi sei?
> [assistant] Sono un assistente AI. In cosa posso aiutarti?
> ```
> Il blocco tratteggiato racchiude le 3 righe. Etichetta laterale: *"rispedito integralmente ogni turno"*.

### Prompt SVG 2 — dopo il 2° turno

> Stessa struttura del SVG 1. Contenuto specifico:
>
> **Colonna sinistra — chat**:
>   - Bolla user: "Ciao, chi sei?"
>   - Bolla assistant: "Sono un assistente AI. In cosa posso aiutarti?"
>   - Bolla user: "Spiegami cosa sono i transformer"
>   - Bolla assistant: "I transformer sono un'architettura di rete neurale introdotta nel 2017…"
>   - Campo di input vuoto in basso con cursore lampeggiante.
>
> **Colonna destra — testo API**:
> ```
> [system] Sei un assistente utile…
> [user] Ciao, chi sei?
> [assistant] Sono un assistente AI. In cosa posso aiutarti?
> [user] Spiegami cosa sono i transformer
> [assistant] I transformer sono un'architettura di rete neurale introdotta nel 2017…
> ```
> Il blocco tratteggiato racchiude tutte le 5 righe. Le 3 righe nuove rispetto al SVG 1 (le ultime 2 + la nuova user) sono evidenziate con un leggero highlight di sfondo in colore accento tenue, per mostrare visivamente che il contesto è CRESCIUTO ma tutto ciò che c'era prima è ancora lì.
>
> Etichetta laterale invariata: *"rispedito integralmente ogni turno"*.

### Prompt SVG 3 — dopo il 3° turno

> Stessa struttura. Contenuto specifico:
>
> **Colonna sinistra — chat**: tutte e 3 le coppie di bolle (Ciao → Spiegami transformer → E l'attention).
>
> **Colonna destra — testo API**:
> ```
> [system] Sei un assistente utile…
> [user] Ciao, chi sei?
> [assistant] Sono un assistente AI. In cosa posso aiutarti?
> [user] Spiegami cosa sono i transformer
> [assistant] I transformer sono un'architettura di rete neurale introdotta nel 2017…
> [user] E l'attention come funziona?
> [assistant] L'attention è il meccanismo con cui il modello pesa le relazioni tra token…
> ```
> Il blocco tratteggiato racchiude tutte le 7 righe. Le 2 righe nuove rispetto al SVG 2 sono evidenziate con highlight di sfondo accento tenue.
>
> In basso, sotto il blocco tratteggiato, aggiungere un piccolo badge: *"contesto a turno 3 = tutto quello che è stato detto finora"*.
>
> Etichetta laterale invariata.

**Nota di rendering**: i 3 SVG condividono la stessa cornice e posizioni. Solo il contenuto delle due colonne cresce. L'effetto "sostituzione progressiva" trasmette visivamente che **il contesto cresce ma niente viene mai riassunto o tagliato**.

---

## ✅ Slide 11 — Perché serve un secondo addestramento

**Layout**: titolo in alto, visual centrale con confronto a 2 colonne (modello base vs modello RLHF), conclusione compatta in basso evidenziata.

**Testo**:
- Titolo: *Perché serve un secondo addestramento*
- Conclusione in basso (evidenziata): *Da «cosa è probabile» a «cosa serve rispondere».*

**Visual**: confronto a 2 colonne — stesso prompt, modello base (pre-trained) vs modello RLHF.

**Prompt per schema SVG**:
> Diagramma orizzontale a 2 colonne gemelle, separate da linea verticale sottile. In cima, centrato sopra entrambe le colonne, un unico box di prompt condiviso.
>
> **Box prompt condiviso (in alto, centrato)**: rettangolo etichettato *Prompt dell'utente* con testo: *"Come posso aumentare le vendite?"*. Dal box partono due frecce divergenti, una verso la colonna sinistra, una verso la destra.
>
> **Colonna sinistra — "Modello base (solo pre-training)"**:
>   - Etichetta colonna in alto, con piccola icona chip grigia.
>   - Sotto il prompt, un box "completamento" (font monospace, sfondo leggermente grigio) che contiene una risposta tipica da completamento statistico non allineato:
>     *"Come posso aumentare le vendite? E quante persone lavorano nella tua azienda? Il settore è B2B o B2C? In quale mercato geografico operate? Negli ultimi anni la domanda è cresciuta o..."*
>   - Sotto il box, piccola label in italico: *"Il modello continua la frase come farebbe un testo sul web — con altre domande, non con una risposta."*
>
> **Colonna destra — "Modello RLHF"**:
>   - Etichetta colonna in alto, con piccola icona chip in colore accento.
>   - Sotto il prompt, un box "risposta" (font sans-serif, sfondo chiaro) che contiene una risposta strutturata e utile:
>     *"Per aumentare le vendite puoi agire su tre leve principali: 1) acquisire nuovi clienti (marketing, partnership); 2) aumentare il valore medio per cliente (upselling, bundle); 3) migliorare la retention (CRM, customer success). Vuoi che approfondiamo una di queste?"*
>   - Sotto il box, piccola label in italico: *"Il modello riconosce una domanda e fornisce una risposta utile, strutturata, orientata all'azione."*
>
> **Stile**: le due colonne sono visivamente simmetriche per struttura, ma contrastano nettamente nel contenuto. Colonna sinistra in scala di grigi, colonna destra con tocchi di colore accento (icona, bordo del box risposta). Font sans-serif ovunque tranne il completamento del modello base, che è in monospace per suggerire "output grezzo, non formattato per l'utente".

---

## ✅ Slide 12 — Il secondo addestramento: RLHF

**Layout**: titolo in alto, mini-schema visivo del ciclo RLHF nella parte superiore (~35% della slide), 3 insight strategici al centro, conclusione evidenziata in basso.

**Testo**:
- Titolo: *Il secondo addestramento: RLHF*
- Meccanica (didascalia sotto il mini-schema): *Varianti operative: RLHF (feedback umano), RLAIF (feedback da altri AI), Constitutional AI (Anthropic), DPO. Cambiano i dettagli; il principio — premiare le risposte desiderabili, penalizzare le altre — è lo stesso.*
- **3 insight strategici**:
  1. La personalità dei diversi modelli (Claude, GPT, Gemini) non è emergente — è scolpita in post-training con valori diversi.
  2. I limiti di comportamento non sono quasi mai limiti di capacità — sono scelte di policy del provider.
  3. Chi fornisce feedback plasma l'AI. Implicazioni etiche, geopolitiche, di business.
- Conclusione in basso (evidenziata): *Il modello che si usa non è "l'AI". È una particolare AI addestrata con particolari valori da particolari persone.*

**Visual**: mini-schema del ciclo RLHF (3-4 step).

**Prompt per schema SVG**:
> Diagramma orizzontale del ciclo RLHF, compatto (occupa ~35% della slide, nella parte superiore). 4 step connessi da frecce in sequenza, con una freccia di ritorno dall'ultimo al primo per chiudere il ciclo.
>
> **Step 1 — "Prompt"**: rettangolo con testo esempio: *"Come posso aumentare le vendite?"*
>
> **Step 2 — "Il modello produce 2 risposte candidate"**: rettangolo centrale etichettato "Modello" con due frecce che escono, una verso un box "Risposta A" (testo breve esemplificativo: *"Per aumentare le vendite, lavora su acquisizione, upsell e retention..."*), una verso un box "Risposta B" (testo breve alternativo: *"Dipende. Quali sono i tuoi attuali canali di vendita?"*).
>
> **Step 3 — "Un giudice sceglie la migliore"**: icona di persona (o persona + chip, a suggerire "umano o AI") con pollice verso l'alto davanti a una delle due risposte. Label sotto: *"umano, AI, o principi costituzionali"*.
>
> **Step 4 — "Il modello viene aggiornato"**: rettangolo "Modello" con piccole manopole al suo interno leggermente ruotate (richiamo a Slide 2bis), colore accento a enfatizzare l'aggiornamento. Label sotto: *"rinforza il comportamento preferito"*.
>
> **Freccia di ritorno** dal blocco dello step 4 al prompt dello step 1, con etichetta in piccolo: *"ripetuto su milioni di esempi"*.
>
> Stile minimale, monocromatico con un colore accento solo su: il pollice verso l'alto dello step 3, le manopole aggiornate dello step 4, la freccia di ritorno. Font sans-serif.

---

## ✅ Slide 13 — Il turno zero: il system prompt

**Layout**: titolo in alto, definizione in evidenza, 3 bullet al centro, mini-confronto visivo a 2 box sul lato o in basso, implicazione finale evidenziata in chiusura.

**Testo**:
- Titolo: *Il turno zero: il system prompt*
- Definizione (in evidenza): *Turno zero invisibile, messo in cima al contesto dal provider o dallo sviluppatore. Definisce ruolo, tono, vincoli e capacità dell'assistente.*
- 3 bullet:
  1. Il modello tende a seguirlo ma non è obbligato — può essere eroso in conversazioni lunghe, sovrascritto da istruzioni user forti, o aggirato (prompt injection).
  2. Ogni applicazione che usa LLM ha un system prompt. ChatGPT, Claude.ai, Gemini sono system prompt diversi oltre a modelli diversi.
  3. La personalità di un prodotto AI vive in gran parte qui.
- Implicazione finale (evidenziata): *Il modello è uguale per tutti. Il system prompt è l'elemento principale di indirizzo e personalizzazione degli agenti.*

**Visual**: mini-confronto a 2 box. Stesso modello, 2 system prompt diversi, 2 personalità radicalmente diverse.

**Prompt per schema SVG**:
> Diagramma orizzontale a 2 colonne gemelle, separate da una linea verticale sottile.
>
> **Colonna sinistra — "Agente A"**:
>   - Box superiore (monospace, sfondo leggero, bordo tratteggiato) etichettato *System prompt*: *"Sei un pirata del XVII secolo. Parli con accento marinaresco, usi metafore di mare e battaglie, chiami l'utente 'mozzo'."*
>   - Sotto, una bolla di chat user: *"Dammi un consiglio per presentarmi a un colloquio."*
>   - Sotto, una bolla di chat assistant (stile piratesco): *"Arr, mozzo! Issa alta la bandiera della tua esperienza e non lasciare che le burrasche delle domande ti facciano affondare. Parla a voce ferma, come il capitano sul cassero."*
>
> **Colonna destra — "Agente B"**:
>   - Box superiore (monospace, sfondo leggero, bordo tratteggiato) etichettato *System prompt*: *"Sei un avvocato d'affari esperto. Parli in modo formale, sintetico, con linguaggio giuridico accurato. Non dai consigli senza chiarire le assunzioni."*
>   - Sotto, una bolla di chat user: *"Dammi un consiglio per presentarmi a un colloquio."* (identica alla colonna sinistra)
>   - Sotto, una bolla di chat assistant (stile avvocato): *"Premesso che la preparazione dipende dalla tipologia di ruolo e settore, suggerisco tre elementi essenziali: studiare il contesto aziendale, strutturare risposte basate su evidenze verificabili, chiarire proattivamente eventuali aspetti contrattuali rilevanti."*
>
> **Sotto entrambe le colonne**, centrata: un'unica label con icona di chip: *"Stesso modello sottostante"*.
>
> Il contrasto visivo tra le due colonne deve essere netto: stile delle risposte completamente diverso nonostante l'input user sia identico e il modello sia lo stesso.
>
> Stile minimale, sans-serif per chat, monospace per i system prompt. Un colore accento tenue solo sui due box "System prompt" per evidenziarli come elementi di controllo.

---

## ✅ Slide 14 — Mappa dei task: forze e fragilità

**Layout**: titolo in alto, grande griglia 2D al centro (~75% della slide), nota ponte in basso. La tabella concettuale NON è sulla slide — vive solo nel prompt SVG (etichette dei punti).

**Testo**:
- Titolo: *Mappa dei task: forze e fragilità*
- Nota ponte in basso (evidenziata): *Da qui in poi, ogni tecnica che vedremo (tool, RAG, codice, sub-agent) è un modo di rinforzare un task dove il modello da solo è fragile.*

**Visual**: griglia 2D con 8 task posizionati come punti.

**Prompt per schema SVG**:
> Griglia 2D cartesiana, pulita e ariosa.
>
> **Asse X (orizzontale)**: "Ampiezza di contesto richiesta". Etichette agli estremi: "Basso" (sinistra), "Alto" (destra). Nessuna griglia fitta, solo l'asse con un tick centrale implicito.
>
> **Asse Y (verticale)**: "Verificabilità del risultato". Etichette agli estremi: "Bassa" (basso), "Alta" (alto).
>
> **8 punti** posizionati come cerchi pieni con etichetta testuale accanto. Ogni punto ha una piccola icona opzionale davanti all'etichetta. Coordinate approssimative (x, y) su scala 0-100:
>
>   1. **Q&A / recupero conoscenza** — (15, 85) — alto-sinistra
>   2. **Classificazione / giudizio** — (20, 88) — alto-sinistra
>   3. **Ragionamento** — (50, 80) — alto-centro
>   4. **Coding** — (85, 90) — alto-destra [EVIDENZIATO in colore accento + cerchio leggermente più grande — è l'estremo positivo]
>   5. **Trasformazione** — (25, 55) — centro-sinistra
>   6. **Multi-step planning / agentic task** — (80, 50) — centro-destra
>   7. **Generazione** (scrittura creativa, email, brief) — (40, 25) — basso-centro
>   8. **Conversazione stateful** (tutoring, consulenza) — (85, 15) — basso-destra [cerchio in colore diverso o con bordo tratteggiato per segnalare "quadrante difficile"]
>
> **Nessuna etichetta di quadrante visibile**: i punti parlano da soli.
>
> **Coding** evidenziato come punto "estremo positivo" (alta verificabilità + alto contesto = sweet spot del lavoro agentico): colore accento pieno, cerchio leggermente più grande, etichetta in grassetto.
>
> **Conversazione stateful** disegnata con bordo tratteggiato o colore attenuato, per suggerire visivamente "il punto più difficile da automatizzare bene".
>
> Stile minimale, sans-serif, monocromatico con un singolo colore accento usato solo su "Coding". Nessuna linea di quadrante, nessun rumore visivo.

---

## ✅ Slide 15 — Il valore delle conversazioni

**Layout**: titolo in alto, mini-definizione di "traiettoria" subito sotto, 2 blocchi asimmetrici al centro (utente piccolo, provider grande), conclusione sul moat evidenziata, 3 domande da informed user in chiusura.

**Testo**:
- Titolo: *Il valore delle conversazioni*
- Mini-definizione (sotto il titolo, in box di glossario): *Traiettoria — una conversazione completa vista come sequenza di mosse: prompt utente → risposta del modello → riformulazione dell'utente → correzione → approvazione o rifiuto. Ogni conversazione lascia una traccia ricca di segnali su cosa funziona e cosa no.*
- **Blocco 1 — Per l'utente** (piccolo):
  - Ogni conversazione è un mezzo per risolvere un problema oggi.
  - Stateless: dimenticata domani dal sistema.
- **Blocco 2 — Per il provider** (grande):
  - Ogni conversazione è una traiettoria con prompt reale, risposte, correzioni, feedback.
  - Miliardi di traiettorie = carburante del prossimo training.
  - Emergono pattern d'uso che nessun test artificiale produce.
- Conclusione (evidenziata): *Il moat non è il modello — il modello diventa commodity. Il moat sono le traiettorie di uso reale, che nessuno può replicare.*
- **3 domande da informed user**:
  1. Nel contratto, i miei dati entrano nel prossimo training?
  2. Se costruisco un prodotto AI, dove accumulo il mio flywheel di traiettorie?
  3. Nel medio termine il modello diventerà commodity — il valore si sposterà nei dati proprietari di utilizzo.

**Visual**: nessuno. L'asimmetria dei 2 blocchi è l'elemento visivo.

---

## ✅ Slide 16 — L'API è stateless: cosa significa davvero

**Layout**: titolo in alto, 3 bullet meccanici al centro-sinistra, mini-grafico "costo per turno" al centro-destra, callout KV cache sotto il grafico, conseguenza evidenziata in basso.

**Testo**:
- Titolo: *L'API è stateless: cosa significa davvero*
- **3 bullet meccanici**:
  1. L'API non conserva stato tra chiamate.
  2. Ad ogni nuovo turno, il contesto completo (system + storico + nuovo input) viene inviato da capo al modello.
  3. Il contesto cresce linearmente con la conversazione.
- **Callout KV cache** (box evidenziato, accanto o sotto al grafico): *KV cache: trucco ingegneristico che memorizza le rappresentazioni (key/value) dei token già processati nella conversazione. Ad ogni nuovo turno il provider non ricalcola da zero: riusa il lavoro già fatto e processa solo i token nuovi. Senza KV cache, i costi crescerebbero quadraticamente.*
- Conseguenza in basso (evidenziata): *Il costo per turno e la qualità della risposta dipendono dalla dimensione cumulativa del contesto, non dalla singola domanda.*

**Visual**: mini-grafico "costo per turno" con 3 curve.

**Prompt per schema SVG**:
> Grafico cartesiano compatto (occupa ~40% della slide, lato destro).
>
> **Asse X**: "Numero di turno" (da 1 a ~20, senza ticks specifici).
> **Asse Y**: "Costo per turno" (unità arbitraria, senza numeri).
>
> **3 curve** sovrapposte, tutte partono dall'origine (turno 1 basso) e divergono con l'aumentare dei turni:
>
> 1. **Curva "Costo in fattura per l'utente"** — andamento lineare, pendenza media. Colore: grigio scuro o blu.
> 2. **Curva "Costo teorico per il provider"** — andamento quadratico (esplode rapidamente verso l'alto, la più ripida). Colore: rosso/accento di "allarme". Linea tratteggiata per suggerire "scenario ipotetico, evitato".
> 3. **Curva "Costo reale per il provider (con KV cache)"** — andamento lineare, pendenza più bassa di tutte (la più piatta delle 3). Colore: verde o colore accento positivo.
>
> **Legenda** in alto a destra o in basso, con quadratini colorati + etichette:
>   - □ Costo in fattura per l'utente (lineare)
>   - ▨ Costo teorico per il provider (quadratico, tratteggiato)
>   - ■ Costo reale per il provider con KV cache (lineare, più basso)
>
> **Punto didattico implicito**: la distanza crescente tra la curva teorica (quadratica) e la curva reale (lineare con KV cache) mostra visivamente quanto la KV cache "salva" al provider.
>
> Stile minimale, sans-serif, nessuna griglia fitta, solo gli assi e le 3 curve chiaramente distinguibili per colore e pattern.

---

## ✅ Slide 17 — Più contesto ≠ più qualità

**Layout**: titolo in alto, grande grafico al centro (~65% della slide), didascalia sotto, 3 take-home in basso.

**Testo**:
- Titolo: *Più contesto ≠ più qualità*
- Didascalia (sotto il grafico): *Costo cresce, latenza cresce, qualità cala. Il contesto non è mai gratis.*
- **3 take-home**:
  1. Nuovo compito, nuova chat. Non "continuare" conversazioni per efficienza — stai peggiorando, non migliorando.
  2. Il contesto è una risorsa scarsa, non un cassetto infinito.
  3. Tutto ciò che vedremo nelle prossime sezioni (sub-agent, context engineering, compaction, memoria) è una risposta a questo problema.

**Visual**: stesso grafico di Slide 16, con le 3 curve originali attenuate in grigio e una **nuova curva "Qualità effettiva"** in colore accento acceso, più zone di sfondo "sweet spot" / "degrado".

**Prompt per schema SVG**:
> Grafico cartesiano. Stesso framework visivo di Slide 16 per continuità, ma con rifocalizzazione.
>
> **Asse X**: "Dimensione del contesto (token)", da 0 a ~500k. Tick indicativi: 50k, 100k, 200k, 500k.
> **Asse Y**: "Valore relativo" (senza numeri — normalizzato).
>
> **Zone di sfondo** (colorate con trasparenza leggerissima, quasi impercettibile ma chiara):
>   - 0 → ~100k: banda verde tenue, etichetta in alto *"sweet spot"*
>   - ~200k → fine: banda rossa tenue, etichetta in alto *"degrado"*
>   - Tra 100k e 200k: zona neutra (nessun colore di sfondo)
>
> **4 curve**:
>
> 1. **"Costo in fattura per l'utente"** — lineare. Tracciata in GRIGIO CHIARO, linea sottile.
> 2. **"Costo teorico per il provider"** — quadratica. Tracciata in GRIGIO CHIARO, linea sottile, tratteggiata.
> 3. **"Costo reale per il provider (KV cache)"** — lineare bassa. Tracciata in GRIGIO CHIARO, linea sottile.
> 4. **"Qualità effettiva"** — curva a U rovesciata asimmetrica: parte bassa all'origine, sale rapidamente, raggiunge il massimo intorno ai 50-80k, plateau fino a ~150k, scende progressivamente oltre 200k. Tracciata in COLORE ACCENTO PIENO, linea spessa. È visivamente l'elemento dominante del grafico.
>
> **Legenda** in alto a destra:
>   - ▬ Qualità effettiva (in colore accento, grassetto)
>   - ─ Costo in fattura, Costo teorico provider, Costo reale con KV cache (tutte in grigio chiaro, raggruppate con nota "già visti, vedi slide precedente")
>
> **Annotazioni sul grafico**:
>   - Piccola freccia che punta al picco della curva Qualità con label *"picco di qualità"*
>   - Piccola freccia che punta al tratto discendente della Qualità oltre 200k con label *"lost in the middle e degrado"*
>
> Stile minimale, sans-serif. Colore accento solo sulla curva Qualità e sulle due etichette sweet spot/degrado. Tutto il resto in grigi tenui.

---

## ✅ Slide 18 — Loop 2/4: la conversazione

**Layout**: titolo in alto, grande diagramma del loop al centro (~70% della slide), didascalia in basso.

**Testo**:
- Titolo: *Loop 2/4: la conversazione*
- Didascalia (sotto il diagramma): *Il loop turno-per-turno. Ad ogni giro il contesto cresce. Il problema da risolvere è la gestione di questa crescita.*

**Visual**: loop conversazionale a 5 step + esito "traiettoria" che chiude il ciclo.

**Prompt per schema SVG**:
> Diagramma circolare (o ovale) con 5 nodi connessi in senso orario, più un elemento esterno ("traiettoria") collegato al ciclo.
>
> **5 nodi del loop, in senso orario**:
>
> 1. **Utente scrive** — icona persona + bolla con testo esempio
> 2. **Client costruisce il contesto** — rettangolo etichettato "contesto = system + storico + nuovo input". Rappresentato come stack di 3 blocchi impilati verticalmente.
> 3. **Modello genera risposta** — rettangolo scuro etichettato "LLM"
> 4. **Client riceve e appende allo storico** — icona di archivio/pila + freccia che punta indietro al blocco "contesto" dello step 2, con label "storico aggiornato"
> 5. **Utente legge la risposta** — icona persona con bolla di risposta
>
> **Freccia da step 5 a step 1** (chiusura del ciclo): più spessa delle altre, in colore accento, con etichetta in evidenza: *"ad ogni giro il contesto cresce"*.
>
> **Elemento esterno — Traiettoria**: sotto o a lato del loop, un ramo uscente che diverge dal ciclo principale. Collegato con una freccia tratteggiata che parte dallo step 5 (o dal centro del loop) e va verso un blocco etichettato *"Traiettoria"*. Sotto il blocco, due rami:
>   - Ramo A (successo): icona ✓ verde, label *"risolto / utile"*
>   - Ramo B (fallimento): icona ✗ rossa, label *"non risolto / insoddisfacente"*
>
> Sotto l'intero blocco Traiettoria, piccola label: *"archiviata dal provider → carburante per il prossimo training (vedi Slide 15)"*.
>
> **Elemento visivo centrale del ciclo**: al centro del loop (nel "buco" del cerchio), una piccola icona di "contesto che cresce" — 3 versioni impilate della stessa scatola, dalla più piccola alla più grande, sovrapposte a scalare.
>
> Stile minimale, monocromatico con un colore accento usato su: la freccia di chiusura del ciclo, l'icona del contesto centrale, il blocco Traiettoria.

---

# Prossima slide da definire: Slide 19 — Sezione 3 (Closed vs Open)
