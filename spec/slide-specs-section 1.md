# Specifica slide consolidate — Lezione MBA Politecnico di Milano
## "Agents in action" — Francesco Gianferrari Pini, Quantyca

**Stato**: slide 1–10 consolidate. Sezione 2 (slide 11–20) implementata — vedi `spec/slide-specs-section-2.md`.

### Struttura modulare

Ogni slide è un file HTML separato in `lezione-mba/slides/`. Il file `presentation.html` li carica dinamicamente via fetch in ordine.

| File | Slide |
|------|-------|
| `slides/slide1-title.html` | Slide 1 — Apertura lezione |
| `slides/slide-div-sec1.html` | Separatore — Sezione 1: Capire l'LLM |
| `slides/slide2-llm-cuore.html` | Slide 2 — LLM: il cuore degli agenti |
| `slides/slide3-training-loop.html` | Slide 3 — Come si addestra un LLM |
| `slides/slide4-pretraining.html` | Slide 4 — Il pre-training di un LLM |
| `slides/slide5-compression.html` | Slide 5 — LLM: Compression through Abstraction |
| `slides/slide6-conoscenza.html` | Slide 6 — La portata della conoscenza |
| `slides/slide7-conseguenze.html` | Slide 7 — Conseguenze della compressione |
| `slides/slide8-genera-testo.html` | Slide 8 — Loop 1/4: Come l'LLM genera testo |
| `slides/slide9-pratica.html` | Slide 9 — Cosa significa in pratica? |
| `slides/slide10-context-window.html` | Slide 10 — Il limite della context window |

Ogni file contiene un singolo `<section>` con tutto il contenuto della slide. Per aggiungere una nuova slide: creare il file in `slides/`, aggiungerlo all'array `slideFiles` in `presentation.html`, e documentarlo qui.

---

## ✅ Slide 1 — Apertura lezione

**Layout**: titolo centrale grande, attribuzione in piccolo sotto il titolo, mappa delle 7 tappe in basso con icone.

