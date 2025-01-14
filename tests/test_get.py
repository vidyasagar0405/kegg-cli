from typer.testing import CliRunner

from kegg_cli.main import app

runner = CliRunner()

expected_result_1 = """
ENTRY       b0002             CDS       T00007
SYMBOL      thrA
NAME        (RefSeq) fused aspartate kinase/homoserine dehydrogenase 1
ORTHOLOGY   K12524  bifunctional aspartokinase / homoserine dehydrogenase 1 [EC:2.7.2.4 1.1.1.3]
ORGANISM    eco  Escherichia coli K-12 MG1655
PATHWAY     eco00260  Glycine, serine and threonine metabolism
            eco00261  Monobactam biosynthesis
            eco00270  Cysteine and methionine metabolism
            eco00300  Lysine biosynthesis
            eco01100  Metabolic pathways
            eco01110  Biosynthesis of secondary metabolites
            eco01120  Microbial metabolism in diverse environments
            eco01230  Biosynthesis of amino acids
MODULE      eco_M00016  Lysine biosynthesis, succinyl-DAP pathway, aspartate => lysine
            eco_M00017  Methionine biosynthesis, aspartate => homoserine => methionine
            eco_M00018  Threonine biosynthesis, aspartate => homoserine => threonine
BRITE       KEGG Orthology (KO) [BR:eco00001]
             09100 Metabolism
              09105 Amino acid metabolism
               00260 Glycine, serine and threonine metabolism
                b0002 (thrA)
               00270 Cysteine and methionine metabolism
                b0002 (thrA)
               00300 Lysine biosynthesis
                b0002 (thrA)
              09110 Biosynthesis of other secondary metabolites
               00261 Monobactam biosynthesis
                b0002 (thrA)
            Enzymes [BR:eco01000]
             1. Oxidoreductases
              1.1  Acting on the CH-OH group of donors
               1.1.1  With NAD+ or NADP+ as acceptor
                1.1.1.3  homoserine dehydrogenase
                 b0002 (thrA)
             2. Transferases
              2.7  Transferring phosphorus-containing groups
               2.7.2  Phosphotransferases with a carboxy group as acceptor
                2.7.2.4  aspartate kinase
                 b0002 (thrA)
POSITION    337..2799
MOTIF       Pfam: Homoserine_dh AA_kinase ACT_9 NAD_binding_3 ACT_7 ACT DUF6247
DBLINKS     NCBI-GeneID: 945803
            NCBI-ProteinID: NP_414543
            Pasteur: thrA
            RegulonDB: RDBECOLIGNC00986
            ECOCYC: EG10998
            ASAP: ABE-0000008
            UniProt: P00561
STRUCTURE   PDB
AASEQ       820
            MRVLKFGGTSVANAERFLRVADILESNARQGQVATVLSAPAKITNHLVAMIEKTISGQDA
            LPNISDAERIFAELLTGLAAAQPGFPLAQLKTFVDQEFAQIKHVLHGISLLGQCPDSINA
            ALICRGEKMSIAIMAGVLEARGHNVTVIDPVEKLLAVGHYLESTVDIAESTRRIAASRIP
            ADHMVLMAGFTAGNEKGELVVLGRNGSDYSAAVLAACLRADCCEIWTDVDGVYTCDPRQV
            PDARLLKSMSYQEAMELSYFGAKVLHPRTITPIAQFQIPCLIKNTGNPQAPGTLIGASRD
            EDELPVKGISNLNNMAMFSVSGPGMKGMVGMAARVFAAMSRARISVVLITQSSSEYSISF
            CVPQSDCVRAERAMQEEFYLELKEGLLEPLAVTERLAIISVVGDGMRTLRGISAKFFAAL
            ARANINIVAIAQGSSERSISVVVNNDDATTGVRVTHQMLFNTDQVIEVFVIGVGGVGGAL
            LEQLKRQQSWLKNKHIDLRVCGVANSKALLTNVHGLNLENWQEELAQAKEPFNLGRLIRL
            VKEYHLLNPVIVDCTSSQAVADQYADFLREGFHVVTPNKKANTSSMDYYHQLRYAAEKSR
            RKFLYDTNVGAGLPVIENLQNLLNAGDELMKFSGILSGSLSYIFGKLDEGMSFSEATTLA
            REMGYTEPDPRDDLSGMDVARKLLILARETGRELELADIEIEPVLPAEFNAEGDVAAFMA
            NLSQLDDLFAARVAKARDEGKVLRYVGNIDEDGVCRVKIAEVDGNDPLFKVKNGENALAF
            YSHYYQPLPLVLRGYGAGNDVTAAGVFADLLRTLSWKLGV
NTSEQ       2463
            atgcgagtgttgaagttcggcggtacatcagtggcaaatgcagaacgttttctgcgtgtt
            gccgatattctggaaagcaatgccaggcaggggcaggtggccaccgtcctctctgccccc
            gccaaaatcaccaaccacctggtggcgatgattgaaaaaaccattagcggccaggatgct
            ttacccaatatcagcgatgccgaacgtatttttgccgaacttttgacgggactcgccgcc
            gcccagccggggttcccgctggcgcaattgaaaactttcgtcgatcaggaatttgcccaa
            ataaaacatgtcctgcatggcattagtttgttggggcagtgcccggatagcatcaacgct
            gcgctgatttgccgtggcgagaaaatgtcgatcgccattatggccggcgtattagaagcg
            cgcggtcacaacgttactgttatcgatccggtcgaaaaactgctggcagtggggcattac
            ctcgaatctaccgtcgatattgctgagtccacccgccgtattgcggcaagccgcattccg
            gctgatcacatggtgctgatggcaggtttcaccgccggtaatgaaaaaggcgaactggtg
            gtgcttggacgcaacggttccgactactctgctgcggtgctggctgcctgtttacgcgcc
            gattgttgcgagatttggacggacgttgacggggtctatacctgcgacccgcgtcaggtg
            cccgatgcgaggttgttgaagtcgatgtcctaccaggaagcgatggagctttcctacttc
            ggcgctaaagttcttcacccccgcaccattacccccatcgcccagttccagatcccttgc
            ctgattaaaaataccggaaatcctcaagcaccaggtacgctcattggtgccagccgtgat
            gaagacgaattaccggtcaagggcatttccaatctgaataacatggcaatgttcagcgtt
            tctggtccggggatgaaagggatggtcggcatggcggcgcgcgtctttgcagcgatgtca
            cgcgcccgtatttccgtggtgctgattacgcaatcatcttccgaatacagcatcagtttc
            tgcgttccacaaagcgactgtgtgcgagctgaacgggcaatgcaggaagagttctacctg
            gaactgaaagaaggcttactggagccgctggcagtgacggaacggctggccattatctcg
            gtggtaggtgatggtatgcgcaccttgcgtgggatctcggcgaaattctttgccgcactg
            gcccgcgccaatatcaacattgtcgccattgctcagggatcttctgaacgctcaatctct
            gtcgtggtaaataacgatgatgcgaccactggcgtgcgcgttactcatcagatgctgttc
            aataccgatcaggttatcgaagtgtttgtgattggcgtcggtggcgttggcggtgcgctg
            ctggagcaactgaagcgtcagcaaagctggctgaagaataaacatatcgacttacgtgtc
            tgcggtgttgccaactcgaaggctctgctcaccaatgtacatggccttaatctggaaaac
            tggcaggaagaactggcgcaagccaaagagccgtttaatctcgggcgcttaattcgcctc
            gtgaaagaatatcatctgctgaacccggtcattgttgactgcacttccagccaggcagtg
            gcggatcaatatgccgacttcctgcgcgaaggtttccacgttgtcacgccgaacaaaaag
            gccaacacctcgtcgatggattactaccatcagttgcgttatgcggcggaaaaatcgcgg
            cgtaaattcctctatgacaccaacgttggggctggattaccggttattgagaacctgcaa
            aatctgctcaatgcaggtgatgaattgatgaagttctccggcattctttctggttcgctt
            tcttatatcttcggcaagttagacgaaggcatgagtttctccgaggcgaccacgctggcg
            cgggaaatgggttataccgaaccggacccgcgagatgatctttctggtatggatgtggcg
            cgtaaactattgattctcgctcgtgaaacgggacgtgaactggagctggcggatattgaa
            attgaacctgtgctgcccgcagagtttaacgccgagggtgatgttgccgcttttatggcg
            aatctgtcacaactcgacgatctctttgccgcgcgcgtggcgaaggcccgtgatgaagga
            aaagttttgcgctatgttggcaatattgatgaagatggcgtctgccgcgtgaagattgcc
            gaagtggatggtaatgatccgctgttcaaagtgaaaaatggcgaaaacgccctggccttc
            tatagccactattatcagccgctgccgttggtactgcgcggatatggtgcgggcaatgac
            gttacagctgccggtgtctttgctgatctgctacgtaccctctcatggaagttaggagtc
            tga
///
"""

