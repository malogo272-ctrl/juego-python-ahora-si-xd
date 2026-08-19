import random
eleccion_maquina = 0
salud_maqui = 250
ataque_enemigo = 0
defensa_enemigo = False

#usuario
salud_user = 250
atacar = 0
curarse = 0
critico_list = 0
energia = 130
def atacar_user(energia,defensa_enemigo,salud_maqui):
 if energia > 80:
    energia = energia - 80 
    critico_list = random.randint(1,3) 
    atacar = random.randint(10,40)
    if critico_list <= 2:
       atacar = atacar * 2 
       print("FUE GOLPE CRITICO y el quitaste: ", atacar, "de daño")
    if defensa_enemigo:
       atacar = atacar // 2 
       print("El enemigo se defendio del ataque parte del ataque")
       defensa_enemigo = False
    salud_maqui = salud_maqui - atacar
    print("ahora quitaste ",atacar, "de daño") 
    return energia,defensa_enemigo,salud_maqui
 else:
     print("no tienes energia suficiente") 
 return energia,defensa_enemigo,salud_maqui
   
def curase_user(salud_user): 
 if salud_user >= 250: 
    print("no puedes curarte mas, tienes la vida al maximo.")
 else: 
     curarse = random.randint(30,60) 
     salud_user = salud_user + curarse
     if salud_user > 250:
        salud_user = 250 
        print("Te curaste:", curarse, "de vida") 
        print("ahora tienes",salud_user, "de vida")
     return salud_user
     
def maquina_mecan(salud_user,defensa_enemigo):
   eleccion_maqui = random.randint(1,4)
   if eleccion_maqui <= 3:
      ataque_enemigo = random.randint(10,80) 
      salud_user = salud_user - ataque_enemigo 
      print("El enemigo te ha atacado")
   elif eleccion_maqui == 4:
     defensa_enemigo = True 
     print("El enemigo decidio defenderse del daño en el sigiente turno")
   return salud_user, defensa_enemigo



print("MENU DEL JUEGO")
print("--------------")
print("1.jugar")
print("2.salir del juego")
usuario = int(input("elige lo que quieras hacaer: "))
if usuario == 1:
   print("--elige tu oponente--")
   print("1.  mono chiquito  ")
   print("2.  mono meidano  ")
   print("3.  mono grande  ")
   oponenete_elegido = int(input("oponente elegido: "))

   print("Bienvenido al juego de combate")
   if oponenete_elegido == 1:
      nombre_enemigo = "Mono pequeño"
      salud_maqui = 150
   elif oponenete_elegido == 2:
      nombre_enemigo = "Mono mediano"
      salud_maqui = 350    
   elif oponenete_elegido == 3:
      nombre_enemigo = "Mono grande"
      salud_maqui = 650 
   while salud_user > 0 and salud_maqui > 0:

     print("esta esta son sus estadisticas: salud tuya: ", salud_user, " salud del enemigo: " ,salud_maqui)
     energia = energia + 20 
     print("esta es tu energia: ", energia) 
     print("1.atacar") 
     print("2.curarse") 
     print("3.huir")
     #ataque de usuario
     eleccion = int(input("que quieres hacer? ")) 
     if eleccion == 1: 
       energia,defensa_enemigo,salud_maqui = atacar_user(energia,defensa_enemigo,salud_maqui)
     elif eleccion == 2:
        salud_user = curase_user(salud_user)
     elif eleccion == 3: 
        print("el juego se ha ha acabado") 
        break
     else: 
       print("la opcion en invalida")

     #turno del enemigo
     if salud_maqui > 0: 
        salud_user,defensa_enemigo = maquina_mecan(salud_user,defensa_enemigo)

   if salud_maqui <= 0: 
       print("haz ganado") 
   elif salud_user <= 0: 
       print("haz perdido lol")   
elif usuario == 2:
   print("haz salido")