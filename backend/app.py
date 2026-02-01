from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.entropy import calculate_entropy
from utils.estimators import estimate_time
from attack_models.brute_force import brute_force_space
from attack_models.dictionary import dictionary_attack
from attack_models.hybrid import hybrid_attack
from attack_models.rule_based import rule_based
from attack_models.mask_attack import mask_reduction
from attack_models.hash_models import hash_multiplier

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    password = data["password"]
    attacker = data["attacker"]
    hash_type = data["hash"]

    results = {}

    entropy = calculate_entropy(password)
    results["entropy"] = entropy

    # Dictionary
    if dictionary_attack(password):
        results["dictionary"] = "Instant crack (common password)"

    # Hybrid
    if hybrid_attack(password):
        results["hybrid"] = "Vulnerable to hybrid attack"

    # Rule based
    if rule_based(password):
        results["rule_based"] = "Rule-based match likely"

    # Brute force
    space = brute_force_space(password)
    space *= mask_reduction(password)
    space *= hash_multiplier(hash_type)

    results["brute_force_time"] = estimate_time(space, attacker)

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
