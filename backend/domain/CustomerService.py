from persistence import CustomerRepository

class CustomerService:
    def __init__(self):
        self.customerRepository = CustomerRepository.CustomerRepository()

    def isEmailAlreadyUsed(self, email):
        result = self.customerRepository.getCustomerFromEmail(email)
        if result == -1:
            return False
        return True

    def addCustomer(self, name, email, username, login):
        self.customerRepository.addCustomer(name, email, username, login)
