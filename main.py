import os, random, requests
from datetime import datetime

# 7 types of African romance
stories = {
 "Village": "Chiamaka waited in village for Obinna who went to Lagos with promise. Today he returns with story...",
 "City Lagos": "Lagos traffic could not stop their love. Amaka meets Chinedu in Danfo...",
 "Japa": "He japa to Canada, she stayed in Onitsha. But love no get visa wahala...",
 "School": "SS3 love that started with extra lesson. Now they want to marry...",
 "Rich vs Poor": "Billionaire son fall in love with poor girl selling akara. Family say no...",
 "Arranged": "Parents arranged marriage, but they find real love inside...",
 "Facebook DM": "He slid into her DM 'hi dear'. Now 2 years later, wedding..."
}

today_type = random.choice(list(stories.keys()))
story = stories[today_type]
time_now = datetime.now().strftime("%d %b %Y %I:%M%p")

print(f"❤️ Iam Chimaco Studio Alive!")
print(f"Type: {today_type}")
print(f"Time: {time_now}")
print(f"Story: {story}")

# FACEBOOK PAGE POSTING (needs FB_PAGE_TOKEN secret)
fb_token = os.getenv("FB_PAGE_TOKEN")
fb_page_id = os.getenv("FB_PAGE_ID", "") # we will get this

if fb_token:
    try:
        # Get Page ID if not set
        if not fb_page_id:
            r = requests.get(f"https://graph.facebook.com/v18.0/me/accounts?access_token={fb_token}")
            print(f"Pages: {r.text[:500]}")
        else:
            message = f"❤️ AFRICAN ROMANCE - {today_type.upper()} ❤️\n\n{story}\n\n#IamChimaco #AfricanLove #Nollywood #LoveStory\n\nPosted {time_now} - 3x daily"
            url = f"https://graph.facebook.com/v18.0/{fb_page_id}/feed"
            res = requests.post(url, data={"message": message, "access_token": fb_token})
            print(f"Facebook post result: {res.text}")
    except Exception as e:
        print(f"FB error: {e}")
else:
    print("No FB_PAGE_TOKEN yet - add it in Secrets to auto post")

# YOUTUBE posting comes next after FB works
print("✅ Robot finished - ready for YouTube next")
