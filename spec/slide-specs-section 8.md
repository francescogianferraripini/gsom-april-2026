# Specifica slide — Sezione 8: Proteggere
## MBA Politecnico di Milano — LLM e agenti AI

**Stato**: v1 — consolidata per rendering (ott. 2026).
**Idea ordinante**: ogni capacità data all'agente è anche una superficie d'attacco. Tre fronti: (1) usare l'AI significa trasferire dati al provider; (2) l'agente può portare fuori dati, da solo o istruito da un contenuto; (3) i coding agent sono un'arma e uno scudo. Filo conduttore del fronte 3: la verificabilità del codice (Sezione 6).
**Taglio**: misto — meccanismo spiegato riusando i concetti del deck (contesto, tool, harness, sandbox) + implicazioni per un manager. Nessun payload operativo.

---

## Indice slide

| # | Titolo | File | Visual |
|---|---|---|---|
| — | Divider *Proteggere* | `slide-div-sec8.html` | barra 8 icone (`fa-shield-halved`) |
| 55 | *Ogni capacità è una superficie d'attacco* (opener) | `slide63-apertura-sec8.html` | SVG perimetro + 3 flussi |
| — | Sotto-divider *Fronte 1 · Usare l'AI* | `slide-div-sec8-f1.html` | barra 3 icone |
| 56 | *Ogni prompt è un trasferimento di dati* | `slide64-prompt-trasferimento.html` | tabella canali |
| 57 | *Il rischio è il canale e il contratto* | `slide65-canale-contratto.html` | 2 card (Samsung, IBM) |
| — | Sotto-divider *Fronte 2 · Agenti che esfiltrano* | `slide-div-sec8-f2.html` | barra 3 icone |
| 58 | *La lethal trifecta* | `slide66-lethal-trifecta.html` | SVG Venn a 3 cerchi |
| 59 | *Prompt injection e fuga "per zelo"* | `slide67-injection-zelo.html` | 2 card contrast |
| — | Sotto-divider *Fronte 3 · Coding agent* | `slide-div-sec8-f3.html` | barra 3 icone |
| 60 | *Si abbassa il costo dell'attacco* | `slide68-costo-attacco.html` | 2 card con numeri |
| 61 | *Stessa capacità, usata per primi da noi* | `slide69-difesa.html` | card principale + 3 card |
| 62 | *Tre fronti, tre domande* (chiusura) | `slide70-tre-domande.html` | tabella + riquadro take-home |

---

## Divider — Sezione 8

- **Etichetta**: *Sezione 8 di 8*
- **Titolo**: *Proteggere*
- **Sottotitolo**: *L'AI come rischio e come arma*
- **Barra icone**: 8 icone; l'ottava (`fa-shield-halved`, *Proteggere*) è attiva. Tutti i divider precedenti sono stati aggiornati a "di 8" con l'ottava icona attenuata.

---

## Sotto-divider dei tre fronti

Slide di separazione tra i tre fronti, con classe `subsection-divider` (in `styles.css`): sfondo chiaro, per distinguerle dai divider di sezione scuri. Struttura: etichetta *Sezione 8 · Fronte N di 3*, titolo accent, sottotitolo muted, barra di 3 icone con il fronte corrente attivo e gli altri attenuati.

| File | Titolo | Sottotitolo | Icona |
|---|---|---|---|
| `slide-div-sec8-f1.html` | *Usare l'AI* | *I dati escono con il prompt* | `fa-cloud-arrow-up` |
| `slide-div-sec8-f2.html` | *Agenti che esfiltrano* | *Quando l'agente porta fuori i dati* | `fa-user-secret` |
| `slide-div-sec8-f3.html` | *Coding agent* | *L'AI come arma e come scudo* | `fa-code` |

Posizione: rispettivamente prima delle slide 56, 58 e 60.

---

## Slide 55 — Ogni capacità è una superficie d'attacco (opener)

**Layout**: titolo + 1 riga di lead + SVG.

**Testo**:
- **Titolo**: *Ogni capacità è una superficie d'attacco*
- **Lead**: *Abbiamo dato all'agente contesto, tool e codice. Ogni capacità che aggiungiamo è anche una superficie d'attacco. Tre fronti:*

**Visual SVG**: `svg/slide63-tre-fronti.svg`

