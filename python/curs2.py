import random
import tkinter

window = tkinter.Tk()
user = 0
exitChoise = "0"
while exitChoise != "EXIT":
 

 print("Vrei sa inveti")
 button = tkinter.Button(window, text="Da",width=40)
 button.pack (padx=10, pady=10)
 button = tkinter.Button(window, text="Nu",width=40)
 button.pack (padx=10, pady=10)
 button = tkinter.Button(window, text="Poate",width=40)
 button.pack (padx=10, pady=10)
 button = tkinter.Button(window, text="Vedem",width=40)
 button.pack (padx=10, pady=10)
 if button == "da":
  print("ce vrei sa inveti :")
  print("1) prog c")
  print("2) prog c#")
  print("3) prog py")
  user = input ("ce program vrei sa inveti? (type: c or c# or py)")
  if user == "c":
     print("Este o alegere buna pentru inceput")
 elif user == "c#":
     print("Este o alegere buna daca vrei sa faci aplicatii")
 elif user == "py":
     print ("Este bun daca vrei sa inveti ML")
 elif user == "poate":
  print("Gandestete bine")
 elif user == "nu":
  print("o zi buna")
 elif user == "vedem":
    print("Sa ne jucam putin.")
    print("Alege un numar, intre 1si 10")
    numar = int(input("Care numar il alegi "))
    if  numar == random.randint(1,10):
       print("Acest numar este corect.")
       print("Ai castigat.")
       exitChoise = "EXIT"
    else:
      print("acest numar este incorect")
      print("Ai pierdut")
    exitChoise = "EXIT"
 exitChoise = input("Apasa inapoi la joc , or EXIT ptr a inchide jocul ")