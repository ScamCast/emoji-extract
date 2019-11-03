from pprint import pprint as pp
import emoji
import regex
import os


class Emojis:

    def __init__(self, text=None):
        self.text = text
        self.emoji_list = []
        self.emoji_dict = {}
        self.count = 0

    def to_list(self, text=None):
        self.emoji_list = []
        self.text = text or self.text
        if not self.text:
            raise Exception('No text string specified for: Emojis().to_list()')
        words = regex.findall(r'\X', self.text)
        for word in words:
            if any(char in emoji.UNICODE_EMOJI for char in word):
                self.count += 1
                self.emoji_list.append(word)
        return self.emoji_list

    def to_dict(self, text=None):
        self.to_list(text)
        self.emoji_dict = {}
        for moji in self.emoji_list:
            if not moji in self.emoji_dict:
                emoji_key = moji
                emoji_value = 1
            elif moji in self.emoji_dict:
                emoji_key = moji
                emoji_value = self.emoji_dict.get(emoji_key) + 1
            self.emoji_dict.update({ emoji_key: emoji_value})
        return self.emoji_dict

    def to_string(self, text=None):
        self.to_list(text)
        return ''.join(self.emoji_list)

    def strip(self, text=None, extra_spaces=True):
        self.to_list(text)
        self.stripped = self.text
        for moji in self.emoji_list:
            self.stripped = self.stripped.replace(moji, '')
        if not extra_spaces:
            """
            ::extra_spaces = True|False
            Remove extra spaces from result string.

                text = '😂 This is a test string 😄😃 This is 😀 a 😊test. 😉😜Test❤️ '

                extra_spaces(text, extra_spaces=True)
                >>> ' This is a test string  This is  a test. Test '

                extra_spaces(text, extra_spaces=False)
                >>> 'This is a test string This is a test. Test'
            """
            while '  ' in self.stripped:
                self.stripped = self.stripped.replace('  ', ' ')
            if self.stripped.startswith(' '):
                self.stripped = self.stripped[1:]
            if self.stripped.endswith(' '):
                self.stripped = self.stripped[:-1]
        return self.stripped



# Test: Write emojis to text file
if __name__ == '__main__':

    emojis = Emojis('😂 This is a test string 😄😃 This is 😀 a 😊test. 😉😜Test❤️ ')

    as_list = emojis.to_list()
    as_dict = emojis.to_dict()
    as_string = emojis.to_string()
    as_strip= emojis.strip()
    as_strip_spaces = emojis.strip(extra_spaces=False)

    scriptpath = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(scriptpath, 'example.txt')

    with open(filepath,'wb') as f:
        f.write(f"""
Input:
text = {emojis.text}

Instance: emojis = Emojis(text)

Method: emojis.to_list()
Output: {as_list}

Method: emojis.to_dict()
Output: {as_dict}

Method: emojis.to_string()
Output: {as_string}

Method: emojis.strip()
Output: {as_strip}

Method: emojis.strip(extra_spaces=False)
Output: {as_strip_spaces}
        """.encode())
