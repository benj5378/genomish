from __future__ import annotations
import copy


class Sequence:
    def __str__(self):
        return self.sequence

    def __repr__(self):
        if len(self.sequence) <= 17:
            return self.sequence
        else:
            return self.sequence[:7] + "..." + self.sequence[-7:]

    def __len__(self):
        return len(self.sequence)

    def reverse(self):
        self.sequence = self.sequence[::-1]

    def getReversed(self):
        new = copy.deepcopy(self)
        new.reverse()
        return new

    def getSpacified(self, numBases=3, numBlocks=5):
        output = ""
        currentBlock = 0
        for i in range(0, len(self.sequence)):
            if (i + 1) % numBases == 0:  # i + 1 as first base i = 0 is 1
                output = output + self.sequence[i - 2 : i + 1] + " "

                currentBlock = currentBlock + 1
                if currentBlock == numBlocks:
                    output = output + "\n"
                    currentBlock = 0
        return output

    def sequenceAlign(self, _seq2: Sequence) -> None:
        seq1 = self.sequence
        seq2 = _seq2.sequence
        progression = 0
        line1 = seq1
        line2 = seq2

        while progression < len(line1):
            offset = self.sequenceAlignNBase(seq1, seq2, 0)
            if offset > 0:
                line1 = line1[:progression] + self.offsetToSpace(offset) + seq1
                line2 = line2[:progression] + seq2
            else:
                line1 = line1[:progression] + seq1
                line2 = line2[:progression] + self.offsetToSpace(offset) + seq2

            # Progression refers to the position of line1/line2 to which alignment
            # has been checked
            progression = progression + offset
            progression = progression + self.getNumMatching(
                line1[progression:], line2[progression:]
            )
            # seq1 and seq2 is set to the remaining amount of bases that has
            # not been checked
            seq1 = line1[progression:]
            seq2 = line2[progression:]

        return line1, line2

    def getNumMatching(self, seq1: str, seq2: Sequence):  # Types are hotfixes
        # seq1 = self.sequence
        # seq2 = _seq2.sequence
        if len(seq1) > len(seq2):
            max = len(seq2)
        else:
            max = len(seq1)

        for i in range(0, max):
            if seq1[i] != seq2[i]:
                return i
        return i + 1  # in case they all matched

    def sequenceAlignNBase(
        self, seq1: str, seq2: str, n: int
    ) -> str:  # Types are hotfixes
        # seq1 = self.sequence
        # seq2 = _seq2.sequence
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

        raise RuntimeError("FATAL ERROR")  # Hotfix warning

    def offsetToSpace(self, offset: int):
        space = ""
        for j in range(0, abs(offset)):
            space = space + " "
        return space
