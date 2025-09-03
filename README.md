# emule-certifier
Script per verificare se file in locale sono già stati scaricati via eMule, confrontando gli hash MD4 dei file archiviati con quelli presenti in link `ed2k://`.

## Funzionalità

- Scansione ricorsiva di una o più cartelle
- Calcolo hash MD4 dei file (PDF, EPUB, MOBI, AZW3)
- Confronto con hash contenuti in link ED2K
- Output CSV con i file già scaricati
- Configurabile via YAML
- Progress bar integrata

## Requisiti

