from flask import Flask, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_temporal_alertas_2026'

@app.route('/procesar_pago')
def procesar_pago():
    # Lógica de simulación de una acción del usuario
    # Creamos el mensaje que se mostrará en la siguiente petición
    flash('¡El pago se ha procesado con éxito!')
    
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    # Aquí es donde el usuario llega redireccionado y verá el mensaje flash
    return 'Panel Principal (Mira la consola o el HTML para ver el mensaje flash)'

if __name__ == '__main__':
    app.run(debug=True) 