*Prompt SVG*:
> Al centro un frame tratteggiato accent etichettato **LA TUA ORGANIZZAZIONE**. Dentro: *Dati riservati* (box accent chiaro, centro-destra), collegato con linee tratteggiate grigie a *Persone* (sopra) e *Agente AI* (sotto); a sinistra *Coding agent · review, ricerca vulnerabilità* con didascalia *"… e come scudo"*. Fuori a destra: *Provider LLM* (didascalia *"i dati escono con il prompt"*) e *Terze parti* (didascalia *"l'agente li manda fuori"*). Fuori a sinistra: *Attaccante + coding agent* (didascalia *"l'AI come arma …"*). Tre frecce accent numerate in cerchi pieni: 1 Persone → Provider, 2 Agente → Terze parti, 3 Attaccante → Coding agent. Riga muted in fondo: *"1 e 2 sono dati in uscita · 3 è capacità: in entrata per chi attacca, interna per chi difende"*. Monocromatico, accent #a1245a.

---

## Slide 56 — Ogni prompt è un trasferimento di dati

**Layout**: titolo + lead + tabella 3 righe + riquadro caso + fonti.

**Testo**:
- **Lead**: *Quando chiamo un LLM, tutto il contesto — system prompt, documenti, storico, tool result — esce dal perimetro. Quattro domande: dove finisce, per quanto resta, se addestra il modello, sotto quale giurisdizione.*
- **Tabella** (provider in forma generica, dettaglio sotto):

| Canale | Usato per il training? | Retention tipica |
|---|---|---|
| API a pagamento · enterprise | No, di default | ~30 giorni per abuse monitoring · zero-data-retention su accordo |
| API tier gratuito | Possibile, con revisione umana | Il provider stesso avverte: non inviare dati riservati |
| App consumer personale | Spesso sì, o a scelta dell'utente | Da mesi ad anni — fino a 5 anni se si accetta il training |

- **Riquadro**: *NYT vs OpenAI (2025) — un giudice ordina di conservare tutti i log, chat cancellate comprese, per mesi. "Cancellato" dipende dal contratto e dalla giurisdizione, non dal pulsante.*

**Dettaglio per il docente** (non in slide):
- OpenAI API: niente training senza opt-in (dal 01/03/2023); log abuse monitoring fino a 30 giorni; ZDR su approvazione. https://developers.openai.com/api/docs/guides/your-data
- Anthropic API/commerciale: cancellazione entro 30 giorni di default. https://privacy.claude.com/en/articles/7996866
- Anthropic consumer (28/08/2025): scelta dell'utente sul training; se sì retention 5 anni, se no 30 giorni; esclusi API, Claude for Work, Bedrock, Vertex. https://www.anthropic.com/news/updates-to-our-consumer-terms
- Gemini API: tier gratuito usato per migliorare i prodotti, con revisori umani e avviso esplicito a non inviare dati riservati; tier a pagamento no. https://ai.google.dev/gemini-api/terms
- NYT vs OpenAI: ordine di conservazione del 13/05/2025, terminato con ordine del 09/10/2025 (effetto dal 26/09/2025); i log già conservati restano.

**Fonti in slide**: policy dati OpenAI API, Anthropic, Google Gemini API (consultate ott. 2026) · Anthropic, *Updates to our consumer terms*, 28/08/2025 · In re OpenAI Copyright Litig., ordini 13/05/2025 e 09/10/2025.

---

## Slide 57 — Il rischio è il canale e il contratto

**Layout**: titolo + lead + 2 card (Samsung | IBM con 3 numeri) + riquadro + riga closed/open + fonti.

**Testo**:
- **Lead**: *Lo stesso modello ha profili di rischio opposti a seconda di come ci si arriva. Lo shadow AI è il dipendente che sceglie il canale sbagliato.*
- **Card Samsung · aprile 2023**: *Ingegneri incollano codice sorgente proprietario in ChatGPT per fare debug. Poche settimane dopo: divieto di AI generativa sui dispositivi aziendali.*
- **Card IBM Cost of a Data Breach · 2025**: *1 su 5* organizzazioni con una violazione legata allo shadow AI · *+670K $* costo medio in più per violazione · *63%* delle organizzazioni violate senza policy di governance AI.
- **Riquadro**: *Vietare non basta: se il canale aziendale non c'è, o è peggiore, si usa quello personale. La leva è offrire il canale giusto — contrattualizzato, con zero-data-retention dove serve.*
- **Riga closed/open**: *E il modello open self-hosted (Sezione 3)? Il trasferimento sparisce — ma sicurezza, aggiornamenti e responsabilità diventano tutti tuoi.*

