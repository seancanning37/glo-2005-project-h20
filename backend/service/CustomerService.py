from persistence import CustomerRepository
from domain.Customer import Customer
from utils import hash


def createCustomerFromCursorInfo(customerInfos):
    customer = Customer()
    customer.id = customerInfos[0]
    customer.name = customerInfos[1]
    customer.phone = customerInfos[2]
    customer.email = customerInfos[3]
    customer.username = customerInfos[4]
    customer.address = customerInfos[5]
    customer.city = customerInfos[7]
    customer.country = customerInfos[8]
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
        if (self.customerRepository.isEmailAlreadyUsed(email)):
            customerId = self.getCustomerIdFromEmail(email)
            hashedPassword = self.customerRepository.getCustomerHashedPasswordFromId(customerId)
            return hash.checkPassword(password, hashedPassword)
        return False

    def addCustomer(self, name, email, username, login):
        self.customerRepository.addCustomer(name, email, username, login)

    def getCustomerIdFromEmail(self, email):
        return self.customerRepository.getCustomerIdFromEmail(email)

    def updateCustomer(self, customerId, parameters):
        return self.customerRepository.updateCustomer(customerId, parameters)

    def getCustomerHashedPasswordFromId(self, customerId):
        return self.customerRepository.getCustomerHashedPasswordFromId(customerId)

    def emailExists(self, email):
        return self.customerRepository.emailExists(email);
