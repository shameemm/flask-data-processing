# Flask Data Retrieval and Processing Application

## Overview
This Flask application simulates a simplified data retrieval and processing system. It includes API endpoints to fetch mock data, process it, and retrieve processed results.

## Features
1. **API Endpoint for Data Retrieval**
   - **Endpoint:** `/fetch-data`
   - **Method:** `GET`
   - **Description:** Simulates fetching data from an external service with mock data.

2. **Data Processing**
   - **Endpoint:** `/process-data`
   - **Method:** `POST`
   - **Description:** Processes the fetched data (e.g., converts all text to uppercase). Requires JSON payload with `data` field containing a list of items to process.

3. **Data Storage**
   - **Endpoint:** `/get-processed-data`
   - **Method:** `GET`
   - **Description:** Returns the processed data stored in memory.

## Setup and Running the Application

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/flask-data-processing.git
   cd flask-data-processing

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv

3. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

5. **Run the Flask Application:**
   ```bash
   python app.py

6. **Access the Application:**
   - **Fetch Data:** `http://127.0.0.1:5000/fetch-data`
   - **Process Data:** Use a POST request to `http://127.0.0.1:5000/process-data` with a JSON body (e.g., `{"data": ["Hness", "D"]}`)
   - **Get Processed Data:** `http://127.0.0.1:5000/get-processed-data`
