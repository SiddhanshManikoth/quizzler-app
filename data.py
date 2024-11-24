import requests

#creating required parameters for api
parameter = {
    "amount": 10,
    "type": "boolean",
}
# fetching data from trivia api
trivia_response = requests.get(url="https://opentdb.com/api.php", params=parameter)
# checking for errors
trivia_response.raise_for_status()
# converting fetch data to json
qna_json = trivia_response.json()
# formating data as per our use
question_data = qna_json["results"]
