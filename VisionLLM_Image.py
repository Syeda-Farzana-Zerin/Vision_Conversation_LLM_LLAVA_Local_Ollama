import streamlit as st
from ollama import chat
from PIL import Image
import tempfile

st.set_page_config(page_title="Image Q&A (LLaVA + Ollama)", layout="centered")

st.title("🖼️ Image Q&A with LLaVA (Local Ollama)")
st.write("Upload an image, it will appear immediately, then ask questions about it.")

# ------------------------------
# Image Upload
# ------------------------------
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Temporary image path (for Ollama)
image_path = None

if uploaded_file:
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    temp_file.write(uploaded_file.read())
    image_path = temp_file.name

    # Show image
    img = Image.open(image_path)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    st.markdown("---")

    # ------------------------------
    # Chat logic
    # ------------------------------
    if "chat" not in st.session_state:
        st.session_state.chat = []

    # Show chat history
    for role, text in st.session_state.chat:
        with st.chat_message(role):
            st.write(text)

    # Chat input box
    user_input = st.chat_input("Ask something about the image…")

    if user_input:
        # Show user message
        st.session_state.chat.append(("user", user_input))
        with st.chat_message("user"):
            st.write(user_input)

        # Send question + image to LLaVA
        response = chat(
            model="llava",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                    "images": [image_path],
                }
            ],
        )

        answer = response["message"]["content"]

        # Save & show assistant reply
        st.session_state.chat.append(("assistant", answer))
        with st.chat_message("assistant"):
            st.write(answer)

else:
    st.info("👆 Upload an image to begin.")
