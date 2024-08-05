import numpy as np
import requests

class dataLogger:

    def __init__(self) -> None:
        self.userName = 'admin'
        self.password = '12345'
        self.IPAdress = '192.168.24.62'
        self.fileFormat = 'html'

    def constructHTTPRequest(self, command: str) -> str:
        """
            Function which creates the base string used for the HTTP request. 
        """
        return 'http://{}:{}@{}/?command={}&uri=dl:public&format={}'.format(userName, password, IPAdress, command, fileFormat)

    def dataQuery(self) -> str:
        HTTPRequest = self.constructHTTPRequest('dataquery') # http://192.168.4.14/?command=dataquery&uri=dl:onemin.ptemp&format=html mode=most-recent&p1=3
        return requests.get(HTTPRequest)

    def browseSymbols(self) -> str:
        HTTPRequest = self.constructHTTPRequest('dataquery') # http://192.168.4.14/?command=browsesymbols&uri=dl:&format=html
        return requests.get(HTTPRequest)

    def setValue(self) -> str:
        HTTPRequest = self.constructHTTPRequest('setvalueex') # http://192.168.4.14/?command=setvalueex&uri=dl:public.flag(1)&value=-1&format=html
        return requests.get(HTTPRequest)

    def clockCheck(self) -> str:
        HTTPRequest = self.constructHTTPRequest('ClockCheck') # http://192.168.4.14/?command=ClockCheck
        return requests.get(HTTPRequest)

    def clockSet(self) -> str:
        HTTPRequest = self.constructHTTPRequest('ClockSet') # http://192.168.4.14/?command=ClockSet&uri=dl:&format=html&time=2019-08-12T15:13:10.123
        return requests.get(HTTPRequest)
    
    def newestFiles(self) -> str:
        fileType = 'jpg'
        HTTPRequest = self.constructHTTPRequest('NewestFile') #   http://192.168.4.14/?command=NewestFile&expr=USR:*.jpg
        return requests.get(HTTPRequest)
    
    def listFiles(self) -> str:
        HTTPRequest = self.constructHTTPRequest('ListFiles') #  http://192.168.4.14/CPU/?command=ListFiles&format=html 
        return requests.get(HTTPRequest)

    def fileControl(self) -> str:
        pass

    def addFile(self) -> str:
        # curl -XPUT -v -S -T "testing.cr6" –user testing:testing1234 http://192.168.4.14/cpu
        pass

dl = dataLogger()
print(dl.constructHTTPRequest('test'))
