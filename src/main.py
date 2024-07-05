from fastapi import FastAPI
from routes.pools_and_swimlanes import router as pools_and_swimlanes_router
from routes.activities_from_pools_and_swimlanes import router as activities_from_pools_and_swimlanes
from routes.process_description_simplification import router as process_description_simplification
from fastapi.responses import HTMLResponse
app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

app.include_router(pools_and_swimlanes_router)
app.include_router(activities_from_pools_and_swimlanes)
app.include_router(process_description_simplification)

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