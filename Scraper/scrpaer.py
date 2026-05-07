import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}

files = {
    # 'file': ('Digit_2.png', '', 'image/png'),
    # 'file': (open("Images/Digit_4.png", "rb"), '', 'image/png'),
    'file': (open(r"..\Images\Digit_7.png", "rb")),
}

response = requests.post('http://127.0.0.1:8000/predict-image/', files=files)
print(response.json()["prediction"])
print("Done")