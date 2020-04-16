akinator = {
	("Он(а) IT'шник(ца)?", "да") : {
		("вопрос", "ответ") : "ответ акинатора", 
		("вопрос", "ответ") : {
			("вопрос", "ответ") : "ответ акинатора"
		}
	}
}




def ask(dictionary):
	try:
		for q, a in dictionary.keys():
			print(q)
			t = input()
			try:
				ask(dictionary[(q,t)])
			except KeyError:
				pass
	except AttributeError:
		print(dictionary)
		exit(0)

ask(akinator)					