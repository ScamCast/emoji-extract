# emoji-extract
 Extract emojis from text






### Emojis(text)
    import Emojis
    text = 😂 This is a test string 😄😃 This is 😀 a 😊test. 😉😜Test❤️
    emojis = Emojis(text)

### emojis.to_list()
    Output: ['😂', '😄', '😃', '😀', '😊', '😉', '😜', '❤️']

### emojis.to_dict()
    Output: {'😂': 1, '😄': 1, '😃': 1, '😀': 1, '😊': 1, '😉': 1, '😜': 1, '❤️': 1}

### emojis.to_string()
    Output: 😂😄😃😀😊😉😜❤️

### emojis.strip()
    Output:  This is a test string  This is  a test. Test

### emojis.strip(extra_spaces=False)
    Output: This is a test string This is a test. Test
