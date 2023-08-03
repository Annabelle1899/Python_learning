from dotenv import load_dotenv
load_dotenv()
import os


def translate(content, From="en", to="zh-Hans"):
    import requests, uuid, json

    # Add your key and endpoint
    key = os.getenv("KEY")
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = os.getenv("LOCATION")

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': From,
        'to': to
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': content
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

    # print(response[0]["translations"][0]["text"])
    return response[0]["translations"][0]["text"]


if __name__ == '__main__':
    print(translate(From="en", to="zh-Hans", content="I would really like to drive your car around the block a few times!"))
    print(translate(content="I would really like to drive your car around the block a few times!"))
    print(translate("I would really like to drive your car around the block a few times!"))