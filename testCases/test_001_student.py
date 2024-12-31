import jsonpath
import requests
import json
import os
#import testData.readDataCL


class Test001:
    baseUrl = "http://localhost:3000/student/"


    def test001_Post(self):
        jsonfile = os.path.abspath(os.curdir) + '\\testData\\student.json'
        print(jsonfile)

        url = self.baseUrl
        path = os.path.abspath(os.curdir) + '\\testData\\inputcontent.json'
        file = open(path, 'r')
        json_input = file.read()
        response = requests.post(url,data=json_input)
        print(response.status_code)
        responseBody = json.loads(response.text)
        newpath = os.path.abspath(os.curdir) + '\\testData\\outcontent.json'
        newfile = open(newpath,'w')
        newfile.write(response.text)
        newfile.close()
        self.sid= jsonpath.jsonpath(responseBody,'id')
        print(self.sid[0])
        Test001.id=self.sid[0]


    def test001_Get(self):
        url=self.baseUrl+Test001.id
        ##send Get request
        response = requests.get(url)
        json_response = json.loads(response.text)

        sdata = jsonpath.jsonpath(json_response , 'id')


        assert response.status_code == 200
    def test001_Update(self):
        url =self.baseUrl+Test001.id
        path= os.path.abspath(os.curdir)+"\\testData\\update.json"
        file = open(path,'r')
        json_input = file.read()
        response = requests.put(url,json_input)
        jsonBody =json.loads(response.text)
        print(jsonpath.jsonpath(jsonBody,"name"))
        print(jsonpath.jsonpath(jsonBody,"Grade"))
        print(response.status_code)
        print(response.headers.get('Content-Length'))

    def test001_Delet(self):
        url = self.baseUrl+Test001.id
        response = requests.delete(url)
        print(response.status_code)
        assert 1 == 1
