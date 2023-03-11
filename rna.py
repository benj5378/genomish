import copy
import dna
import sequence


class RNA(sequence.Sequence):
    def __init__(self, arg) -> None:
        if isinstance(arg, str):
            seq = arg
            for base in seq:
                if base not in "ACGU":
                    raise ValueError(
                        "Non-RNA base characters! Only accepts sequences consisting of A, C, G ang U"
                    )
            self.sequence = seq
        elif isinstance(arg, dna.DNA):
            DNA = arg.getComplementary()
            self.sequence = DNA.sequence.replace("T", "U")
        else:
            raise TypeError("Constructor does not accept this type")

    def complementary(self):
        self.sequence = (
            self.sequence.replace("A", "x")
            .replace("U", "A")
            .replace("x", "U")
            .replace("C", "x")
            .replace("G", "C")
            .replace("x", "G")
        )

    def getComplementary(self):
        new = copy.deepcopy(self)
        new.complementary()
        return new
