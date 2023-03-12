import json
import re
import sequence


class RestrictionEnzyme:
    def __init__(self, name: str) -> None:
        with open("restriction_enzymes.json", "r") as file:
            database = json.load(file)

        for restrictionEnzyme in database:
            if restrictionEnzyme["enzyme name"] == name:
                self.name = restrictionEnzyme["enzyme name"]
                self.site = restrictionEnzyme["recognition sequence with cleavage site"]
                return

        return ValueError("Could not find restriction enzyme with name {name}")

    def cutSequence(self, seq: sequence.Sequence) -> list:
        """Will fail at overlapping recognitionsite matches!"""
        # Remove cut site identifier. Replace N with wildcard
        recognitionsite = self.site.replace("^", "").replace("N", ".")
        recognitionsitestarts = [
            match.start() for match in re.finditer(recognitionsite, seq.sequence)
        ]

        fragments = list()
        start = 0
        for recognitionsitestart in recognitionsitestarts:
            stop = recognitionsitestart + self.site.index("^")
            fragments.append(seq.getCut(start, stop))

            # Prepare for next iteration
            start = stop
        # Add last remaining fragment
        fragments.append(seq.getCut(stop, len(seq.sequence)))

        return fragments
