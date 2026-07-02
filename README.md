# 🌍 Remote Sensing AI Platform

> AI-powered Remote Sensing Image Analysis Platform developed during the **SUPARCO Internship 2026**.

An end-to-end web application for remote sensing image enhancement and AI-assisted image understanding. The platform performs image preprocessing operations such as enhancement, denoising, sharpening, and deblurring while enabling **Visual Question Answering (VQA)** using a Vision-Language Model running locally through Ollama.

---

## 🚀 Features

- 📤 Upload Remote Sensing Images
- ✨ Image Enhancement
- 🧹 Image Denoising
- 🔍 Image Sharpening
- 🌫️ Image Deblurring
- 🤖 AI-powered Visual Question Answering (VQA)
- 📥 Download Processed Images
- 💻 Runs Completely Offline using Ollama
- 🔄 Modular AI Architecture (Easy Model Replacement)

---

## 🏗️ Architecture

```
                 +---------------------+
                 |     Frontend        |
                 | HTML • CSS • JS     |
                 +----------+----------+
                           |
                           |
                           ▼
                 +---------------------+
                 | FastAPI Backend     |
                 +----------+----------+
                           |
        ---------------------------------------------
        |          |           |            |
        ▼          ▼           ▼            ▼
 Enhancement   Denoise    Sharpen      Deblur
        |
        ▼
  Processed Image
        |
        ▼
 Vision Language Model (Qwen3-VL:8B)
        |
        ▼
 AI Generated Answer
```

---

# 🛠 Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Python
- FastAPI
- Uvicorn
- OpenCV
- NumPy
- Pillow
- Pydantic

## AI

- Ollama
- Qwen3-VL:8B

---

# 📂 Project Structure

```
Remote-Sensing-AI/
│
├── Backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── uploads/
│   │   └── outputs/
│   │
│   ├── main.py
│   └── requirements.txt
│
├── Frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── images/
│   └── icons/
│
└── README.md
```

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/Remote-Sensing-AI.git

cd Remote-Sensing-AI
```

---

## 2. Install Ollama

Download:

https://ollama.com/download

Pull the Vision Language Model:

```bash
ollama pull qwen3-vl:8b
```

Verify installation:

```bash
ollama list
```

---

## 3. Install Backend Dependencies

```bash
cd Backend

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Backend

```bash
uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

---

# 🌐 Running the Frontend

Open the **Frontend** folder in VS Code.

Launch using **Live Server**.

The frontend automatically communicates with

```
http://127.0.0.1:8000
```

---

# 🖼 Using the Platform

1. Upload a remote sensing image.
2. Select an image processing operation:
   - Enhancement
   - Denoising
   - Sharpening
   - Deblurring
3. View the processed result.
4. Download the processed image.
5. Ask questions about the uploaded image using AI.

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload` | Upload Image |
| POST | `/process/enhance` | Enhance Image |
| POST | `/process/denoise` | Denoise Image |
| POST | `/process/sharpen` | Sharpen Image |
| POST | `/process/deblur` | Deblur Image |
| POST | `/inference/ask` | Visual Question Answering |

---

# 🔄 Changing the Vision-Language Model

The project is modular and supports replacing the underlying VLM with minimal code changes.

Example:

```python
response = ollama.chat(
    model="qwen3-vl:8b",
)
```

Replace with

```python
response = ollama.chat(
    model="llama3.2-vision:90b",
)
```

Only the VLM integration layer needs modification.

---

# 📸 Screenshots

Add screenshots here.

```
docs/images/home.png

docs/images/upload.png

docs/images/enhancement.png

docs/images/vqa.png
```

---

# 🔮 Future Work

- Real-time video processing
- Object Detection
- Semantic Segmentation
- Land Cover Classification
- Multi-spectral Image Support
- Batch Processing
- Cloud Deployment
- Additional Vision-Language Models

---

# 👨‍💻 Author

**Ali Hassan**


---

# ⭐ Acknowledgements

- SUPARCO
- FastAPI
- OpenCV
- Ollama
- Alibaba Qwen Team
