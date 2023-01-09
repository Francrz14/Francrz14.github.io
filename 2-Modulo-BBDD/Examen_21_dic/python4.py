
@app.route("/welcome/<string:nombre>")
def api(nombre):
   return f"<h1>Bienvenido a mi app, {nombre}</h1>"