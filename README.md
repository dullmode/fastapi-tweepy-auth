# fastapi-tweepy-auth 
 
### Features
get personal access token and access token secret(consumer keys) using tweepy and fastapi
 
### Requirement

* tweepy==3.9.0
* fastapi==0.45.0
* .env file

### Installation
install modules
```bash
pip install tweepy
pip install fastapi
```
clone file
```bash
git clone https://github.com/dullmode/fastapi-tweepy-auth.git
```
set consumer keys to .env file
```bash
echo -e API_KEY=xxxxxxxx\\n\
    API_KEY_SECRET=xxxxxxxx > fastapi-tweepy-auth/service/.env
```
 
### Usage
```bash
cd fastapi-tweepy-auth
python service/main.py
```
 
### Note
you need to set `http://127.0.0.1:5000/callback` to callback url, which you can set
in twitter developer portal 
