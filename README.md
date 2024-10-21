Data Analysis and Visualization Dashboard

This project is a web-based data visualization dashboard that fetches real-time weather data using the OpenWeather API and displays interactive charts to help users analyze temperature trends across different cities.

Features
Fetches real-time weather data for various cities.
Displays temperature trends using interactive visualizations.
Built using Flask for the backend and Plotly for data visualization.
Tech Stack
Backend: Python, Flask
Data Processing: Pandas, NumPy
Visualization: Plotly, Matplotlib
API: OpenWeather API
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/your-repo.git
cd your-repo
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your OpenWeather API key:

Create an account on OpenWeather and generate an API key.
Replace YOUR_API_KEY in app.py with your actual API key.
Run the application:

bash
Copy code
python app.py
Open your browser and go to:

arduino
Copy code
http://127.0.0.1:5000/
Usage
The dashboard fetches real-time weather data for a specified city and displays the current temperature, weather conditions, and a trend chart.
