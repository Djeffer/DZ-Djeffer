class Student:

    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

    class LaptopSpecifications:
        def __init__(self, model, processor, memory, c_name):
            self.model = model
            self.processor = processor
            self.memory = memory
            self.c_name = c_name

        def print_laptop(self):
            print(f'{self.c_name.name} => {self.model}, {self.processor}, {self.memory}')


s = Student("Roman")
lap = s.LaptopSpecifications("HP", "i7", "16", s)
lap.print_laptop()
s = Student("Vladimir")
lap = s.LaptopSpecifications("HP", "i7", "16", s)
lap.print_laptop()

