                                                                        #Comienzo del juego

def presentacion():
    print("        *                                                            *        ")
    print("      *   *                                                        *   *      ")
    print("    *       *                                                    *       *    ")
    print("  *           *                                                *           *  ")
    print("*               *           BIENVENIDO AL JUEGO              *               *")
    print("  *           *                 El AHORCADO                    *           *  ")
    print("    *       *                                                    *       *    ")
    print("      *   *                                                        *   *      ")
    print("        *                                                            *        ")

                                                                         #Final del juego

def conclusion():
    print("------------------------------------------------------------------------------")
    print("        *                                                            *        ")
    print("      *   *                                                        *   *      ")
    print("    *       *                                                    *       *    ")
    print("  *           *                                                *           *  ")
    print("*               *              MUCHAS GRACIAS                *               *")
    print("  *           *                   POR JUGAR                    *           *  ")
    print("    *       *                                                    *       *    ")
    print("      *   *                                                        *   *      ")
    print("        *                                                            *        ")
    print("------------------------------------------------------------------------------")

                                                                        #Niveles del juego

def niveles():
    print("En este juego hay 4 niveles:")
    print("Nivel facil = 1")
    print("Nivel intermedio = 2")
    print("Nivel dificil = 3")
    print("Nivel hardcore = 4")
    selectnivel=int(input("Ingresa el numero del nivel que quieres jugar: "))
    print("------------------------------------------------------------------------------")
    if(selectnivel==1):
        print("Has seleccionado el nivel facil")
        facil()
    if(selectnivel==2):
        print("Has seleccionado el nivel intermedio")
        intermedio()
    if(selectnivel==3):
        print("Has seleccionado el nivel dificil")
        dificil()
    if(selectnivel==4):
        print("Has seleccionado el nivel hardcore")
        hardcore()

                                                                           #Nivel Fácil

def facil():
    print("En el nivel facil tienes 5 intentos para lograr adivinar la palabra")
    print(" ")
    print("Tambien puedes elegir entre las 2 categorias de este nivel:")
    print("Colores = 1")
    print("Animales = 2")
    selectfacil=int(input("Selecciona la categoria ingresando el numero: "))
    print("-----------------------------------------------------------------------------")
    if(selectfacil==1):
        print("Has seleccionado la categoria: Colores")
        colores()
    if(selectfacil==2):
        print("Has seleccionado la categoria: Animales")
        animales()

                                                                      #Categoría Colores (Fácil)

def listacolores():
    import random
    coloreslista=['Azul','Rojo','Verde','Amarillo','Naranja','Blanco','Negro','Morado','Rosa','Fucsia','Turquesa','Lila','Gris','Marron','Beige','Plateado','Dorado','Lavanda','Marfil','Esmeralda']
    return random.choice(coloreslista).upper()

def colores():
    print("")
    palabra=listacolores()
    adivinar=[]
    mostrar=[]
    intentos=5
    letra=''
    run=True
    adivinar=list(palabra)
    for item in adivinar:
        mostrar.append("_")
    while run:
        print(' '.join(mostrar))
        letra=input("Adivina la palabra introduciendo una letra: ").upper()
        for num in range(2):
            print()
        fallo=False
        if letra not in adivinar:
            fallo=True
            intentos=intentos-1
            print("Fallaste. Te quedan",intentos, "intentos")
        else:
            for key, value in enumerate(adivinar):
                if(value==letra):
                    mostrar[key]=value
        if(intentos<=0):
            run=False
            print("Has perdido la partida. La palabra era: ",palabra)
        elif(adivinar==mostrar):
            run=False
            print("Has ganado la partida. La palabra es: ",palabra)

                                                                     #Categoría Animales (Facil)

def listanimales():
    import random
    animaleslista=['Abeja','Ballena','Cangrejo','Elefante','Flamenco','Gallo','Gorila','Gusano','Jirafa','Koala','Langosta','Leopardo','Loro','Mariposa','Pulpo','Sapo','Tigre','Zorro','Tortuga','Serpiente']
    return random.choice(animaleslista).upper()

def animales():
    print("")
    palabra=listanimales()
    adivinar=[]
    mostrar=[]
    intentos=5
    letra=''
    run=True
    adivinar=list(palabra)
    for item in adivinar:
        mostrar.append("_")
    while run:
        print(' '.join(mostrar))
        letra=input("Adivina la palabra introduciendo una letra: ").upper()
        for num in range(2):
            print()
        fallo=False
        if letra not in adivinar:
            fallo=True
            intentos=intentos-1
            print("Fallaste. Te quedan", intentos, "intentos")
        else:
            for key, value in enumerate(adivinar):
                if (value==letra):
                    mostrar[key]=value
        if(intentos<=0):
            run = False
            print("Has perdido la partida. La palabra era: ", palabra)
        elif(adivinar==mostrar):
            run=False
            print("Has ganado la partida. La palabra es: ", palabra)

                                                                     #Nivel Intermedio (Geografía)

