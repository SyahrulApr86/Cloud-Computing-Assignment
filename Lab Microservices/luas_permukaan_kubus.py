import json

def handle(req):
    try:
        # Parsing request JSON
        request_data = json.loads(req)
        panjang_rusuk = float(request_data.get("panjang_rusuk"))

        # Menghitung luas permukaan kubus
        luas_permukaan = 6 * (panjang_rusuk ** 2)

        # Menyiapkan response JSON
        response = {
            "luas_permukaan": luas_permukaan,
            "status": "success"
        }
        return json.dumps(response)
    
    except (TypeError, ValueError):
        return json.dumps({
            "error": "Parameter panjang_rusuk tidak valid",
            "status": "error"
        })
