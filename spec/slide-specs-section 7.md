# Specifica slide — Sezione 7: Context engineering
## MBA Politecnico di Milano — LLM e agenti AI

**Stato**: v2 — ristrutturata rispetto alla v1 (vedi nota in fondo).
**Idea ordinante**: l'harness è l'attore, context engineering è la disciplina che l'harness pratica. La sezione si costruisce in tre blocchi — (A) attore, (B) leve, (C) chiusura.

---

## Indice slide

| # | Titolo | Visual |
|---|---|---|
| 44 | *Context engineering* (opener) | SVG convergenza 4 pratiche → banner CE, dentro frame harness |
| 45 | *Harness — chi fa davvero le cose* | nessuno |
| 46 | *Context engineering come disciplina* | griglia 4 leve |
| 47 | *Compaction e pruning* | nessuno (2 card contrast) |
| 48 | *Progressive disclosure — il pattern skill* | tabella MCP vs Skill + SVG directory |
| 49 | *Memoria — demistificazione e meccanica* | SVG ciclo memoria |
| 50 | *Memoria — fasi operative e rischi* | nessuno (2 card) |
| 51 | *Sandbox — confini dell'esecuzione* | tabella confini |
| 52 | *Harness landscape — chi c'è oggi* | immagine esterna |
| 53 | *Building block e composizione* | SVG strati concentrici + barra trasversale |
| 54 | *I quattro loop in un colpo d'occhio* | SVG 4 mini-loop affiancati |

---

## Slide 44 — Context engineering (opener)

**Layout**: titolo + 1 riga di lead + SVG "converge-under-umbrella".

**Testo**:
- **Titolo**: *Context engineering*
- **Lead**: *System prompt, scelta dei tool, sub-agent, skill: li abbiamo costruiti uno a uno. Manca il nome che li lega.*

**Visual SVG**: *slide46-ce-opener.svg*

*Prompt SVG*:
> 4 piccoli box in alto (*system prompt · tool · sub-agent · skill*) con frecce che convergono verso il basso su una banner ampia con accent color e scritta **CONTEXT ENGINEERING — il nome che li lega**. Tutto racchiuso in un frame esterno tratteggiato etichettato **HARNESS · il software che esegue** (tag piccolo posizionato in alto a sinistra del frame). Sotto la banner, una riga in grigio muted: *"una disciplina · cosa entra nel contesto, quando, per quanto tempo"*. Dal fondo del frame harness, freccia accent in uscita verso un rettangolo **CONTESTO** (sfondo light accent), e da lì freccia grigia verso **Modello**. Stile minimale, monocromatico con accent #a1245a.

**Rationale**: allinea l'opener al pattern delle altre sezioni (bridge frame), e illustra direttamente il messaggio della slide — le 4 pratiche già viste convergono sotto un nome, e l'harness è il software che le esegue per produrre il contesto.

---

## Slide 45 — Harness — chi fa davvero le cose

**Layout**: titolo + definizione + lista bullet + riquadro con bordo.

**Testo**:
- **Titolo**: *Harness — chi fa davvero le cose*
- **Definizione**: *Il software che circonda il modello e gestisce tutto ciò che non è pura generazione di testo.*
- **6 responsabilità** (bullet):
  - **Costruisce e mantiene il contesto** — assembla system prompt, storico turni, tool definition, tool result a ogni chiamata API
  - **Esegue i tool quando il modello li richiama** — intercetta la richiesta strutturata e la traduce in chiamata reale
  - **Applica policy di sicurezza e autorizzazione** — decide quali azioni sono permesse in base al contesto e all'utente
  - **Orchestra i sub-agent** — lancia agenti figli, raccoglie le sintesi, le restituisce al padre
  - **Gestisce lo stato persistente** — memoria, sessioni, contesti tra conversazioni diverse
  - **Fornisce osservabilità** — log, tracce, metriche per debugging e monitoring in produzione