def intermedio():
    print("En el nivel intermedio (EL NIVEL GEOGRAFIA) tienes 8 intentos para lograr adivinar la palabra")
    print(" ")
    print("Tambien puedes elegir entre las 2 categorias de este nivel:")
    print("Paises = 1")
    print("Ciudades = 2")
    selectintermedio=int(input("Selecciona la categoria ingresando el numero: "))
    print("---------------------------------------------------------------")
    if(selectintermedio==1):
        print("Has seleccionado la categoria: Paises")
        paises()
    if(selectintermedio==2):
        print("Has seleccionado la categoria: Ciudades")
        ciudades()

                                                                 #Categoría Países (Intermedio)

def listapaises():
    import random
    paiseslista=['Afganistan','Alemania','Australia','Bolivia','Brazil','Bulgaria','Chipre','Colombia','Dinamarca','Egipto','Finlandia','Indonesia','Islandia','Jamaica','Mozambique','Somalia','Jugoslavia','Venezuela','Pakistan','Groenlandia']
    return random.choice(paiseslista).upper()

def paises():
    print("")
    palabra=listapaises()
    adivinar=[]
    mostrar=[]
    intentos=8
    letra=''
    run=True
    adivinar=list(palabra)
    for item in adivinar:
        mostrar.append("_")
    while run:
        print(' '.join(mostrar))
        letra=input("Adivina la palabra introduciendo una letra: ").upper()
        for num in range(2):
            print()
        fallo=False
        if letra not in adivinar:
            fallo=True
            intentos=intentos-1
            print("Fallaste. Te quedan",intentos, "intentos")
        else:
            for key, value in enumerate(adivinar):
                if(value==letra):
                    mostrar[key]=value
        if (intentos<=0):
            run=False
            print("Has perdido la partida. La palabra era: ",palabra)
        elif(adivinar==mostrar):
            run=False
            print("Has ganado la partida. La palabra es: ",palabra)

                                                              #Categoria Ciudades (Intermedio)

                                                                #Categoría Ciudades (Intermedio)

def listaciudades():
    import random
    ciudadeslista=['Estambul','Bangkok','Amsterdan','Melbourne','Barcelona','Vancouver','Manchester','Johannesburgo','Caracas','Bordeaux','Kagoshima','Winnipeg','Alejandría','Frankfurt','Zurich','Helsinki','Reikiavik','Wellington','Damasco','Montevideo']
    return random.choice(ciudadeslista).upper()

def ciudades():
    print("")
    palabra=listaciudades()
    adivinar=[]
    mostrar=[]
    intentos=8
    letra=''
    run=True
    adivinar=list(palabra)
    for item in adivinar:
        mostrar.append("_")
    while run:
        print(' '.join(mostrar))
        letra=input("Adivina la palabra introduciendo una letra: ").upper()
        for num in range(2):
            print()
        fallo=False
        if letra not in adivinar:
            fallo=True
            intentos=intentos-1
            print("Fallaste. Te quedan",intentos, "intentos")
        else:
            for key, value in enumerate(adivinar):
                if(value==letra):
                    mostrar[key]=value
        if (intentos<=0):
            run=False
            print("Has perdido la partida. La palabra era: ",palabra)
        elif(adivinar==mostrar):
            run=False
            print("Has ganado la partida. La palabra es: ",palabra)

                                                                        #Nivel Dificil

def dificil():
    print("En el nivel dificil tienes 12 intentos para lograr adivinar la palabra")
    print(" ")
    print("Tambien puedes elegir entre las 2 categorias de este nivel:")
    print("Marcas de Autos = 1")
    print("Instrumentos Musicales = 2")
    selectdificil=int(input("Selecciona la categoria ingresando el numero: "))
    print("---------------------------------------------------------------")
    if (selectdificil==1):
        print("Has seleccionado la categoria: Marcas de Autos")
        cars()
    if (selectdificil==2):
        print("Has seleccionado la categoria: Instruemntos Musicales")
        music()

                                                            #Categoría Marcas de Autos (Difícil)

def listacars():
    import random
    marcasdeautoslista=['Amphicar','Autobianchi','Bentley','Bugatti','AlfaRomeo','Chevrolet','Daihatsu','DeLorean','Encava','Freightliner','Ferrari','Hyundai','Lamborghini','Lincoln','Maserati','Mitsubishi','Peugeot','Renault','Ssangyong','Volkswagen']
    return random.choice(marcasdeautoslista).upper()

def cars():
    print("")
    palabra=listacars()
    adivinar=[]
    mostrar=[]
    intentos=12
    letra = ''
    run=True
    adivinar=list(palabra)
    for item in adivinar:
        mostrar.append("_")
    while run:
        print(' '.join(mostrar))
        letra=input("Adivina la palabra introduciendo una letra: ").upper()
        for num in range(2):
            print()
        fallo=False
        if letra not in adivinar:
            fallo=True
            intentos=intentos-1
            print("Fallaste. Te quedan",intentos, "intentos")
        else:
            for key, value in enumerate(adivinar):
                if(value==letra):
                    mostrar[key]=value
        if (intentos<=0):
            run=False
            print("Has perdido la partida. La palabra era: ",palabra)
        elif(adivinar==mostrar):
            run = False
            print("Has ganado la partida. La palabra es: ",palabra)

                                                       #Categoría Instrumentos Musicales (Difícil)

