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
| 34 | *Modellazione della conoscenza — 1/3: dai dati all'architettura informativa* | piramide DIKW |
| 35 | *Modellazione della conoscenza — 2/3: l'Enterprise Knowledge Graph* | trapezio EKG a tre strati |
| 36 | *Modellazione della conoscenza — 3/3: il Knowledge Graph come contesto per gli agenti* | ciclo retrieval/learning tra agenti e EKG |
| 37 | *MCP — il protocollo standard per i tool* | sequenza a 3 step, system prompt che si riempie |
| 38 | *Browser use — l'agente pilota un browser* | form "Nuovo ticket" in compilazione |
| 39 | *Bash / code execution — il tool universale* | nessuno |

**Nota numerazione**: la slide di apertura della Sezione 5 è nuova rispetto al brief originale (che partiva direttamente dalla Slide 31). È etichettata "5.0" in attesa della rinumerazione complessiva della lezione.

**Nota posizionamento delle slide 34–36**: le tre slide di modellazione della conoscenza erano originariamente in Sezione 7 (come pratiche di context engineering). Spostate qui come *abilitatore* della famiglia della conoscenza (RAG / search-as-a-tool / Deep Research): senza architettura informativa a monte, quei pattern non producono risposte affidabili.

---

## Filo rosso visivo ricorrente

Pattern emergenti da mantenere coerenti in fase di rendering:

- **Callout sicurezza**: stesso trattamento grafico in Slide 31 e Slide 39 (bordo/sfondo distintivo)
- **Flussi sequenziali numerati**: Slide 33 (4 fasi) e Slide 37 (3 step) condividono la grammatica visiva
- **Tabelle compatte**: Slide 31 e Slide 38 usano tabelle come elemento portante
- **Blocchi paralleli con etichetta forte**: Slide 39 (3 proprietà) usa uno stile a cartellini riconoscibile
- **Slide 34–36**: trittico "Modellazione della conoscenza" con narrativa continua (piramide → EKG → ciclo agenti); titoli segmentati `1/3 · 2/3 · 3/3` per far percepire la sequenza

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

## Slide 34 — Modellazione della conoscenza — 1/3: dai dati all'architettura informativa

**Layout:** Titolo + due colonne (SVG piramide a sinistra, testo a destra) + riquadro con bordo

**Titolo:** Modellazione della conoscenza — 1/3: dai dati all'architettura informativa

**Riga introduttiva:** I dati grezzi non bastano. Per essere riutilizzabili — da utenti e da agenti — devono essere arricchiti di contesto e semantica di dominio, altrimenti tecnicamente l'informazione c'è ma praticamente non è azionabile.

**Colonna sinistra — Visual SVG:** Piramide a 4 livelli (DIKW-style) con annotazioni laterali.

*Prompt per SVG:*
> Piramide a 4 strati orizzontali, dal basso verso l'alto: `DATA` (base, larga, pallido), `INFORMATION`, `KNOWLEDGE`, `INTELLIGENCE` (apice, colore accento). Su ogni transizione tra strati, etichetta a sinistra con freccia curva che punta verso lo strato superiore: tra Data e Information → "Context"; tra Information e Knowledge → "Semantics"; tra Knowledge e Intelligence → "Actions". Sulla destra, una freccia verticale grande che attraversa la piramide dal basso all'alto con tre tacche "+": ogni tacca all'altezza di una transizione è etichettata con ciò che viene sommato — in basso "METADATA", al centro "RELATIONS", in alto "ALGORITHMS". Stile minimale, monocromatico con colore accento, coerente con il resto delle slide.

**Colonna destra — testo:** I quattro livelli, ciascuno aggiunge contesto al precedente:

- **Dati** — asset fisici grezzi (tabelle, file, topic, bucket, contenuti non strutturati)
- **+ Metadati → Informazione** — i dati diventano comprensibili a livello base
- **+ Relazioni → Conoscenza** — semantica di dominio: concetti, attributi, relazioni esplicite
- **+ Algoritmi → Intelligenza** — traduzione degli insight in decisioni e azioni di business

**Riquadro con bordo:**
L'AI aumenta efficienza, produttività e soddisfazione degli utenti solo se i dati sono completi, affidabili e interpretabili. L'architettura informativa precede logicamente l'adozione dell'AI — anche se in pratica si fanno in parallelo, perché l'AI è l'occasione per farla finalmente.

**Visual:** SVG piramide DIKW (descritto sopra).

