import requests
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class RequestWrapper:
    def __init__(self):
        pass

    @staticmethod
    def get(url: str,
            data: dict = None,
            headers: dict = None,
            params: dict = None):
        log.debug(f"getting {url} with {headers} and {params}")
        try:
            result = requests.get(url=url,
                                  params=params,
                                  headers=headers,
                                  data=data)
            if result.status_code == 200:
                print(result.content)
        except Exception:
            raise Exception(f"Cannot get {url}")

    @staticmethod
    def post(url: str,
             data: dict = None,
             headers: dict = None,
             params: dict = None):
        try:
            result = requests.post(url=url,
                                   params=params,
                                   headers=headers,
                                   data=data)
            if result.status_code == 200:
                print(result.content)
        except Exception:
            raise Exception(f"Cannot post {url}")

    @staticmethod
    def put(url: str,
            data: dict = None,
            headers: dict = None,
            params: dict = None):
        try:
            result = requests.put(url=url,
                                  params=params,
                                  headers=headers,
                                  data=data)
            if result.status_code == 200:
                print(result.content)
        except Exception:
            raise Exception(f"Cannot put {url}")

    @staticmethod
    def delete(url: str,
               data: dict = None,
               headers: dict = None,
               params: dict = None):
        try:
            result = requests.delete(url=url,
                                     params=params,
                                     headers=headers,
                                     data=data)
            if result.status_code == 200:
                print(result.content)
        except Exception:
            raise Exception(f"Cannot delete {url}")


if __name__ == '__main__':
    url = "http://www.baidu.com/s?"
    params = {'wd': 'python'}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/54.0.2840.99 Safari/537.36"}

    RequestWrapper.get(url=url,
                       params=params,
                       headers=headers)