**Testo**:
- Titolo: *Agents in action*
- Attribuzione (piccola): *Francesco Gianferrari Pini — Quantyca*
- Mappa 7 tappe (piccole, in basso, con icona sopra l'etichetta):
  1. Capire l'LLM — icona chip/cervello stilizzato
  2. Conversare — icona bolla di chat
  3. Scegliere il modello — icona lucchetto vs lucchetto aperto
  4. Agire — icona chiave inglese
  5. Estendere l'agente — icona set di strumenti / griglia
  6. Programmare — icona parentesi graffe `{ }`
  7. Progettare il contesto — icona blocchi impilati / layer

**Visual**: nessun diagramma aggiuntivo; la mappa icone-tappe È l'elemento visivo.

---

## ✅ Slide 2 — LLM: il cuore degli agenti

**Layout**: titolo in alto, definizione centrale evidenziata, 3 bullet estesi sotto, schema visivo in basso (o a destra della definizione).

**Testo**:
- Titolo: *LLM: il cuore degli agenti*
- Definizione centrale (in evidenza): *Un LLM è una funzione matematica che, data una sequenza di token, produce una distribuzione di probabilità sul prossimo token.*
- 3 bullet estesi:
  1. **Input**: una sequenza di token, che sono le unità in cui l'LLM "vede" il testo — approssimativamente parole o frammenti di parole.
  2. **Output**: non una parola, ma una distribuzione di probabilità che assegna un valore a ogni token del vocabolario (decine di migliaia di possibilità).
  3. **Nessun concetto di "conversazione", "risposta" o "istruzione"**: a questo livello l'LLM non sa di parlare con qualcuno. È una funzione che completa testo plausibile. L'assistente conversazionale che conosciamo è una costruzione che aggiungeremo nelle prossime slide.

**Visual**: uno schema centrale con il blocco "LLM" al centro. Da sinistra entrano 3 input diversi (frasi incomplete), da destra escono 3 distribuzioni di probabilità (mini grafici a barre).

**Prompt per schema SVG**:
> Diagramma orizzontale a 3 livelli paralleli, tutti che convergono su un unico blocco centrale "LLM".
> A sinistra, tre rettangoli input impilati verticalmente:
>   - "Il gatto è sul…"
>   - "La capitale di Francia è…"
>   - "Buongiorno, come…"
> Ogni rettangolo ha una freccia che punta al blocco centrale scuro "LLM (funzione)".
> Dal blocco centrale escono 3 frecce verso destra, ognuna verso un mini grafico a barre verticali etichettato:
>   - Output 1: tavolo (0.35) · divano (0.20) · letto (0.15) · tetto (0.10) · altro (0.20)
>   - Output 2: Parigi (0.78) · Lione (0.08) · Marsiglia (0.05) · Francia (0.04) · altro (0.05)
>   - Output 3: stai (0.40) · va (0.35) · sta (0.12) · ti (0.08) · altro (0.05)
> Stile minimale, monocromatico con un colore accento per il blocco LLM e le barre più alte delle distribuzioni. Font sans-serif.

---

## ✅ Slide 3 — Come si addestra un LLM

**Layout**: titolo in alto, grande SVG centrale che occupa ~80% della slide, didascalia di 1-2 righe in basso.

**Testo**:
- Titolo: *Come si addestra un LLM*
- Didascalia in basso: *Miliardi di parametri partono casuali. Trilioni di micro-aggiustamenti li portano a predire il prossimo token in modo sempre più accurato.*

**Visual**: diagramma ibrido — ciclo narrativo a 5 step + mini grafico di loss che scende.

**Prompt per schema SVG**:
> Diagramma a due livelli che coesistono sulla stessa slide.
>
> **Livello superiore — ciclo narrativo a 5 step in sequenza orizzontale** (frecce che collegano uno step al successivo, con freccia di ritorno dall'ultimo al primo per indicare ripetizione):
>
> Step 1 — "Frase dal corpus": rettangolo con testo esempio "Il gatto è sul tavolo"
> Step 2 — "Maschera l'ultima parola": stesso rettangolo con "Il gatto è sul ___" (la parola "tavolo" coperta/sfumata)
> Step 3 — "Il modello predice": rettangolo scuro centrale "LLM" con all'interno rappresentazione di tante piccole manopole/dial (griglia 6×4 di cerchietti), da cui esce una mini distribuzione di probabilità: "divano 0.28 / tavolo 0.22 / letto 0.18 / ..."
> Step 4 — "Confronta con la verità": icona bilancia o simbolo "=?", con etichetta "errore = distanza tra predizione e parola reale"
> Step 5 — "Aggiorna i parametri": freccia che torna al blocco LLM dello step 3, con le manopole leggermente ruotate (colore accento che evidenzia l'aggiornamento). Label piccola accanto alla freccia: "backpropagation + gradient descent"
>
> Una freccia circolare grande sotto tutti gli step con etichetta "ripetuto trilioni di volte".
>
> **Livello inferiore — mini grafico di loss** (in basso a destra, compatto, occupa ~25% della larghezza):
> Asse X: "step di training" (da 0 a N, numero non specificato)
> Asse Y: "errore di predizione (loss)"
> Curva decrescente che parte alta, scende ripidamente all'inizio, poi si appiattisce asintoticamente verso un plateau basso ma non zero.
> Etichetta piccola: "la loss scende man mano che i parametri si aggiustano"
>
> Stile minimale, monocromatico con un colore accento usato SOLO su: le manopole aggiornate nello step 5, la curva di loss, e la freccia "ripetuto trilioni di volte". Tutto il resto in grigio scuro / nero. Font sans-serif.

---

## ✅ Slide 4 — Il pre-training di un LLM

**Layout**: titolo in alto, sottotitolo, 3 bullet di meccanica, nota in basso. Infografica di scala a 5 livelli occupa ~50% della slide (a destra o in basso).

**Testo**:
- Titolo: *Il pre-training di un LLM*
- Sottotitolo: *Come nasce questa funzione*
- 3 bullet:
  1. **Pre-training**: addestramento su enormi corpus di testo (web, libri, codice).
  2. **Obiettivo**: prevedere il prossimo token a partire dai precedenti.
  3. **Scala tipica (modelli di frontiera 2026)**: 25–50 trilioni di token in input, 400 miliardi – 1 trilione+ di parametri nel modello.
- Nota in basso: *Alla fine del training, il modello è in grado di completare ogni frase attingendo ad ogni elemento di conoscenza, ma non necessariamente è "utile" a sostenere una conversazione o risolvere un problema.*

**Visual**: infografica comparativa di scala a 5 livelli, barre su scala logaritmica.

**Prompt per infografica SVG**:
> Infografica a 5 righe orizzontali impilate verticalmente. Ogni riga ha: icona a sinistra, etichetta testuale, barra orizzontale in scala logaritmica, numero a destra.
> Asse comune: scala logaritmica delle parole/token (da 10^8 a 10^14).
> Righe (dall'alto in basso):
>   1. [icona persona che legge] — "Un lettore medio, nell'intera vita" — barra cortissima — "~200 milioni di parole"
>   2. [icona enciclopedia] — "Wikipedia, tutte le lingue" — barra più lunga — "~10 miliardi di parole"
>   3. [icona edificio biblioteca] — "Grande biblioteca universitaria (20M volumi)" — barra ancora più lunga — "~1 trilione di parole"
>   4. [icona chip/cervello, EVIDENZIATA in colore accento] — "Training di un LLM di frontiera (2026)" — barra molto più lunga — "~25-50 trilioni di token"
>   5. [icona mondo/web in grigio] — "Tutto il testo digitale di qualità sul web" — barra massima — "~50-100 trilioni di token (limite che ci stiamo avvicinando)"
> La riga 4 è il focus visivo (colore accento); la riga 5 è disegnata in grigio con etichetta "frontiera dei dati disponibili".
> Stile minimale, sans-serif, monocromatico con un colore accento solo sulla riga 4.

---

## ✅ Slide 5 — LLM: Compression through Abstraction

**Layout**: titolo in alto, concetto centrale in evidenza, 3 bullet sotto, citazione in basso in stile "pull quote". Visual occupa il lato destro o la parte inferiore.

**Testo**:
- Titolo: *LLM: Compression through Abstraction*
- Concetto centrale (in evidenza): *Per far stare trilioni di token in miliardi di parametri, il modello è costretto a costruire rappresentazioni astratte — non memorizza, modella.*
- 3 bullet:
  1. Non c'è spazio per memorizzare letteralmente il training set.
  2. Il modello "impara" concetti, relazioni, regolarità del mondo.
  3. Le capacità emergenti (ragionamento, analogia, transfer tra domini) sono sottoprodotto della compressione, non funzionalità programmate.
- Citazione in basso (pull quote, Ted Chiang — New Yorker): *"ChatGPT è un JPEG sfocato del web, che, per comprimere, ha dovuto capire."*

**Visual**: diagramma combinato — imbuto di compressione + metafora JPEG.

**Prompt per schema SVG**:
> Diagramma verticale a due livelli con metafora visiva integrata.
>
> **Parte superiore — la "materia prima"**: area rettangolare larga riempita da tanti piccoli pittogrammi eterogenei disposti densamente (icone di documenti, libri, pagine web, snippet di codice, articoli — almeno 30-40 elementi piccoli in griglia disordinata). Etichetta laterale: "Trilioni di token · web, libri, codice".
>
> **Transizione al centro — imbuto di compressione**: grande forma a imbuto che va dall'area superiore larga a un'area inferiore stretta. Sull'imbuto, in verticale, label piccola: "compressione per astrazione".
>
> **Parte inferiore — il "modello"**: area rettangolare più piccola, divisa visivamente in due sotto-zone affiancate:
>   - A sinistra: rete di nodi astratti connessi da linee — pochi nodi etichettati con concetti rappresentativi: "sintassi", "causa-effetto", "temporalità", "oggetti e proprietà", "analogia". Non pittogrammi concreti, ma nodi concettuali.
>   - A destra, come "echo visivo" della citazione: una piccola immagine pixelata/JPEG compressa — un riquadro con gradienti sfocati che suggerisce un'immagine del mondo (paesaggio o volto stilizzato) riconoscibile ma sfumata. Etichetta sotto: "riconoscibile, non fedele".
>
> **Punto visivo centrale**: gli elementi inferiori NON sono una versione "rimpicciolita" di quelli superiori — sono qualitativamente diversi. La compressione è concettuale, non letterale.
>
> Stile minimale, sans-serif, monocromatico con un colore accento solo sull'imbuto e sulla rete di nodi astratti.

---

## ✅ Slide 6 — La portata della conoscenza

**Layout**: titolo in alto, sottotitolo, 2 blocchi paralleli (sinistra/destra) che occupano la parte centrale, nota conclusiva in basso.

**Testo**:
- Titolo: *La portata della conoscenza*
- Sottotitolo: *Una conseguenza del training su scala*
- **Blocco sinistro — Ampiezza**: L'LLM ha "letto" ordini di grandezza più testo di qualunque singolo essere umano.
- **Blocco destro — Implicazione**: Su qualsiasi dominio di conoscenza pubblica (medicina, diritto, codice, marketing, ingegneria) la baseline informativa è superiore a quella di un laureato medio nel campo.
- Nota in basso: *Indipendentemente dall'ambito di utilizzo, un modello moderno sfrutta una mole enorme di informazioni (non sempre di altissima qualità o veridicità) per dare una risposta. È certamente già una capacità "super-umana", e nasce dalla capacità di comprimere attraverso una astrazione.*

**Visual**: nessuno. La struttura a 2 blocchi è l'elemento visivo.

---

## ✅ Slide 7 — Conseguenze della compressione

**Layout**: titolo in alto, 2 colonne contrastive al centro (sinistra/destra), regola pratica in basso come blocco evidenziato.

**Testo**:
- Titolo: *Conseguenze della compressione*
- **Colonna sinistra — Dove è forte**:
  - Framing concettuali su qualunque dominio
  - Ragionamento e analogia
  - Trasformazione di testo (traduzione, sintesi, riformattazione)
- **Colonna destra — Dove serve cautela**:
  - Fatti puntuali (date, numeri, citazioni letterali)
  - Conoscenza post-cutoff
  - Dettagli tecnici su nicchie poco rappresentate
  - Dati proprietari non nel training
  - Calcoli numerici precisi e passaggi matematici lunghi
- Regola pratica in basso (evidenziata): *Fidati del framing, verifica i fatti. Le allucinazioni non sono un bug morale del modello — sono il comportamento strutturale di un compressore lossy a cui chiedi di ricostruire ciò che non ha memorizzato bene.*

**Visual**: nessuno. Il contrasto tra le 2 colonne è l'elemento visivo.

---

## ✅ Slide 8 — Loop 1/4: Come l'LLM genera testo

**Layout**: titolo in alto, grande visual narrativo al centro (~70% della slide), didascalia sotto.

**Testo**:
- Titolo: *Loop 1/4: Come l'LLM genera testo*
- Didascalia (sotto il diagramma): *Il modello non pianifica una risposta. Produce un token alla volta. Ogni nuovo token viene appeso al contesto e il contesto completo viene rivalutato per produrre il successivo.*

**Visual**: sequenza narrativa che mostra il contesto che cresce token dopo token, con freccia laterale che chiarisce che ogni riga è una chiamata indipendente al modello. Ogni riga è divisa visivamente in due zone: il context (sfondo scuro, testo grigio chiaro) e il token appena generato (sfondo accento semitrasparente, testo accento bold). Una legenda in alto spiega i due colori.

**Prompt per schema SVG**:
> Visual narrativo verticale che mostra l'evoluzione del contesto token dopo token.
>
> **Legenda in alto**: due riquadri con etichetta — "context (input al modello)" (sfondo scuro) e "token generato (output)" (sfondo accento).
>
> **Colonna centrale** — una pila verticale di 7-8 righe, ognuna è un "contesto" a un certo istante. Ogni riga è composta da due rettangoli adiacenti: uno scuro per il context e uno con sfondo accento semitrasparente per il token appena generato. I token del context sono in grigio chiaro, il nuovo token è in colore accento bold.
>
> Sequenza delle righe (dall'alto verso il basso):
>   1. `Il`                          (token nuovo: "Il")
>   2. `Il gatto`                    (token nuovo: "gatto")
>   3. `Il gatto è`                  (token nuovo: "è")
>   4. `Il gatto è sul`              (token nuovo: "sul")
>   5. `Il gatto è sul tavolo`       (token nuovo: "tavolo")
>   6. `Il gatto è sul tavolo e`     (token nuovo: "e")
>   7. `Il gatto è sul tavolo e dorme` (token nuovo: "dorme")
>   8. `Il gatto è sul tavolo e dorme.` (token nuovo: "." — con piccolo simbolo di STOP accanto)
>
> Tra ogni riga e la successiva, una piccola freccia verticale verso il basso.
>
> **A destra della pila** — diagramma del loop con 4 passi numerati (①–④):
> - ① box "contesto" → ② box "LLM" → ③ box "token" → ④ freccia tratteggiata accent che torna a ① ("appeso al contesto")
> - Titolo sopra: *"ogni riga = una chiamata al modello:"*
> - Footer sotto: *"↻ si ripete fino al token di STOP"*
>
> **A sinistra della pila** — etichetta verticale più piccola con una graffa che abbraccia tutte le righe: *"il contesto cresce di un token per volta"*.
>
> **In fondo** — sotto l'ultima riga, piccolo badge/etichetta: *"token di STOP → fine generazione"*.
>
> Stile minimale, monocromatico con un solo colore accento (usato per: l'ultimo token di ogni riga, il diagramma loop a destra, il badge STOP). Font sans-serif, monospace per il testo nelle righe del contesto per enfatizzare la natura "token".

---

## ✅ Slide 9 — Cosa significa in pratica?

**Layout**: titolo in alto, 3 bullet al centro, seed narrativo in chiusura evidenziato.

**Testo**:
- Titolo: *Cosa significa in pratica?*
- 3 bullet:
  1. **Stesso prompt ≠ stessa risposta**: il sampling è probabilistico. Il non-determinismo è strutturale, non un bug.
  2. **Lo streaming non è UX**: le parole che compaiono una per una riflettono la meccanica reale. Il modello genera mentre l'utente legge.
  3. **Non c'è pianificazione globale**: il modello non "sa dove sta andando" prima di iniziare. Ogni token è locale.
- Seed narrativo (in chiusura, evidenziato): *Questo è il primo mattoncino. I prossimi tre loop — conversazione, tool, codice — lo avvolgono uno sull'altro.*

**Visual**: nessuno.

---

## ✅ Slide 10 — Il limite della context window

**Layout**: titolo in alto, blocco analogia esteso in apertura (prosa narrativa), 2 bullet di sostanza sotto.

**Testo**:
- Titolo: *Il limite della context window*
- Blocco analogia (apertura, in prosa): *Il protagonista di Memento. Un uomo colpito da amnesia anterograda — ricorda la sua vita prima dell'incidente, ma ogni nuovo ricordo svanisce in pochi minuti. Sopravvive scrivendo tutto su Polaroid e tatuaggi: tutto ciò che gli serve sapere ora deve essere fisicamente davanti ai suoi occhi, ora. Un LLM funziona allo stesso modo. Il training è la "vita prima": conoscenza enorme, ma congelata. Tutto il resto — la conversazione in corso, i documenti caricati, i risultati dei tool — esiste per il modello solo se è dentro la finestra di contesto in questo preciso istante. Niente viene automaticamente ricordato tra una chiamata e l'altra.*
- 2 bullet di sostanza:
  1. **Costo**: il meccanismo di attention è O(n²) sulla lunghezza del contesto. Raddoppiare il contesto più che raddoppia il costo di calcolo.
  2. **Qualità**: anche quando "ci sta", il modello non usa bene tutto il contesto. Tende a ricordare meglio inizio e fine, peggio il centro — fenomeno noto come *lost in the middle*.

**Visual**: nessuno.


