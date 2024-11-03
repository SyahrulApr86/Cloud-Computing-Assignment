import json

def handle(req):
    try:
        # Parsing request JSON
        request_data = json.loads(req)
        panjang_sisi = float(request_data.get("panjang_sisi"))

        # Menghitung luas persegi
        luas = panjang_sisi ** 2

        # Menyiapkan response JSON
        response = {
            "luas": luas,
            "status": "success"
        }
        return json.dumps(response)
    
    except (TypeError, ValueError):
        return json.dumps({
            "error": "Parameter panjang_sisi tidak valid",
            "status": "error"
        })
