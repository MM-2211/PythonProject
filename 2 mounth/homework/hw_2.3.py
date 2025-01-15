class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    
    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value: int):
        self.__memory = value

    def make_computations(self):
        return self.cpu + self.memory

    def __str__(self):
        return f"Компьютер с центральным процессором: {self.__cpu} и с памятью: {self.__memory}"

    def __eq__(self, other):
        return self.__memory == other.memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.sim_cards_list):
            operator = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с номера {sim_card_number}, используется оператор: {operator} ")
        else:
            print("Неверная сим-карта")

    def __str__(self):
        return f"Телефон с сим-картами {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Чтобы дойти до {location}, нужно выйти на улицу 'Советская' и дойти до 'Горького' и повернуть на право")

    def __str__(self):
        return f"Смартфон с процессором {self.cpu}, с памятью на {self.memory} ГБ и с сим-картами {self.sim_cards_list}"

computer = Computer(10, 512)
phone = Phone(["Megacom", "O!", "Beeline"])
smartphone1 = SmartPhone(5, 128, ["Megacom", "O!"])
smartphone2 = SmartPhone(4, 256, ["Beeline", "O!"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print(computer.make_computations())

phone.call(1, "+996 774 345 564")
phone.call(2, "+996 555 342 453 ")

smartphone1.use_gps("ГУМ")
smartphone2.use_gps("Дордой Плаза")

print(computer != smartphone2)

