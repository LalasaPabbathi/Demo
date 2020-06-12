import json
import jsonpath
import requests

with open('urldata.json') as readdata:
    readurl = json.load(readdata)      #read json from a file


def test_fetchdata():
    getresponse = requests.get(readurl['get'])
    json_response = json.loads(getresponse.content)   #converts json string document into python dictionary
    assert getresponse.status_code == 200
    id = jsonpath.jsonpath(json_response, 'data[0].id')
    assert id[0] == 7


def test_postdata():
    post_response = requests.post(readurl["post"],
                        {
                            "name": "morpheus",
                            "job": "leader"
                        }
                        )
    json_response = json.loads(post_response.content)
    id = jsonpath.jsonpath(json_response, "id")
    print(id)
    assert post_response.status_code == 201

    with open('postop.json', 'w') as readdata:
        opdata = json.dump(json_response, readdata)  #json format into a file


def test_updatedata():
    put_response = requests.put(readurl["put"],
                       {
                           "name": "morpheus",
                           "job": "zion resident"
                       }
                       )
    json_response = json.loads(put_response.content)
    updated = jsonpath.jsonpath(json_response, "updatedAt")
    print(updated)
    assert put_response.status_code == 200

    with open('putop.json', 'w') as readdata:
        opdata = json.dump(json_response, readdata)


def test_deletedata():
    url = requests.delete(readurl["delete"])
    assert url.status_code == 204
