# Image Dataset Generator
Simple asynchronous image generator, scraping images from Google images.
Can run up to 6 different keywords, each on separate thread, downloading them asynchronously.

Creates a compressed file containing images for every specified keywords.
You can get ~700 images per keyword on average.

### Build the container
```
docker build -t <name> .
```
### Run the container
```
docker run -p 5000:5000 <name>
```

# Preview

|<img src="https://github.com/user-attachments/assets/c77e5a6c-9952-4a20-949a-5ddaee6c2b92">|
|---|
|<img src="https://github.com/user-attachments/assets/d4c72999-1334-4c9c-826b-f270a673542a">|


|![dog](https://github.com/user-attachments/assets/e602e36e-3cf8-4b46-983e-ac3227fde03f)|![mouse](https://github.com/user-attachments/assets/77cb96a8-0b82-42f5-8a3d-088c79343c25)|
|---|---|
|![cat](https://github.com/user-attachments/assets/bd911feb-f7e9-4227-bd9c-e1ea47533373)|![ant](https://github.com/user-attachments/assets/750d625a-fe91-419c-9770-43e4233269e1)|










