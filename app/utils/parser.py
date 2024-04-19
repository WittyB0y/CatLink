import requests
from lxml import html

LEVEL_OF_LINK = {
    "website": 1,
    "book": 2,
    "article": 3,
    "music": 4,
    "video": 5

}


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

            # get og:type
            og_type = tree.xpath('//meta[@property="og:type"]/@content')
            og_type = og_type[0].strip() if og_type else None
            og_type = LEVEL_OF_LINK[og_type] if og_type is not None else 1

            return {
                "title": title,
                "description": description,
                "image": image,
                "link_type": og_type
            }
        else:
            return {
                "title": "error",
                "description": f"status code {response.status_code}",
                "link_type": 1
            }
    except Exception:
        return None
