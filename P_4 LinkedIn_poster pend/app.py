import gradio as gr
import requests
import json

# LinkedIn API details (replace these with your actual tokens)
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
AUTHOR_URN = "urn:li:person:YOUR_PERSON_URN"

# Function to post message to LinkedIn
def post_to_linkedin(message):
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0"
    }

    post_data = {
        "author": AUTHOR_URN,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": message
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(post_data))
    
    if response.status_code == 201:
        return "✅ Successfully posted to LinkedIn!"
    else:
        return f"❌ Failed to post: {response.text}"

# Gradio premium-style UI
with gr.Blocks(theme=gr.themes.Base(primary_hue="blue")) as app:
    gr.Markdown("# 💼 Post to LinkedIn\nUse Python to post a message on your LinkedIn feed.")
    msg = gr.Textbox(label="Your LinkedIn Post", placeholder="Write your professional message here...")
    submit = gr.Button("Post Now 🚀")
    output = gr.Textbox(label="Result")
    
    submit.click(fn=post_to_linkedin, inputs=msg, outputs=output)

app.launch()
