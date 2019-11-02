import emoji
import regex



test_str = '''
Th👽is i👽s 😊a t👽👽👽👽👽👽est strin👽g.👙👙.
🤔 🙈 😌 💕 👭 👙 👩🏾‍🎓 👨‍👩‍👦‍👦 😊 🙅🏽 🙅🏽
.'''



## Extract emojis from text and return a list ##

def extract_emojis(text):

    emoji_list = []
    data = regex.findall(r'\X', text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI for char in word):
            emoji_list.append(word)

    return emoji_list


extracted_emojis = extract_emojis(test_str)
print(extracted_emojis)




## Extract emojis from string and return a
## dictionary with a count of each emoji

def extract_emoji_dict(text):

    emoji_list = []
    data = regex.findall(r'\X', text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI for char in word):
            emoji_list.append(word)

    emoji_dict = {}
    for moji in emoji_list:
        if not moji in emoji_dict:
            emoji_key = moji
            emoji_value = 1
        elif moji in emoji_dict:
            emoji_key = moji
            emoji_value = emoji_dict.get(emoji_key) + 1

        emoji_dict.update({ emoji_key: emoji_value})

    return emoji_dict


emoji_dict_count = extract_emoji_dict(test_str)
print(emoji_dict_count)



# Test: Write emojis to text file

with open('emoji.txt','wb') as E:
    for x in emoji_dict_count:
        E.write(x.encode())
