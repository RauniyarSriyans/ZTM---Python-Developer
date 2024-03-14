from translate import Translator

translator = Translator(to_lang="ja")

try: 
    with open('./terminal.txt') as my_file:
        text = my_file.readline()
        translation = translator.translate(text)
        print(translation)
        with open('./translate.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('check your file path')
