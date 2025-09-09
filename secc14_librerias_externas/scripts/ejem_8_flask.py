
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Landing Page</title>
        <!-- Agregar Bulma desde un CDN -->
        <link href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css" rel="stylesheet">
    </head>
    <body>
        <section class="hero is-fullheight">
            <div class="hero-body">
                <div class="container has-text-centered">
                    <h1 class="title">
                        ¡Hola! Soy una app web desde Python
                    </h1>
                    <h2 class="subtitle">
                        Esta es una landing page construida con Flask y Bulma.
                    </h2>
                    <a class="button is-danger is-large" href="https://flask.palletsprojects.com/en/2.0.x/">Documentación de Flask</a>
                    <a class="button is-link   is-large" href="https://bulma.io/">Documentación de Bulma</a>
                </div>
            </div>
        </section>
    </body>
    </html>
    '''
if __name__ == '__main__': app.run(debug=True)