**Fonti**: TechCrunch, 02/05/2023 · IBM, *Cost of a Data Breach Report 2025*, 30/07/2025.
**Da non usare**: la cifra "97% senza controlli di accesso AI" attribuita a IBM — non verificata.

---

## Slide 58 — La lethal trifecta

**Layout**: titolo + lead + griglia 2 colonne (SVG a sinistra | "togli un vertice" a destra) + fonte.

**Testo**:
- **Lead**: *Un agente diventa pericoloso quando ha insieme tre cose. Prese una a una sono innocue; tutte e tre insieme, chi scrive un contenuto può far uscire i tuoi dati.*
- **Colonna destra** — *Togli un vertice e l'attacco si spezza:*
  - **Niente dati privati** — l'agente che legge il web lavora su fonti pubbliche
  - **Niente contenuti non fidati** — l'agente sui dati interni non legge email esterne
  - **Niente canale esterno** — rete bloccata, ogni invio approvato da un umano
  - Riquadro: *È una decisione di design, non una patch.*

**Visual SVG**: `svg/slide66-lethal-trifecta.svg`

*Prompt SVG*:
> Diagramma di Venn a 3 cerchi grigi semitrasparenti: *Dati privati* (email, documenti, database interni), *Contenuti non fidati* (web, email in arrivo, issue), *Canale verso l'esterno* (inviare email, chiamate HTTP, scrivere su repo pubblici). Solo l'intersezione tripla è piena in accent #a1245a con la scritta bianca **RISCHIO**. Didascalia accent corsivo in fondo: *"chi controlla il contenuto controlla l'agente"*.

**Fonte**: Simon Willison, *The lethal trifecta for AI agents*, 16/06/2025 — https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/

---

## Slide 59 — Prompt injection e fuga "per zelo"

**Layout**: titolo + 2 card contrast + riga "perché funziona" + riquadro mitigazioni + fonti.

**Testo**:
- **Card sinistra — Prompt injection** (*qualcuno scrive istruzioni dentro i dati*):
  1. Arriva un'email con istruzioni nascoste
  2. L'assistente la legge: entra nel contesto
  3. Esegue le istruzioni: raccoglie dati interni
  4. Li codifica in un link verso un server esterno
  - *EchoLeak — Microsoft 365 Copilot, giu. 2025, gravità 9.3/10: zero click.*
  - *Anche: GitHub MCP (mag. 2025) — un issue pubblico porta l'agente a copiare dati privati in una pull request pubblica.*
