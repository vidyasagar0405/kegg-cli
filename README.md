# kegg-cli

[![PyPI - Version](https://img.shields.io/pypi/v/kegg-cli.svg)](https://pypi.org/project/kegg-cli)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kegg-cli.svg)](https://pypi.org/project/kegg-cli)

-----


> [!NOTE]
> You MUST make absolutely sure to comply with the conditions of using KEGG and its API: http://www.kegg.jp/kegg/legal.html and http://www.kegg.jp/kegg/rest/.


## Table of Contents

- [Installation](#installation)
- [Features](#Features)
- [Commands](#commands)
  - [info](#info)
  - [get](#get)
  - [list](#list)
  - [find](#find)
  - [conv](#conv)
  - [link](#link)
  - [get_seq](#get_seq)
- [License](#license)
- [Contributing](#Contributing)

## Features

- Query KEGG database information
- Retrieve entries from KEGG databases
- List database entries
- Search by keywords
- Convert between KEGG and external database IDs
- Find related entries between KEGG databases
- Download gene sequences (nucleotide or amino acid)

## Installation

### Via pip

```console
pip install kegg-cli
```

### From source

```bash
git clone https://www.github.com/vidyasagar0405/kegg-cli
cd kegg-cli
pip install .
```

## Commands

you can use conventional KEGG API commands such as info, get, list, find, conv, link, see below for example usage
check KEGG REST API documentation for more info: https://www.kegg.jp/kegg/rest/keggapi.html

### info

```bash
kegg-cli info kegg
```

### get

- Retrives gene entry
```bash
kegg-cli get eco:b0002
```
- Enclose ids in "double quotes", use -op/--option for options for available options check KEGG REST API
```bash
kegg-cli get "hsa:10458 ece:Z5100" -op aaseq
```

### list

- Returns the list of KEGG organisms with taxonomic classification
```bash
kegg-cli list organism
```
- Returns the list of the genes
```bash
kegg-cli list "rsz:19816419 rsz:19816420" 
```

- Returns the list of human pathways
```bash
kegg-cli list pathway -org hsa
```

### find

- Returns compound ids with the said formula
```bash
kegg-cli find C7H10O5 -db compound -op formula
```
- Returns genes involved in cancer in humans
```bash
kegg-cli find "cancer hsa"
```
- Returns Pathways with RNA in their name
```bash
kegg-cli find "rna" -db pathway
```

### conv

- Converts KEGG geneIDS to NCBI proteinIDs
```bash
kegg-cli conv ncbi-proteinid "rsz:19816419 rsz:19816420 rsz:19816421 rsz:19816422"
```

- Converts KEGG geneIDS to NCBI geneIDs
```bash
kegg-cli conv ncbi-geneid "rsz:19816419 rsz:19816420 rsz:19816421 rsz:19816422" 
```

- Converts NCBI geneIDs to KEGG geneIDS
```bash
kegg-cli conv genes "ncbi-geneid:19816419 ncbi-geneid:19816420 ncbi-geneid:19816421 ncbi-geneid:19816422" 
```

- Converts NCBI proteinIDs to KEGG geneIDS
```bash
kegg-cli conv genes "ncbi-proteinid:YP_009046967 ncbi-proteinid:YP_009046968 ncbi-proteinid:YP_009046969 ncbi-proteinid:YP_009046970" 
```

### link


- Returns genes linked to the rsz00966 pathway
```bash
kegg-cli link rsz rsz00966 
```

- Returns compounds linked to the rsz00966 pathway
```bash
kegg-cli link cpd map00010 
```

- Returns pathways linked to the given genes
```bash
kegg-cli link pathway "hsa:10458 ece:Z5100"
```

### get-seq

It is not a part of KEGG REST API, but uses link and get API calls to get the nucleotide sequence (ntseq) or amino acid sequence (aaseq).

get-seq can be used in four different ways:

- Fetches the ntseq (default) of the given genes and saves it to a file named with time_date.fasta
```bash
kegg-cli get-seq "rsz:108806876 rsz:108839148" 
```

- Fetches the aaseq of the given genes and saves it to a file named with time_date.fasta
```bash
kegg-cli get-seq "rsz:108806876 rsz:108839148" --seq-type aaseq 
```

- Fetches the aaseq of the given genes and saves it to a file named path/to/file.fasta
```bash
kegg-cli get-seq "rsz:108806876 rsz:108839148" --seq-type aaseq -o path/to/file.fasta 
```

- Fetches the aaseq of the genes in the file (one per line) and saves it to a file named path/to/file.fasta
```bash
kegg-cli get-seq /home/vs/Documents/bioinfo/practise/kegg/rsz_rsz_M00005_genes.tsv --seq-type aaseq -o expected_aaseq.fasta 
```

- Fetches the aaseq of the genes in the second column (0 based indexing) of the file (one per line) and saves it to a file named path/to/file.fasta (delimiter can also be changed with --delimiter, defaults to '\t')
```bash
kegg-cli get-seq /home/vs/Documents/bioinfo/practise/kegg/rsz_rsz_M00005_genes.tsv --field 1 --seq-type aaseq -o expected_aaseq.fasta
```

- Fetches the ntseq of all the genes in the given pathway (make sure to add 'path:' prefix, to the pathway ID. One pathway at a time)
```bash
kegg-cli get-seq path:minc00966 --seq-type ntseq -o tests/data/expected_pathway_ntseq.fasta 
```

- Fetches the ntseq of all the genes in the given module (make sure to add 'md:' prefix, to the module ID. One module at a time)
```bash
kegg-cli get-seq md:rsz_M00005 --seq-type ntseq -o tests/data/expected_module_ntseq.fasta 
```

## License

`kegg-cli` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
