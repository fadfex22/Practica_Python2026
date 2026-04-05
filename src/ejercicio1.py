def ejercicio1():

    text = """Beautiful is better than ugly. 
    Explicit is better than implicit. 
    Simple is better than complex. 
    Complex is better than complicated. 
    Flat is better than nested. 
    Sparse is better than dense. 
    Readability counts. 
    Special cases aren't special enough to break the rules. 
    Although practicality beats purity. 
    Errors should never pass silently. 
    Unless explicitly silenced. 
    In the face of ambiguity, refuse the temptation to guess. 
    There should be one-- and preferably only one --obvious way to do it. 
    Although that way may not be obvious at first unless you're Dutch. 
    Now is better than never. 
    Although never is often better than *right* now. 
    If the implementation is hard to explain, it's a bad idea. 
    If the implementation is easy to explain, it may be a good idea. 
    Namespaces are one honking great idea -- let's do more of those!"""

    lineas = []

    for _ in text.split("\n"):
        lineas.append(_)

    palabras = []

    for _ in lineas:
        for word in _.split():
            palabras.append(word)

    prom_palabras = round(len(palabras) / len(lineas), 2)

    print("Total de lineas: ", len(lineas))
    print("Total de palabras: ", len(palabras))
    print("Promedio de palabras por linea: ", prom_palabras)
    print(f"Lineas por encima del promedio ({prom_palabras} palabras): ")
    for linea in lineas:
        if len(linea.split()) > prom_palabras:
            print(f"- {linea.strip()}")