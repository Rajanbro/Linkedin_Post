from flask import Flask, request, redirect
import requests
import webbrowser

CLIENT_ID = "86jpilk3oz82dr"
CLIENT_SECRET = "WPL_AP1.WY1MjBwf9RY2UskS.Duq5PA=="
REDIRECT_URI = "http://localhost:8000/callback"

app = Flask(__name__)

@app.route("/")
def login():
    auth_url = (
        "https://www.linkedin.com/oauth/v2/authorization"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=r_liteprofile%20w_member_social"
    )
    return redirect(auth_url)

@app.route("/callback")
def callback():
    print(request.url)

    code = request.args.get("code")
    if not code:
        return "❌ Code not received from LinkedIn."

    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(token_url, data=data, headers=headers)
    access_token = response.json().get("access_token")

    if not access_token:
        return f"❌ Error getting access token: {response.text}"

    # Get URN
    headers = {"Authorization": f"Bearer {access_token}"}
    me_response = requests.get("https://api.linkedin.com/v2/me", headers=headers)
    me_data = me_response.json()

    return f"""
    ✅ Access Token: {access_token}<br><br>
    ✅ Author URN: urn:li:person:{me_data['id']}<br><br>
    Copy and paste these into your Gradio project!
    """

if __name__ == "__main__":
    webbrowser.open("http://localhost:8000")
    app.run(port=8000)
