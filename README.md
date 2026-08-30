# ✈️ Flight Delay Prediction

A machine learning web application that predicts flight departure delays based on weather, operational, and historical data using **Linear Regression**.

---

## 📂 Project Structure

```
Flight_Delay_Model/
│
├── app.py                  # Flask web application (entry point)
├── train_model.py          # Model training script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
│
├── data/
│   └── flight_delay_dataset.csv    # Training dataset
│
├── models/
│   └── flight_delay_model.pkl      # Trained model (pickle)
│
├── notebooks/
│   └── flight_delay_analysis.ipynb # EDA & experimentation notebook
│
├── static/
│   ├── css/
│   │   └── style.css               # Application styles
│   └── images/
│       └── flightimage.jpg         # Background image
│
└── templates/
    └── index.html                  # Prediction form UI
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd Flight_Delay_Model
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate        # Linux / macOS
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### Run the Web App
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`

### Re-train the Model
```bash
python train_model.py
```

---

## 📊 Input Features

| Feature                   | Description                        |
|---------------------------|------------------------------------|
| Distance (km)             | Flight distance in kilometers      |
| Scheduled Hour            | Departure hour (0–23)              |
| Day of Week               | Day of the week (1–7)              |
| Month                     | Month of the year (1–12)           |
| Airline Rating            | Airline service rating (1.0–5.0)   |
| Previous Delays           | Number of prior delays             |
| Weather Severity Index    | Weather severity score (0–100)     |
| Air Traffic Density       | Air traffic load (0.0–1.0)         |
| Aircraft Age (years)      | Age of the aircraft                |
| Wind Speed (km/h)         | Wind speed at departure            |
| Precipitation (mm)        | Rainfall amount                    |
| Temperature (°C)          | Ambient temperature                |
| Visibility (km)           | Visibility range                   |
| Runway Congestion Index   | Runway congestion (0.0–1.0)        |
| Crew Rest Hours           | Crew rest duration before flight   |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **ML:** scikit-learn (Linear Regression)
- **Frontend:** HTML, CSS (Poppins font, Glassmorphism)
- **Serialization:** Joblib

---

## 📄 License

This project is for educational purposes.
