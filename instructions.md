# Instructions

You'll probably need to install flask:
```bash
pip3 install flask
```
## Launching the Flask server:
In one terminal:
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

## Testing API
To simulate a POST request, in another terminal:
```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"tweet":"President Trump officially resigned as President of the United States via tweet last night"}' http://localhost:5000/fakenews/api/v1.0/predict
```

Should output:
```bash
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/1.0.1 Python/3.7.5
Date: Tue, 05 May 2020 20:52:06 GMT

{
  "prediction": "fake"
}

```