- **Riquadro**: *Quando si dice "Claude ha fatto X", Claude ha deciso X e l'harness ha eseguito X. Il confine è sottile ma cruciale — quasi tutta la sicurezza, l'affidabilità, la qualità di un agente in produzione vivono nell'harness.*

**Visual**: nessuno.

---

## Slide 46 — Context engineering come disciplina

**Layout**: titolo + definizione + griglia 4 leve (2×2) + riga di transizione.

**Testo**:
- **Titolo**: *Context engineering come disciplina*
- **Definizione**: *Progettare cosa vive nel contesto del modello a ogni chiamata — includere ciò che serve, escludere ciò che non serve, decidere per quanto resta. È il lavoro principale dell'harness.*
- **4 leve** (blocchi paralleli, label forte + 1 riga):
  - **Compaction e pruning** — ridurre il contesto che cresce
  - **Progressive disclosure** — caricare on-demand solo ciò che serve
  - **Memoria** — persistenza oltre la singola sessione
  - **Sandbox** — confini dell'esecuzione (adiacente: non è contesto, ma condivide lo stesso attore)
- **Riga di transizione** (in corsivo, sotto la griglia): *Una leva per slide, nei prossimi blocchi.*

**Visual**: la griglia 2×2 è l'elemento visivo.

---

## Slide 47 — Compaction e pruning — gestire il contesto che cresce

**Layout**: titolo + 2 colonne simmetriche (card) + riquadro.

**Testo**:
- **Titolo**: *Compaction e pruning — gestire il contesto che cresce*
- **Colonna sinistra — Pruning**:
  - **Definizione** — tagliare parti del contesto non più rilevanti (tool result vecchi, turni obsoleti)
  - **Policy** — quali informazioni sono sicure da dimenticare?
  - **Rischio** — dimenticare qualcosa che serviva
- **Colonna destra — Compaction**:
  - **Definizione** — sostituire parti del contesto con una loro sintesi
  - **Policy** — tipicamente un sub-agent riassume gli ultimi N turni e la sintesi rimpiazza gli originali
  - **Rischio** — la sintesi perde dettagli che emergeranno come importanti più avanti
- **Riquadro**: *Entrambe sono lossy — si perde informazione in cambio di spazio. La scelta di cosa comprimere o buttare è una delle decisioni più delicate di un agente in produzione. Non esiste policy universale — dipende dal task.*

**Visual**: le due card affiancate.

---

## Slide 48 — Progressive disclosure — il pattern skill

**Layout**: titolo + sottotitolo + tabella MCP vs Skill (in alto) + SVG directory/meccanica (al centro) + 2 micro-card in basso (esempio | richiamo bash).

**Testo**:
- **Titolo**: *Progressive disclosure — il pattern skill*
- **Sottotitolo**: *Due modi opposti di esporre tool e conoscenza al modello.*
- **Tabella MCP vs Skill** (3 righe, invariata):

  | | MCP | Skill |
  |---|---|---|
  | Tool definition | Sempre in contesto | Descrizione minima in contesto |
  | Costo | Fisso all'inizio della sessione | Pagato solo se la skill viene caricata |
  | Efficienza | Inefficiente se pochi tool servono davvero | Carica solo il necessario |

- **Definizione skill**: *Una directory con documentazione, istruzioni, esempi, eventuali script. Un file principale (`SKILL.md`) spiega al modello cosa la skill offre e come usarla.*
- **Micro-card 1 — Esempio**: *Skill "prodotti e pricing" → directory con SKILL.md (istruzioni di navigazione), listino strutturato, regole di sconto, riferimenti a tool specifici.*
- **Micro-card 2 — Meccanica**: *In Claude Code il meccanismo è il tool bash: il modello esplora la directory e legge i file. Altri harness usano meccanismi proprietari equivalenti.*

