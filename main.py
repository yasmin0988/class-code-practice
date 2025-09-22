from house import House
from lesson import Lesson
from person import Person
from product import Product
from sim_card import SimCard
from visit import Visit


house1 = House("white", 2, 20, 12)
print(house1)

lesson1 = Lesson("Mohammadi", 17.5, 3)
print(lesson1)

person1 = Person("female", 19, "Iranian")
print(person1)

product1 = Product("Milk", 90000, "10-12-2025")
print(product1)

sim_card1 = SimCard(98912, "irancell", 16)
print(sim_card1)

visit1 = Visit(98912, "1-1-2026", "14:30:00", 1500000)


