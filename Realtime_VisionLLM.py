import streamlit as st
from ollama import chat
from PIL import Image, ImageEnhance
import tempfile

st.set_page_config(page_title="Webcam Q&A (LLaVA + Ollama)", layout="centered")

st.title("🎥 Webcam Vision Q&A with LLaVA (Local Ollama)")
st.write("Use your webcam below, then ask questions about what the camera captures.")

st.markdown("### 📸 Webcam")
camera_image = st.camera_input("Take a snapshot with your webcam")

# Chat state
if "chat" not in st.session_state:
    st.session_state.chat = []

# Only proceed once a picture is taken
if camera_image is not None:

    # Load the image
    img = Image.open(camera_image)

    # --------------------------------------------
    # ⭐ BRIGHTNESS FIX
    # --------------------------------------------
    enhancer = ImageEnhance.Brightness(img)
    bright_img = enhancer.enhance(1.8)   # Increase brightness (1.8 = +80%)
    # You may adjust to 2.0 or 2.2 if needed
    # --------------------------------------------

    # Save bright image to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    bright_img.save(temp_file.name)
    image_path = temp_file.name

    # Show brightened image
    st.image(bright_img, caption="Brightened Webcam Image", use_container_width=True)

    st.markdown("---")
    st.subheader("💬 Chat about what the webcam sees")

    # Display previous chat history
    for role, text in st.session_state.chat:
        with st.chat_message(role):
            st.write(text)

    # Chat input
    user_input = st.chat_input("Ask something about the webcam image…")

    if user_input:
        # Add user message
        st.session_state.chat.append(("user", user_input))
        with st.chat_message("user"):
            st.write(user_input)

        # Send brightened image + question to LLaVA
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

        # Add assistant message
        st.session_state.chat.append(("assistant", answer))
        with st.chat_message("assistant"):
            st.write(answer)

else:
    st.info("📌 Use the webcam above to capture an image first.")
