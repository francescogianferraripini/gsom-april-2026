# Specifica slide — Sezione 7: Context Engineering
## MBA Politecnico di Milano — LLM e agenti AI

---

## Slide 44 — Context engineering

**Layout:** Titolo + riga introduttiva + lista bullet

**Titolo:** Context engineering

**Corpo:**
Breve intro descrittiva che spiega cosa si intende per context engineering, seguita da lista dei concetti già visti nelle sezioni precedenti, re-etichettati esplicitamente come context engineering:

- Il system prompt che definisce l'agente
- La scelta di quali tool esporre
- I sub-agent per isolare lavoro sporco
- Il caveat MCP "non connetterli tutti"
- La sintesi dei tool result

**Visual:** Nessuno.

---

## Slide 45 — Harness — chi fa davvero le cose

**Layout:** Titolo + definizione + lista bullet + riquadro con bordo

**Titolo:** Harness — chi fa davvero le cose

**Definizione:** Il software che circonda il modello e gestisce tutto ciò che non è pura generazione di testo.

**Corpo:** Lista bullet, 6 voci con una riga di spiegazione ciascuna:

- **Costruisce e mantiene il contesto** — assembla system prompt, storico turni, tool definition, tool result ad ogni chiamata API
- **Esegue i tool quando il modello li richiama** — intercetta la richiesta strutturata del modello e la traduce in chiamata reale
- **Applica policy di sicurezza e autorizzazione** — decide quali azioni sono permesse in base al contesto e all'utente
- **Orchestra i sub-agent** — lancia agenti figli, raccoglie le sintesi, le restituisce al padre
- **Gestisce lo stato persistente** — memoria, sessioni, contesti tra conversazioni diverse
- **Fornisce osservabilità** — log, tracce, metriche per debugging e monitoring in produzione

**Riquadro con bordo:**
Quando si dice "Claude ha fatto X", Claude ha deciso X e l'harness ha eseguito X. Il confine è sottile ma cruciale — quasi tutta la sicurezza, l'affidabilità, la qualità di un agente in produzione vivono nell'harness.

**Visual:** Nessuno.

---

## Slide 46 — Compaction e pruning — gestire il contesto che cresce

**Layout:** Titolo + due colonne affiancate simmetriche + riquadro con bordo

**Titolo:** Compaction e pruning — gestire il contesto che cresce

**Corpo:** Due colonne affiancate simmetriche.

**Colonna sinistra — Pruning:**
- **Definizione:** Tagliare via parti del contesto non più rilevanti (tool result vecchi, turni obsoleti)
- **Policy:** Quali informazioni sono sicure da dimenticare?
- **Rischio:** Dimenticare qualcosa che serviva

**Colonna destra — Compaction:**
- **Definizione:** Sostituire parti del contesto con una loro sintesi
- **Policy:** Tipicamente un sub-agent riassume gli ultimi N turni e la sintesi rimpiazza gli originali
- **Rischio:** La sintesi perde dettagli che emergeranno come importanti più avanti

**Riquadro con bordo:**
Entrambe sono lossy — si perde informazione in cambio di spazio. La scelta di cosa comprimere o buttare è una delle decisioni più delicate di un agente in produzione. Non esiste policy universale — dipende dal task.

**Visual:** Nessuno.

---

## Slide 47 — Progressive disclosure — caricare conoscenza on-demand

**Layout:** Titolo + tabella comparativa

**Titolo:** Progressive disclosure — caricare conoscenza on-demand

**Corpo:** Tabella comparativa MCP vs Skill su 3 dimensioni:

| | MCP | Skill |
|---|---|---|
| Tool definition | Sempre in contesto | Descrizione minima in contesto |
| Costo | Fisso all'inizio della sessione | Pagato solo se la skill viene caricata |
| Efficienza | Inefficiente se pochi tool servono davvero | Carica solo il necessario |

**Visual:** La tabella stessa.

---

## Slide 48 — Skill — il pattern tecnico

**Layout:** Titolo + definizione + esempio + richiamo bash + visual SVG

