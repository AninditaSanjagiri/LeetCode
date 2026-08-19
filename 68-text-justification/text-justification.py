class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0

        while i < len(words):
            line_words = []
            line_length = 0

            # Find words that fit on this line
            while i < len(words) and line_length + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_length += len(words[i])
                i += 1

            # Last line or line with only one word
            if i == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)

            else:
                # Spaces that need to be distributed
                total_spaces = maxWidth - line_length
                gaps = len(line_words) - 1

                space = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""

                for j in range(gaps):
                    line += line_words[j]
                    line += " " * (space + (1 if j < extra else 0))

                line += line_words[-1]
                result.append(line)

        return result