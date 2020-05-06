import json
import urllib.request
import pprint

#function that taskes a https request and converts into json
def url_get(a):
    url = urllib.request.Request((a),headers={'User-Agent' : 'Riley Rohloff'})
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    names = data['data'] 
    return names

#variable that is generic attask API unsecured login
attask = url_get('https://rileyrohloff.my.workfront.com/version')

#API key for my Workfront user to make HTTPS request while not logged in. Or for running a script in the python shell
api_key = 'apikeygoeshere'


# function that encompasses my url_get function to make the URL more dynamic for my request. 
def workfront_request():
        
    print("OBJ TYPES TO CHOOSE FROM:\nOPTASK\nTASK\nPROJ\nHOUR")
    print("OBJ TYPE",end=' ')
    a = input('>> ')
    url = url_get('https://rileyrohloff.my.workfront.com/attask/api-unsupported/{a}/search?apiKey={api_key}'.format(a=a,api_key=api_key))
    return url


#THIS IS WHERE THE USER WILL START THE SCRIPT
object_1 = workfront_request()

#allows me to specify my keys based on my obj type define in my above funtion
def start():
        print('STATUS KEY EXCLUDE: CUR\tDED\tINP\tCPL',end=' ')
        status_1 = str(input('>>  '))
        print("AND",end=' ')
        status_2 = str(input('>>  '))
        for item in object_1:
                if item['status'] != status_1 and item['status'] != status_2:
                        print('\nOBJCODE: ' + item['objCode'])
                        print('Name: ' +item['name'])
                        print('\tStatus: ' + item['status'])
                        print('\tID: ' + item['ID'])
                        
        workfront_request()

start()


#my FOR loop that iterates though whatever object type I specify in my search_request function to return key:value json data. 
# for item in object_1:
#     if item['status'] != status_1 and item['status'] != status_2:
#         print('\nOBJCODE: ' + item['objCode'])
#         print('Name: ' +item['name'])
#         print('\tStatus: ' + item['status'])
#         print('\tEntry Date: ' + item['ID])
        
        








