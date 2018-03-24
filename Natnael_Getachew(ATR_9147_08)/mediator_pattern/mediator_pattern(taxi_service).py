class ControlCenter:
    ##The MEDIATOR class
    def __init__(self):
        self.drivers = [] 

    def takeCall(self, customer):
        for driver in self.drivers:
            if driver.location == customer.location:
                self.delegateTask(driver, customer)
        
    def delegateTask(self, driver, customer):
        driver.customerPhone = customer.phoneNumber
        print("Dear", customer.name, "a taxi will arrive at", customer.location, "shortly") 

    def registerDriver(self, driver):
        self.drivers.append(driver)
        


class Customer:
    ##A COLLEAGUE class
    def __init__(self, name, location, phoneNumber, controlCenter):
        self.name = name
        self.location = location
        self.phoneNumber = phoneNumber
        self.controlCenter = controlCenter

    def callTaxi(self):
        print (self.name,": I need a taxi at", self.location)
        self.controlCenter.takeCall(self)
        


class TaxiDriver:
    ##A COLLEAGUE class
    def __init__(self, name, location, customerPhone):
        self.name = name
        self.location = location
        self.customerPhone = customerPhone
        
        


def main():
    controlCenter = ControlCenter()
    taxiDriver = TaxiDriver("nati", "5 kilo", "")
    customer = Customer("mezi", "5 kilo", "555-000", controlCenter)
    controlCenter.registerDriver(taxiDriver)
    customer.callTaxi()


if __name__ == "__main__":
    main()
