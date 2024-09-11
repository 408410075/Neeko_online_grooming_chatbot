from flask import Flask, request
import requests, json

def webhook(request):
    req = request.get_json(silent=True, force=True)
    try:
        pageName = req.get('pageInfo').get("displayName")
        sessionInfo = req.get('sessionInfo')
        sessionName = req.get('sessionInfo').get("session")
    except AttributeError:
        return 'json error'
    
    try: 
        param = req.get('sessionInfo').get("parameters").get("gender_s")
    except:
        param = 0
    
    if (pageName == "About the friend"):
        param = 0

    if (param == "she"):
        res = {"sessionInfo": sessionInfo}
    else:
        input = req.get('text').lower()
        res = getRes(input, sessionName)

    return json.dumps(res, indent = 4)



# generate response
def getRes(input, sessionName):

    if ('she' in input or 'her' in input):
        gender_s = "she"
        gender_o = "her"
    else:
        gender_s = "he"
        gender_o = "him"
    
    sessionInfo = {
                "session": sessionName,
                "parameters": {
                    "gender_s": gender_s,
                    "gender_o": gender_o
                }
            }
    res = {"sessionInfo": sessionInfo}

    return res
