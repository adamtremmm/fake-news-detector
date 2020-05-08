# fake-news-detector
Twitter fake news detection software

## Frontend Instructions

Install NPM:

Go to:

https://nodejs.org/en/

Install AngularCLI:

```bash
npm install -g @angular/cli
```

Run:

```bash
cd front-end/src/
ng serve
```

## Backend Instructions

Install Flask:
```bash
pip3 install flask
```

Run:
```bash
cd /src
python3 app.py
```
This should result in the following output (may also see some sklearn DeprecationWarnings interspersed):
```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 460-484-693

```

Now you can use the front end to start Tweeting!
