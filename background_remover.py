import streamlit as st
from rembg import remove
from PIL import Image
import io

def main():
    st.title("Remove Background from Image")
    st.write("Upload an image, and this app will remove its background.")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)
        
        with st.spinner("Removing background..."):
            output_image = remove(image)
            
        st.image(output_image, caption="Background Removed", use_column_width=True)
        
        img_bytes = io.BytesIO()
        output_image.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()
        
        st.download_button(label="Download Image", 
                           data=img_bytes, 
                           file_name="background_removed.png", 
                           mime="image/png")

if __name__ == "__main__":
    main()
