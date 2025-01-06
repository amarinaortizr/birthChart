#!/usr/bin/env python
# Banco de palabras para el autocompletado
#signos = ["Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"]
signos = ["Aries", "Acuario", "Cancer", "Capricornio", "Escorpio", "Geminis", "Leo", "Libra", "Piscis" ,  "Sagitario", "Tauro",  "Virgo"]

casasSignos = ["Casa 1 (Aries)", "Casa 2 (Tauro)", "Casa 3 (Geminis)", "Casa 4 (Cancer)", "Casa 5 (Leo)", "Casa 6 (Virgo)", "Casa 7 (Libra)", "Casa 8 (Escorpio)", "Casa 9 (Sagitario)", "Casa 10 (Capricornio)", "Casa 11 (Acuario)", "Casa 12 (Piscis)"]
#marina
casas = ["Casa 1", "Casa 2", "Casa 3", "Casa 4", "Casa 5", "Casa 6", "Casa 7", "Casa 8", "Casa 9", "Casa 10", "Casa 11", "Casa 12"]

fuego = "El Fuego está asociado con la pasión, la creatividad, la impulsividad, el hacer, la transformacion."
aire = "El Aire está asociado con la comunicación, la intelectualidad, los pensamientos, los conflictos."
agua = "El Agua está asociado con la sensibilidad, las emociones, los sentimientos."
tierra = "La Tierra está asociado con la estabilidad, la practicidad, lo terrenal."

#soles
soles = {}
#general
soles["general"] = " El Sol dirige la personalidad, la identidad, el ego y la conciencia.\
                         Es nuestro signo primario, el indicador más potente de quiénes somos. (Quien soy?)"
#  marina agregar signo de que es agua etc y lla palabra clave de inicio 0, viaje 1, talentos 2, retos 3,
#aries revisitar aries marina
#viaje
soles[signos[0]] = ["El guerrero. Signo de fuego (" + fuego + ")"]
soles[signos[0]].append("Viaje en el que debes de fusionar la autoconfianza con la paciencia y el altruismo.\
                        El crecimiento espiritual llega al reconocer que estas creando karma con cada uno de tus actos.\
                        Debes desarrollar autocontrol y consideracion a los demas para que surga tu confianza en lugar de actuar de manera irracional y egoista.")
#talentos
soles[signos[0]].append("Persona con iniciativa, firmeza y voluntad, una persona franca y con potencial para ser un verdadero lider\
                         Los Aries son directos y honestos. Lo que ves es lo que son realmente, y lo que dicen es lo que realmente quieren decir.\
                         Si un Aries cambia de idea no tendrá problema en expresarlo ni en corregir el rumbo inmediatamente.\
                         Puede lograr grandes cosas, siempre y cuando se tome el tiempo de empezar desde la intención pura,\
                         y de desarrollar la consideración y la moderación.")
#retos
soles[signos[0]].append("Retos con el egoismo, el descaro, personas inpacientes, impulsivas e intolerantes.\
                        se puede volver dominante, conflictivo, ensimismado e insensible.\
                        Al carecer de autocontrol es a veces temperamental y puede estallar y ser desagradable,\
                        Problemas con escuchar puntos de vista diferentes a los suyos.")

#acuario
#viaje
soles[signos[1]] = ["El autentico. Signo de Aire (" + aire + ")"]
soles[signos[1]].append("Viaje en el que debes de experimentar la libertad: primero mental, luego la autoexpresion y al final la de la comunidad.\
                    Necesitas romper ataduras y los limites destruyendo la opresion que se te impone.\
                    Eres una persona creativa que puede solucionar de forma ingeniosa los problemas.\
                    La clave es aprender que la verdadera libertad comienza en tu interior, una vez que aprendas a conectar contigo,\
                    podras abrirte a los demas y ofrecer tus dones a la comunidad.")
