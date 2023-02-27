MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', '!':'-.-.--'}

#Decode the Morse code
def decode_morse(morse_code):
    words = morse_code.split("   ")
    res = []
    for i in words:
        word = i.split()
        res.append(word)

    to_return = []
    for i in res:
        translated_word = []
        for j in i:
            for k in MORSE_CODE_DICT.keys():
                if j == MORSE_CODE_DICT[k]:
                    translated_word.append(k)
                    break
        to_return.append(translated_word)

    final_string = ""
    for i in to_return:
        final_string += " " + ''.join(i)
    return final_string[1:]

print(decode_morse('-.-- ..- .-. .-   .. ...   -.- .-.. --- .-- -.'))


def code_morse(morse_code):
    words = morse_code.split()
    result = ""

    for i in words:
        cur_word = ""
        for j in i:
            cur_word += MORSE_CODE_DICT[j] + " "
        result += cur_word[:-1] + "   "

    return result[:-3]

print(code_morse('YURA IS KLOWN'))