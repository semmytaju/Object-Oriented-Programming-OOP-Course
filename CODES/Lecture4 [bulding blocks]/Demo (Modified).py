# create class
class Car:
    # variables
    
    # constructor without parameter
    def __init__(self):
        self.car_color = "Red"
        self.car_brand = "Toyota"
        self.car_year = "Tahun 2023"

    # method 1
    def carInfo(self):
        print("Car Color is {0}".format(self.car_color))
        print("Car brand is {0}".format(self.car_brand))

    # method 2
    def carPark(self):
        print("Parking time is over.")
        return "Return car park.!!!"

    # method 3
    def carSpeed(self):
        print("Car speed so too fast.")
        return "Return car speed.!!!"

    # method 4
    def carStatus(self):
        return "The car is in good condition."

    # main method
    def main(self):
        print("This is the main function of the class.")

        # call functions
        self.carInfo()
        self.carPark()
        self.carSpeed()

if __name__ == '__main__':
    # create object of class
    obj_car = Car()
    
    obj_car.main()
    print(obj_car.car_color)
    print(obj_car.car_brand)
    print(obj_car.car_year)  # Print output of variable car_year
    
    print("{0}".format(obj_car.carPark()))
    print("{0}".format(obj_car.carSpeed()))
    print(obj_car.carStatus())  # Print output of method carStatus
