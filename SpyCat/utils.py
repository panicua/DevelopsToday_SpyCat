import requests


def cat_breed_api_get() -> set | None:
    request = requests.get("https://api.thecatapi.com/v1/breeds")
    breeds = set()
    if request.status_code == 200:
        for breed in request.json():
            breeds.add(breed['name'])
        return breeds

    print(f"CatBreedAPI error: {request.status_code}")