class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""
        for str in strs:
            encoded_str += str + "π" 
        return encoded_str


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_str = []
        split_string = s.split("π")

        if split_string and split_string[-1] == "":
            split_string.pop()

        for str in split_string:
            if str != "":
                decoded_str.append(str)
            else:
                decoded_str.append("")
        return decoded_str
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))