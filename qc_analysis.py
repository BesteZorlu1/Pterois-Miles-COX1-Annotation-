from pathlib import Path
from collections import Counter

# Input FASTA file
fasta_file = Path("data/raw/Pterois_miles.fasta")

# Read FASTA
text = fasta_file.read_text()

# Store sequences
sequences = {}
current_id = None

for line in text.splitlines():
    line = line.strip()

    if line.startswith(">"):
        current_id = line.split()[0][1:]
        sequences[current_id] = ""

    elif line:
        sequences[current_id] += line.upper()

# Quality control analysis
for seq_id, seq in sequences.items():

    counts = Counter(seq)

    gc = (counts["G"] + counts["C"]) / len(seq) * 100

    ambiguous = len(seq) - sum(
        counts[base] for base in "ATGC"
    )

    print("\nSequence:", seq_id)
    print("Length:", len(seq), "bp")
    print("A:", counts["A"])
    print("T:", counts["T"])
    print("G:", counts["G"])
    print("C:", counts["C"])
    print("GC%:", round(gc, 2))
    print("Ambiguous bases:", ambiguous)