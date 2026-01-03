import requests

def get_joke():
    url = f"https://official-joke-api.appspot.com/random_joke"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        joke_data = {
            "type": data["type"],
            "description": data["setup"],
            "punchline": data["punchline"],
            "id": data["id"]
        }
        return joke_data
    else:
        print(f"There was an error.")
        return None  

def main():
  joke_data = get_joke()

  if joke_data:
      print(f"Type: {joke_data['type']}")

if __name__ == "__main__":
    main()
