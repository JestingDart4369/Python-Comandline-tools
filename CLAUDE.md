# CLAUDE.md - Python-Comandline-tools

## Project Overview

Interactive CLI toolbox with 8 utility modules for daily tasks. Uses pyfiglet and inquirer for a menu-driven interface.

**Architecture**: Client application that connects to centralized API Gateway for all external API access.

## Structure

```
├── main.py                     # Main menu launcher
├── setup_and_run.py            # Dependency installer + launcher
├── requirements/
│   ├── apikey.py               # Gateway credentials (gitignored)
│   └── gateway.py              # Gateway client (JWT auth + API methods)
├── 00_DownloadSorting/         # Organize Downloads folder
├── 02_Edubase/                 # Download books from Edubase (web scraping)
├── 03_weather/                 # Current weather lookup
├── 04_Forcast/                 # Weather forecasts (hourly + daily)
├── 05_Mailing/                 # Send emails via gateway
├── 06_Passwords/               # Encrypted password manager (Fernet)
├── 07_Banking/                 # Bank statement CSV analyzer
└── 08_Annoying/                # Automation tool (WhatsApp/Discord)
```

## API Gateway Integration

All external APIs (OpenWeather, Geoapify, IPRegistry, Resend) are accessed through the centralized API Gateway at `https://api.novaroma-homelab.uk`.

### Gateway Client (`requirements/gateway.py`)

**Authentication**:
- JWT Bearer token authentication
- Automatic token refresh (tokens expire after 1 hour, refresh at 55 minutes)
- Credentials stored in `requirements/apikey.py` (gitignored)

**Available Methods**:
- `get_weather(city, units)` - Current weather by city name
- `get_hourly_forecast(lat, lon, units)` - 48-hour hourly forecast
- `get_daily_forecast(lat, lon, days, units)` - Multi-day forecast
- `geocode(city)` - Convert city name to coordinates
- `get_location_from_ip(ip)` - Get location from IP address
- `send_email(to, subject, html, from_email)` - Send emails via Resend

### Modules Using Gateway

| Module | Gateway Methods Used |
|--------|---------------------|
| `03_weather/01_Weather.py` | `geocode()`, `get_weather()` |
| `04_Forcast/01_Forcast.py` | `geocode()`, `get_hourly_forecast()`, `get_daily_forecast()` |
| `05_Mailing/01_SendMail.py` | `send_email()` |

## Configuration & Security

### Credentials File (`requirements/apikey.py`)

**CRITICAL: This file is gitignored and contains sensitive data!**

```python
# API Gateway Configuration (centralized API access)
GATEWAY_URL = "https://api.novaroma-homelab.uk"
GATEWAY_USERNAME = "..."
GATEWAY_PASSWORD = "..."

# Email configuration (for gateway send_email calls)
email = "Cmd@api.novaroma-homelab.uk"

# Non-API credentials (web scraping, local services)
edubase_username = "..."
edubase_password = "..."
```

### Protected Files (.gitignore)

**Never commit these files:**
- `/requirements/apikey.py` - Gateway credentials
- `/03_weather/apikey.py` - Legacy (if exists)
- `/04_Forcast/apikey.py` - Legacy (if exists)
- `/05_Mailing/apikey.py` - Legacy (if exists)
- `/06_Passwords/02_Password_collection` - Encrypted password vault
- `/06_Passwords/key.key` - Fernet encryption key
- `/07_Banking/02_Bankauszüge/*` - Bank statements

## Security Benefits of Gateway

1. **No API Keys in Client Code**: All external API keys stored server-side only
2. **Centralized Authentication**: Single username/password for all services
3. **Token-Based Security**: JWT tokens with automatic refresh and expiration
4. **Credential Isolation**: Only gateway credentials in client code, external API keys never exposed

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run main menu
python main.py

# Or use setup script (installs deps + runs)
python setup_and_run.py
```

## Testing

Test gateway connectivity:
```bash
python -c "from requirements.gateway import GatewayClient; from requirements import apikey; g = GatewayClient(apikey.GATEWAY_URL, apikey.GATEWAY_USERNAME, apikey.GATEWAY_PASSWORD); print(g.get_weather('London'))"
```

## Common Tasks

### Add New Gateway-Backed Feature
1. Check if endpoint exists in gateway (`/docs` or `index.html`)
2. If not, request new endpoint in API Gateway project
3. Add method to `requirements/gateway.py`
4. Use in your module: `gateway.new_method(...)`

### Update Gateway Credentials
1. Edit `requirements/apikey.py`
2. Update `GATEWAY_USERNAME` or `GATEWAY_PASSWORD`
3. Do NOT commit this file!
