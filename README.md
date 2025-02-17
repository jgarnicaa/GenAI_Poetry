# GenAI Poetry - AI-Powered Poetry Generator

## 📌 Project Overview
GenAI Poetry is an AI-powered poetry generator capable of creating poems in **English and Spanish**. The model was fine-tuned from **GPT-2** to specialize in poetry generation, ensuring coherent and creative outputs. The application consists of a **backend** (FastAPI) handling the model inference and a **frontend** (Streamlit) providing an interactive web interface.

## 🚀 Project Structure
The repository contains the following directories:

- **`backend/`** - Contains the FastAPI backend, including model inference logic and API endpoints.
- **`frontend/`** - Contains the Streamlit web interface for user interaction.
- **`webapp/`** - Main folder for deployment, containing backend, frontend, and Docker configuration.
- **`model/`** - Stores the fine-tuned GPT-2 model (must be downloaded separately).
- **`data/`** - Includes datasets used for training the model.
- **`docs/`** - Documentation and architecture diagrams.

## 🛠️ Running the Project Locally
### **Prerequisites**
Ensure you have the following installed:
- **Python 3.8+**
- **Docker & Docker Compose**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/jgarnicaa/GenAI_Poetry.git
cd GenAI_Poetry
```

### **2️⃣ Download the Model**
Download the fine-tuned GPT-2 model and place it in `webapp/backend/model/`:
```bash
wget -P webapp/backend/ https://genaipoetry-bucket.s3.eu-west-3.amazonaws.com/model/
```

### **3️⃣ Run the Application**
Start the application using Docker Compose:
```bash
cd webapp
docker-compose up --build -d
```

### **4️⃣ Access the Web Interface**
Once running, access the poetry generator at:
```bash
http://0.0.0.0:8501
```

## 🌍 Accessing the Live Version on AWS EC2
If deployed on an AWS EC2 instance, access the application using the public IP:
```bash
http://13.39.47.61:8501
```

Ensure that the EC2 security group allows inbound traffic on port **8501**.

## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it!

## 🤝 Contributing
Contributions are welcome! Fork the repo and submit a pull request with improvements.

## 📧 Contact
For questions or collaborations, contact **Eduardo Garnica** via GitHub.


