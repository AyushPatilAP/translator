from translate import Translator

translator=Translator(to_lang='hi')
with open('yee.txt',mode='r') as my_file:
		text=my_file.read()
		translation=translator.translate(text)
		with open('test-hi.txt',mode='w') as my_file2:
			my_file2.write(translation)