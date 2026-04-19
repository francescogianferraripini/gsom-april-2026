# Specifica Slide — Sezione 6: L'agente che scrive ed esegue codice

Stato: consolidato per rendering. Testi definitivi, prompt SVG pronti.

Slide incluse: 38–43.

---

## Slide 38 — Apertura Sezione 6

**Layout**: titolo + frame + anticipazione diretta.

**Testo**
- **Titolo**: *L'agente che scrive ed esegue codice*
- **Frame**: *Il codice è il tool di ultima istanza. Non sblocca una capacità specifica — sblocca capacità arbitrarie senza doverle pre-definire.*
- **Anticipazione**: *Due modi di usare il codice in un agente: come tool interno, come prodotto finale. Condizionano tutto il resto.*

**Visual**: nessuno.

**Note docente**: richiamo a bash (Slide 36) a voce, non in slide.

---

## Slide 39 — Code as tool vs code as product

**Layout**: titolo + tabella a 2 righe + riga esempi + take-home.

**Testo**
- **Titolo**: *Code as tool vs code as product*
- **Tabella**:

| | Code as tool | Code as product |
|---|---|---|
| **Cosa fa** | Scrive codice per risolvere internamente un task; il codice non è il deliverable | Scrive software come deliverable: è il risultato del lavoro |
| **Ciclo di vita del codice** | Usa-e-getta: eseguito una volta, spesso invisibile all'utente, non salvato | Persistente: versionato, committato, mantenuto nel tempo |

- **Riga esempi (sotto la tabella)**: *Esempi — code as tool: Claude for PowerPoint. Code as product: Claude Code, Cursor, GitHub Copilot.*
- **Take-home**: *Quando un fornitore dice "la nostra AI scrive codice", chiedere quale dei due. Sono due mondi con beneficiari, rischi e metriche di valore diversi.*

**Visual**: la tabella.

---

## Slide 40 — Code as tool — il pattern operativo

**Layout**: titolo + esempio in scatola + SVG flow a 6 step + 2 bullet.

**Testo**
- **Titolo**: *Code as tool — il pattern operativo*
- **Esempio (scatola evidenziata in alto)**: User: *"Qual è stato il fatturato medio per trimestre nel 2023?"*
- **Bullet (sotto il visual)**:
  - L'utente vede la risposta, non il codice. Il codice è plumbing interno.
  - Un LLM "a mano" sbaglia la media di 50 numeri. Con Python la calcola esatta.

**Visual — Prompt SVG**
> Flow orizzontale a 6 step connessi da frecce. Step 1: "Riceve task". Step 2: "Decide che serve codice". Step 3: "Scrive script (Python/SQL)". Step 4: "Esegue in sandbox". Step 5: "Legge output". Step 6: "Risponde in linguaggio naturale". Gli step 2–5 sono racchiusi in un riquadro tratteggiato con etichetta "invisibile all'utente"; step 1 e 6 restano fuori dal riquadro, a rappresentare l'interfaccia utente visibile. Stile minimale, monocromatico con un colore accento.

---

## Slide 41 — Code as product — coding agent e affidabilità

**Layout**: titolo + riga prodotti in cima + blocco "Scala" + blocco "TDD" + chiusura + SVG.

**Testo**
- **Titolo**: *Code as product — coding agent e affidabilità*
- **Riga prodotti (in cima)**: *Claude Code · Cursor · GitHub Copilot*
- **Blocco "Scala"**: *Stesso pattern del code as tool (scrivi-esegui-verifica), moltiplicato per un progetto reale: molti file, dipendenze, test suite, git, pull request. Rientrano in gioco sub-agent (esplorare codebase) e skill (codificare convenzioni di progetto).*
- **Blocco "TDD come meccanismo di affidabilità"** (3 bullet):
  - Si specifica il comportamento atteso come test *prima* di far generare il codice.
  - Il test è **contratto**: l'agente sa quando ha finito.
  - Il test è **feedback loop deterministico**: l'agente sa se è sulla strada giusta.
- **Chiusura**: *Il ruolo umano si sposta su definizione del contratto e supervisione.*

