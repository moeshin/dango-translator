import requests

_MAP_LANGUAGE = {
    "jap": "jp",
    "eng": "en",
}
_BASE_URL = "https://fanyi.baidu.com"


def get_language(language, to_lower=True):
    if to_lower:
        language = language.lower()
    return _MAP_LANGUAGE.get(language, language)


class BaiduFanyiOCR:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "Referer": _BASE_URL,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/111.0.0.0 Safari/537.36"
        }

    def init(self):
        self.session.head(_BASE_URL)

    def request(self, image, src="jp", dest="zh"):
        return self.session.post(_BASE_URL + "/getocr", data={
            "from": src,
            "to": dest,
        }, files=[
            ('image', ('image.png', image, 'image/png'))
        ])


_instance = None


def instance():
    global _instance
    if not _instance:
        _instance = BaiduFanyiOCR()
        _instance.init()
    return _instance


def main():
    ocr = instance()
    image = "./config/other/image.jpg"

    with open(image, "rb") as fp:
        data = fp.read()

    print(ocr.request(data).json())

    # for i in range(5):
    #     start = time.time()
    #     with ocr.request(data) as resp:
    #         print(i, "%.03f" % (time.time() - start), resp.json())
    #     time.sleep(0.5)


if __name__ == "__main__":
    main()
