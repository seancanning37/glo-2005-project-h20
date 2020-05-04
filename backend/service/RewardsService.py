from persistence import RewardsRepository
from domain.Rewards import Rewards


class RewardsService:
    def __init__(self):
        self.rewardsRepository = RewardsRepository.RewardsRepository()

    def get(self, customer_id):
        return Rewards(self.rewardsRepository.get(customer_id))