**Titolo:** Skill — il pattern tecnico

**Definizione:** Una directory con documentazione, istruzioni, esempi, eventuali script. Un file principale (SKILL.md) spiega al modello cosa la skill offre e come usarla.

**Esempio:** Skill "prodotti e pricing" → directory con SKILL.md (istruzioni di navigazione), listino prodotti strutturato, regole di sconto, riferimenti a tool specifici.

**Richiamo bash:** In Claude Code, il meccanismo sottostante è il tool bash — il modello esplora la directory e legge i file. Altri harness usano meccanismi proprietari equivalenti.

**Visual:** SVG unico con due aree affiancate.

*Prompt per SVG:*
> Schema diviso in due aree affiancate. Area sinistra: struttura directory a forma di albero. Cartella radice `skills/`, sotto-cartella `prodotti-pricing/`, file interni: `SKILL.md` (evidenziato con colore accento), `listino/`, `regole/`, `esempi/`. Annotazione accanto a SKILL.md: "sempre visibile al modello (1 riga di descrizione)". Annotazione sul resto della directory: "caricato on-demand". Area destra: meccanica in 3 passi con frecce verticali numerate: (1) "modello vede solo descrizione minima della skill" → (2) "decide che serve, richiede caricamento" → (3) "harness carica contenuto SKILL.md nel contesto". Stile minimale, monocromatico con un colore accento.

---

## Slide 49 — Modellazione della conoscenza — 1: dai dati all'architettura informativa

**Layout:** Titolo + due colonne (SVG piramide a sinistra, testo a destra) + riquadro con bordo

**Titolo:** Modellazione della conoscenza — 1: dai dati all'architettura informativa

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

---

## Slide 50 — Modellazione della conoscenza — 2: l'Enterprise Knowledge Graph

**Layout:** Titolo + definizione + due colonne (SVG struttura EKG a sinistra, testo a destra) + riquadro con bordo

**Titolo:** Modellazione della conoscenza — 2: l'Enterprise Knowledge Graph

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

---

## Slide 51 — Modellazione della conoscenza — 3: il Knowledge Graph come contesto per gli agenti

**Layout:** Titolo + concetto chiave + SVG (sopra) + due colonne retrieval/learning + lista bullet vantaggi + riquadro con bordo

**Titolo:** Modellazione della conoscenza — 3: il Knowledge Graph come contesto per gli agenti

**Concetto chiave:** L'Enterprise Knowledge Graph è il contesto comune che più agenti AI condividono per migliorare ricerca, interrogazione dei dati e supporto agli utenti nell'estrazione di insight.

**Visual SVG:** Ciclo virtuoso EKG ↔ agenti.

*Prompt per SVG:*
> Diagramma orizzontale in due blocchi verticali. In alto, una fila di 4-5 triangoli identici che rappresentano agenti AI (ognuno con una piccola fumetto/chat bubble al centro con scritta "AI"). In basso, il trapezio "ENTERPRISE KNOWLEDGE GRAPH" con i tre strati già descritti (ontology in alto, data products al centro, physical assets in basso) — stesso stile della slide 50 ma più schematico. Tra agenti e EKG, due frecce verticali affiancate: una freccia in su etichettata "RETRIEVAL" (dall'EKG verso gli agenti), una freccia in giù etichettata "LEARNING" (dagli agenti verso l'EKG). Le due frecce evidenziano il ciclo bidirezionale. Stile minimale, monocromatico con colore accento.

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
L'EKG è la forma aziendale di ciò che, nel pattern agente, abbiamo chiamato skill: una mappa navigabile ai domini di conoscenza, collegata a dati reali e governata. Se il prossimo progetto AI parte con "prendiamo i PDF e mettiamoli in un vector store", fermarsi. Partire da: quali sono i domini di conoscenza, chi ne è owner, qual è l'ontologia, quali data product li espongono.

**Visual:** SVG ciclo retrieval/learning tra agenti AI e EKG (descritto sopra).

---

## Slide 52 — Sandboxes — confini espliciti per l'esecuzione

**Layout:** Titolo + definizione + tabella + riquadro con bordo

