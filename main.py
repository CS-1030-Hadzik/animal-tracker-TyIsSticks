from animal import Animal
from dog import Dog

if __name__ == "__main__":

    kitty = Animal("Kitty", "Feline")
    fido = Dog("Fido", "Canine", "Bulldog")

    print (kitty)
    kitty.speak()

    print (fido)
    fido.speak()


    print("\nAll tracked animals:")
    for animal in Animal.all_animals:
        print(f"  - {animal}")
    
    