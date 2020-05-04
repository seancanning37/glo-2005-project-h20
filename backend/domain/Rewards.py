class Rewards:
    def __init__(self, rewardsInfo):
        self.customer_id = int(rewardsInfo[0])
        self.money_earned = float(rewardsInfo[1])