**Visual SVG**: struttura directory + meccanica in 3 passi (già prodotto come `svg/slide50-skill-pattern.svg`).

*Prompt SVG originale*:
> Schema diviso in due aree affiancate. Area sinistra: struttura directory a forma di albero. Cartella radice `skills/`, sotto-cartella `prodotti-pricing/`, file interni: `SKILL.md` (evidenziato con colore accento), `listino/`, `regole/`, `esempi/`. Annotazione accanto a SKILL.md: "sempre visibile al modello (1 riga di descrizione)". Annotazione sul resto della directory: "caricato on-demand". Area destra: meccanica in 3 passi con frecce verticali numerate: (1) "modello vede solo descrizione minima della skill" → (2) "decide che serve, richiede caricamento" → (3) "harness carica contenuto SKILL.md nel contesto". Stile minimale, monocromatico con un colore accento.

**Rationale**: fusione di ex Slide 47 (tabella sottile) + ex Slide 48 (skill pattern). La tabella da sola era troppo sottile; la meccanica skill da sola perdeva il confronto con MCP che motiva il pattern. Insieme la slide ha densità normale.

---

## Slide 49 — Memoria — demistificazione e meccanica

**Layout**: titolo + riga introduttiva + SVG ciclo memoria + 5 bullet meccanica + riquadro.

**Testo**:
- **Titolo**: *Memoria — demistificazione e meccanica*
- **Riga introduttiva** (corsivo): *"Memoria" è un termine abusato. Suggerisce che il modello ricordi nel senso umano. Non è così.*
- **Visual SVG**: ciclo a due sessioni con archivio al centro (già prodotto come `svg/slide56-memoria-ciclo.svg`, qui viene posto sopra la meccanica)

*Prompt SVG originale*:
> Diagramma orizzontale con tre colonne. Colonna sinistra "Sessione 1": utente e modello che si scambiano messaggi (bolle alternate), sotto una freccia con etichetta "harness estrae fatti" che punta verso il centro. Colonna centrale "Archivio persistente": rettangolo con etichetta "DB / vector store", riceve frecce dalla sessione 1 (salvataggio) e invia frecce alla sessione 2 (recupero). Una freccia orizzontale con etichetta "tempo" collega le due sessioni. Colonna destra "Sessione 2": freccia dall'archivio con etichetta "harness inietta fatti nel contesto" che precede la conversazione, poi utente e modello che si scambiano messaggi con un'annotazione "memoria già presente". Stile minimale, monocromatico con colore accento per le frecce harness → archivio → harness.

- **5 bullet meccanica**:
  - Il modello è **stateless** — nessuna memoria tra chiamate (richiamo Slide 10)
  - La "memoria" è un **sistema esterno** gestito dall'harness
  - L'harness decide **cosa salvare** fuori dal contesto corrente (fatti sull'utente, preferenze, sintesi)
  - Lo salva in **archivio persistente** (DB, vector store, file)
  - Al turno successivo, l'harness **recupera i fatti rilevanti** e li inietta nel contesto
- **Riquadro**: *Memoria dell'agente = RAG sulle sue stesse conversazioni passate. Non è che il modello "si ricorda di voi" — è che l'harness ha archiviato fatti su di voi e ve li re-inietta nel contesto quando parlate di nuovo.*

---

## Slide 50 — Memoria — fasi operative e rischi

**Layout**: titolo + 2 card affiancate (3 fasi a sinistra, 4 rischi a destra).

**Testo**:
- **Titolo**: *Memoria — fasi operative e rischi*
- **Colonna sinistra — 3 fasi operative**:
  - **Estrazione** — un sub-agent scorre la conversazione ed estrae fatti memorizzabili ("l'utente preferisce risposte brevi")
  - **Gestione** — i fatti vengono organizzati, deduplicati, aggiornati quando cambiano
  - **Recupero** — al turno successivo, i fatti rilevanti vengono iniettati nel contesto
