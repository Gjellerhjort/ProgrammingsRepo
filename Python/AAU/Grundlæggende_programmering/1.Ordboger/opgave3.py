animal: str = 'cat'

def change_animal_to_dog() -> None:
     global animal
     animal = 'dog'

change_animal_to_dog()

print(animal)