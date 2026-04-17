# Specifica Sezione 4 — Tool calling (v2)
## Lezione MBA Politecnico di Milano — "Da cosa sono fatti gli agenti AI"
### Francesco Gianferrari Pini, Quantyca

**Stato**: slide 21–30 consolidate (v2, revisione completa).
**Filo narrativo della sezione**: esempio CRM (customer service) come continuità tra Slide 22 → 25.
**Prossima slide da definire**: Slide 31 (Sezione 5 — Tipi di tool).

---

## ✅ Slide 21 — Apertura Sezione 4

**Layout**: titolo grande centrato, 2 sottotitoli sotto, nessun visual.

**Testo**:
- Titolo: *Dall'agente che parla all'agente che agisce*
- Sottotitolo 1: *Fino a qui, un modello che genera testo. Da qui, un modello che decide quali azioni intraprendere nel mondo.*
- Sottotitolo 2: *Distinzione fondamentale: il modello non esegue. Emette richieste strutturate di esecuzione. L'esecuzione la fa il software che lo circonda — l'harness.*

**Note di design**: prima occorrenza del termine "harness" — verrà definito formalmente in Slide 45. Nessun visual.

---

## ✅ Slide 22 — Tool calling: l'intuizione

**Layout**: titolo in alto, mini-chat centrata nella slide (~50% dell'area), chiusura discorsiva in basso.

**Testo**:
- Titolo: *Un esempio*
- Mini-chat (bolle stile messenger, con piccola icona ingranaggio ⚙ accanto alla bolla dell'assistant):
  - User: *"Qual è lo stato dell'ordine #A-7842 del cliente Rossi SpA?"*
  - Assistant: *"L'ordine #A-7842 (Rossi SpA) è in spedizione dal 12 aprile, consegna prevista il 16 aprile. Tracking DHL 1234567890."*
- Chiusura discorsiva: *Una risposta precisa, specifica, verificabile. Eppure questi dati non esistono nel training del modello — nessun ordine, nessun cliente, nessun sistema gestionale aziendale fa parte di ciò su cui è stato addestrato. Il modello non può saperlo da solo. Allora come ha fatto?*

**Visual**: bolle chat semplici, stile messenger. L'icona ingranaggio accanto alla risposta dell'assistant è il seme visivo della curiosità che si scioglie in Slide 23. La domanda finale è lasciata sospesa.

---

## ✅ Slide 23 — Tool calling: la meccanica

**Layout**: titolo in alto, diagramma a 4 attori (~60% della slide), testo discorsivo in basso.

**Testo**:
- Titolo: *La meccanica del tool call*
- Testo discorsivo (3 punti sotto il diagramma):
  - *Il modello non ha eseguito nulla — ha emesso una richiesta strutturata, e l'harness ha fatto il lavoro.*
  - *Ogni tool call aggiunge almeno due round-trip prima della risposta finale: la richiesta e il risultato. Su task complessi con tool multipli, i round-trip si moltiplicano — e con loro latenza e costo.*
  - *Il modello sceglie quale tool usare leggendo le descrizioni che gli sono state fornite. Una descrizione ambigua o mal scritta produce scelte sbagliate — non è un problema del modello, è un problema di design.*

**Visual** — prompt per schema SVG:
> Diagramma orizzontale con 4 colonne verticali, etichette in cima: "User", "Harness" (con badge **"esegue"**), "Model" (con badge **"decide"**), "External API". Frecce orizzontali numerate 1–8 in sequenza dall'alto verso il basso:
> 1. User → Harness: *"Qual è lo stato dell'ordine #A-7842 di Rossi SpA?"*
> 2. Harness → Model: contesto + tool definitions
> 3. **Model → Harness**: `tool_call {tool:"query_crm", args:{customer:"Rossi SpA", order:"A-7842"}}` — freccia in **colore accento**
> 4. Harness → External API: chiamata al CRM
> 5. **External API → Harness**: `{status:"shipped", eta:"2025-04-16", tracking:"DHL 1234567890"}` — freccia in **colore accento**
> 6. Harness → Model: contesto aggiornato con tool result
> 7. Model → Harness: *"L'ordine #A-7842 è in spedizione…"*
> 8. Harness → User: risposta in linguaggio naturale
>
> I badge "decide" (su Model) e "esegue" (su Harness) sono piccoli, posizionati sotto l'etichetta della colonna. Le frecce 3 e 5 sono in colore accento per evidenziare ciò che è nuovo rispetto al loop conversazionale puro. Stile minimale, font sans-serif.

---

## ✅ Slide 24 — Cosa finisce nel contesto quando si usano tool

**Layout**: titolo in alto, tabella a 4 colonne + riga esempio (~65% della slide), chiusura discorsiva in basso.

**Testo**:
- Titolo: *Cosa finisce nel contesto quando si usano tool*
- Tabella (5 righe: 4 componenti + 1 riga esempio ancorata alla narrazione CRM):

| Componente | Quando | Dimensione tipica | Persistenza |
|---|---|---|---|
| Definizione tool | Una volta, in cima | 100–300 token × n° tool | Tutta la conversazione |
| Tool call | Ad ogni invocazione | Piccola (nome + argomenti) | Tutta la conversazione |
| Tool result | Ad ogni invocazione | Variabile — da decine a decine di migliaia di token | Tutta la conversazione |
| Turni user/assistant | Come prima | Piccola | Tutta la conversazione |
| **Esempio: agente customer service con 3 tool (query_crm, search_kb, create_ticket)** | — | ~600 token (def) + ~200 (call) + ~12k (result) = **~13k token di overhead** prima della risposta | — |

- Chiusura discorsiva: *Il contesto non contiene solo lo scambio tra utente e agente. Contiene anche tutto ciò che i tool hanno recuperato dal mondo esterno — ogni result, ogni documento restituito, ogni risposta API. E niente viene mai ripulito automaticamente.*

**Visual**: la tabella è l'elemento visivo. Riga esempio in grassetto o con sfondo tenue distinto.

---

## ✅ Slide 25 — I tool accelerano il context rot

**Layout**: titolo in alto, 2 mini-grafici affiancati (~40% della slide), paradosso centrale in evidenza, 3 take-home, ponte alla Slide 26 in chiusura.

**Testo**:
- Titolo: *I tool accelerano il context rot*
- Paradosso centrale (in evidenza, sotto i grafici): *I tool sono la risposta al limite più evidente del modello da solo: non sa quello che non sa, e non può agire nel mondo. Ma ogni tool call deposita nel contesto il suo risultato — e lì resta per tutta la sessione. Il problema che risolvono è reale; il problema che creano lo è altrettanto.*
- 3 take-home:
  - *Esporre all'agente solo i tool strettamente necessari al task. Ogni definizione di tool paga un costo fisso di contesto anche se il tool non viene mai chiamato.*
  - *Dimensionare i tool result. Un tool che restituisce 50k token grezzo non è un tool ben progettato — è un carico. Un buon tool filtra, sintetizza, restituisce solo ciò che serve per la decisione successiva.*
  - *Preferire tool ben definiti a tool generici. Un tool che fa una cosa sola, bene, consuma meno descrizione e viene scelto con più precisione di un tool multi-funzione.*
- Ponte finale (chiusura della slide): *La prossima tecnica — i sub-agent — è un modo per non pagare questo costo.*

**Visual** — prompt per schema SVG:
> Due grafici cartesiani affiancati, stessi assi su entrambi (X: numero di turni 0–20; Y: dimensione contesto in token 0–50k).
>
> Grafico sinistro, titolo "Conversazione pura": curva lineare leggera, sale gradualmente fino a circa 5k token al turno 20.
>
> Grafico destro, titolo "Conversazione con tool": curva a scalini — ogni 2–3 turni un salto verticale corrispondente a un tool result; raggiunge circa 40–50k token al turno 20.
>
> Stessa scala Y su entrambi per permettere confronto visivo immediato. Stile minimale, etichette chiare.

---

## ✅ Slide 26 — Sub-agent: il problema e l'analogia

**Layout**: titolo in alto, layout a 2 colonne — testo a sinistra (~60%), schema minimale padre/figlio a destra (~40%).

**Testo** (colonna sinistra):
- Titolo: *Sub-agent: delegare per gestire meglio il contesto*
- Apertura (una riga): *Il problema: ogni tool result rimane nel contesto per tutta la sessione — e satura.*
- Analogia: *Il manager di progetto non legge personalmente i 200 documenti del due diligence. Chiede a un collaboratore di farlo — e di tornare con un executive summary di due pagine. Il manager mantiene il suo contesto strategico pulito. Il collaboratore si sporca le mani.*
- Pattern: *Il pattern sub-agent funziona esattamente così: un agente figlio riceve un task delegato, lavora con il proprio contesto isolato, e restituisce al padre solo il risultato sintetizzato. Il contesto del padre non viene mai contaminato dal processo.*

**Visual** — prompt per schema SVG (colonna destra):
> Due rettangoli sovrapposti verticalmente con frecce bidirezionali.
> In alto: rettangolo "Agente padre" con piccolo box interno etichettato "contesto pulito ✓".
> Freccia verso il basso etichettata "delega task".
> In basso: rettangolo "Sub-agent" con piccolo box interno etichettato "contesto isolato".
> Freccia verso l'alto etichettata "restituisce sintesi".
> Stile minimalissimo, solo struttura, nessun dettaglio aggiuntivo.

---

## ✅ Slide 27 — Sub-agent: meccanica, benefici, esempi

**Layout**: titolo in alto, diagramma gerarchico (~50% della slide), 4 benefici e 4 esempi reali in basso.

**Testo**:
- Titolo: *Come funziona il pattern sub-agent*
- 5 benefici (ordine: risparmio token → isolamento → parallelizzazione → specializzazione → contenimento errori), testo 13pt (override via `--text-size` sul container, header colonne a 15pt):
  - **Risparmio token** *(evidenziato in colore secondary/teal)* — il padre non reitera sul contesto dei figli
  - **Isolamento** — padre vede solo il risultato
  - **Parallelizzazione** — più figli in contemporanea
  - **Specializzazione** — prompt e tool propri
  - **Contenimento errori** — fallimento figlio non intacca il padre
- 3 esempi reali, stesso font:
  - **Claude Code** — esplorazione codebase
  - **Deep Research** — fonti parallele
  - **OpenClaw** — agente generalista multi-sub-agent

**Visual** — prompt per schema SVG:
> Diagramma gerarchico. In alto al centro: rettangolo "Agente padre" con contesto visualizzato come box pulito (poche righe ordinate). Da questo partono 3 frecce verso il basso etichettate "spawn", che raggiungono 3 rettangoli "Sub-agent 1", "Sub-agent 2", "Sub-agent 3", ognuno con il proprio contesto visualizzato come box più affollato (più righe, più denso). Ogni sub-agent ha a sua volta una freccia verso un mini-tool con etichetta (es. "web search", "file read", "query DB"). Dai 3 sub-agent, frecce verso l'alto tornano al padre con etichetta "sintesi". Contrasto visivo chiaro: contesto padre pulito, contesti figli affollati.

---

## ✅ Slide 28 — Effetti collaterali dei sub-agent

**Layout**: titolo in alto, 4 effetti collaterali (con micro-icona discreta per ciascuno), 3 take-home. Slide con composizione tipografica a blocchi.

**Testo**:
- Titolo: *I sub-agent non sono gratis*
- 4 effetti collaterali (micro-icona lineare monocromatica accanto a ciascuno):
  - **Perdita di informazione nella sintesi** *(icona: filtro con goccia che esce)* — il padre vede solo ciò che il figlio sceglie di riportare. Dettagli scartati nella sintesi sono irrecuperabili
  - **Debugging e osservabilità complessi** *(icona: albero ramificato)* — le tracce diventano alberi, spesso non completamente persistiti. Errori difficili da riprodurre e analizzare
  - **Errori composti silenziosi** *(icona: tessere domino che cadono)* — un figlio che sbaglia produce una sintesi "ragionevole" che il padre usa come base per decisioni ulteriori. L'errore si nasconde negli handoff
  - **Nuova superficie di prompt injection** *(icona: freccia deviata)* — un sub-agent con accesso web può essere manipolato da contenuti esterni e contaminare la sintesi restituita al padre
- 3 take-home:
  - *Sub-agent vincono su task esplorativi, parallelizzabili, o che richiedono contesti specializzati. Perdono su task lineari o dove la tracciabilità è critica.*
  - *Regola pratica: se ti viene chiesto di spiegare esattamente cosa ha fatto l'agente passo dopo passo — audit, compliance, debug — il pattern sub-agent rende tutto più difficile. La delega isola il contesto, ma isola anche la traccia.*
  - *Sul costo: dipende dal pattern — misurare, non assumere. A volte un sub-agent costa meno perché il padre non paga il result grezzo.*

**Visual**: 4 micro-icone discrete, una per effetto collaterale. Stile lineare monocromatico (non fumettistico), solo come marcatori visivi dei blocchi.

---

## ✅ Slide 29 — Il loop agentico con tool (evoluzione del loop conversazionale)

**Layout**: titolo + sottotitolo in alto, diagramma pentagonale (riusa il layout della slide 22) con sub-ciclo tool sul nodo Modello (~55%), didascalia, bullet operativo in fondo.

**Testo**:
- Titolo: *Il loop agentico con tool*
- Sottotitolo: *Stesso loop conversazionale, con un sub-ciclo tool dentro al turno del modello*
- Didascalia: *Il loop esterno è identico a prima. Cambia solo il nodo Modello: invece di rispondere subito, può emettere una tool call, attendere il risultato, e re-iterare N volte prima di chiudere il turno. Il numero di cicli interni non è predeterminato — lo decide il modello a runtime.*
- Bullet operativo: *Limiti obbligatori in produzione: un tetto al numero di tool call per turno, un timeout per singola esecuzione, un budget di token per sessione. Senza, l'agente può entrare in cicli infiniti.*

**Visual** — schema SVG (deve essere un'evoluzione visiva del loop conversazionale della slide 22):
> Riusa esattamente il pentagono della slide 22 (5 nodi: Utente scrive → Client costruisce contesto → Modello decide → Client appende allo storico → Utente legge risposta → back), con identici stili, colori, posizioni e la freccia di chiusura accent "ad ogni giro il contesto cresce". Stesso box "contesto" crescente al centro.
> Il nodo "Modello" (accent primary/berry) prende un sottotitolo "risponde o chiama tool".
> **Novità**: a destra del pentagono, un sub-ciclo in colore secondary/teal: dal Modello → "Harness esegue tool" (bordo teal) → "Tool result nel contesto" (bordo teal) → freccia di ritorno (tratteggiata teal) verso Modello, etichettata "N volte". Caption sotto: "sub-ciclo tool (interno al turno)".
> L'intento visivo: lo spettatore deve riconoscere il pentagono noto e capire a colpo d'occhio che l'unica vera novità è il loop teal interno al nodo Modello.

---

## ✅ Slide 30 — Eval

**Layout**: titolo in alto, definizione, 3 peculiarità discorsive, 3 implicazioni strategiche. Nessun visual.

**Testo**:
- Titolo: *Eval: la differenza tra prodotto e demo*
- Definizione: *Suite di test per sistemi agentici. Concettualmente analoga ai test automatici del software — ma con tre differenze fondamentali che cambiano tutto.*
- 3 peculiarità (discorsive):
  - *Prima: gli output non sono binari. Un test software passa o fallisce. Una risposta di un agente può essere corretta, parzialmente corretta, corretta nel contenuto ma sbagliata nel tono, o corretta oggi e sbagliata domani dopo una modifica al system prompt. Si usano modelli come giudici di altri modelli — LLM-as-judge — per valutare dimensioni qualitative che non si possono ridurre a vero/falso.*
  - *Seconda: lo stesso input non produce lo stesso output. Il sampling è probabilistico per costruzione. Ogni test va eseguito N volte, e si misura una distribuzione di successo — non un singolo risultato.*
  - *Terza: il dataset di test richiede lavoro umano serio. Non si genera automaticamente. Serve raccogliere casi reali, costruire edge case, includere tentativi di prompt injection, esempi ambigui. È un artefatto che si cura nel tempo, non si crea una volta.*
- 3 implicazioni strategiche:
  - Ogni modifica al system prompt, aggiunta di tool, riconfigurazione di sub-agent va validata contro l'eval suite. Senza, si procede per sensazione — e le sensazioni sugli LLM sono sistematicamente fuorvianti
  - I progetti agentici seri spendono più tempo a costruire e curare eval che a scrivere prompt
  - Quando un fornitore AI dice *"abbiamo migliorato il prompt"*, la domanda è: *"Lo dite perché avete visto esempi che vi piacciono, o perché la vostra eval suite mostra un miglioramento misurabile?"*

**Visual**: nessuno. Slide parlata, il testo discorsivo è la forza.

---

## Sintesi modifiche v1 → v2

| Slide | Modifica principale |
|---|---|
| 21 | Titolo: "L'agente che agisce" → **"Dall'agente che parla all'agente che agisce"** |
| 22 | Esempio meteo → **esempio CRM** (ordine #A-7842 Rossi SpA). Aggiunta **icona ingranaggio ⚙** come seme visivo |
| 23 | Diagramma ri-ancorato all'esempio CRM (`query_crm` tool). Aggiunti **badge "decide" / "esegue"** sulle colonne Model/Harness |
| 24 | Riga esempio ancorata alla narrazione CRM: **agente customer service con 3 tool (query_crm, search_kb, create_ticket)** |
| 25 | Aggiunto **terzo take-home** (granularità: tool ben definiti vs generici). Aggiunto **ponte esplicito** alla Slide 26 in chiusura |
| 26 | **Apertura accorciata** a una riga (il problema è già piantato da Slide 25) |
| 27 | Invariata |
| 28 | Aggiunto **terzo take-home sul costo** ("misurare, non assumere"). Aggiunte **4 micro-icone** per gli effetti collaterali |
| 29 | Aggiunto **sottotitolo "Terzo loop — l'agente decide cosa fare"**. Bullet operativo più concreto ("un tetto", "un timeout", "un budget") |
| 30 | Invariata |

**Filo narrativo introdotto**: l'esempio CRM (customer service, ordine #A-7842 di Rossi SpA) funge da continuità tra Slide 22, 23 e 24, dando alla sezione un sapore aziendale coerente con il pubblico MBA.

---

# Prossima slide da definire: Slide 31 — API tools (Sezione 5 — Tipi di tool)
