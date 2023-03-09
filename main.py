import optparse
from protein import Protein
# from gui import gui_start_window


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


def makeRNA(DNA):
    return DNA.replace("T", "U")


def makeDNAtemplate(DNA):
    return flip(complementary(DNA))

def offsetToSpace(offset : int):
    space = ""
    for j in range(0, abs(offset)):
        space = space + " "
    return space


def sequenceAlignNBase(seq1 : str, seq2 : str, n : int) -> str:
    """Align seq1 to the n base of seq2"""
    # print(f"sequenceAlignNBase({seq1}, {seq2}, {n}")
    # Iterate over each base in seq2
    for i in range(0, len(seq2)):
        # print(i)
        # Check if base of seq1 mathces the i base of seq2
        if seq1[n] == seq2[i]:
            if __name__ == "__main__" and False:
                print("Found match")
                # Make the number of spaces offset needed to align sequences
                space = offsetToSpace(i - n)
                if i - n > 0:
                    print(space + seq1)
                    print(seq2)
                else:
                    print(seq1)
                    print(space + seq2)
            else:
                # Returns how much seq1 if offsetted compared to seq2
                return i - n
            break


def getNumMatching(seq1 : str, seq2 : str):
    if len(seq1) > len(seq2):
        max = len(seq2)
    else:
        max = len(seq1)

    for i in range(0, max):
        if seq1[i] != seq2[i]:
            return i
    return i + 1  # in case they all matched


def spacify(seq: str, numBases=3, numBlocks=5):
    output = ""
    currentBlock = 0
    for i in range(0, len(seq)):
        if (i + 1) % numBases == 0:  # i + 1 as first base i = 0 is 1
            output = output + seq[i - 2 : i + 1] + " "

            currentBlock = currentBlock + 1
            if currentBlock == numBlocks    :
                output = output + "\n"
                currentBlock = 0
    return output


def sequenceAlign(seq1: str, seq2: str) -> None:
    progression = 0
    line1 = ""
    line2 = ""

    for i in range(0, 8):
        offset = sequenceAlignNBase(seq1, seq2, 0)
        if offset > 0:
            line1 = line1[:progression] + offsetToSpace(offset) + seq1
            line2 = line2[:progression] + seq2
        else:
            line1 = line1[:progression] + seq1
            line2 = line2[:progression] + offsetToSpace(offset) + seq2

        progression = progression + offset
        seq1 = line1[progression:]
        seq2 = line2[progression:]
        progression = progression + getNumMatching(seq1, seq2)
        seq1 = line1[progression:]
        seq2 = line2[progression:]
        # print(seq1)
        # print(seq2)

    print(line1)
    print(line2)


def main(DNA="", RNA="", DNAtemplate=""):
    if bool(RNA) + bool(DNA) + bool(DNAtemplate) > 1:
        raise ValueError("Should I use RNA, DNA or DNAtemplate?")
    if bool(RNA) + bool(DNA) + bool(DNAtemplate) < 1:
        raise ValueError("No information given!")
    elif RNA:
        DNA = makeDNA(RNA=RNA)
        DNAtemplate = makeDNAtemplate(DNA)
    elif DNA:
        RNA = makeRNA(DNA)
        DNAtemplate = makeDNAtemplate(DNA)
    elif DNAtemplate:
        DNA = makeDNA(DNAtemplate=DNAtemplate)
        RNA = makeRNA(DNA=DNA)

    protein = Protein(RNA)
    chain = print(protein)

    print("DNA complementary:   " + DNA + " / " + reverse(DNA))
    print("DNA template:        " + DNAtemplate + " / " + reverse(DNAtemplate) + "\n")
    print("mRNA:                " + RNA + " / " + reverse(RNA) + "\n")
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