**Titolo:** Sandboxes — confini espliciti per l'esecuzione

**Definizione:** Ambiente isolato in cui l'agente esegue codice, bash, tool che manipolano il mondo, con confini tecnici verificabili.

**Tabella:**

| Confine | Perché conta |
|---|---|
| Filesystem limitato | L'agente accede solo alle cartelle di lavoro designate |
| Rete limitata | Solo endpoint autorizzati — no exfiltration, no lateral movement |
| Credenziali limitate | Principio di minimo privilegio — l'agente non ha più accesso di quanto serve |
| Tempo limitato | Ogni esecuzione scade — previene loop infiniti e consumo silenzioso di risorse |
| Risorse limitate | CPU, memoria, disco espliciti — previene denial-of-service accidentale |

**Riquadro con bordo:**
Sandbox è alla sicurezza degli agenti quello che il container è al deployment del software. Nessun agente serio gira senza.

**Visual:** La tabella stessa.

---

## Slide 53 — Memoria — demistificazione

**Layout:** Titolo + riga introduttiva + lista bullet + riquadro con bordo

**Titolo:** Memoria — demistificazione

**Riga introduttiva:** "Memoria" è un termine abusato. Suggerisce che il modello ricordi nel senso umano. Non è così.

**Meccanica** (bullet):

- Il modello è stateless — nessuna memoria tra chiamate (richiamo Slide 10)
- La "memoria" è un sistema esterno gestito dall'harness
- L'harness decide cosa salvare fuori dal contesto corrente (fatti sull'utente, preferenze, sintesi di conversazioni passate)
- Lo salva in archivio persistente (DB, vector store, file)
- Al turno successivo, l'harness recupera i fatti rilevanti e li inietta nel contesto

**Riquadro con bordo:**
Memoria dell'agente = RAG sulle sue stesse conversazioni passate. Non è che il modello "si ricorda di voi" — è che l'harness ha archiviato fatti su di voi e ve li re-inietta nel contesto quando parlate di nuovo.

**Visual:** Nessuno.

---

## Slide 54 — Memoria — meccanica e rischi

**Layout:** Titolo + visual SVG + lista bullet fasi + lista bullet rischi

**Titolo:** Memoria — meccanica e rischi

**Visual SVG:** Diagramma a due sessioni nel tempo con archivio al centro.

*Prompt per SVG:*
> Diagramma orizzontale con tre colonne. Colonna sinistra "Sessione 1": utente e modello che si scambiano messaggi (bolle alternate), sotto una freccia con etichetta "harness estrae fatti" che punta verso il centro. Colonna centrale "Archivio persistente": rettangolo con etichetta "DB / vector store", riceve frecce dalla sessione 1 (salvataggio) e invia frecce alla sessione 2 (recupero). Una freccia orizzontale con etichetta "tempo" collega le due sessioni. Colonna destra "Sessione 2": freccia dall'archivio con etichetta "harness inietta fatti nel contesto" che precede la conversazione, poi utente e modello che si scambiano messaggi con un'annotazione "memoria già presente". Stile minimale, monocromatico con colore accento per le frecce harness → archivio → harness.

**3 fasi operative:**

- **Estrazione:** Un sub-agent periodicamente scorre la conversazione ed estrae fatti memorizzabili ("l'utente preferisce risposte brevi", "lavora su progetto X")
- **Gestione:** I fatti vengono organizzati, deduplicati, aggiornati quando cambiano
- **Recupero:** Al turno successivo, i fatti rilevanti vengono recuperati e iniettati nel contesto

**4 rischi:**

- **Memoria obsoleta:** Salva un fatto che cambia nel tempo — la memoria non si aggiorna automaticamente
- **Privacy:** Cosa viene salvato, per quanto, con quale consenso — rilevante per GDPR
- **Cross-contamination:** Memoria di una conversazione influenza un'altra dove non dovrebbe
- **Gaslight da memoria:** L'agente "ricorda" cose false iniettate in passato da utente o attaccante

**Visual:** SVG ciclo memoria (descritto sopra).

