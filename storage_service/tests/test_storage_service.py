from tests.conftest import client


def test_add_meme(client):

    with open("memes/5Psm79C8upM.jpg", 'rb') as file:
        response = client.post("http://127.0.0.1:8000/private-api/v1/memes/", files={'file': file})

    assert response.status_code == 200

    # cleanup
    client.delete("http://127.0.0.1:8000/private-api/v1/memes/1")

def test_get_meme(client):

    with open("memes/5Psm79C8upM.jpg", 'rb') as file:
        client.post("http://127.0.0.1:8000/private-api/v1/memes/", files={'file': file})

    response = client.get("http://127.0.0.1:8000/private-api/v1/memes/1")
    assert response.status_code == 200

    # cleanup
    client.delete("http://127.0.0.1:8000/private-api/v1/memes/1")

def test_get_memes(client):

    with open("memes/5Psm79C8upM.jpg", 'rb') as file:
        client.post("http://127.0.0.1:8000/private-api/v1/memes/", files={'file': file})

    with open("memes/r4vsWkzUc6A.jpg", 'rb') as file:
        client.post("http://127.0.0.1:8000/private-api/v1/memes/", files={'file': file})

    response = client.get("http://127.0.0.1:8000/private-api/v1/memes/")
    assert response.status_code == 200

    client.delete("http://127.0.0.1:8000/private-api/v1/memes/1")
    client.delete("http://127.0.0.1:8000/private-api/v1/memes/2")

def test_update_file(client):

    with open("memes/5Psm79C8upM.jpg", 'rb') as file:
        client.post("http://127.0.0.1:8000/private-api/v1/memes/", files={'file': file})


    with open("memes/r4vsWkzUc6A.jpg", 'rb') as file:
        response = client.put("http://127.0.0.1:8000/private-api/v1/memes/1", files={'file': file})

    assert response.status_code == 200

    client.delete("http://127.0.0.1:8000/private-api/v1/memes/1")


