# MacroDetect

A web application that uses computer vision to segment food items in a photo and analyze their macronutrient distribution (proteins, carbohydrates, fats, vegetables, and others).

---

## Project Structure

```
MacroDetect/
│
├── backend/                      # FastAPI backend with AI model
│   ├── main.py
│   │
│   ├── model/
│   │   └── unet_resnet101.pth   # <-- Downloaded model goes here
│   │
│   └── utils/
│       ├── __init__.py
│       ├── processing.py
│       └── download_model.py
│
├── frontend/                     # HTML/CSS/JS static frontend
│   ├── index.html
│   ├── analyze.html
│   ├── details.html
│   ├── about.html
│   ├── contact.html
│   │
│   ├── css/
│   │   └── styles.css
│   │
│   ├── js/
│   │   ├── analyze.js
│   │   └── details.js
│   │
│   └── assets/
│       ├── aboutImage1.jpg
│       ├── aboutImage2.jpg
│       ├── aboutImage3.jpg
│       ├── HomeImage.jpg
│       ├── logo.png
│       ├── Alejandro.jpeg
│       ├── Jessica.jpeg
│       └── Laura.jpeg
│
├── requirements.txt
├── README.md
└── .gitignore

---

## Technologies Used

- **Python** — backend logic and model inference
- **FastAPI** — REST API framework
- **PyTorch** — deep learning model (UNet + ResNet101)
- **OpenCV** — image processing
- **NumPy** — numerical operations
- **Pillow** — image I/O
- **HTML5 / CSS3 / JavaScript** — frontend interface
- **Uvicorn** — ASGI server

---

## Requirements

Before running the project, make sure you have installed:

- Python 3.9 or newer
- pip
- Git
- A modern web browser (Chrome, Edge, Firefox, etc.)

---

## 1. Clone the Repository

```bash
git clone https://github.com/Alejandrosaldana06/MacroDetect.git
cd MacroDetect
```

---

## 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

**On Windows:**

```bash
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Download the AI Model

The trained AI model is not included directly in the repository due to GitHub file size limitations.

Run the following script to download it automatically:

```bash
python backend/utils/download_model.py
```

The model will be placed at:

```
backend/model/unet_resnet101.pth
```

Alternatively, you can download it manually from Google Drive and place it in the path above:

> [Trained Model (ResNet101) — Google Drive](https://drive.google.com/file/d/1SdH4zte5QoSmw6d7CQXLnj9r8BD6TtZF/view?usp=sharing)

---

## 5. Run the Backend

From the root project directory:

**On Windows:**

```bash
set PYTHONPATH=./backend
uvicorn backend.main:app --reload
```

**On macOS/Linux:**

```bash
export PYTHONPATH=./backend
uvicorn backend.main:app --reload
```

The backend will be available at:

```
http://127.0.0.1:8000
```

---

## 6. Run the Frontend

Open a second terminal and move to the frontend directory:

```bash
cd frontend
```

Start a local server:

```bash
python -m http.server 8080
```

Open the application in your browser:

```
http://localhost:8080
```

> You can also use the **Live Server** extension in Visual Studio Code for live reloading.

---

## 7. How the Application Works

1. Open the **Analyze** page and upload a food image (`.jpg` or `.png`).
2. The backend processes the image using the AI segmentation model.
3. The application generates:
   - A segmentation mask
   - A macronutrient percentage chart
   - A detailed nutritional analysis
4. Navigate to the **Details** page to view and download the generated segmentation mask.

---

## Additional Resources

### Training Dataset and Generated Masks

The training dataset and generated segmentation masks are not included in the repository due to GitHub storage limitations.

> Google Drive download: `PASTE_YOUR_TRAINING_LINK_HERE`

---

## Notes

- Large files (datasets, training outputs, masks, and AI models) were excluded from the repository to keep it lightweight and compatible with GitHub limits.
- The repository contains all source code needed to run the application.
- Make sure the **backend server is running** before using the frontend.

---

## Authors

- David Alejandro Saldaña Moreno
- Laura Natalia Gomez
- Jessica Alejandra Barragan

---

## Repository

GitHub: [https://github.com/Alejandrosaldana06/MacroDetect](https://github.com/Alejandrosaldana06/MacroDetect)