amino = {
    "UUU": "Phe",
    "UUC": "Phe",
    "CUA": "Leu",
    "CUG": "Leu",
    "CUU": "Leu",
    "CUC": "Leu",
    "CUA": "Leu",
    "CUG": "Leu",
    "AUU": "Ile",
    "AUC": "Ile",
    "AUA": "Ile",
    "AUG": "Met",
    "GUU": "Val",
    "GUC": "Val",
    "GUA": "Val",
    "GUG": "Val",
    "UCU": "Ser",
    "UCC": "Ser",
    "UCA": "Ser",
    "UCG": "Ser",
    "CCU": "Pro",
    "CCC": "Pro",
    "CCA": "Pro",
    "CCG": "Pro",
    "ACU": "Thr",
    "ACC": "Thr",
    "ACA": "Thr",
    "ACG": "Thr",
    "GCU": "Ala",
    "GCC": "Ala",
    "GCA": "Ala",
    "GCG": "Ala",
    "UAU": "Tyr",
    "UAC": "Tyr",
    "CAU": "His",
    "CAC": "His",
    "CAA": "Gin",
    "CAG": "Gin",
    "AAU": "Asn",
    "AAC": "Asn",
    "AAA": "Lys",
    "AAG": "Lys",
    "GAU": "Asp",
    "GAC": "Asp",
    "GAA": "Glu",
    "GAG": "Glu",
    "UGU": "Cys",
    "UGC": "Cys",
    "UGG": "Trp",
    "CGU": "Arg",
    "CGC": "Arg",
    "CGA": "Arg",
    "CGG": "Arg",
    "AGA": "Arg",
    "AGG": "Arg",
    "AGU": "Ser",
    "AGC": "Ser",
    "GGU": "Gly",
    "GGC": "Gly",
    "GGA": "Gly",
    "GGG": "Gly",
    "UAA": "Stop",
    "UAG": "Stop",
    "UGA": "Stop",
}


def flip(string):
    output = string.replace("5'", "x").replace("3'", "5'").replace("x", "3'")
    return output


def reverse(string):
    output = (
        string.replace("3'", "x")
        .replace("5'", "y")[::-1]
        .replace("x", "3'")
        .replace("y", "5'")
    )
    return output


def complementary(string):
    output = (
        string.replace("A", "x")
        .replace("T", "A")
        .replace("x", "T")
        .replace("C", "x")
        .replace("G", "C")
        .replace("x", "G")
    )
    return output


def makeDNA(RNA="", DNAtemplate=""):
    if RNA:
        return RNA.replace("U", "T")
    elif DNAtemplate:
        return flip(complementary(DNAtemplate))
    raise ValueError("Missing arguments")


def makeRNA(DNA=""):
    return DNA.replace("T", "U")


def makeDNAtemplate(DNA=""):
    return flip(complementary(DNA))


def run(DNA="", RNA="", DNAtemplate=""):
    chain = ""

    if bool(RNA) + bool(DNA) + bool(DNAtemplate) > 1:
        raise ValueError("Should I use RNA, DNA or DNAtemplate?")
    if bool(RNA) + bool(DNA) + bool(DNAtemplate) < 1:
        raise ValueError("No information given!")
    elif RNA:
        DNA = makeDNA(RNA=RNA)
        DNAtemplate = makeDNAtemplate(DNA=DNA)
    elif DNA:
        RNA = makeRNA(DNA=DNA)
        DNAtemplate = makeDNAtemplate(DNA=DNA)
    elif DNAtemplate:
        DNA = makeDNA(DNAtemplate=DNAtemplate)
        RNA = makeRNA(DNA=DNA)

    if "AUG" in RNA:
        n = RNA.index("AUG")

        while (
            n + 3 < len(RNA)
            and RNA[n : n + 3] in amino
            and amino[RNA[n : n + 3]] != "Stop"
        ):
            chain = chain + amino[RNA[n : n + 3]] + "-"
            n = n + 3
        chain = chain[:-1]
    else:
        chain = "no start codon"

    print("DNA complementary:   " + DNA + " / " + reverse(DNA))
    print("DNA template:        " + DNAtemplate + " / " + reverse(DNAtemplate) + "\n")
    print("mRNA:                " + RNA + " / " + reverse(RNA) + "\n")
    print("protein chain:       " + chain)


DNA = ""
DNAtemplate = ""  # Example: DNAtemplate = "3'-TACCCCAGCGGACGC-5'"
RNA = ""

run(DNA, RNA, DNAtemplate)
