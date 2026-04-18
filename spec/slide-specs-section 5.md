# Sezione 5 — Tipi di tool

**Specifica consolidata delle slide**
*Lezione MBA Politecnico di Milano — LLM e agenti AI*

---

## Indice slide

| # | Titolo | Visual |
|---|---|---|
| 5.0 | *Tipi di tool — il catalogo* | nessuno |
| 31 | *API tools — l'archetipo* | tabella esempi + snippet tool definition annotato + callout sicurezza |
| 32 | *La famiglia della conoscenza — 3 pattern* | mini-scala a 3 gradini (pattern / tool / sistema agentico) |
| 33 | *Anatomia di Deep Research* | diagramma 4 fasi con loop di ritorno F3→F2 |
| 34 | *MCP — il protocollo standard per i tool* | sequenza a 3 step, system prompt che si riempie |
| 35 | *Browser use — l'agente pilota un browser* | form "Nuovo ticket" in compilazione |
| 36 | *Bash / code execution — il tool universale* | nessuno |

**Nota numerazione**: la slide di apertura della Sezione 5 è nuova rispetto al brief originale (che partiva direttamente dalla Slide 31). È etichettata "5.0" in attesa della rinumerazione complessiva della lezione.

---

## Filo rosso visivo ricorrente

Pattern emergenti da mantenere coerenti in fase di rendering:

- **Callout sicurezza**: stesso trattamento grafico in Slide 31 e Slide 36 (bordo/sfondo distintivo)
- **Flussi sequenziali numerati**: Slide 33 (4 fasi) e Slide 34 (3 step) condividono la grammatica visiva
- **Tabelle compatte**: Slide 31 e Slide 35 usano tabelle come elemento portante
- **Blocchi paralleli con etichetta forte**: Slide 36 (3 proprietà) usa uno stile a cartellini riconoscibile

---

## Slide 5.0 — Apertura Sezione 5

**Layout**: titolo + 2 sottotitoli + mini-mappa delle 5 categorie in basso.

**Stile narrativo**: ponte minimalista, coerente con gli opener di Slide 21 e Slide 38.

### Testo

- **Titolo**: *Tipi di tool — il catalogo*
- **Sottotitolo 1**: *Fino a qui: la meccanica del tool call. Da qui: quali tool esistono davvero.*
- **Sottotitolo 2**: *5 categorie che coprono la quasi totalità degli agenti oggi in produzione.*
- **Mappa in basso** (piccola, in linea, eco della mappa di Slide 0):
  - API tools · Knowledge access · MCP · Browser use · Code execution

### Visual

Nessuno oltre al testo.

---

## Slide 31 — API tools

**Layout**: titolo + definizione + 2 colonne (tabella esempi | snippet annotato) + callout sicurezza a piena larghezza.

### Testo

- **Titolo**: *API tools — l'archetipo*

- **Definizione** (sotto titolo, a piena larghezza):
  *Qualunque endpoint HTTP diventa una capacità dell'agente definendo lo schema della sua API (nome, descrizione, parametri, autenticazione).*

- **Colonna sinistra — Esempi aziendali** (tabella compatta):

  | Sistema | Operazione tipica |
  |---|---|
  | CRM (Salesforce, HubSpot) | Lookup cliente, aggiornamento record |
  | DB relazionale | Query strutturate su dati operativi |
  | Sistema di ticketing | Apertura ticket, aggiornamento stato |
  | Email transazionale | Invio notifiche e comunicazioni |
  | ERP | Operazioni su ordini, inventario |
  | Pagamenti (Stripe) | Charge, refund, gestione subscription |

- **Colonna destra — Anatomia di una tool definition** (snippet JSON annotato):

  ```json
  {
    "name": "get_customer",
    "description": "Retrieve customer data by ID from the CRM.",
    "input_schema": {
      "type": "object",
      "properties": {
        "customer_id": {
          "type": "string",
          "description": "Unique identifier of the customer"
        }
      },
      "required": ["customer_id"]
    }
  }
  ```

  Con **3 annotazioni laterali** collegate ai campi:
  - `name` → *come l'agente lo chiama*
  - `description` → *su questo testo l'agente decide se usarlo*
  - `input_schema` → *parametri tipizzati*

