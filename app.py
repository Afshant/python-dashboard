from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import requests

app = Flask(__name__)

# Sample data-fetching function
def fetch_data():
    # Example: Use an API or local CSV
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=461dd2ad084f12a253366ce3e3b8370b'
    response = requests.get(api_url)
    json_data = response.json()
    df = pd.json_normalize(json_data)
    return df

@app.route('/')
def dashboard():
    df = fetch_data()
    df = df.groupby('name')['main.temp'].mean().reset_index()
    # Generate plot using Plotly
    fig = px.line(df, x='name', y='main.temp', title="City Temperature Trends")
    graph_html = fig.to_html(full_html=False)
    return render_template('dashboard.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
