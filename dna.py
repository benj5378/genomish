import copy
import rna
import sequence


class DNA(sequence.Sequence):
    def __init__(self, arg) -> None:
        if isinstance(arg, str):
            seq = arg
            for base in seq:
                if base not in "ACGT":
                    raise ValueError(
                        "Non-DNA base characters! Only accepts sequences consisting of A, C, G ang T"
                    )
            self.sequence = seq
        elif isinstance(arg, rna.RNA):
            RNA = arg.getComplementary()
            self.sequence = RNA.sequence.replace("U", "T")
        else:
            raise TypeError("Constructor does not accept this type")

    def complementary(self):
        self.sequence = (
            self.sequence.replace("A", "x")
            .replace("T", "A")
            .replace("x", "T")
            .replace("C", "x")
            .replace("G", "C")
            .replace("x", "G")
        )

    def getComplementary(self):
        new = copy.deepcopy(self)
        new.complementary()
        return new
