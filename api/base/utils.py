import random

def slugGenerate(name):
   slug =  (''.join(random.choice(name.replace(" ", "_")) for i in range(30))).lower()

   return slug

def requestCheck(a):
   if a != None:
      print(a)
      return a
   else:
      return ""