- **Colonna destra — 4 rischi**:
  - **Memoria obsoleta** — salva un fatto che cambia nel tempo, non si aggiorna da sé
  - **Privacy** — cosa viene salvato, per quanto, con quale consenso (GDPR)
  - **Cross-contamination** — memoria di una conversazione influenza un'altra dove non dovrebbe
  - **Gaslight da memoria** — l'agente "ricorda" cose false iniettate in passato da utente o attaccante

**Visual**: le due card.

---

## Slide 51 — Sandbox — confini dell'esecuzione

**Layout**: titolo + definizione + tabella + riquadro.

**Testo**:
- **Titolo**: *Sandbox — confini dell'esecuzione*
- **Definizione**: *Ambiente isolato in cui l'agente esegue codice, bash, tool che manipolano il mondo — con confini tecnici verificabili.*
- **Tabella** (5 righe, invariata):

  | Confine | Perché conta |
  |---|---|
  | Filesystem limitato | L'agente accede solo alle cartelle di lavoro designate |
  | Rete limitata | Solo endpoint autorizzati — no exfiltration, no lateral movement |
  | Credenziali limitate | Minimo privilegio — l'agente non ha più accesso di quanto serve |
  | Tempo limitato | Ogni esecuzione scade — previene loop infiniti e consumo silenzioso |
  | Risorse limitate | CPU, memoria, disco espliciti — previene denial-of-service accidentale |

- **Riquadro**: *Sandbox è alla sicurezza degli agenti quello che il container è al deployment del software. Nessun agente serio gira senza.*

**Visual**: la tabella.

---

## Slide 52 — Harness landscape — chi c'è oggi

**Layout**: titolo + nota introduttiva + immagine.

**Testo**:
- **Titolo**: *Harness landscape — chi c'è oggi*
- **Nota introduttiva**: *Il modello è sempre più commodity. La differenziazione si sposta qui.*
- **Immagine**: `https://pbs.twimg.com/media/HFt-18tagAABD_I?format=jpg&name=large`

**Visual**: immagine esterna.

---

## Slide 53 — Building block e composizione

**Layout**: titolo + SVG a strati concentrici + riquadro.

**Testo**:
- **Titolo**: *Building block e composizione*
- **Visual SVG**: diagramma a strati concentrici (già prodotto come `svg/slide59-mattoncini.svg`)

*Prompt SVG originale*:
> Diagramma a strati concentrici quadrati o rettangolari, dal più piccolo al più grande.
> Strato 1 (centro, più piccolo): "Loop atomico — token per token"
> Strato 2 (intorno al 1): "Loop conversazionale — turno per turno · system prompt · statelessness"
> Strato 3 (intorno al 2): "Loop agentico con tool — decidi, agisci, osserva · sub-agent · eval · MCP"
> Strato 4 (esterno, più grande): "Loop agentico con codice — scrivi, esegui, verifica · TDD · sandbox · verificabilità"
> Sul lato destro, una barra verticale con colore accento che attraversa tutti gli strati dall'alto al basso, etichettata: "Context engineering — compaction · pruning · skill · modellazione della conoscenza · memoria · harness". La barra indica che la disciplina si applica a tutti i livelli.
> Stile minimale, ordinato, monocromatico con un colore accento per la barra trasversale.

- **Riquadro**: *Da domani, quando si parlerà di AI agentica, si sentiranno suonare dei concetti. Quelli sono i building block.*

**Nota**: il termine "mattoncini" è stato sostituito con "building block" sia nel titolo che nel testo del riquadro. La barra trasversale del SVG può essere rietichettata se si produce una nuova versione del file.

---

## Slide 54 — I quattro loop in un colpo d'occhio

**Layout**: titolo + SVG 4 mini-loop in riga + 1 riga di chiusura.

**Testo**:
- **Titolo**: *I quattro loop in un colpo d'occhio*
- **Visual SVG**: 4 mini-schemi affiancati, stessa altezza, separati da frecce sottili di progressione

