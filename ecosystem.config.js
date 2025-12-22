import scrapers from './pm2.processes.js';

module.exports = {
  apps: scrapers.map(scraper => ({
    name: scraper.name,
    script: '.venv/Scripts/python.exe',
    args: `-u ${scraper.scriptPath} ${scraper.args || ''}`,
    cwd: __dirname,
    interpreter: 'none',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'production',
      PYTHONIOENCODING: 'utf-8'
    },
    error_file: `./logs/${scraper.name}-err.log`,
    out_file: `./logs/${scraper.name}-out.log`,
    log_file: `./logs/${scraper.name}-combined.log`,
    time: true
  }))
};