- **Card destra — Fuga "per zelo"** (*nessun attaccante: l'agente fa il suo lavoro, troppo*):
  - Cerca sul web con nomi e numeri del cliente nella query
  - Allega il documento sbagliato a un'email
  - Pubblica una credenziale in un repo o in un issue
  - Passa dati a un server MCP di terze parti
  - *E non solo riservatezza: Replit (lug. 2025) — l'agente cancella il database durante un code freeze.*
- **Perché funziona**: *per il modello istruzioni e dati sono lo stesso testo nel contesto (Sezione 2).*
- **Mitigazioni**: *minimo privilegio · sandbox e rete limitata (Sezione 7) · approvazione umana per ogni azione verso l'esterno.*

**Fonti**: Aim Security / MSRC, CVE-2025-32711, giu. 2025 · Invariant Labs, 26/05/2025 · OECD AI Incidents, Replit, 19/07/2025.
**Caso di riserva** (non in slide): Supabase MCP, lug. 2025 — istruzioni in un ticket di supporto portano un agente Cursor con chiave `service_role` a leggere la tabella dei token e riscriverla nel ticket. https://simonwillison.net/2025/Jul/6/supabase-mcp-lethal-trifecta/

---

## Slide 60 — Si abbassa il costo dell'attacco

**Layout**: titolo + lead + card principale (2 numeri + dettaglio) + card secondaria + nota visibilità + fonti.

**Testo**:
- **Lead**: *Un attacco sofisticato richiedeva un team esperto. Oggi un attore piccolo orchestra un coding agent che fa gran parte del lavoro: ricognizione, exploit, movimento laterale.*
- **Card — Cyber-spionaggio orchestrato con Claude Code · nov. 2025**: *~30* obiettivi (tech, finanza, chimica, enti pubblici) · *80–90%* del lavoro tattico svolto dall'AI, umani solo nei punti decisionali · *Gruppo attribuito a un attore statale cinese; riuscito in un numero ridotto di casi. L'agente ha anche allucinato credenziali: i limiti di affidabilità valgono anche per chi attacca.*
- **Card — "Vibe hacking" · ago. 2025**: *Un singolo attore estorce almeno 17 organizzazioni — sanità, servizi di emergenza, enti pubblici. L'agente sceglie quali dati rubare e scrive le richieste di riscatto, a volte oltre 500K $.*
- **Nota**: *I casi documentati vengono dai provider che li rilevano sulle proprie piattaforme: è un limite di visibilità, non un'esclusiva.*

**Fonti**: https://www.anthropic.com/news/disrupting-AI-espionage (13/11/2025) · https://www.anthropic.com/news/detecting-countering-misuse-aug-2025 (27/08/2025).

---

## Slide 61 — Stessa capacità, usata per primi da noi

**Layout**: titolo + lead + card principale con bordo accent + 3 card + riquadro pratico + fonti.

**Testo**:
- **Lead**: *Il codice è verificabile (Sezione 6): un exploit funziona o no, una vulnerabilità si riproduce o no. Per questo l'AI migliora in fretta — da entrambi i lati.*
- **Card principale — Project Glasswing · apr. 2026**: *Un modello dato solo ai manutentori di software critico trova migliaia di vulnerabilità gravi — tra cui un bug di OpenBSD vecchio di 27 anni. I laboratori stessi trattano questa capacità come dual-use.*
- **3 card**:
  - *DARPA AIxCC · ago. 2025* — 18 zero-day reali trovati da sistemi autonomi, ~152 $ per task
  - *XBOW · giu. 2025* — un agente autonomo primo nella classifica USA di HackerOne
  - *Google Big Sleep · lug. 2025* — vulnerabilità SQLite trovata prima che fosse sfruttata
- **Riquadro**: *In pratica: review di sicurezza automatica su ogni pull request (es. Claude Code /security-review, OpenAI Codex Security). Nella pipeline, non una tantum.*

**Fonti**: https://www.anthropic.com/glasswing (07/04/2026) · https://www.darpa.mil/news/2025/aixcc-results (08/08/2025) · https://xbow.com/blog/top-1-how-xbow-did-it/ (24/06/2025) · Google, Big Sleep / CVE-2025-6965, lug. 2025.

---

## Slide 62 — Tre fronti, tre domande (chiusura)

**Layout**: titolo + tabella 3×4 + riquadro take-home. Chiude la sezione e l'intero deck.

**Tabella**:

| Fronte | Rischio | Controllo chiave | La domanda da fare |
|---|---|---|---|
| 1 · Usare l'AI | Dati riservati escono con il contesto verso il provider | Canale aziendale contrattualizzato, zero-data-retention, policy d'uso | *"Su quale canale passano i nostri dati, per quanto restano, addestrano il modello?"* |
| 2 · Agenti | L'agente porta fuori dati, da solo o istruito da un contenuto | Spezzare la trifecta: minimo privilegio, sandbox, approvazione umana | *"Questo agente ha insieme dati privati, input non fidati e un canale verso l'esterno?"* |
| 3 · Coding agent | Attacchi più economici, più rapidi, alla portata di pochi | Review e ricerca di vulnerabilità automatiche nella pipeline | *"Usiamo noi l'AI sul nostro codice prima che lo faccia un attaccante?"* |

- **Take-home**: *Un agente ha i permessi che gli dai. La sicurezza si decide nell'harness, non nel modello.*

---

## Note

- Solo deck italiano; porting nel deck EN (`lezione-mba-en/build.py`) e rigenerazione dei PDF da fare dopo la revisione.
- Le policy dei provider (slide 56) cambiano spesso: riverificarle prima di ogni edizione della lezione.
