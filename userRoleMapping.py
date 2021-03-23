# The script allows to collect list of users, assinged roles, last login.
# Use Cases:
#   1. Clean up after RBAC migration that left many "Automatically created role"
#   2. Clean up Dorment users 
#   3. Perform access Audit

import requests
import json
import pprint

#Collect Credentials and Global variables
#cloudWAFAPIid=int(input("Enter Cloud WAF API key ID : "))
#cloudWAFkey=input("Enter Cloud WAF API key : ")
#AccountID = int(input("Enter Account ID :"))
accountID = 1814107
cloudWAFAPIid= 42836
cloudWAFkey="ab9e8e9c-ffec-4454-8ff1-45f82b7c9f5b"

# Get list of all user Emails that has any roles assinged to it. 
# #Roles are only at RBAC account level.
def alluserEmails():
    baseurl="https://api.imperva.com/user-management/v1/roles"
    params={'accountId': accountID,'api_id': cloudWAFAPIid, 'api_key': cloudWAFkey }

    allroles=requests.get(baseurl,params)
    if allroles.status_code != 200:
        print('Status:', allroles.status_code, 'Headers:', allroles.headers, 'Error Response:',allroles.json())
        exit()
    rolesEmails = list()

    for r in allroles.json():
        for u in r['userAssignment']:
            rolesEmails.append(u['userEmail'])
    return list(set(rolesEmails))

def getUserDetails(roleAndEmail):
    for user in roleAndEmail:
        baseurl="https://api.imperva.com/user-management/v1/users"
        params={'accountId': accountID ,'api_id': cloudWAFAPIid, 'api_key': cloudWAFkey, 'userEmail' : user }
        userdetails=requests.get(baseurl,params)
        if userdetails.status_code != 200:
            print('Status:', allusers.status_code, 'Headers:', allusers.headers, 'Error Response:', allusers.json())
            exit()
        userobject=userdetails.json()
        if userobject['rolesDetails']:
            pprint.pprint(userobject)

    
userEmails = alluserEmails()
userdetails = getUserDetails(userEmails)


