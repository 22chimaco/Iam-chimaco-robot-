import os, requests
token=os.environ.get("FB_PAGE_TOKEN")
page_id=os.environ.get("FB_PAGE_ID")
print(f"Token exists: {bool(token)}")
print(f"Page ID from secret: {page_id}")
message="Test post from robot! If you see this on Facebook page, robot works! #IamChimaco"
url=f"https://graph.facebook.com/v20.0/{page_id}/feed"
r=requests.post(url, data={"message":message,"access_token":token})
print(f"POST RESULT: {r.text}")
