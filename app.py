import cv2
import streamlit as st

def main():
    st.title("Real-time Camera Stream with Streamlit")

    # Open the camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("Unable to access the camera. Please check your camera connection.")
        return

    # Set the video capture properties
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()

        if not ret:
            st.error("Error reading frame from the camera.")
            break

        # Display the frame using Streamlit
        st.image(frame, channels="BGR")

    # Release the camera when the app is closed
    cap.release()

if __name__ == "__main__":
    main()
