from persistence import CustomerRepository
from .Customer import Customer

def createCustomerFromCursorInfo(customerInfos):
    customer = Customer()
    customer.id = customerInfos[0]
    customer.name = customerInfos[1]
    customer.phone = customerInfos[2]
    customer.email = customerInfos[3]
    customer.username = customerInfos[4]
    customer.address = customerInfos[6]
    customer.city = customerInfos[8]
    customer.country = customerInfos[9]
    return customer


class CustomerService:
    def __init__(self):
        self.customerRepository = CustomerRepository.CustomerRepository()

    def getCustomerFromId(self, customerId):
        customer = createCustomerFromCursorInfo(self.customerRepository.getCustomerFromId(customerId))
        return customer

    def isEmailAlreadyUsed(self, email):
        return self.customerRepository.isEmailAlreadyUsed(email)

    def isUsernameAlreadyUsed(self, username):
        return self.customerRepository.isUsernameAlreadyUsed(username)

    def areLoginInformationsValid(self, email, password):
        return self.customerRepository.areLoginInformationsValid(email, password)

    def addCustomer(self, name, email, username, login):
        self.customerRepository.addCustomer(name, email, username, login)

    def getCustomerIdFromEmail(self, email):
        return self.customerRepository.getCustomerIdFromEmail(email)

    def updateCustomerName(self, customerId, newName):
        return self.customerRepository.updateCustomerName(customerId, newName)

