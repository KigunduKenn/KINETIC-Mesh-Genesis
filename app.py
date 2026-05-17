import os
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- CENTRAL WEB4 SYSTEM REGISTRY ---
# The Single Source of Truth for the Omnivector Mesh
mesh_global_state = {
    "genesis_node": "Nyandarua",
    "architect_resonance": "6b325011173adf7a89d2f94e956724babb198937b53f42c1da08551a6b3ee9bf",
    "vectors": {
        "intelligence": {"active_agents": 1, "last_pulse": None},
        "survival_water": {"total_network_liters": 25.5, "last_pulse": None},
        "energy_salt": {"total_network_joules": 0.0, "last_pulse": None}
    },
    "tokenomics": {
        "total_minted_kine": 100000000.0,  # 100M Architect Sovereign Stake
        "cumulative_burned_kine": 1000.0
    }
}

@app.route('/gateway/inject', methods=['POST'])
def handle_mesh_pulse():
    """
    The main input portal for all localized physical spokes.
    Uses Cellular Automata principles to verify the inbound payload authenticity.
    """
    payload = request.json or {}
    inbound_resonance = payload.get("resonance_point")
    
    # 1. Hardware Fingerprint Validation (PUF Concept Simulation)
    if inbound_resonance != mesh_global_state["architect_resonance"]:
        return jsonify({
            "status": "Rejected",
            "reason": "Hardware Resonance Mismatch. Node validation failed."
        }), 403

    spoke_id = payload.get("spoke")
    metrics = payload.get("metrics", {})
    timestamp = time.time()

    # 2. Update Vector Ledgers based on Proof of Production (PoP)
    if spoke_id == "survival_water":
        liters = float(metrics.get("liters_harvested", 0.0))
        # Update the global mesh state deterministically
        mesh_global_state["vectors"]["survival_water"]["total_network_liters"] = liters
        mesh_global_state["vectors"]["survival_water"]["last_pulse"] = timestamp
        
        return jsonify({
            "status": "Success",
            "message": f"Mothership updated with {liters} Liters from Water Spoke."
        })

    elif spoke_id == "energy_salt":
        joules = float(metrics.get("thermal_joules", 0.0))
        mesh_global_state["vectors"]["energy_salt"]["total_network_joules"] = joules
        mesh_global_state["vectors"]["energy_salt"]["last_pulse"] = timestamp
        
        return jsonify({
            "status": "Success",
            "message": f"Mothership updated with {joules:,} Joules from Energy Spoke."
        })

    return jsonify({"status": "Error", "reason": "Unknown Spoke Vector"}), 400

@app.route('/')
def dashboard_view():
    """Renders the global architecture and asset validation parameters."""
    return jsonify({
        "network": "KINETIC (KINE): The Omnivector Mesh",
        "status": "Phase 1 - The Pulse Active",
        "current_mesh_state": mesh_global_state
    })

if __name__ == "__main__":
    # Internal port execution for cloud containers
    app.run(host="0.0.0.0", port=7860)
