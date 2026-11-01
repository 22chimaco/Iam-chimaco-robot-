import os
import requests

token = os.environ.get("FB_PAGE_TOKEN")
page_id = os.environ.get("FB_PAGE_ID")

print(f"Token exists: {bool(token)}")
print(f"Page ID: {page_id}")

if not token or not page_id:
    print("ERROR: Missing token or page_id")
    exit(1)

message = """Chiamaka waited in village for Obinna who went to Lagos...

3 months no call. Her mother says "Marry Chief's son!"

But today, bike man brings letter...

Obinna is back, but not alone 😭

PART 1 - Should I continue? Comment YES!

#IamChimaco #Nollywood #NigerianStory"""

url = f"https://graph.facebook.com/v20.0/{page_id}/feed"
res = requests.post(url, data={"message": message, "access_token": token})
print(f"POST RESULT: {res.text}")

if res.status_code == 200 and "id" in res.json():
    print("SUCCESS! POSTED TO FACEBOOK!")
else:
    print("FAILED - Check token permissions")
