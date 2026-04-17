# Specifica Sezione 3 — Modelli closed vs open
## Lezione MBA Politecnico di Milano — "Agents in action"
### Francesco Gianferrari Pini, Quantyca

**Stato**: slide 19, 20 consolidate.
**Prossima slide da definire**: Slide 21 (Sezione 4 — Tool calling).

---

## ✅ Slide 19 — Closed Model vs Open Weights vs Open Source

**Layout**: titolo in alto, tabella a 3 colonne al centro (occupa ~70% della slide), nota in basso.

**Testo**:
- Titolo: *Closed Model vs Open Weights vs Open Source*
- Tabella a 3 colonne:

| Categoria | Cosa è aperto | Esempi |
|---|---|---|
| Closed / API-only | Niente. Accesso solo via API del provider | GPT, Claude, Gemini |
| Open weight | Pesi scaricabili. Training code e dataset tipicamente no | Llama (Meta), Mistral, DeepSeek, Qwen, Gemma |
| Open source "vero" | Pesi + training code + dataset | OLMo (AllenAI) — tipicamente dietro la frontiera |

- Nota in basso: *"Open" quasi sempre significa open weight. I pesi sono scaricabili, ma training data e codice restano chiusi.*

**Visual**: nessuno oltre alla tabella.

---

## ✅ Slide 20 — Trade-off decisionale: quando closed, quando open

**Layout**: titolo in alto, tabella comparativa a 3 colonne nella metà superiore, nota moat subito sotto la tabella, riquadro visivo "Aggiornamento 2026" (box con bordo distinto) nella metà inferiore, take-home in chiusura.

**Testo**:
- Titolo: *Trade-off decisionale: quando closed, quando open*
- Tabella a 3 colonne:

| Dimensione | Closed | Open |
|---|---|---|
| Qualità di frontiera | In testa oggi | A 6-12 mesi, ma il gap si chiude |
| Costo a scala | Pay-per-token, lineare con l'uso | Costo infrastruttura fisso, marginale vicino a zero |
| Privacy / data residency | Dati al provider (tranne piani enterprise) | Totalmente in casa, sovrano |
| Customization | Fine-tuning limitato, no accesso ai pesi | Fine-tuning completo, quantizzazione, RAG |
| Effort di adozione | Zero infrastruttura | Richiede GPU, MLOps, competenze |
| Geopolitica / compliance | Dipendenza da vendor USA o Cina | Sovranità, compatibilità AI Act europeo |

- Nota moat *(collegamento a Slide 15, in evidenza sotto la tabella)*: *Con closed: paghi il token E regali le traiettorie. Con open: paghi l'infrastruttura, le traiettorie restano tue.*

- **Riquadro "Aggiornamento 2026"** *(box con bordo distinto, colore accento tenue di sfondo)*:
  *La frontiera si chiude più velocemente del previsto. Modelli open-weight da ~30B parametri (es. Gemma 4) raggiungono qualità comparabile a modelli closed di classe Sonnet 4.5 su molti task concreti, eseguibili in inferenza su singola GPU consumer (NVIDIA 4090). Open non è più solo "più economico" — è anche "di qualità comparabile" per molti casi d'uso. Il ritardo rispetto ai modelli di frontiera rimane tuttavia reale: circa 6 mesi.*

- Take-home *(in chiusura)*: *Closed per sperimentare velocemente, open per scalare volumi, privacy, customization. La scelta è per use case, non ideologica.*

**Visual**: tabella + riquadro "Aggiornamento 2026" con bordo e sfondo distinto.

---

# Prossima slide da definire: Slide 21 — Apertura Sezione 4 (Tool calling)
