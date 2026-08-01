# COVID-19 Global Tracker Notification

A simple Python application that fetches the latest global COVID-19 statistics and displays them as a Windows desktop notification every hour.

## Features

- Fetches real-time global COVID-19 data
- Displays:
  - Total Cases
  - Total Deaths
  - Total Recovered
- Windows toast notifications
- Automatically updates every 60 minutes

## Technologies Used

- Python 3
- requests
- winotify
- Disease.sh COVID-19 API

## Project Structure

```
covid-tracker/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/covid-tracker.git
cd covid-tracker
```

### 2. Create a virtual environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The application will:

1. Fetch the latest global COVID-19 statistics.
2. Display a Windows notification.
3. Repeat the process every 60 minutes.

## API Used

Disease.sh API

Endpoint:

```
https://disease.sh/v3/covid-19/all
```

Example Response

```json
{
  "cases": 704753890,
  "deaths": 7010681,
  "recovered": 675619811
}
```

## Sample Notification

```
COVID-19 Global Update

Cases: 704753890
Deaths: 7010681
Recovered: 675619811
```

## Requirements

- Python 3.8+
- Windows 10/11 (for toast notifications)
- Internet connection

## Future Improvements

- Country-wise statistics
- Custom notification interval
- GUI dashboard
- Logging support
- Background startup option

## License

This project is licensed under the MIT License.