- **Callout sicurezza** (in basso, tutta larghezza, stile evidenziato):
  > **Principio di minimo privilegio.** Un tool read-only su CRM è diverso da un tool che sposta denaro. Esporre all'agente solo i tool strettamente necessari al task, con scope il più ristretto possibile.

### Nota per il docente (in voce, non in slide)

L'autenticazione non è nello schema inviato al modello — è gestita dall'harness quando esegue la chiamata HTTP effettiva. Per questo lo snippet non contiene un campo auth.

### Visual — Prompt SVG per lo snippet annotato

> Box monospaziato contenente lo snippet JSON, su sfondo neutro chiaro. Tre etichette/callout laterali collegate tramite linee sottili ai rispettivi campi del JSON:
> - "name" → "come l'agente lo chiama"
> - "description" → "su questo testo l'agente decide se usarlo"
> - "input_schema" → "parametri tipizzati"
>
> Le linee di connessione sono in colore accento. Il JSON ha sintassi evidenziata in modo minimale (chiavi in un colore, stringhe in un altro). Stile pulito, simile a documentation web moderna.

---

## Slide 32 — La famiglia della conoscenza (3 pattern)

**Layout**: titolo + sottotitolo + 3 blocchi con meta-etichetta + bullet finale + mini-scala visuale.

**Ordine dei livelli**: segue l'evoluzione storica e concettuale (RAG nasce per primo come pattern architetturale, poi search-as-tool con la maturità del tool calling, infine Deep Research come sistema agentico che combina entrambi).

### Testo

- **Titolo**: *La famiglia della conoscenza — 3 pattern*

- **Sottotitolo**: *Tre pattern per accedere a conoscenza non nel training.*

- **Livello 1 — RAG (Retrieval-Augmented Generation)** ⟵ *un pattern architetturale*
  - Prima della generazione, un retriever (vector DB, search engine, DB aziendale) estrae i chunk rilevanti
  - I chunk vengono iniettati nel contesto, la risposta è ancorata alla conoscenza proprietaria
  - Il modello non decide *se* cercare — la ricerca avviene sempre, prima

- **Livello 2 — Search-as-a-tool** ⟵ *un tool*
  - La ricerca diventa una tool call: il modello decide quando, cosa, come cercare
  - Abilita il modello a iterare — cercare, leggere, raffinare la query, ricercare
  - Risolve il knowledge cutoff in modo dinamico

- **Livello 3 — Deep Research** ⟵ *un sistema agentico*
  - Pianificazione, sub-agent paralleli, loop di steering, sintesi finale con citazioni
  - Combina RAG e search orchestrati in multi-fase
  - *Dettaglio nella prossima slide*

- **Bullet finale in basso** (stile piano, non callout):
  *Quando un fornitore propone un prodotto AI per l'azienda: come conosce i nostri dati? RAG su quale base, aggiornata come, con quali policy di accesso?*

### Visual — Prompt SVG

> Mini-scala a 3 gradini crescenti disposti orizzontalmente o verticalmente accanto ai 3 blocchi di testo. Ogni gradino è etichettato con il proprio livello di meta-classificazione:
> - Gradino 1 (più basso): "pattern architetturale" — RAG
> - Gradino 2 (medio): "tool" — Search-as-a-tool
> - Gradino 3 (più alto): "sistema agentico" — Deep Research
>
> La scala suggerisce crescente complessità/sofisticazione architetturale, non crescente capacità (sono architetture diverse, non versioni migliori l'una dell'altra). Stile minimale, monocromatico con accento di colore sul gradino più alto.

---

## Slide 33 — Anatomia di Deep Research