expected_result_2 = """
>hsa:10458 K05627 BAI1-associated protein 2 | (RefSeq) BAIAP2, BAP2, FLAF3, IRSP53, WAML; BAR/IMD domain containing adaptor protein 2 (A)
MSLSRSEEMHRLTENVYKTIMEQFNPSLRNFIAMGKNYEKALAGVTYAAKGYFDALVKMG
ELASESQGSKELGDVLFQMAEVHRQIQNQLEEMLKSFHNELLTQLEQKVELDSRYLSAAL
KKYQTEQRSKGDALDKCQAELKKLRKKSQGSKNPQKYSDKELQYIDAISNKQGELENYVS
DGYKTALTEERRRFCFLVEKQCAVAKNSAAYHSKGKELLAQKLPLWQQACADPSKIPERA
VQLMQQVASNGATLPSALSASKSNLVISDPIPGAKPLPVPPELAPFVGRMSAQESTPIMN
GVTGPDGEDYSPWADRKAAQPKSLSPPQSQSKLSDSYSNTLPVRKSVTPKNSYATTENKT
LPRSSSMAAGLERNGRMRVKAIFSHAAGDNSTLLSFKEGDLITLLVPEARDGWHYGESEK
TKMRGWFPFSYTRVLDSDGSDRLHMSLQQGKSSSTGNLLDKDDLAIPPPDYGAASRAFPA
QTASGFKQRPYSVAVPAFSQGLDDYGARSMSRNPFAHVQLKPTVTNDRCDLSAQGPEGRE
HGDGSARTLAGR
>ece:Z5100 K12786 LEE-encoded effector EspF | (GenBank) espF; espF (A)
MLNGISNAASTLGRQLVGIASRVSSAGGTGFSVAPQAVRLTPVKVHSPFSPGSSNVNART
IFNVSSQVTSFTPSRPAPPPPTSGQASGASRPLPPIAQALKEHLAAYEKSKGPEALGFKP
ARQAPPPPTSGQASGASRPLPPIAQALKEHLAAYEKSKGPEALGFKPARQAPPPPTSGQA
SGASRPLPPIAQALKEHLAAYEKSKGPEALGFKPARQAPPPPTGPSGLPPLAQALKDHLA
AYEQSKKG
"""


def test_get_no_arg():
    result = runner.invoke(app, ["get", "eco:b0002"])
    assert result.exit_code == 0
    assert expected_result_1.strip() in result.output.strip()


def test_get_option():
    result = runner.invoke(app, ["get", "hsa:10458 ece:Z5100", "-op", "aaseq"])
    assert result.exit_code == 0
    assert expected_result_2.strip() in result.output.strip()
