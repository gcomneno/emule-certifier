import csv
import yaml
from pathlib import Path
from Crypto.Hash import MD4
from tqdm import tqdm

def load_config(yaml_path='config.yaml'):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def extract_md4_hashes_from_ed2k(file_path):
    hashes = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) >= 5:
                md4_hash = parts[4]
                if len(md4_hash) == 32:
                    hashes.add(md4_hash.upper())
    return hashes

def calculate_md4(file_path):
    h = MD4.new()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest().upper()
    except Exception as e:
        print(f"Errore nel calcolo hash per {file_path}: {e}")
        return None

def scan_and_hash_files(archive_paths, extensions):
    local_hashes = {}
    all_files = []

    for folder in archive_paths:
        p = Path(folder)
        if not p.exists():
            print(f"Cartella non trovata: {folder}")
            continue
        
        print(f"📁 Scansionando la cartella: {folder}")
        
        # Raccogli i file da questa cartella
        for file in p.rglob('*'):
            if file.suffix.lower() in extensions:
                all_files.append(file)

    print(f"🔍 Analizzando {len(all_files)} file...")

    for file in tqdm(all_files, desc="Calcolo hash MD4"):
        md4 = calculate_md4(file)
        if md4:
            local_hashes[md4] = str(file)

    return local_hashes

def write_csv(matches, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['MD4 Hash', 'File Locale'])
        for md4, path in matches.items():
            writer.writerow([md4, path])

def main():
    config = load_config()

    archive_paths = config.get('archive_paths', [])
    extensions = [ext.lower() for ext in config.get('extensions', ['.pdf', '.epub'])]
    ed2k_links_file = config.get('ed2k_links_file', 'ed2k_links.txt')
    output_csv = config.get('output_csv', 'risultato_confronto.csv')

    print("🔍 Estrazione hash da link ed2k...")
    ed2k_hashes = extract_md4_hashes_from_ed2k(ed2k_links_file)

    print("📁 Scansione dei file archiviati...")
    local_files = scan_and_hash_files(archive_paths, extensions)

    print("🧬 Confronto hash...")
    matches = {md4: path for md4, path in local_files.items() if md4 in ed2k_hashes}

    print(f"✅ Trovati {len(matches)} file già scaricati.")
    write_csv(matches, output_csv)
    print(f"📄 Risultato salvato in: {output_csv}")

if __name__ == '__main__':
    main()
