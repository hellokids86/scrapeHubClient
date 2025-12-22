# ScrapeHub Robot Installation Guide

## Prerequisites
- Python 3.12+
- PM2 (Node.js process manager)
- Git

## Installation Steps



### 1. Create and activate virtual environment
```bash
# Create virtual environment
python -m venv .venv


```

### 2. Install dependencies
```bash
# Make sure virtual environment is activated first (windows)
.venv\Scripts\python.exe -m pip install -r requirements.txt
```



### 3. Create a .env file

Make a copy of the .env.example and rename to ".env". Then set the SCRAPEHUB_API_KEY and SCRAPEHUB_API_HOST

```
SCRAPEHUB_API_KEY=your_api_key_here
SCRAPEHUB_API_HOST=https://your-scrapehub-host.com
```

### 4. Make your own scrapers.

Look at ExampleScraper.py to understand how to make your own scraper.

Place each scraper in a new folder named `src/scrapers/{scrapername}` to keep things organized.




### 5. Start robots with PM2

Edit the pm2.processes.js "scrapers" var to include your scrapers you want to install with pm2:

```bash
pm2 start ecosystem.config.js
pm2 save
```

## Useful PM2 Commands

- `pm2 list` - View all running processes
- `pm2 logs` - View logs for all processes
- `pm2 logs <name>` - View logs for specific scraper
- `pm2 restart ecosystem.config.js` - Restart all scrapers
- `pm2 stop <name>` - Stop a specific scraper
- `pm2 delete <name>` - Remove a scraper from PM2
- `pm2 save` - Save current process list
- `pm2 startup` - Configure PM2 to start on system boot



## Troubleshooting

- If PM2 commands aren't found, install it globally: `npm install -g pm2`
- If scrapers won't start, check logs with: `pm2 logs`
- Verify Python version: `python --version` (must be 3.12+)