# CLAUDE.md - Python-Comandline-tools

## Project Overview

Interactive CLI toolbox with 8 utility modules for daily tasks. Uses pyfiglet and inquirer for a menu-driven interface.

## Structure

```
├── main.py                     # Main menu launcher
├── setup_and_run.py            # Dependency installer + launcher
├── requirements/
│   └── apikey.py               # API credentials (gitignored)
├── 00_DownloadSorting/         # Organize Downloads folder
├── 02_Edubase/                 # Download books from Edubase (submodule)
├── 03_weather/                 # Current weather lookup
├── 04_Forcast/                 # 7-day weather forecast
├── 05_Mailing/                 # Send emails via Resend API
├── 06_Passwords/               # Encrypted password manager (Fernet)
├── 07_Banking/                 # Bank statement CSV analyzer
└── 08_Annoying/                # Automation tool (WhatsApp/Discord)
```

## APIs Used

| API | Used In | Purpose | Key Variable |
|-----|---------|---------|--------------|
| **OpenWeather** | 03_weather, 04_Forcast | Weather data | `api_key_weather` |
| **Geoapify** | 03_weather, 04_Forcast | Geocoding | `api_key_geo` |
| **Resend** | 05_Mailing | Email sending | `apikey_mail` |
| **Edubase** | 02_Edubase | Book downloads (web scraping) | Username/password |

## Current API Implementation

**Weather Module** (`03_weather/01_Weather.py:18-30`):
- Direct calls to `api.openweathermap.org/data/2.5/weather`
- Direct calls to `api.geoapify.com/v1/geocode/search`

**Forecast Module** (`04_Forcast/01_Forcast.py`):
- Direct calls to `api.openweathermap.org/data/2.5/forecast/daily`
- Direct calls to Geoapify geocoding

**Mailing Module** (`05_Mailing/01_SendMail.py`):
- Uses `resend` Python SDK
- Sends emails via Resend API

## Configuration

**API Keys** (`requirements/apikey.py`):
```python
apikey_mail = "..."           # Resend API key
api_key_geo = "..."           # Geoapify key
api_key_weather = "..."       # OpenWeather key
edubase_username = "..."
edubase_password = "..."
```

## Migration to API Gateway

**Target**: Use centralized API gateway at `https://api.novaroma-homelab.uk` instead of direct API calls.

**Benefits**:
- Centralized API key management
- Authentication via JWT tokens
- No API keys exposed in client code
- Usage tracking and rate limiting

**Required Changes**:
1. Add gateway authentication (JWT tokens)
2. Replace direct API calls with gateway endpoints
3. Update geocoding and weather modules
4. Add email proxy endpoint to gateway