---

## Slide 55 — Harness landscape — chi c'è oggi

**Layout:** Titolo + nota introduttiva + immagine

**Titolo:** Harness landscape — chi c'è oggi

**Nota introduttiva:** Il modello è sempre più commodity. La differenziazione si sposta qui.

**Corpo:** Immagine da includere:
`https://pbs.twimg.com/media/HFt-18tagAABD_I?format=jpg&name=large`

**Visual:** Immagine esterna (URL sopra).

---

## Slide 56 — Context engineering — recap

**Layout:** Titolo + due colonne da 3 voci ciascuna

**Titolo:** Context engineering — recap

**Corpo:** 2 colonne da 3 voci ciascuna, label in grassetto + mezza riga descrittiva.

**Colonna sinistra:**
- **Harness** — il software che circonda il modello e gestisce esecuzione, sicurezza, orchestrazione
- **Compaction e pruning** — ridurre il contesto cresciuto, con perdita di informazione controllata
- **Progressive disclosure via skill** — caricare nel contesto solo ciò che serve, quando serve

**Colonna destra:**
- **Modellazione della conoscenza** — strutturare ciò che l'agente deve poter trovare e navigare
- **Sandbox** — confini tecnici espliciti per l'esecuzione sicura
- **Memoria** — persistenza delle informazioni rilevanti oltre la singola sessione

**Note:** Nessun testo di chiusura. Transizione alla demo gestita a voce.

**Visual:** Nessuno.

---

## Slide 57 — Mattoncini e composizione

**Layout:** Titolo + visual SVG a strati concentrici + riquadro con bordo

**Titolo:** Mattoncini e composizione

**Visual SVG:** Diagramma a strati concentrici.

*Prompt per SVG:*
> Diagramma a strati concentrici quadrati o rettangolari, dal più piccolo al più grande.
> Strato 1 (centro, più piccolo): "Loop atomico — token per token"
> Strato 2 (intorno al 1): "Loop conversazionale — turno per turno · system prompt · statelessness"
> Strato 3 (intorno al 2): "Loop agentico con tool — decidi, agisci, osserva · sub-agent · eval · MCP"
> Strato 4 (esterno, più grande): "Loop agentico con codice — scrivi, esegui, verifica · TDD · sandbox · verificabilità"
> Sul lato destro, una barra verticale con colore accento che attraversa tutti gli strati dall'alto al basso, etichettata: "Context engineering — compaction · pruning · skill · modellazione della conoscenza · memoria · harness". La barra indica che la disciplina si applica a tutti i livelli.
> Stile minimale, ordinato, monocromatico con un colore accento per la barra trasversale.

**Riquadro con bordo:**
Da domani, quando si parlerà di AI agentica, si sentiranno suonare dei concetti. Quelli sono i mattoncini.

---

## Riepilogo visivi Sezione 7

| Slide | Titolo | Visual |
|---|---|---|
| 44 | Context engineering | Nessuno |
| 45 | Harness | Nessuno |
| 46 | Compaction e pruning | Nessuno |
| 47 | Progressive disclosure | Tabella MCP vs Skill |
| 48 | Skill — il pattern tecnico | SVG: directory + meccanica (unico) |
| 49 | Modellazione conoscenza — 1: piramide architettura informativa | SVG: piramide DIKW (Data → Information → Knowledge → Intelligence) |
| 50 | Modellazione conoscenza — 2: Enterprise Knowledge Graph | SVG: trapezio EKG a tre strati (ontology / data products / physical assets) |
| 51 | Modellazione conoscenza — 3: contesto per gli agenti | SVG: ciclo retrieval/learning tra agenti AI e EKG |
| 52 | Sandboxes | Tabella confini |
| 53 | Memoria — demistificazione | Nessuno |
| 54 | Memoria — meccanica e rischi | SVG: ciclo memoria due sessioni |
| 55 | Harness landscape | Immagine esterna (URL) |
| 56 | Context engineering recap | Nessuno |
| 57 | Mattoncini e composizione | SVG: strati concentrici + barra trasversale |