*Prompt SVG*:
> Quattro mini-schemi affiancati in orizzontale, stessa altezza, separati da frecce sottili di progressione. Ogni riquadro ha: numero del loop (1/4 … 4/4), titolo breve, topologia minimale ridotta all'essenza, una sola label con la novità.
> - **1/4 — Atomico (token)**: linea orizzontale con 3 token sequenziali che escono da un blocco "LLM". Label: *"genera un token alla volta"*.
> - **2/4 — Conversazionale (turno)**: cerchio chiuso a 3 nodi (utente → modello → contesto che cresce → utente). Label: *"statelessness + system prompt"*.
> - **3/4 — Agentico con tool (azione)**: stesso cerchio del 2/4, con un sub-ciclo laterale sul nodo modello (tool call → result → modello, "N volte"). Sub-ciclo in colore accento. Label: *"il modello decide cosa fare"*.
> - **4/4 — Con codice (verifica)**: cerchio chiuso a 4 nodi (task → scrivi → esegui → verifica → back a scrivi se fail). Freccia di ritorno in colore accento con etichetta "feedback deterministico". Label: *"si corregge da solo"*.
> Ogni riquadro riprende la grammatica visiva del suo loop originale (Slide 8, 20, 31, 44) ma semplificata al minimo. Stile monocromatico con accento coerente con il resto della lezione.

- **Riga di chiusura** (corsivo, sotto il visual): *Ogni loop contiene il precedente. Il contesto cresce ad ogni livello — ed è per questo che esiste il livello finale, la disciplina.*

**File SVG nuovo**: `svg/slide54-loop-recap.svg`.

---

## Sintesi modifiche v1 → v2

| Modifica | Dettaglio |
|---|---|
| Opener riformulato | Da lista-recap a bridge frame con 2 sottotitoli, coerente con Sez. 4/5/6 |
| Nuova Slide 46 | *Context engineering come disciplina* — mappa delle 4 leve, colma il vuoto tra harness e tecniche |
| Merge 47+48 → 48 | Tabella MCP vs Skill + meccanica skill in un'unica slide (la tabella da sola era sottile) |
| Split memoria rinominato | 49 *"demistificazione e meccanica"* (con SVG), 50 *"fasi operative e rischi"* |
| Sandbox spostata | Da posizione 49 a posizione 51 — dopo le leve del contesto, come "confini dell'esecuzione" |
| Recap testuale eliminato | Ex Slide 53 rimossa: Mattoncini / Building block è già il recap visivo |
| Rinominata 54 → 53 | *Mattoncini* → *Building block* (titolo e riquadro) |
| Nuova Slide 54 | *I quattro loop in un colpo d'occhio* — recap finale dedicato ai loop |

**Totale**: 11 slide (stesso conteggio della v1), con gerarchia esplicita attore → leve → chiusura.

---

## Riepilogo visivi Sezione 7

| Slide | Titolo | Visual | File SVG |
|---|---|---|---|
| 44 | Context engineering | SVG convergenza | `slide46-ce-opener.svg` |
| 45 | Harness | nessuno | — |
| 46 | CE come disciplina | griglia 4 leve | — |
| 47 | Compaction e pruning | 2 card contrast | — |
| 48 | Progressive disclosure — skill | tabella + SVG | `slide50-skill-pattern.svg` |
| 49 | Memoria — demistificazione | SVG ciclo | `slide56-memoria-ciclo.svg` |
| 50 | Memoria — fasi e rischi | 2 card | — |
| 51 | Sandbox | tabella | — |
| 52 | Harness landscape | immagine esterna | — |
| 53 | Building block | SVG strati + barra | `slide59-mattoncini.svg` |
| 54 | Loop recap | SVG 4 mini-loop | `slide54-loop-recap.svg` (nuovo) |