**File:** `slides/slide51-conoscenza-problema.html` + `svg/slide49-piramide-ia.svg`

---

## Slide 35 — Modellazione della conoscenza — 2/3: l'Enterprise Knowledge Graph

**Layout:** Titolo + definizione + due colonne (SVG struttura EKG a sinistra, testo a destra) + riquadro con bordo

**Titolo:** Modellazione della conoscenza — 2/3: l'Enterprise Knowledge Graph

**Definizione:** Un Enterprise Knowledge Graph (EKG) virtuale è il modo elegante di rappresentare l'architettura informativa: collega la conoscenza semantica di dominio ai dati presenti in piattaforma e ai metadati di contesto.

**Colonna sinistra — Visual SVG:** Trapezio a tre strati che rappresenta la struttura dell'EKG.

*Prompt per SVG:*
> Trapezio verticale con base larga in basso e lato superiore più stretto, diviso in tre strati orizzontali (tonalità progressivamente più scure dal basso all'alto). Strato superiore — "ENTERPRISE ONTOLOGY": un piccolo grafo con 3-4 nodi circolari collegati da archi (concetti e relazioni). Strato intermedio — "DATA PRODUCTS": due esagoni affiancati. Etichetta laterale sinistra con freccia verso il grafo: "Semantic Linking" (a segnalare il collegamento verticale tra data product e ontologia). Strato inferiore — "PHYSICAL DATA ASSETS": a sinistra icone di file/documenti con label "UNSTRUCTURED", a destra icone di tabelle/cilindri DB con label "STRUCTURED", collegate da linee tratteggiate agli esagoni dei Data Product sopra. Cornice esterna del trapezio con etichetta "ENTERPRISE KNOWLEDGE GRAPH". Stile minimale, monocromatico con colore accento.

**Colonna destra — testo:** Tre elementi costitutivi dell'EKG, label in grassetto + 1-2 righe:

- **Ontologia aziendale** — modello concettuale a grafo interpretabile da umani e applicazioni. Esprime il dominio in termini di *concetti* (Cliente, Prodotto, Ordine), *attributi* (Stato del cliente, Descrizione del prodotto) e *relazioni* semantiche (Prodotto "comprato da" Cliente). Più espressiva del Business Glossary tradizionale.
- **Data Product** — unità di modularizzazione, ownership e deployment. Ognuno ha un Data Product Owner, un ciclo di vita indipendente, interfacce esplicite governate da data contract. Registrati nel Data Product Catalog, accessibili via Data Product Marketplace.
- **Asset fisici + Semantic Linking** — tabelle, viste, topic, bucket, contenuti non strutturati. I metadati tracciano il collegamento semantico (lineage verticale) tra ogni asset — fino al singolo campo — e i concetti dell'ontologia. Abilita interoperabilità tra strutturati e non strutturati.

**Riquadro con bordo:**
I quattro pilastri: conoscenza di dominio come patrimonio differenziante · collegamento esplicito semantica ↔ dati · interoperabilità strutturati/non strutturati · approccio strategico, incrementale, orientato al valore. Costruire un EKG è un progetto di data e information architecture, non di AI.

**Visual:** SVG trapezio EKG a tre strati (descritto sopra).

**File:** `slides/slide52-conoscenza-elementi.html` + `svg/slide50-ekg-trapezoid.svg`

---

## Slide 36 — Modellazione della conoscenza — 3/3: il Knowledge Graph come contesto per gli agenti

**Layout:** Titolo + concetto chiave + SVG (sopra) + due colonne retrieval/learning + lista bullet vantaggi + riquadro con bordo

**Titolo:** Modellazione della conoscenza — 3/3: il Knowledge Graph come contesto per gli agenti

**Concetto chiave:** L'Enterprise Knowledge Graph è il contesto comune che più agenti AI condividono per migliorare ricerca, interrogazione dei dati e supporto agli utenti nell'estrazione di insight.

**Visual SVG:** Ciclo virtuoso EKG ↔ agenti.

*Prompt per SVG:*
> Diagramma orizzontale in due blocchi verticali. In alto, una fila di 4-5 triangoli identici che rappresentano agenti AI (ognuno con una piccola fumetto/chat bubble al centro con scritta "AI"). In basso, il trapezio "ENTERPRISE KNOWLEDGE GRAPH" con i tre strati già descritti (ontology in alto, data products al centro, physical assets in basso) — stesso stile della slide 35 ma più schematico. Tra agenti e EKG, due frecce verticali affiancate: una freccia in su etichettata "RETRIEVAL" (dall'EKG verso gli agenti), una freccia in giù etichettata "LEARNING" (dagli agenti verso l'EKG). Le due frecce evidenziano il ciclo bidirezionale. Stile minimale, monocromatico con colore accento.

**Due colonne — ciclo EKG ↔ agenti:**

**Colonna sinistra — Retrieval:**
Gli agenti consultano il grafo per recuperare contesto di dominio affidabile (concetti, relazioni, data product rilevanti) e produrre risposte pertinenti, ancorate a dati reali e non a congetture.

**Colonna destra — Learning:**
Gli agenti contribuiscono a estendere l'architettura: persistono nel Knowledge Graph nuovi elementi di conoscenza, informazioni o dati appresi nelle conversazioni con gli esperti di dominio o estratti da contenuti non strutturati già presenti in azienda.

**Tre vantaggi operativi:**

- **Riuso dei dati** — design modulare dei Data Product collegati all'ontologia: si ricompongono per più casi d'uso, riducendo i costi nel medio-lungo periodo
- **Semantica di dominio condivisa** — la formalizzazione riduce ambiguità e frizioni fra unità di business
- **Gap business ↔ IT ridotto** — il linguaggio del business si avvicina alla terminologia IT, diffondendo cultura dei dati

**Riquadro con bordo:**
L'EKG è la forma aziendale della *skill* — una mappa navigabile ai domini di conoscenza, collegata a dati reali e governata. Il pattern "skill" verrà ripreso formalmente in Sezione 7. Se il prossimo progetto AI parte con "prendiamo i PDF e mettiamoli in un vector store", fermarsi. Partire da: quali sono i domini di conoscenza, chi ne è owner, qual è l'ontologia, quali data product li espongono.

**Visual:** SVG ciclo retrieval/learning tra agenti AI e EKG (descritto sopra).

**File:** `slides/slide53-conoscenza-skill.html` + `svg/slide51-ekg-agenti.svg`

**Nota**: il richiamo esplicito alla *skill* è un forward reference a Sezione 7. Resta comunque comprensibile al primo passaggio (skill = pacchetto di conoscenza caricabile on-demand, intuizione leggibile dal contesto).

---

## Slide 37 — MCP (Model Context Protocol)

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

## Slide 38 — Browser use

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

## Slide 39 — Bash / code execution

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

4. **Slide 34–36 — trittico modellazione della conoscenza spostato in Sezione 5**: le 3 slide erano in Sezione 7 come pratiche di context engineering. Spostate qui come *abilitatore* della famiglia della conoscenza (Slide 32) e di Deep Research (Slide 33): senza architettura informativa a monte, RAG / search-as-a-tool / Deep Research non producono risposte affidabili. Il richiamo a *skill* nel recap di Slide 36 resta come forward reference a Sezione 7 (accettabile: skill è leggibile intuitivamente come "pacchetto di conoscenza caricabile on-demand").

5. **Slide 37 — aggiunta esplicita dell'iniezione nel system prompt**: il brief non chiariva dove vanno a finire le tool definition dopo il discovery MCP. Esplicitato in testo e nel visual per creare continuità con la Slide 31 (dove si vede *com'è fatta* una tool definition).

6. **Slide 37 — tagline spostata**: la frase "Se un'integrazione AI proprietaria non espone MCP, è vendor lock-in" è stata spostata dalla posizione di take-home autonomo a bullet finale del Blocco B.

7. **Slide 38 — 3 caveat invece di 4**: rimosso il caveat "Fragile" (l'UI cambia e l'agente si rompe). Rinominata la colonna dei limiti in "Caveat" (più neutro del "Perché costa caro" proposto inizialmente).

8. **Slide 38 — take-home integrato, non frase-bandiera**: il messaggio "scelta di ultima istanza, non di prima" è integrato come bullet finale in corsivo dentro la colonna "Quando serve", invece che isolato in fondo alla slide.

9. **Slide 39 — etichetta "Componibile" invece di "Substrato"**: la terza proprietà è stata rinominata per essere più attiva e meno accademica. Lega anche al tono generale della lezione (mattoncini, composizione).

10. **Slide 39 — nessun rimando esplicito a Sez. 6/7**: il brief suggeriva "→ Sez. 6" e "→ Sez. 7" come ponti visivi. Rimossi per pulizia; i rimandi restano impliciti nel testo delle proprietà.
