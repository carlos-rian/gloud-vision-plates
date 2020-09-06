from dotenv import load_dotenv
from flask import Flask, request, jsonify, Response
from api.authorize import check_if_plate_have_permission
from api.get_plate import get_plates
from api.save_file import save_file

load_dotenv("/home/carlos-rian/Documentos/Projetos Jussi/GCP/api-vision/.env")

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def receive_image():
    if request.method == "GET":
        return """<form method="POST" enctype="multipart/form-data" action="/">
        <input type="file" name="file" multiple="">
        <input type="submit" value="add">
        </form>"""
    dir_files = save_file(req=request)
    if not dir_files:
        return (jsonify({"message": "file not found"}), 404, {"Content-Type": "application/json"})

    list_placas = []
    for dir_file in dir_files:
        placas = get_plates(filepath=dir_file)
        for placa in placas:
            if check_if_plate_have_permission(placa=placa):
                return (jsonify({"message": "success", "plate": placa}), 201, {"Content-Type": "application/json"})

    return (jsonify({"message": "failure, plate not found."}), 422, {"Content-Type": "application/json"})
