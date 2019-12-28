import sys
import os
import time

sys.path.append(os.path.join("..",".."))
from Structures.Python.animal_queue import AnimalQueue

if __name__ == "__main__":
    animal_shelter = AnimalQueue()
    animals = ["Dog", "Dog", "Cat", "Dog", "Cat", "Cat", "Dog"]
    for animal in animals:
        animal_shelter.enqueue(animal)
        time.sleep(0.01)
    animal_shelter.print_queue()
    animal_shelter.dequeue_cat()
    animal_shelter.print_queue()
    animal_shelter.dequeue_dog()
    animal_shelter.print_queue()
    animal_shelter.dequeue_any()
    animal_shelter.print_queue()
    animal_shelter.dequeue_any()
    animal_shelter.dequeue_any()
    animal_shelter.print_queue()

