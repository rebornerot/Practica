class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return f"{self.name} издаёт звук"

    def info(self):
        return f"Имя: {self.name}, Вид: {self.species}"



class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Кошка")
        self.breed = breed  

    def make_sound(self):
        return f"{self.name} мяукает"

    def scratch_furniture(self):
        return f"{self.name} царапает мебель!"

    def info(self):
        base_info = super().info() 
        return f"{base_info}, Порода: {self.breed}"



def main():
    print("=== Демонстрация наследования и полиморфизма ===\n")


    dog = Animal("Шарик", "Собака")
    print("1. Объект базового класса (Animal):")
    print(dog.info())
    print(dog.make_sound())
    print()

    cat = Cat("Нео", "Вислоухая")
    print("2. Объект производного класса (Cat):")
    print(cat.info())            
    print(cat.make_sound())     
    print(cat.scratch_furniture())  
    print()

    print("3. Полиморфизм — одинаковый вызов, разное поведение:")
    animals = [dog, cat]
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")
    print()

    print("4. Проверка наследования:")
    print(f"Cat — подкласс Animal: {issubclass(Cat, Animal)}")
    print(f"cat — экземпляр Animal: {isinstance(cat, Animal)}")



if __name__ == "__main__":
    main()