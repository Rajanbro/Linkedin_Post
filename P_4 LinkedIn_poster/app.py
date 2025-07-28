import gradio as gr

# Mock function to simulate posting to LinkedIn
def post_to_linkedin(message):
    if not message.strip():
        return "❌ Please enter a message to post."
    # Simulate a delay or processing if desired
    return "✅ (Demo) Successfully posted to LinkedIn! (No real API call was made.)"

# Gradio premium-style UI
with gr.Blocks(theme=gr.themes.Base(primary_hue="blue")) as app:
    gr.Markdown("# 💼 Post to LinkedIn (Demo)\nThis is a mock demo. No real LinkedIn post will be made.")
    msg = gr.Textbox(label="Your LinkedIn Post", placeholder="Write your professional message here...")
    submit = gr.Button("Post Now 🚀")
    output = gr.Textbox(label="Result")
    
    submit.click(fn=post_to_linkedin, inputs=msg, outputs=output)

app.launch()
