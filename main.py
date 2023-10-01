from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# Directory where you want to save the uploaded images
upload_dir = "uploaded_images"

# Create the directory if it doesn't exist
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

@app.get("/")
async def initial():
    return JSONResponse(content={"message": "server started successfully"}, status_code=200)


@app.post("/upload/")
async def upload_image(file: UploadFile):
    try:
        # Combine the directory path and the file name
        file_path = os.path.join(upload_dir, file.filename)

        # Save the file to the specified directory
        with open(file_path, "wb") as image_file:
            image_file.write(file.file.read())

        return JSONResponse(content={"message": "Image uploaded successfully"}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": f"An error occurred: {str(e)}"}, status_code=500)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
