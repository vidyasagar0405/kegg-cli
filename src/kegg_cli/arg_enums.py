from enum import StrEnum


class SeqType(StrEnum):
    ntseq = "ntseq"
    aaseq = "aaseq"


class InfoDatabase(StrEnum):
    kegg = "kegg"
    pathway = "pathway"
    brite = "brite"
    module = "module"
    ko = "ko"
    genes = "genes"
    vg = "vg"
    vp = "vp"
    ag = "ag"
    ligand = "ligand"
    compound = "compound"
    glycan = "glycan"
    reaction = "reaction"
    rclass = "rclass"
    enzyme = "enzyme"
    variant = "variant"
    disease = "disease"
    drug = "drug"
    dgroup = "dgroup"


class ListDatabase(StrEnum):
    pathway = "pathway"
    brite = "brite"
    module = "module"
    ko = "ko"
    vg = "vg"
    vp = "vp"
    ag = "ag"
    genome = "genome"
    compound = "compound"
    glycan = "glycan"
    reaction = "reaction"
    rclass = "rclass"
    enzyme = "enzyme"
    network = "network"
    variant = "variant"
    disease = "disease"
    drug = "drug"
    dgroup = "dgroup"
    organism = "organism"
