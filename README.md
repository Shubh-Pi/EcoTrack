# EcoTrack AI – AI-Based Carbon Footprint Predictor & Sustainability Planner

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-red)
![ML](https://img.shields.io/badge/ML-Random%20Forest-green)

---

## 🌍 Introduction

Climate change and rising carbon emissions are critical global challenges. Most individuals lack concrete knowledge about their personal carbon footprint and actionable steps to reduce it.

**EcoTrack AI** addresses this by providing an intelligent platform that analyzes lifestyle patterns, predicts personalized carbon footprint using machine learning, and delivers a dynamic 30-day improvement plan to help users make informed decisions toward sustainable living.

---

## ✨ Features

- **AI-Based Carbon Footprint Prediction** using Random Forest model
- **Category-Wise Emission Analysis** (Transport, Utilities, Lifestyle)
- **Lifestyle Stress Index and Green Score** metrics
- **Dynamic 30-Day Improvement Plan** with personalized recommendations
- **What-If Analysis** for emission reduction scenarios
- **Interactive Streamlit Dashboard** with modern UI
- **Data-Driven Recommendations** (not hardcoded)

---

## 🏗️ Project Architecture

1. User input through Streamlit UI
2. Data preprocessing and feature scaling (StandardScaler)
3. Carbon footprint prediction using Random Forest
4. Impact analysis and recommendation generation
5. Visualization and results rendering

---

## 📁 Directory Structure

```
EcoTrack-AI/
├── app/
│   └── app.py                # Main Streamlit application
├── model/
│   ├── eco_model.pkl         # Trained Random Forest model
│   └── scaler.pkl            # Feature scaler
├── data/
│   ├── raw/                  # Raw dataset
│   └── processed/            # Processed dataset
├── static/
│   └── styles.css            # Custom CSS for UI
├── requirements.txt          # Project dependencies
└── README.md                 # Documentation
```

---

## 📊 Dataset Description

- **Source**: Kaggle Carbon Footprint Dataset
- **Features**: Transport distance, electricity usage, water usage, diet type, waste generated, travel frequency, vehicle type, energy source
- **Target Variable**: Carbon_Footprint_Kg (annual emissions in kg)

---

## 🤖 Machine Learning Model

**Algorithm**: Random Forest Regressor

**Why Random Forest?**
- Handles non-linear relationships effectively
- Provides feature importance insights
- Robust to outliers and noise
- Excellent generalization performance

**Preprocessing**: Data cleaning, categorical encoding, feature scaling with StandardScaler

---

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| **Mean Absolute Error (MAE)** | 3.59 kg |
| **Root Mean Square Error (RMSE)** | 4.57 kg |
| **R² Score** | 0.93 |

The model explains 93% of variance in carbon footprint data with an average prediction error of just 3.59 kg.

---

## 🛠️ Technology Stack

- **Language**: Python 3.8+
- **Frontend**: Streamlit, Custom CSS
- **ML**: Scikit-learn (Random Forest, StandardScaler)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Altair
- **Tools**: VS Code, Jupyter Notebook

---

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/EcoTrack-AI.git
cd EcoTrack-AI
```

**2. Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
cd app
streamlit run app.py
```

Access the app at `http://localhost:8501`

---

## 📖 Usage

1. Enter lifestyle inputs (transport, utilities, lifestyle habits)
2. Click **"Predict Carbon Footprint"**
3. View your carbon footprint results and category breakdown
4. Review personalized 30-day improvement plan
5. Use What-If analysis to simulate emission reductions

---

## 📊 Results & Output

- **Carbon Footprint Prediction**: Annual emissions in kg CO₂
- **Impact Breakdown**: Visual charts showing emission sources
- **Green Score & Lifestyle Stress**: Sustainability metrics
- **30-Day Plan**: Personalized daily actions to reduce emissions

---

## 🔮 Future Enhancements

- User authentication and progress tracking
- Real-time data integration with smart devices
- Advanced Deep Learning models
- Mobile application development
- Cloud deployment (AWS, Streamlit Cloud)

---

## 🎯 Conclusion

EcoTrack AI successfully demonstrates machine learning's power in addressing environmental challenges. With 93% prediction accuracy, the application empowers individuals to understand and reduce their carbon footprint through data-driven insights and personalized recommendations.

---

## 📄 License

This project is for **educational purposes** as part of a machine learning capstone project.

---

**Made with 💚 for a Sustainable Future**
