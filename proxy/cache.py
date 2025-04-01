from mimetypes import init
from abc import ABC, abstractmethod
import http.client


class Request(ABC):
    @abstractmethod
    def get(self,id:int):
        pass


class GetRequest(Request):
    def __init__(self,domain:str,path:str):
        self.__domain = domain
        self.__path = path

    def get(self,id:int):
        print("Se va al servicio")
        conn = http.client.HTTPSConnection(self.__domain)
        conn.request("GET",f"/{self.__path}/{id}")
        response = conn.getresponse()
        if response.status == 200:
            data = response.read()
            return data.decode("utf-8")
        else:
            print(f"error solicitud {response.status}")
        conn.close()

class CacheGetRequest(Request):
    def __init__ (self,get_request: GetRequest):
        self.__get_request = get_request
        self.__cache = {}

    def get(self,id:int):
        if id in self.__cache:
            print(f"Proxy:Obtenemos la informacion de {id} del cache")
            return self.__cache[id]

        print(f"Proxy: se realiza solicitud de {id}")
        data = self.__get_request.get(id)
        self.__cache[id] = data
        return data
get_request = GetRequest("jsonplaceholder.typicode.com","posts")
#print(get_request.get(1))


cache_get_request = CacheGetRequest(get_request)
print(cache_get_request.get(1))
print(cache_get_request.get(1))
