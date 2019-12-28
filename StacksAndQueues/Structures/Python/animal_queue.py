import datetime

from .queue import Queue

class AnimalQueue:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
    def enqueue(self, animal):
        if animal == "Cat":
            self.cats.enqueue(animal, datetime.datetime.now())
        elif animal == "Dog":
            self.dogs.enqueue(animal, datetime.datetime.now())
        return
    def dequeue_dog(self):
        dog = self.dogs.dequeue()
        return dog
    def dequeue_cat(self):
        cat = self.cats.dequeue()
        return cat
    def dequeue_any(self):
        cat = self.cats.first()
        dog = self.dogs.first()
        if cat.timestamp < dog.timestamp:
            return self.dequeue_cat()
        else:
            return self.dequeue_dog()
    def print_queue(self):
        cat_pos = 0
        dog_pos = 0
        string = ''
        while cat_pos < len(self.cats.queue) or dog_pos < len(self.dogs.queue):
            cat = self.cats.queue[cat_pos].timestamp
            dog = self.dogs.queue[dog_pos].timestamp
            if cat < dog:
                string += 'Cat|'
                cat_pos += 1
            else:
                string += 'Dog|'
                dog_pos += 1
            if cat_pos >= len(self.cats.queue):
                for i in range(dog_pos, len(self.dogs.queue)-1):
                    string += 'Dog|'
                string+='Dog'
                break
            elif dog_pos >= len(self.dogs.queue):
                for i in range(cat_pos, len(self.cats.queue)-1):
                    string += 'Cat|'
                string+='Cat'
                break
        print(string)
