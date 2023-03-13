import json
import re
import sequence


class RestrictionEnzyme:
    def __init__(self, name: str = None, jsonObject=None) -> None:
        if not name and not jsonObject:
            raise TypeError("Too many arguments given")
        elif name:
            with open("restriction_enzymes.json", "r") as file:
                database = json.load(file)

            for restrictionEnzyme in database:
                if restrictionEnzyme["enzyme name"] == name:
                    self.name = restrictionEnzyme["enzyme name"]
                    self.site = restrictionEnzyme[
                        "recognition sequence with cleavage site"
                    ]
                    return

            return ValueError("Could not find restriction enzyme with name {name}")
        elif jsonObject:
            self.name = jsonObject["enzyme name"]
            self.site = jsonObject["recognition sequence with cleavage site"]

    def cutSequence(self, seq: sequence.Sequence) -> list:
        """Will fail at overlapping recognitionsite matches!"""

    def getRecognitionSite(self):
        # Remove cut site identifier. Replace N with wildcard
        return self.site.replace("^", "")

    def getCleavageSiteOffset(self) -> int:
        """Returns the offset at which the cut site is located compared to
        the recognitionsite. Example, CGA^TA will return 3"""
        return self.site.find("^")

    def getRecognitionSiteStarts(self, seq: sequence.Sequence) -> list:
        return [
            match.start()
            for match in re.finditer(
                self.getRecognitionSite().replace("N", "."), seq.sequence
            )
        ]

    def getCutLocations(self, seq: sequence.Sequence) -> list:
        return [
            s + self.getCleavageSiteOffset() for s in self.getRecognitionSiteStarts(seq)
        ]
        # return [r + self.getCleavageSiteOffset() for r in self.getRecognitionSiteStarts(seq)]

    def cutSequence(self, seq: sequence.Sequence) -> list:
        """Will fail at overlapping recognitionsite matches!"""
        fragments = list()
        start = 0
        for cutLocation in self.getCutLocations(seq):
            fragments.append(seq.getCut(start, cutLocation))

            # Prepare for next iteration
            start = cutLocation
        # Add last remaining fragment
        fragments.append(seq.getCut(cutLocation, len(seq.sequence)))

        return fragments
