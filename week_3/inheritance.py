import csv
import os


class CarBase:
    """Родительский класс"""

    required = []

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = self.validate_value(brand)
        self.photo_file_name = self.validate_photo_name(photo_file_name)
        self.carrying = float(self.validate_value(carrying))
    
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]
        

    def validate_photo_name(self, ph_filename):
        ext = ['.jpg', '.jpeg', '.png', '.gif']
        root_ext = os.path.splitext(ph_filename)
        if root_ext[1] in ext:
            return ph_filename
        else:
            raise ValueError

    @staticmethod
    def validate_value(value):
        if value == '':
            raise ValueError
        return value

    @classmethod
    def create_from_dict(cls, data):
        """создает экземпляр класса из словаря с параметрами"""
        parameters = [data[parameter] for parameter in cls.required]
        return cls(*parameters)

class Car(CarBase):
    """Класс легковых машин"""
    car_type = 'car'
    required = ['brand', 'photo_file_name', 'carrying', 'passenger_seats_count']

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(self.validate_value(passenger_seats_count))


class Truck(CarBase):
    """Класс грузовиков"""

    car_type = 'truck'
    required = ['brand', 'photo_file_name', 'carrying', 'body_whl']

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand,photo_file_name, carrying)
        self.body_length, self.body_width, self.body_height = self.parse_whl(body_whl)

    


    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height

    def parse_whl(self, body_whl):
        try:
            length, width, height = (float(c) for c in body_whl.split("x", 2))
        except Exception:
            length, width, height = 0.0, 0.0, 0.0
        return length, width, height
    


class SpecMachine(CarBase):
    """Класс спец.техники"""

    car_type = 'spec_machine'
    required = ['brand', 'photo_file_name', 'carrying', 'extra']
    
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = self.validate_value(extra)


def get_car_list(csv_filename):
    car_types = {'car': Car, 'spec_machine': SpecMachine, 'truck': Truck}
    csv.register_dialect('cars', delimiter=';')
    car_list = []

    with open(csv_filename, 'r') as file:
        reader = csv.DictReader(file, dialect='cars')
        for row in reader:
            try:
                car_class = car_types[row['car_type']]
                car_list.append(car_class.create_from_dict(row))
            except Exception:
                pass
    return car_list

def _main():
    car = Car('mazda', '123.jpeg', '123', '1')
    truck = Truck('Nissan', 't1.jpg', '2.5', '2.4x2.3x2')
    get_car_list("coursera_week3_cars.csv")

if __name__ == "__main__":
    _main()   
    


