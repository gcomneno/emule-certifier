# eMule-Certifier
_Un semplice strumento per certificare file locali confrontandoli con link ED2K._

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📖 Descrizione

**eMule-Certifier** è uno script in Python pensato per chi gestisce librerie di ebook o collezioni di file scaricati.  
Lo scopo è verificare se un file locale (PDF, EPUB, MOBI, AZW3) è già stato scaricato tramite eMule, confrontando l’**hash MD4** calcolato con quello contenuto nei link `ed2k://`.

Utile per:
- Controllare duplicati
- Creare report dei file già presenti
- Tenere ordinata la propria libreria

---

## ✨ Funzionalità

- ✅ Scansione ricorsiva di directory
- ✅ Calcolo dell’hash MD4 compatibile eMule
- ✅ Confronto con una lista di link ED2K
- ✅ Report CSV con i risultati
- ✅ Configurazione personalizzabile via `config.yaml`
- ✅ Barra di progresso per monitorare lo stato

---

## ⚙️ Installazione

Requisiti:
- Python **3.9 o superiore**
- Moduli indicati in `requirements.txt`

Clona il repository e installa le dipendenze:

```bash
git clone https://github.com/gcomneno/emule-certifier.git
cd emule-certifier
pip install -r requirements.txt
```

---

## 🚀 Utilizzo

Esempio di comando base:

```bash
python emule_certifier.py --input links.txt --path ./ebooks --output report.csv
```

Opzioni principali:
- `--input` → file di testo con link ED2K (uno per riga)
- `--path` → directory locale da scansionare
- `--output` → file CSV di report (default: `report.csv`)
- `--config` → file YAML alternativo per le impostazioni

---

## 📊 Esempio di Output

Esempio di `report.csv` generato:

```csv
file,hash,found
./ebooks/libro1.epub,0123456789ABCDEF0123456789ABCDEF,YES
./ebooks/libro2.pdf,ABCDEF0123456789ABCDEF0123456789,NO
```

---

## 🔧 Configurazione (`config.yaml`)

Puoi personalizzare il comportamento tramite un file YAML:

```yaml
# File di configurazione esempio
paths:
  - ./ebooks
  - ./pdfs
extensions: [".pdf", ".epub", ".mobi", ".azw3"]
output: report.csv
```

---

## ⚠️ Limitazioni

- Supporta solo i formati: **PDF, EPUB, MOBI, AZW3**
- Calcolo hash MD4 può essere lento su file molto grandi
- Non scarica file, si limita alla verifica

---

## 🛠️ Roadmap

- Parallelizzazione del calcolo hash
- Supporto a ulteriori formati
- Esportazione anche in JSON
- Interfaccia web minimale

---

## 🤝 Contributi

Contributi benvenuti!  
Apri una [issue](https://github.com/gcomneno/emule-certifier/issues) o una pull request con le tue proposte.

---

## 📜 Licenza

Distribuito sotto licenza **MIT**.  
Vedi il file [LICENSE](LICENSE) per maggiori dettagli.
