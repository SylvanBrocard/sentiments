import requests

@app.route("/model")
def summarize(userTxt):
    url = "http://localhost:5000/model/predict"
    data = {
    "text": [
        userTxt
        ]
    }

    res = requests.post(url, json=data)

    return res.text



print(summarize("nick gordon 's father -lrb- left and right -rrb- gave an interview about the 25-year-old fiance of bobbi kristina brown . it has been reported that gordon , 25 , has threatened suicide and has been taking xanax since . whitney houston 's daughter was found unconscious in a bathtub in january . on wednesday , access hollywood spoke exclusively to gordon 's stepfather about his son 's state of mind ."))