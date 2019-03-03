import json
import urllib.request
import urllib.parse
import sched, time


taskID = []

apiKey = input("What is your API Key?  ")
domain = input("What is your Workfront domain? ")


def url_get(a):
    url = urllib.request.Request((a),headers={'User-Agent' : 'Riley Rohloff'})
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    names = data['data'] 
    return names

def call_1():
    customer_api = url_get(f'https://{domain}.my.workfront.com/attask/api-unsupported/task/search?DE:Status%20Notes_Mod=notblank&fields=parameterValues&apiKey={apiKey}')
    for item in customer_api:
            taskID.append(item['ID'])
            
def delay(a):
    time.sleep(a)
        






#This is my verification function that included some basic steps that get consent of the user to go ahead and run the below API calls to Workfront.
def start():
    print("Do you understand that this program is meant for the intention of deleting Custom field values in your system? Which means that any previous values that were or are now associated with the Custom Fields will be gone and cannot be easily retrieved?")

    choice = str(input(">> "))



    if 'Yes' in choice:
        call_1()
    elif 'No' in choice:
        print("We cannot authorize this script to run if you do not comply. Terminating script now...")
        exit("EXITING")
    else: 
        print("That is not a valid option. Options should include either 'Yes' or 'No' values. Please Try again.")
        start()
start()


# payload_1 = urllib.request.urlopen(f'https://rileyrohloff.my.workfront.com/attask/api-unsupported/task/{taskID[0]}?DE:Status%20Notes=&method=PUT&apiKey=9321lg99y5vqhad6i26eekj7555ad96j')
# data2 = json.loads(payload_1.read())
# print("\nData:\n")
# print('SUCCESS')

# payload_2 = urllib.request.urlopen(f'https://rileyrohloff.my.workfront.com/attask/api/v9.0/task/{taskID[1]}?updates={{"DE:Status%20Notes":"Riley%20Sucks"}}&method=PUT&apiKey=9321lg99y5vqhad6i26eekj7555ad96j')
# data3 = json.loads(payload_2.read())
# print("\nData:\n")
# print('SUCCESS')


#API call payload that sends blank updates to wide the field on the tasks specified from my original search query to Workfront. Also pulling all items (Workfront Task IDs) from my list to format them into my variable call.


def payload_call():
    if len(taskID) != 0:
        for ID in taskID:
            payload_1 = urllib.request.urlopen(f'https://{domain}.my.workfront.com/attask/api-unsupported/task/{ID}?DE:Status%20Notes=&method=PUT&apiKey={apiKey}')
            data2 = json.loads(payload_1.read())
            print(f"\nSENDING PAYLOAD TO Task: {ID}\n")
            print('SUCCESS')
        print('ALL PAYLOADS SENT SUCCUSSFULLY')      
    else:
        print('No IDs to pull')
payload_call()