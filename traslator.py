from translate import Translator

translator=Translator(to_lang='hi')
with open('#your file',mode='r') as my_file:
		text=my_file.read()
		translation=translator.translate(text)
		with open('#the new file',mode='w') as my_file2:
			my_file2.write(translation)
