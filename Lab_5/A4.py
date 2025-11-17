def read_protein_data(filename):
    proteins = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                protein_data = (
                    parts[0].strip(),  # name
                    parts[1].strip(),  # organism
                    parts[2].strip()   # sequence
                )
                proteins.append(protein_data)
    return proteins
