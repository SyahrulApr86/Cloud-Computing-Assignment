import json

def handle(req):
    # Misalnya, kita mengharapkan request dalam bentuk JSON
    request_data = json.loads(req)
    
    # Lakukan logika atau operasi yang dibutuhkan
    name = request_data.get("name", "world")
    
    # Siapkan response
    response = {
        "greeting": f"Hello, {name}!",
        "status": "success"
    }
    
    # Kembalikan response dalam format JSON
    return json.dumps(response)
