import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "abcdnehakvisgreat1705"
USERNAME = "itsnehakv"
parameters = {
    "token": TOKEN,  #---we generate token (i.e, user types it)
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
#-------request and checking if it was a success--------
#commented out since after running this, our acc in pixela has been created
#IMP__MUST BE TYPED
#
# response = requests.post(url=pixela_endpoint, json=parameters,headers=headers)
# print(response.text)

#OUTPUT--->{"message":"Success. Let's visit https://pixe.la/@itsnehakv17 , it is your profile page!","isSuccess":true}


graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
#POST - /v1/users/<username>/graphs  (from documentation)
graph_params={
    "id":"graph1",  #not like a token, like a variable
    "name":"My reading progress",
    "unit":"pages",
    "type":"int",
    "color":"ichou"
}
GRAPH_ID="graph1"
# graph_response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(graph_response.text)

date=datetime.datetime.now()
date_val=date.strftime("%Y%m%d")
print(date_val)
activity_params={
    "date":date_val,
    "quantity":input("How many pages did you read today?"),
}
activity_endpoint=f"{graph_endpoint}/{GRAPH_ID}"
activity_response=requests.post(url=activity_endpoint,json=activity_params,headers=headers)
print(activity_response.text)

put_method_endpoint=f"{activity_endpoint}/{date_val}"
put_method_params={
    "quantity":"5",
}
# put_response=requests.put(url=put_method_endpoint,json=put_method_params,headers=headers)
# print(put_response.text)
delete_method_endpoint=f"{activity_endpoint}/{date_val}"
# delete_response=requests.delete(url=put_method_endpoint,headers=headers)
# print(delete_response.text)
