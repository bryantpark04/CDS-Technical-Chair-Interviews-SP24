from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <html>
        <head>
            <title>Cornell Data Science</title>
        </head>
        <style>
        html, body {
            height: 100%;
        }
        
        html {
            display: table;
            margin: auto;
        }
        
        body {
            display: table-cell;
            vertical-align: middle;
        }
            
        img {
            width: auto;
            height: 20%;
        }
        </style>
        <body>
        
        <img src="https://cornelldata.science/cds_logo.png" alt="CDS LOGO" class="center">
        <p style="text-align: center">Cornell Data Science</p>
        
        </body>
        </html>
        """


@app.get("/subteams/{st}", response_class=HTMLResponse)
async def index(st: str):
    return f"""
    <html>
        <head>
            <title>Cornell Data Science</title>
        </head>
        <style>
        html, body {{
            height: 100%;
        }}

        html {{
            display: table;
            margin: auto;
        }}

        body {{
            display: table-cell;
            vertical-align: middle;
        }}

        img {{
            width: auto;
            height: 20%;
        }}
        </style>
        <body>

        
        <p style="text-align: center">You are from subteam {st}</p>

        </body>
        </html>
        """

