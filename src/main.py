from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})


@app.get("/")
def index():
    html_content = """
    <html>
        <head>
            <title>🔥🔥 REST SERVER IS RUNNING 🔥🔥</title>
        </head>
        <body style="display:flex;justify-content:center;padding-top:100px">
            <h1>Fastapi🔥🔥BPMN🔥🔥Server Is Running</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)