from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
DATA_FILE = "annonces.json"

@app.route("/", methods=["GET"])
def home():
    return "Serveur actif"

@app.route("/annonce", methods=["POST"])
def receive_annonce():
    data = request.json
    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400

    annonces = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            annonces = json.load(f)

    annonces.append(data)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(annonces, f, ensure_ascii=False, indent=2)

    return jsonify({"status": "ok", "nb_total": len(annonces)})