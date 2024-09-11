from flask import Flask, request
import requests, json, re

CHANNEL_ACCESS_TOKEN = "<CHANNEL_ACCESS_TOKEN>"

def webhook(request):
    req = request.get_json(silent=True, force=True)

    try:
        userId = req.get("payload").get("data").get("source").get("userId")
        partialRes(userId)
    except:
        pass

    try:
        pageName = req.get('pageInfo').get("displayName")
    except AttributeError:
        return 'json error'
    
    input = req.get('text')
    if pageName == "Detection":
        res = getRes(input, 1)
    if pageName == "Warning":
        res = getRes(input)

    return json.dumps(res, indent = 4)


# get espd model predictd result
def getModelResult(text):
    url = "<MODEL_API_URL>"
    data = { 'text': text }
    res = requests.post(url, json=data)
    result = res.json()["return"]

    return result
            

# generate response
def getRes(input, overflow=0):
    text = re.sub(r"[^a-zA-Z0-9() ]", "", input.replace('\n'," "))
    result = float(getModelResult(text))

    if (result > 0.5):
        res1 = ["The result shows that someone may have bad intentions towards you."]
        res2 = ["Maybe we can talk about him. Would you want to share more about him?"]
        if (overflow):
            # target page : Warning
            target = "<PAGE_ID>"
    else:
        res1 = ["There seems to be no apparent danger in this conversation."]
        res2 = ["Feel free to talk me more if you need. I will be here."]
        # target page : Request
        target = "<PAGE_ID>"
    
    messages = [
                    { "text": { "text": res1 } },
                    { "text": { "text": res2 } }
               ]
    fulfillmentResponse = {"messages": messages}
    
    if (result > 0.5 and not overflow):
        res = {"fulfillmentResponse":fulfillmentResponse}
    else:
        res = {"fulfillmentResponse":fulfillmentResponse, "targetPage": target}

    return res
    
# sent partial response to user
def partialRes(userId):

    headers = { "Content-Type": "application/json", "Authorization": "Bearer "+ CHANNEL_ACCESS_TOKEN }
    data = json.dumps({
        "to": userId,
        "messages":[
            {
                "type":"text",
                "text":"Ok. Just a moment."
            },
        ]
    })
    r = requests.post("<LINE_MESSAGE_API_URL>", headers=headers, data=data)

    if r.status_code != 200:
        log(r.status_code)
        log(r.text)