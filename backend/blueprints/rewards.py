from flask import Blueprint, jsonify

from service.RewardsService import RewardsService

rewards = Blueprint("rewards", __name__, url_prefix="/")

@rewards.route("rewards/<customer_id>", methods=['GET'])
def getRewards(customer_id):
    rewardsService = RewardsService()
    rewards = rewardsService.get(customer_id)
    return jsonify(rewards.__dict__)


