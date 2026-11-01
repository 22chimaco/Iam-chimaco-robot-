import os
import requests

token = os.environ.get("FB_PAGE_TOKEN")
page_id = os.environ.get("FB_PAGE_ID")

# If page ID not set, auto find it
if token and not page_id:
    r = requests.get(f"https://graph.facebook.com/v18.0/me/accounts?access_token={token}")
    print("Pages:", r.text)
    data = r.json().get("data", [])
    if data:
        page_id = data[0]["id"]
        token = data[0]["access_token"]

message = """Chiamaka waited in village for Obinna who went to Lagos...

3 months no call. Her mother says "Marry Chief's son!"

But today, bike man brings letter...

Obinna is back, but not alone 😭

PART 1 - Should I continue? Comment YES!

#IamChimaco #Nollywood #NigerianStory"""

if token and page_id:
    url = f"https://graph.facebook.com/v18.0/{page_id}/feed"
    res = requests.post(url, data={"message": message, "access_token": token})
    print("POST RESULT:", res.text)
    if "id" in res.text:
        print("SUCCESS POSTED TO FACEBOOK!")
    else:
        print("Failed - check token")
else:
    print("No token or page_id found")
    if token:
        r = requests.get(f"https://graph.facebook.com/v18.0/me/accounts?access_token={token}")
        print(r.text)
