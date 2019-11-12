FLASK_APP=app.py
APP_SETTINGS=config.DevelopmentConfig
DATABASE_URL=postgresql://localhost/simple
FLASK_DEBUG=0
# These are just some variables that you should set to your own correct value for mailing errors.
# Don't think this works, but a reminder to set these variables is enough for now
# TODO @Sander possibly figure out how to set up a dedicted mail server (now using gmail)
MAIL_SERVER=localhost
MAIL_PORT=25
MAIL_USE_TLS=1
MAIL_USERNAME=username
MAIL_PASSWORD=password
MAIL_ADMIN_FLASK=your@example.com