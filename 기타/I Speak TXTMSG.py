def translate_short_form(short_form):
    translation_table = {
        'CU': 'see you',
        ':-)': 'I’m happy',
        ':-( ': 'I’m unhappy',
        ';-)': 'wink',
        ':-P': 'stick out my tongue',
        '(~.~)': 'sleepy',
        'TA': 'totally awesome',
        'CCC': 'Canadian Computing Competition',
        'CUZ': 'because',
        'TY': 'thank-you',
        'YW': 'you’re welcome',
        'TTYL': 'talk to you later'
    }

    return translation_table.get(short_form, short_form)

def main():
    while True:
        short_form = input()
        translation = translate_short_form(short_form)
        print(translation)
        if short_form == 'TTYL':
            break

if __name__ == "__main__":
    main()
