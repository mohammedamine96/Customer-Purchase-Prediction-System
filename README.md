# Customer Purchase Prediction System

A professional desktop application for predicting whether a customer will buy a computer based on their demographic data. This application utilizes the K-Nearest Neighbors (KNN) algorithm with Cosine Similarity and Simple Matching to provide accurate predictions.

## 🚀 Features

*   **Desktop Interface**: Runs as a standalone desktop application using `eel`.
*   **Dual Algorithms**:
    *   **Cosine Similarity (Ordinal)**: Converts categorical data to ordinal vectors for precise similarity calculation.
    *   **Simple Matching**: A straightforward approach comparing attribute matches.
*   **Interactive UI**: User-friendly interface to input customer data (Age, Income, Student Status, Credit Rating).
*   **Visual Results**: Displays top 5 nearest neighbors and their similarity scores.
*   **Real-time Prediction**: Instantly predicts "Yes" or "No" for buying a computer.

## 🛠️ Technologies Used

*   **Python**: Core programming language.
*   **Flask**: Backend framework for handling logic and routing.
*   **Eel**: Library for converting the web app into a native desktop GUI.
*   **HTML/CSS**: Frontend for the user interface.
*   **JSON**: Data storage for the training dataset.

## 📦 Installation

1.  **Clone the repository** (or extract the project files).
2.  **Install dependencies**:
    Ensure you have Python installed. Then run:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is missing, install manually: `pip install flask eel`)*

## 🖥️ Usage

1.  **Run the application**:
    Execute the `desktop.py` script to launch the application.
    ```bash
    python desktop.py
    ```
2.  **Interact**:
    *   Select values for Age, Income, Student, and Credit Rating.
    *   Click "Predict" (or the relevant button) to see the results.
    *   View the detailed table of nearest neighbors and the final prediction.

## 📂 Project Structure

*   `desktop.py`: The entry point for the desktop application. Handles window creation and server threading.
*   `app.py`: The Flask application logic.
*   `knn_solver.py`: Contains the implementation of KNN algorithms and data processing.
*   `dataset.json`: The training dataset containing historical customer data.
*   `static/`: Contains static assets (CSS, loader).
*   `templates/`: Contains HTML templates.

## 🧩 Algorithms Explained

### Cosine Similarity (Ordinal)
Categorical attributes are mapped to ordinal values (e.g., Low=1, Medium=2, High=3). The cosine similarity between the query vector and dataset vectors is calculated to find the nearest neighbors.

### Simple Matching
Calculates similarity by counting the number of matching attributes between the query and the dataset instances.

---
*Created by Mohammed Amine Darri*
