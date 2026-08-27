# Pterois-Miles-COX1-Annotation-
In silico annotation and comparative analysis of the COX1 gene in the lionfish (Pterois miles).
# Pterois miles COX1 Annotation

## Project Overview

This project focuses on the **in silico analysis of the cytochrome c oxidase subunit I (COX1/COI) gene** in *Pterois miles* (red lionfish).

The aim of this project is to develop a simple and reproducible bioinformatics workflow for COX1 sequence analysis, starting from publicly available nucleotide sequences and progressing toward sequence comparison and phylogenetic analysis.

The project is developed as an open-source educational bioinformatics project.

---

## Objectives

The main objectives of this project are:

* Collect COX1 nucleotide sequences from *Pterois* species.
* Perform basic sequence quality control.
* Calculate nucleotide composition and GC content.
* Identify ambiguous nucleotide positions.
* Verify sequence identity using BLAST.
* Compare COX1 sequences among *Pterois* species.
* Perform multiple sequence alignment.
* Construct a phylogenetic tree.
* Interpret the results from an evolutionary perspective.

---

## Project Structure

```text
Pterois-Miles-COX1-Annotation/
│
├── data/
│   ├── raw/
│   │   ├── Pterois_miles.fasta
│   │   ├── Pterois_russelii.fasta
│   │   └── Pterois_volitans.fasta
│   │
│   └── processed/
│
├── figures/
│
├── results/
│   └── qc_report.txt
│
├── scripts/
│   └── qc_analysis.py
│
└── README.md
```

---

# 1. Data Collection

The initial dataset contains publicly available COX1 nucleotide sequences from *Pterois* species.

The current *Pterois miles* FASTA file contains two sequence records:

| Accession  | Species         | Length |
| ---------- | --------------- | -----: |
| PX789826.1 | *Pterois miles* | 407 bp |
| OL691767.1 | *Pterois miles* | 589 bp |

Additional *Pterois* sequences are included for future comparative and phylogenetic analyses.

---

# 2. Sequence Quality Control

Basic sequence quality control was performed using **Python**.

The QC analysis evaluated:

* Sequence length
* A, T, G and C nucleotide composition
* GC content
* Ambiguous nucleotide positions

The analysis was implemented in:

```text
scripts/qc_analysis.py
```

---

## QC Results

| Sequence   | Length (bp) | GC (%) | Ambiguous Bases |
| ---------- | ----------: | -----: | --------------: |
| PX789826.1 |         407 |  42.01 |              38 |
| OL691767.1 |         589 |  46.86 |               0 |

### PX789826.1

The PX789826.1 sequence is 407 bp long and has a GC content of 42.01%.

A total of **38 ambiguous nucleotide positions** were detected.

The detected IUPAC ambiguity codes include:

* `R` = A/G
* `K` = G/T
* `Y` = C/T
* `W` = A/T
* `M` = A/C

These ambiguity codes were retained and were **not arbitrarily converted** into a single nucleotide.

### OL691767.1

The OL691767.1 sequence is 589 bp long and has a GC content of 46.86%.

No ambiguous nucleotide positions were detected.

---

# 3. Ambiguous Nucleotide Analysis

For PX789826.1, the positions of ambiguous nucleotides were identified using Python.

The detected positions were recorded to allow further evaluation during sequence alignment and comparative analysis.

Ambiguous nucleotides will be retained during downstream analyses when supported by the selected alignment and phylogenetic methods.

---

# 5. Tools and Resources

The project currently uses:

* **NCBI GenBank** — nucleotide sequence data
* **NCBI BLAST** — sequence similarity analysis
* **Python** — sequence quality control and analysis
* **GitHub** — version control and open-source project documentation

Additional bioinformatics tools will be added as the project progresses.

--- 


## Sequence Identification

The query sequence PX789826.1 was identified as a partial mitochondrial COX1 sequence of *Pterois miles*.

BLAST analysis supported its identification as *Pterois miles* COX1.

## Multiple Sequence Alignment

Multiple sequence alignment was performed using MAFFT v7.526.

The alignment included two *Pterois miles* COX1 sequences:

- PX789826.1
- OL691767.1

The final alignment length was 589 bp.

## Alignment Quality Control

Alignment quality was evaluated using Python and Biopython.

The quality control script calculated:

- Number of sequences
- Alignment length
- Number of gaps
- Number of ambiguous nucleotide positions

### QC Results

| Sequence | Gaps | Ambiguous bases |
|----------|------|-----------------|
| PX789826.1 | 182 | 38 |
| OL691767.1 | 0 | 0 |

The PX789826.1 sequence contains several ambiguous nucleotide positions and gaps in the alignment. This is consistent with the sequence being a shorter partial COX1 sequence and containing ambiguous IUPAC nucleotide codes.

The OL691767.1 sequence showed no gaps or ambiguous bases in the final alignment.

## Software

- MAFFT v7.526
- Python 3.13
- Biopython

## Project Structure

```text
Pterois-Miles-COX1-Annotation/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── results/
│   ├── alignment/
│   ├── phylogeny/
│   ├── blast_results.txt
│   └── qc_report.txt
│
├── scripts/
│   └── alignment_qc.py
│
├── figures/
│
├── Pterois_miles_COX1.fasta.fasta
└── README.md


This repository is an educational open-source bioinformatics project developed to practice nucleotide sequence analysis, annotation, comparative genomics, and phylogenetic workflows.


## Author

**Beste Zorlu**

Biology & Aquatic Sciences and Engineering 
İstanbul University

