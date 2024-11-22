class Animal:
    def __init__(self, name, species, age, color, weight):
        self.name = name
        self.species = species
        self.age = age
        self.color = color
        self.weight = weight
        print(f"Створено тварину: {self.name}, вид: {self.species}")


    def display_info(self):
        print(f"Ім'я: {self.name}, Вид: {self.species}, Вік: {self.age}, Колір: {self.color}, Вага: {self.weight} кг")


    def grow_older(self):
        self.age += 1
        print(f"{self.name} постаріла на рік. Тепер її вік: {self.age} років.")


    def change_weight(self, new_weight):
        self.weight = new_weight
        print(f"Вага {self.name} змінена на {self.weight} кг.")


    def __del__(self):
        print(f"Тварина {self.name} видалена.")


cat = Animal("Мурка", "Кішка", 3, "сірий", 4.5)
dog = Animal("Бобик", "Собака", 5, "чорний", 10.0)


cat.display_info()
cat.grow_older()
cat.change_weight(5.0)
cat.display_info()


dog.display_info()
dog.grow_older()
dog.change_weight(11.0)
dog.display_info()