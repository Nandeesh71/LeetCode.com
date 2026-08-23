class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        freq = [[] for _ in range(len(s)+1)]

        for i in s:
            count[i] = 1 + count.get(i, 0)
        
        for i, c in count.items():
            freq[c].append(i)

        output = []

        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                output.append(j * i)


        return "".join(output)     