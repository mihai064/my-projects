import time
print("hello")
var1 = input("what's your name? ")
print("nice to meet you",var1)
user_reply = input("do you wanna play something? ")
if user_reply == "yes":
  ur2 = input("greatfull. so do you like programmig? ")
  if ur2 == "yes":
   print ("let's learn python")
   user_reply2 = input ("do you want to try to make a calculator? ")
   if user_reply2 == "yes":
      a = input("a=")
      b = input("b=")
      ur3 = input ("what do you wanna do with this?")
      if ur3 == "+":
       print(int(a) + int(b))
      if ur3 == "-":
       print(int(a) - int(b))
      if ur3 == "*":
       print(int(a) * int(b))
      if ur3 == "/":
       print(int(a) / int(b))
  if user_reply2 == "no":
        print ("let's make a timer then")
        timer_timer = input ("how many seconds?")
        s=1
        while int(s) < int(timer_timer):
            print (s)
            s=s+1
            time.sleep(1.0)
            if int(s) == int(timer_timer) / 2:
                print("that's half")         
        else:
            print ("timer out")

         

else:
  print ("ok. bye then.")