**Visual — Prompt SVG**
> Diagramma orizzontale a 3 zone collegate da frecce.
> Zona 1 (sinistra): icona stilizzata di persona, freccia verso rettangolo "Test / spec". Label sotto: "Umano — definisce il contratto".
> Zona 2 (centro): icona agente che riceve input "Test / spec" (freccia dalla zona 1) e produce rettangolo "Codice". Label sotto: "Agente — scrive per soddisfare il contratto".
> Zona 3 (destra): icona "Test runner" che riceve sia Test (da zona 1) sia Codice (da zona 2). Due esiti: Pass (freccia verso destra → done) e Fail (freccia di ritorno all'Agente in zona 2, loop). Label sotto: "Test runner — verifica deterministica".
> Il loop fail → agente in colore accento per evidenziare l'iterazione.
> Stile minimale monocromatico con un colore accento.

---

## Slide 42 — Loop 4/4: con verifica deterministica

**Layout**: titolo + sottotitolo piccolo + SVG + 2 blocchi testuali.

**Testo**
- **Titolo**: *Loop 4/4: con verifica deterministica*
- **Sottotitolo (piccolo, in alto)**: *1° atomico (token) · 2° conversazionale (turno) · 3° con tool (azione) · 4° con codice (verifica)*
- **Blocchi (sotto il visual)**:
  - **A runtime** — *L'agente si corregge da solo. L'output del test rientra nel contesto come segnale netto: più tentativi, convergenza al codice che funziona.*
  - **In training** — *Lo stesso loop è il cuore del RL sul codice. Il provider fa generare codice su milioni di task con test, esegue, usa pass/fail come reward. Segnale netto = riaddestramento efficace. Gli LLM migliorano nel codice più rapidamente che in domini con feedback ambiguo.*

**Visual — Prompt SVG**
> Diagramma circolare in senso orario con 4 nodi: (1) "Task / intenzione" → (2) "Scrivi codice" → (3) "Esegui in sandbox" → (4) "Verifica (test passati? output corretto?)" → torna a (2) se fail, esce se pass. La freccia di ritorno da (4) a (2) è etichettata "feedback deterministico" in colore accento. Il nodo (4) ha due uscite esplicite: ramo "fail" (torna a 2) e "pass" (end). Stile minimale, cerchio chiuso — visivamente diverso dal flusso lineare con biforcazione della Slide 41.

---

## Slide 43 — La verificabilità come predittore di automazione

**Layout**: titolo + frase ponte + regola evidenziata + tabella contrastiva (2 colonne con colore) + caveat.

**Testo**
- **Titolo**: *La verificabilità come predittore di automazione*
- **Frase ponte (sotto il titolo)**: *Abbiamo visto che nel codice l'AI migliora rapidamente perché il feedback è netto. Generalizziamo.*
- **Regola (in evidenza, box o corsivo forte)**: *Se una professione intellettuale ha output immediatamente e binariamente verificabile, è a pressione di automazione elevata. Se il successo richiede giudizio qualitativo, negoziazione, contesto sociale, la pressione è più bassa — almeno per ora.*
- **Tabella contrastiva** (colonna sinistra in colore accento, colonna destra in neutro):

| Alta verificabilità → pressione alta | Bassa verificabilità → pressione bassa |
|---|---|
| Scrittura di codice con test | Strategia aziendale |
| Debugging | Negoziazione |
| Ottimizzazione logistica (routing, scheduling) | Leadership |
| Dimostrazione matematica in sistema formale | Vendita consulenziale complessa |
| Calcolo strutturale e simulazione fisica | Diagnosi medica in casi ambigui |
| Riconciliazione contabile | Decisioni etiche |

- **Caveat (riga finale)**: *Verificabilità non è sostituibilità totale. Resta il ruolo umano di definire il contratto, gestire casi fuori pattern, rispondere delle conseguenze. Il pattern sposta il lavoro, non sempre lo cancella.*

**Visual**: la tabella contrastiva colorata.

---

## Riepilogo Sezione 6

| Slide | Titolo | Visual | File |
|---|---|---|---|
| 38 | L'agente che scrive ed esegue codice | — | `slide40-apertura-sec6.html` |
| 39 | Code as tool vs code as product | Tabella 2 righe | `slide41-code-tool-vs-product.html` |
| 40 | Code as tool — il pattern operativo | SVG: flow a 6 step (step 2–5 racchiusi in "invisibile all'utente") | `slide42-code-as-tool-pattern.html` + `svg/slide42-code-as-tool-flow.svg` |
| 41 | Code as product — coding agent e affidabilità | SVG: contratto umano-agente via test | `slide43-code-as-product.html` + `svg/slide43-code-as-product.svg` |
| 42 | Loop 4/4: con verifica deterministica | SVG: loop circolare a 4 nodi | `slide44-quarto-loop.html` + `svg/slide44-quarto-loop.svg` |
| 43 | La verificabilità come predittore di automazione | Tabella contrastiva colorata | `slide45-verificabilita-automazione.html` |

Divider di sezione (transizione con sfondo scuro, non numerato nel brief): `slide-div-sec6.html`.

Totale: 6 slide + 1 divider. 3 SVG prodotti. 2 tabelle.
