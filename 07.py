# slovar = {"a":1, "b":2, "c":3}

# try:
# 	value = slovar["d"]
# except KeyError:
# 	print ("Произошла ключевая ошибка (KeyError)!")
# else:
# 	print ("Ошибок не было, однако!")


slovar = {"a":1, "b":2, "c":3}

try:
	value = slovar["a"]
except KeyError:
	print ("Произошла ключевая ошибка (KeyError)!")
else:
	print ("Ошибок не было, однако!")
finally:
	print ("Последнее заявление выполнено!")