#talentos
soles[signos[1]].append("Personas originales, inventivas, progresistas interesadas en el humanitarismo.\
                         personas fascinantes para pasar el rato, sus mentes danzan llevandolos a lugares inesperados.\
                         Cuando examinan algo lo ven de formas distintas a el resto con perpectivas diferentes\
                         resuelven problemas facilmente encontrando soluciones unicas, personas con grandes ideas.\
                         Unen a las personas en comunidad, son espontaneos, autenticos y originales si los dejan ser.")
#retos
soles[signos[1]].append("Retos con lo impredecibles, testarudos e inconformistas que pueden llegar a ser.\
                         Se pueden revelar de una mala forma contra las opresiones, provocar a los demas sobrepasando sus limites.\
                         Se crean enemigos y hieren a las personas sin razon. Pueden volverse frios y les cuesta mantenerse en la realidad,\
                         ya que buscan la libertad y les parece mucho mas emocionante")

#cancer
#viaje
soles[signos[2]] = ["El Sensible. Signo de Agua (" + agua + ")"]
soles[signos[2]] = ["Viaje en el que debes aprender a proteger tu sensibilidad\
                     y poder usarla como don, compartiendo tu compasion. Desarrollar autoconciencia,\
                     para que cuando los sentimientos te consuman, podras reconocerlo y volver\
                     tranquilamente a tu centro. Al superar esto, podras sentir la profundidad\
                     de la existencia humana sin pesar."]
#talentos
soles[signos[2]].append("Personas amables, imaginativas y perceptivas, metiendose a su mundo de fantasia.\
                         Buen anfitrion, cuida de sus invitados y los atiende, crea sensacion de hospitalidad y seguridad.\
                         Puede ahondar en las emociones de los demas y sentirlas con ellos. Son personas entregadas\
                         aman a sus amigos y familiares profundamente y con naturalidad.\
                         Puede mostrar cierta dureza para proteger su vulnerabilidad.")
#retos
soles[signos[2]].append("Retos con el mal humor, la vulnerabilidad y las inseguridades.\
                         Puede llegar a ser temperamental, afilado y evasivo. Cuando no se siente\
                         seguro puede volverse duro y cerrarse, escondiendose y llevando a cabo actos de crueldad.\
                         Puede llegar a adoptar el salvajismo de otros y perder el coraje para ser vulnerable.")


#capricornio
#viaje
soles[signos[3]] = ["El Diligente. Signo de Tierra (" + tierra + ")"] #marina pendiente aqui me quede
soles[signos[3]] = ["Viaje en el que debes de experimentar la libertad: primero mentar, luego la autoexpresion y al final la de la comunidad.\
                    Necesitas romper ataduras y los limites destruyendo la opresion que se te impone.\
                    Eres una persona creativa que puede solucionar de forma ingeniosa los problemas.\
                    La clave es aprender que la verdadera libertad comienza en tu interior, una vez que aprendas a conectar contigo,\
                    podras abrirte a los demas y ofrecer tus dones a la comunidad."]
#talentos
soles[signos[3]].append("Personas originales, inventivas, progresistas interesadas en el humanitarismo.\
                         personas fascinantes para pasar el rato, sus mentes danzan llevandolos a lugares inesperados.\
                         Cuando examinan algo lo ven de formas distintas a el resto con perpectivas diferentes\
                         resuelven problemas facilmente encontrando soluciones unicas, personas con grandes ideas.\
                         Unen a las personas en comunidad, son espontaneos, autenticos y originales si los dejan ser.")
#retos
soles[signos[3]].append("Retos con lo impredecibles, testarudos e inconformistas que pueden llegar a ser.\
                         Se pueden revelar de una mala forma contra las opresiones, provocar a los demas sobrepasando sus limites.\
                         Se crean enemigos y hieren a las personas sin razon. Pueden volverse frios y les cuesta mantenerse en la realidad,\
                         ya que buscan la libertad y les parece mucho mas emocionante")
