from fastapi import FastAPI
from fastapi.Screenshotsfiles import ScreenshotsFiles

app = FastAPI()

# Cho phép truy cập thư mục Screenshots
app.mount("/Screenshots", ScreenshotsFiles(directory="Screenshots"), name="Screenshots")
