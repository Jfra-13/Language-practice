from translate import Translator

translator = Translator(from_lang='spanish', to_lang='english')

txt = input('Dime lo que deseas traducir: ')
res = translator.translate(txt)
print(res)