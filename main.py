import optparse
from protein import Protein
import dna
import rna

# from gui import gui_start_window


def main(DNA="", RNA="", DNAtemplate=""):
    if bool(RNA) + bool(DNA) + bool(DNAtemplate) > 1:
        raise ValueError("Should I use RNA, DNA or DNAtemplate?")
    if bool(RNA) + bool(DNA) + bool(DNAtemplate) < 1:
        raise ValueError("No information given!")
    elif RNA:
        DNA = str(dna.DNA(RNA))
        DNAtemplate = str(DNA.getComplementary())
    elif DNA:
        RNA = str(rna.RNA(DNA))
        DNAtemplate = str(RNA.getComplementary(DNA))
    elif DNAtemplate:
        DNA = str(dna.DNA(DNAtemplate).getComplementary())
        RNA = str(rna.RNA(dna.DNA(DNA)))

    protein = Protein(RNA)
    chain = str(protein)

    print("DNA complementary:   " + DNA + " / " + DNA)
    print("DNA template:        " + DNAtemplate + " / " + DNAtemplate + "\n")
    print("mRNA:                " + RNA + " / " + RNA + "\n")
    print("protein chain:       " + chain)


if __name__ == "__main__":
    p = optparse.OptionParser()
    p.add_option("--DNAtemplate")
    p.add_option("-g", "--gui", action="store_true")
    options, arguments = p.parse_args()

    if options.gui:
        gui_start_window.run()

    DNAtemplate = options.DNAtemplate
    main(DNAtemplate=DNAtemplate)
