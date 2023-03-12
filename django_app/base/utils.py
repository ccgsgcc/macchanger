import random 

def slugGenerate(name:str):
   slug =  (''.join(random.choice(name.replace(" ", "_")) for i in range(30))).lower()

   return slug