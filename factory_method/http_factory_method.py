import http.client
from abc import ABC, abstractmethod

class HttpRequest(ABC):
    @abstractmethod
    def request(self, id: int) -> str:
        pass

class HttpGet(HttpRequest):
    def __init__(self, domain: str, path: str):
        self.__domain = domain
        self.__path = path

    def request(self, id: int) -> str:
        conn = http.client.HTTPSConnection(self.__domain)
        conn.request("GET", f"/{self.__path}/{id}")
        response = conn.getresponse()

        if response.status == 200:
            data = response.read()
            return data.decode("utf-8")
        else:
            print(f"Erri en la solicitud {response.status}")

        conn.close()

class HttpRequestFactory(ABC):
    def __init__(self, domain: str, path: str):
        self._domain = domain
        self._path = path

    @abstractmethod
    def create(self) -> HttpRequest:
        pass 

class HttpGetFactory(HttpRequestFactory):
    def create(self):
        return HttpGet(self._domain, self._path)
    
http_get_factory = HttpGetFactory("jsonplaceholder.typicode.com", "posts")
http_get = http_get_factory.create()

res = http_get.request(10)
print(res)