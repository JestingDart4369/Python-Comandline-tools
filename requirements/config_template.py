# ──────────────────────────────────────────────────────────────
# API Gateway – client configuration
# ──────────────────────────────────────────────────────────────
# Copy this file to  config.py  and fill in your values.
# NEVER commit config.py to Git — it's in .gitignore.
# ──────────────────────────────────────────────────────────────

# Gateway URL (public endpoint)
GATEWAY_URL = "https://your-gateway-url.com"

# Your gateway account credentials  (created via /settings/users)
GATEWAY_USERNAME = "your-username"
GATEWAY_PASSWORD = "your-password"

# Email address used as sender for /email/send calls
EMAIL_FROM = "yourapp@your-domain.com"

# ── non-gateway credentials ─────────────────────────────────
# Edubase (web scraping — not related to the API gateway)
EDUBASE_USERNAME = "your-edubase-username"
EDUBASE_PASSWORD = "your-edubase-password"
