import os
from dotenv import load_dotenv
import tweepy
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

load_dotenv()
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_KEY_SECRET')

@app.get("/")
def read_root():
    auth = tweepy.OAuthHandler(api_key, api_secret)
    return RedirectResponse(auth.get_authorization_url())


@app.get("/callback")
def read_item( oauth_token: str, oauth_verifier: str):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.request_token = {'oauth_token': oauth_token, 'oauth_token_secret': oauth_verifier}
    auth.get_access_token(oauth_verifier)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    status = api.verify_credentials(include_email=True)
    provider_id = status.id_str
    name = status.name
    email = status.email
    profile_image = status.profile_image_url_https
    return {"provider_id": provider_id,
            "name": name,
            "email":email,
            "profile_image": profile_image
            }