**Layout**: titolo + diagramma protagonista (~70% della slide) + didascalia a 4 righe compatte.

**Stile narrativo**: slide focalizzata sulla dinamica. Il diagramma è il protagonista; il testo lo supporta senza duplicare. Il "test dei 4 punti" per l'informed user viene dato dal docente a voce, non in slide.

### Testo

- **Titolo**: *Anatomia di Deep Research*

- **Didascalia sotto il diagramma** (4 righe compatte):
  - **F1 — Elicitation del piano** · l'agente principale analizza la richiesta e produce un piano strutturato
  - **F2 — Retrieve paralleli** · sub-agent con contesto isolato esplorano fonti diverse simultaneamente
  - **F3 — Loop di steering** · l'agente principale confronta i risultati col piano e spawna nuovi sub-agent sui gap
  - **F4 — Sintesi finale** · integrazione in documento strutturato con citazioni — l'utente vede solo questo

### Visual — Prompt SVG

> Diagramma orizzontale con 4 fasi sequenziali, ognuna in un riquadro distinto.
>
> - **Fase 1 "Elicitation del piano"**: icona di agente singolo accanto a un documento con righe (rappresentazione visuale del piano).
> - **Fase 2 "Retrieve paralleli"**: icona di agente singolo in alto; sotto, 3-4 sub-agent in parallelo, ognuno con una freccia che punta a una fonte diversa (web, documenti interni, database).
> - **Fase 3 "Steering loop"**: agente centrale con frecce cicliche verso i sub-agent (con possibilità di aggiungerne di nuovi); etichetta "gap analysis" vicino all'agente centrale.
> - **Fase 4 "Sintesi finale"**: agente centrale che produce un documento strutturato con citazioni visibili.
>
> Frecce fluide tra le fasi. **La fase 3 ha una freccia di ritorno alla fase 2** per mostrare la natura iterativa del processo. Stile minimale, monocromatico con colore accento sulla freccia di ritorno F3→F2 per evidenziare l'iterazione.

---

## Slide 34 — MCP (Model Context Protocol)

**Layout**: titolo + sottotitolo/analogia + 3 blocchi narrativi (A/B/C) + visual orizzontale a 3 step.

**Stile narrativo**: slide di demistificazione. MCP è uno dei buzzword più densi del 2025-26; la slide smonta l'idea "MCP è una cosa nuova" (falso) e costruisce l'idea giusta "MCP è un protocollo di discovery e invocazione" (vero). La struttura a 3 blocchi è strumento di controllo della densità.

### Testo

- **Titolo**: *MCP — il protocollo standard per i tool*

- **Sottotitolo / analogia** (1 riga sotto titolo):
  *MCP sta ai tool come USB sta ai dispositivi. Un connettore standard, non un nuovo dispositivo.*

- **Blocco A — Cos'è (e cosa non è)**
  - **Non** è un nuovo tipo di tool. Non cambia la meccanica del tool call (richiesta strutturata → esecuzione → result nel contesto).
  - **È** un protocollo che standardizza due cose:
    - *Discovery* — l'agente chiede al server "quali tool offri?" e riceve lo schema
    - *Invocazione* — formato di chiamata e risposta uniforme su qualunque server MCP
  - Dopo il discovery, le tool definition scelte finiscono nel **system prompt** dell'agente e restano lì per tutta la sessione.

- **Blocco B — Perché conta**
  - Riduce il vendor lock-in: stessa integrazione su qualunque agente compatibile
  - Centinaia di server pubblici già disponibili (GitHub, Linear, Notion, Gmail, DB) — layer su cui si stanno costruendo gli **app-store per agenti**
  - *Se un'integrazione AI proprietaria non espone MCP, è vendor lock-in.*