def listamusic():
    import random
    instrumentosmusicaleslista=['Guimbarda','Zeusofono','Armonica','Phominx','Epigonio','Gadulka','Birbyne','Frula','Violoncello','Contrabajo','Ukelele','Lijerica','Silnyen','Laud','Yaybahar','Tubulum','Flageolet','Cornamusa','Acordeon','Launchpad']
    return random.choice(instrumentosmusicaleslista).upper()

def music():
    print("")
    palabra=listamusic()
    adivinar=[]
    mostrar=[]
    intentos=12
    letra=''
    run=True
    adivinar=list(palabra)
    for item in adivinar:
        mostrar.append("_")
    while run:
        print(' '.join(mostrar))
        letra=input("Adivina la palabra introduciendo una letra: ").upper()
        for num in range(2):
            print()
        fallo=False
        if letra not in adivinar:
            fallo=True
            intentos=intentos-1
            print("Fallaste. Te quedan",intentos, "intentos")
        else:
            for key, value in enumerate(adivinar):
                if(value==letra):
                    mostrar[key]=value
        if(intentos<=0):
            run=False
            print("Has perdido la partida. La palabra era: ",palabra)
        elif(adivinar==mostrar):
            run=False
            print("Has ganado la partida. La palabra es: ",palabra)

                                                                     #Nivel Hardcore

def hardcore():
    print("En el nivel hardcore (EL NIVEL CIENCIA) tienes 15 intentos para lograr adivinar la palabra")
    print(" ")
    print("Tambien puedes elegir entre las 2 categorias de este nivel:")
    print("Elementos de la Tabla Periodica = 1")
    print("Enfermedades del Cuerpo Humano = 2")
    selecthardcore=int(input("Selecciona la categoria ingresando el numero: "))
    print("---------------------------------------------------------------")
    if (selecthardcore==1):
        print("Has seleccionado la categoria: Elementos de la Tabla Periodica")
        quimica()
    if (selecthardcore==2):
        print("Has seleccionado la categoria: Enfermedades del Cuerpo Humano")
        cuerpo()

                                                      #Categoria Elementos de la Tabla Periódica (Hardcore)

def listaquimica():
    import random
    quimicalista=['Germanio','Hidrogeno','Molibdeno','Neptunio','Oxigeno','Praseodimio','Rutherfordio','Silice','Tantalio','Xenon','Wolframio','Vanadio','Rubidio','Paladio','Plutonio','Niquel','Manganeso','Krypton','Lawrencio','Californio']
    return random.choice(quimicalista).upper()

def quimica():
    print("")
    palabra=listaquimica()
    adivinar=[]
    mostrar=[]
    intentos=15
    letra=''
    run=True
    adivinar=list(palabra)
    for item in adivinar:
        mostrar.append("_")
    while run:
        print(' '.join(mostrar))
        letra=input("Adivina la palabra introduciendo una letra: ").upper()
        for num in range(2):
            print()
        fallo=False
        if letra not in adivinar:
            fallo=True
            intentos=intentos-1
            print("Fallaste. Te quedan",intentos, "intentos")
        else:
            for key, value in enumerate(adivinar):
                if(value==letra):
                    mostrar[key]=value
        if(intentos<=0):
            run=False
            print("Has perdido la partida. La palabra era: ",palabra)
        elif(adivinar==mostrar):
            run=False
            print("Has ganado la partida. La palabra es: ",palabra)

                                                        #Categoría Enfermedades del Cuerpo Humano

def listabody():
    import random
    cuerpolista=['Gastritis','Tuberculosis','Criptorquidia','Balanitis','Tricomoniasis','Glaucoma','Barotrauma','Osteoporosis','Seborrea','Dermatitis','Hemofilia','Sarampion','Hemocromatosis','Bruxismo','Anisakidosis','Chikungunya','Hipermetropia','Telangiectasias','Shigelosis','Uveitis']
    return random.choice(cuerpolista).upper()

def cuerpo():
    print("")
    palabra=listabody()
    adivinar=[]
    mostrar=[]
    intentos=15
    letra=''
    run=True
    adivinar=list(palabra)
    for item in adivinar:
        mostrar.append("_")
    while run:
        print(' '.join(mostrar))
        letra=input("Adivina la palabra introduciendo una letra: ").upper()
        for num in range(2):
            print()
        fallo=False
        if letra not in adivinar:
            fallo=True
            intentos=intentos-1
            print("Fallaste. Te quedan", intentos, "intentos")
        else:
            for key, value in enumerate(adivinar):
                if (value==letra):
                    mostrar[key]=value
        if (intentos<=0):
            run=False
            print("Has perdido la partida. La palabra era: ", palabra)
        elif(adivinar==mostrar):
            run=False
            print("Has ganado la partida. La palabra es: ", palabra)






                                                                         #Menú Principal
presentacion()
niveles()
conclusion()

