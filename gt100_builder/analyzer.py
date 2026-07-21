from collections import Counter, defaultdict


class ParameterAnalyzer:
    def __init__(self, params: dict):
        self.params = params

    def prefixes(self):
        counter = Counter()

        for key in self.params.keys():
            parts = key.split("_")
            counter[parts[0]] += 1

        return counter

    def hierarchy(self):
        groups = defaultdict(Counter)

        for key in self.params.keys():
            parts = key.split("_")

            if len(parts) >= 2:
                groups[parts[0]][parts[1]] += 1
            else:
                groups[parts[0]]["_"] += 1

        return groups