class Protein:
    codons = {
        "AAA": "Lys",
        "AAC": "Asn",
        "AAG": "Lys",
        "AAU": "Asn",
        "ACA": "Thr",
        "ACC": "Thr",
        "ACG": "Thr",
        "ACU": "Thr",
        "AGA": "Arg",
        "AGC": "Ser",
        "AGG": "Arg",
        "AGU": "Ser",
        "AUA": "Ile",
        "AUC": "Ile",
        "AUG": "Met",
        "AUU": "Ile",
        "CAA": "Gln",
        "CAC": "His",
        "CAG": "Gln",
        "CAU": "His",
        "CCA": "Pro",
        "CCC": "Pro",
        "CCG": "Pro",
        "CCU": "Pro",
        "CGA": "Arg",
        "CGC": "Arg",
        "CGG": "Arg",
        "CGU": "Arg",
        "CUA": "Leu",
        "CUC": "Leu",
        "CUG": "Leu",
        "CUU": "Leu",
        "GAA": "Glu",
        "GAC": "Asp",
        "GAG": "Glu",
        "GAU": "Asp",
        "GCA": "Ala",
        "GCC": "Ala",
        "GCG": "Ala",
        "GCU": "Ala",
        "GGA": "Gly",
        "GGC": "Gly",
        "GGG": "Gly",
        "GGU": "Gly",
        "GUA": "Val",
        "GUC": "Val",
        "GUG": "Val",
        "GUU": "Val",
        "UAA": "Stop",
        "UAC": "Tyr",
        "UAG": "Stop",
        "UAU": "Tyr",
        "UCA": "Ser",
        "UCC": "Ser",
        "UCG": "Ser",
        "UCU": "Ser",
        "UGA": "Stop",
        "UGC": "Cys",
        "UGG": "Trp",
        "UGU": "Cys",
        "UUA": "Leu",
        "UUC": "Phe",
        "UUG": "Leu",
        "UUU": "Phe",
    }

    def __init__(self, RNA: str, startAtAUG: bool=False) -> None:
        if startAtAUG and "AUG" not in RNA:
            raise ValueError("Looking for AUG but no AUG in RNA")
        elif startAtAUG:
            i = RNA.index("AUG")
        else:
            i = 0

        self.chain = []
        while i + 3 <= len(RNA) and self.codons[RNA[i : i + 3]] != "Stop":
            if not RNA[i : i + 3] in self.codons:
                raise TypeError(f"Could not finde {RNA[i : i + 3]}")
            self.chain.append(self.codons[RNA[i : i + 3]])
            i = i + 3

    def __str__(self):
        return "-".join(self.chain)