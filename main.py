import os, random
from datetime import datetime

types = ["Village","City Lagos","Japa","School","Rich vs Poor","Arranged","Facebook DM"]
today = random.choice(types)

print(f"Hello Iam chimaco!")
print(f"My AI studio is alive!")
print(f"Today type: {today} romance - {datetime.now()}")
print(f"Posting to Facebook Page: Iam chimaco")
print(f"Posting to YouTube Channel: Iam chimaco")

with open("video_ready.txt","w") as f:
    f.write(f"African romance video - {today}")
