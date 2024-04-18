import requests
from lxml import html


def extract_data_from_url(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            # convert HTML to ElementTree obj
            tree = html.fromstring(response.content.decode("utf-8"))

            # get title from page
            title = tree.xpath('//title/text()')
            title = title[0].strip() if title else None

            # get description from meta tag description
            description = tree.xpath('//meta[@name="description"]/@content')
            description = description[0].strip() if description else None

            # get link on picture from og:image
            image = tree.xpath('//meta[@property="og:image"]/@content')
            image = image[0].strip() if image else None

            return {
                "title": title,
                "description": description,
                "image": image,
            }
        else:
            return {
                "title": "error",
                "description": f"status code {response.status_code}"
            }
    except Exception:
        return None
