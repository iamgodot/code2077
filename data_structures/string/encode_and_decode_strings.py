# Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/


class Codec:
    """
    1. We can use a non-ASCII character as the delimiter.
    2. Use both a delimiter and an escape character.
    3. Chunked transfer encoding with a length plus the delimiter before each chunk.
    """

    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        # with # and /, there're 3 cases: #, /# and //
        # with /: and /, they can be merged into 2 cases: /: and //
        # essentially the same approach
        res = ""
        for s in strs:
            # NOTE: here we need to replace / before #
            res += s.replace("/", "//").replace("#", "/#")
            res += "#"
        return res

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        s_cur = ""
        while i < len(s):
            char = s[i]
            if char == "#":
                res.append(s_cur)
                s_cur = ""
                i += 1
            elif char == "/":
                # // or /#
                if s[i : i + 2] == "//":
                    s_cur += "/"
                else:
                    s_cur += "#"
                i += 2
            else:
                s_cur += char
                i += 1
        return res
