# Classification of animals.
# Dumisani Mathabathe
# 11/03/2025

print('Welcome to the Biology Expert')
print('-----------------------------')
print('Answer the following questions by selecting from among the options.')
skeleton = input('The skeleton is (internal/external)?\n')
if skeleton == 'internal':
  fertilisation = input('The fertilisation of eggs occurs (within the body/outside the body)?\n')
  if fertilisation == 'within the body':
    production = input('Young are produced by (waterproof eggs/live birth)?\n')
    if production == 'waterproof eggs':
      skin = input('The skin is covered by (scales/feathers)?\n')
      if skin == 'scales':
        print('Type of animal: Reptile')
      elif skin == 'feathers':
        print('Type of animal: Bird')
    elif production == 'live birth':
        print("Type of animal: Mammal")    
  elif fertilisation == 'outside the body':
    habitat = input('It lives (in water/near water)?\n')
    if habitat == 'in water':
      print('Type of animal: Fish')
    elif habitat == 'near water':
      print('Type of animal: Amphibian')    
elif skeleton == 'external':
    print('Type of animal: Arthropod')
    