- **Blocco C — Il trabocchetto**
  *Ogni server MCP connesso paga token nel contesto: le sue tool definition sono sempre presenti nel system prompt. Connetterne 10 "nel caso servissero" può saturare metà del contesto prima ancora che l'agente inizi a lavorare. Quando un prodotto dice di supportare "50 MCP", chiedere quali si attivano di default — la differenza tra "disponibile" e "sempre in contesto" è sostanziale.*

### Visual — Prompt SVG

> Diagramma orizzontale a 3 step con due attori principali (Harness e Server MCP), più l'artefatto System prompt.
>
> - **Step 1 (sinistra)**: rettangolo "Harness" con freccia verso rettangolo "Server MCP"; etichetta sulla freccia "list_tools()".
> - **Step 2 (centro)**: rettangolo "Server MCP" con freccia di ritorno verso "Harness"; etichetta sulla freccia "schema dei tool disponibili".
> - **Step 3 (destra)**: rettangolo "Harness" con freccia verso un'icona grande "System prompt dell'agente", rappresentata come foglio/documento che si riempie di tool definition (righe tipo "tool: get_weather", "tool: create_ticket"); etichetta sulla freccia "iniezione".
>
> Sotto il foglio del system prompt, un'annotazione piccola: *"restano qui per tutta la sessione"*.
>
> Stile minimale, monocromatico con colore accento sulle frecce di interazione con il server MCP (step 1 e step 2).

---

## Slide 35 — Browser use

**Layout**: titolo + definizione + riga prodotti + 2 colonne contrastive + visual form.

**Stile narrativo**: slide "sì ma con cautela". Il paradigma è intuitivamente attraente, ma l'informed user deve saper vedere i limiti. Il messaggio controintuitivo ("scelta di ultima istanza, non di prima") è integrato come bullet finale nella colonna "Quando serve".

### Testo

- **Titolo**: *Browser use — l'agente pilota un browser*

- **Definizione** (1 riga sotto il titolo):
  *L'agente riceve screenshot della pagina e produce azioni: click, scroll, scrittura in form, navigazione.*

- **Riga prodotti esempio** (orizzontale, stile tag):
  Claude Computer Use (Anthropic) · Browser Use (open source) · OpenAI Operator

- **Due colonne contrastive**:

  | Quando serve | Caveat |
  |---|---|
  | SaaS legacy senza API | **Lento** — ogni azione è un round-trip con screenshot |
  | Sistemi interni senza interfaccia programmatica | **Costoso** — gli screenshot come input consumano molti token |
  | Web automation su siti senza endpoint | **Opaco** — le azioni sono viste, non strutturate, quindi difficili da auditare |
  | *Scelta di ultima istanza, non di prima — sblocca il long tail delle automazioni aziendali.* | |

### Visual — Prompt SVG

> Rappresentazione stilizzata di un piccolo form web "Nuovo ticket di supporto" parzialmente compilato.
>
> Campi visibili: Titolo, Priorità (dropdown), Descrizione, pulsante "Invia".
>
> Stato del form:
> - Campo "Titolo": testo digitato "Malfunzionamento stampante"
> - Campo "Priorità": dropdown aperto con opzioni visibili (Bassa / Media / Alta)
>
> **Annotazioni laterali in stile fumetto/commento tecnico** che mostrano le azioni dell'agente, in ordine:
> 1. "click sul campo Titolo"
> 2. "type: Malfunzionamento stampante"
> 3. "click su dropdown Priorità"
> 4. "select: Alta"
>
> Piccola icona di cursore del mouse posizionata sul dropdown aperto.
>
> Stile minimale, monocromatico con colore accento sugli elementi interattivi (campo focus, opzione selezionata nel dropdown) e sulle annotazioni.

---

## Slide 36 — Bash / code execution

**Layout**: titolo + sottotitolo + 3 proprietà a blocchi paralleli + callout sicurezza.

**Stile narrativo**: slide-ponte di chiusura della Sezione 5. Non è solo un'altra categoria di tool — è il tool che sblocca lo spazio delle capacità, e il substrato delle Sezioni 6 (codice) e 7 (skill). Il rimando alle sezioni successive è implicito nel testo delle proprietà, non esplicitato con etichette.

