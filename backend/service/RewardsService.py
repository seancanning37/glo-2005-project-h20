from persistence import RewardsRepository


class RewardsService:
    def __init__(self):
        self.RewardsService = RewardsService.RewardsRepository()

    def get(self, customer_id):
        return self.RewardsService.get(customer_id)

