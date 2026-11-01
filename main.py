import os
import requests

token = os.environ.get("FB_PAGE_TOKEN")
page_id = os.environ.get("FB_PAGE_ID")

print(f"Token exists: {bool(token)}")

# Auto find page ID if not provided
if token and not page_id:
    r = requests.get(f"https://graph.facebook.com/v20.0/me/accounts?access_token={token}")
    print(f"Pages response: {r.text}")
    data = r.json().get("data", [])
    if data:
        page_id = data[0]["id"]
        token = data[0]["access_token"]
        print(f"Found Page: {data[0]['name']} ID: {page_id}")

if not token or not page_id:
    print("ERROR: No token or page_id - add FB_PAGE_TOKEN secret")
    exit()

message = """Chiamaka waited in village for Obinna who went to Lagos...

3 months no call. Her mother says "Marry Chief's son!"

But today, bike man brings letter...

Obinna is back, but not alone 😭

PART 1 - Should I continue? Comment YES!

#IamChimaco #Nollywood #NigerianStory"""

url = f"https://graph.facebook.com/v20.0/{page_id}/feed"
res = requests.post(url, data={"message": message, "access_token": token})
print(f"POST RESULT: {res.text}")

if "id" in res.json():
    print("SUCCESS POSTED TO FACEBOOK!")
else:
    print("Failed to post - check token permissions")