### Testo

- **Titolo**: *Bash / code execution — il tool universale*

- **Sottotitolo** (1 riga sotto il titolo):
  *L'agente può eseguire comandi shell o codice in un ambiente sandboxato. Accesso a filesystem, librerie, script.*

- **Le 3 proprietà** (blocchi paralleli con etichetta forte a cartellino):

  - **Universale** → *Non sblocca una capacità specifica. Sblocca lo spazio delle capacità: se c'è bash, c'è accesso a tutto l'universo software.*

  - **Generativo** → *Invece di avere 20 tool predefiniti, l'agente scrive uno script che risolve il task specifico. È il cuore dei coding agent.*

  - **Componibile** → *Bash permette di comporre pacchetti di capacità — le skill: directory di file, istruzioni e script che l'agente apre ed esegue quando servono. Senza bash come tool, niente skill.*

- **Callout sicurezza** (stile coerente con Slide 31, in basso, tutta larghezza):
  > **Tool più potente = tool più pericoloso.** Sempre sandboxato: container isolato, no accesso a reti private, no credenziali sensibili in environment, limiti di risorse espliciti.

### Visual

Nessuno.

---

## Riepilogo decisioni editoriali significative

Decisioni prese durante l'intervista che si discostano o integrano il brief originale:

1. **Nuovo opener Sezione 5 (Slide 5.0)**: il brief originale partiva direttamente con Slide 31. Aggiunto un opener di tipo "ponte minimalista" per coerenza con altre sezioni e per dare all'audience la mappa delle 5 categorie.

2. **Slide 32 — ordine dei 3 livelli invertito**: il brief proponeva Search-as-a-tool → RAG → Deep Research. L'ordine adottato è RAG → Search-as-a-tool → Deep Research, che rispetta la cronologia di emersione (RAG 2020-21, Search-as-tool 2023+, Deep Research 2024+) e la progressione di sofisticazione architetturale. Meta-etichette "pattern / tool / sistema agentico" per chiarire che i 3 livelli sono eterogenei.

3. **Slide 33 — focus sulla dinamica, non sul test informed user**: il brief conteneva anche un caveat su costo/latenza e un "test dei 4 punti" per valutare i fornitori. Entrambi rimossi dalla slide per asciutezza visiva; il docente li darà a voce.

4. **Slide 34 — aggiunta esplicita dell'iniezione nel system prompt**: il brief non chiariva dove vanno a finire le tool definition dopo il discovery MCP. Esplicitato in testo e nel visual per creare continuità con la Slide 31 (dove si vede *com'è fatta* una tool definition).

5. **Slide 34 — tagline spostata**: la frase "Se un'integrazione AI proprietaria non espone MCP, è vendor lock-in" è stata spostata dalla posizione di take-home autonomo a bullet finale del Blocco B.

6. **Slide 35 — 3 caveat invece di 4**: rimosso il caveat "Fragile" (l'UI cambia e l'agente si rompe). Rinominata la colonna dei limiti in "Caveat" (più neutro del "Perché costa caro" proposto inizialmente).

7. **Slide 35 — take-home integrato, non frase-bandiera**: il messaggio "scelta di ultima istanza, non di prima" è integrato come bullet finale in corsivo dentro la colonna "Quando serve", invece che isolato in fondo alla slide.

8. **Slide 36 — etichetta "Componibile" invece di "Substrato"**: la terza proprietà è stata rinominata per essere più attiva e meno accademica. Lega anche al tono generale della lezione (mattoncini, composizione).

9. **Slide 36 — nessun rimando esplicito a Sez. 6/7**: il brief suggeriva "→ Sez. 6" e "→ Sez. 7" come ponti visivi. Rimossi per pulizia; i rimandi restano impliciti nel testo delle proprietà.
