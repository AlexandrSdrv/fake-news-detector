import gradio as gr
from transformers import pipeline

classifier = pipeline("text-classification", model="./model")

def predict(text):
    result = classifier(text, truncation=True, max_length=256)[0]
    label = "🔴 Fake News" if result["label"] == "LABEL_0" else "🟢 Real News"
    confidence = result["score"]
    return f"{label}\nConfidence: {confidence:.2%}"

demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(
        lines=5,
        placeholder="Paste a news headline or article here...",
        label="News Text"
    ),
    outputs=gr.Textbox(label="Prediction"),
    title="🔍 Fake News Detector",
    description="Paste any news headline or article and I'll tell you if it's likely fake or real.",
    examples=[
        ["Scientists discover that drinking coffee cures all diseases permanently"],
        ["Federal Reserve holds interest rates steady amid inflation concerns"],
    ]
)

demo.launch()