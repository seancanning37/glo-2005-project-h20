from persistence import CustomerRepository

class CustomerService:
    def __init__(self):
        self.customerRepository = CustomerRepository.CustomerRepository()

    def isEmailAlreadyUsed(self, email):
        return self.customerRepository.isEmailAlreadyUsed(email)

    def isUsernameAlreadyUsed(self, username):
        return self.customerRepository.isUsernameAlreadyUsed(username)

    def areLoginInformationsValid(self, email, password):
        return self.customerRepository.areLoginInformationsValid(email, password)


    def addCustomer(self, name, email, username, login):
        self.customerRepository.addCustomer(name, email, username, login)
