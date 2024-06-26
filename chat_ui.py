from anthropic import Anthropic
import dotenv
import os
import gradio as gr
import ai_assistant as ai

dotenv.load_dotenv()

def greet(name: str) -> str:
    return f"Hello {name}!"

gr.themes.Soft()
user_input = gr.Textbox(label="Your Input:", placeholder="Enter your question here")
system_output = gr.Textbox(label="System Output:")
desc = gr.Markdown("### Welcome to My Chatbot (using Claude-3 Opus)")

chatbot_ui = gr.Interface(
    fn=ai.chat_with_assistant, 
    inputs=[user_input], 
    outputs=[system_output],
    title="Experiment with Anthrop\c Models",
    description=desc.value,
    theme=gr.themes.Soft()
    )

#demo = gr.Interface(fn=greet, inputs="text", outputs="text")

chatbot_ui.launch()
