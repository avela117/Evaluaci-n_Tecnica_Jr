from flask import Flask, render_template_string, request, redirect, url_for
import pyodbc

app = Flask(__name__)

def obtener_categorias():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=(localdb)\\MSSQLLocalDB;'
        'DATABASE=bd_et;'
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT CodigoCategoria FROM Categoria")
    categorias = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return categorias

def obtener_anios():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=(localdb)\\MSSQLLocalDB;'
        'DATABASE=bd_et;'
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT YEAR(Fecha) FROM Venta ORDER BY YEAR(Fecha)")
    anios = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return anios

def obtener_categorias_2019():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 18 for SQL Server};'
        'SERVER=(localdb)\\MSSQLLocalDB;'
        'DATABASE=bd_et;'
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT c.CodigoCategoria
        FROM Venta v
        JOIN Producto p ON v.CodigoProducto = p.CodigoProducto
        JOIN Categoria c ON p.CodigoCategoria = c.CodigoCategoria
        WHERE YEAR(v.Fecha) = 2019
    """)
    categorias = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return categorias

@app.route('/', methods=['GET', 'POST'])
def lista_ventas():
    ventas = []
    categoria_filtro = ''
    anio_filtro = ''
    ventas_2019 = []
    categoria_2019_filtro = ''
    categorias_2019 = obtener_categorias_2019()

    if request.method == 'POST':
        if 'limpiar' in request.form:
            return redirect(url_for('lista_ventas'))

        # Buscador1 (Principal)
        if 'buscar_principal' in request.form:
            categoria_filtro = request.form.get('categoria', '')
            anio_filtro = request.form.get('anio', '')
            conn = pyodbc.connect(
                'DRIVER={ODBC Driver 18 for SQL Server};'
                'SERVER=(localdb)\\MSSQLLocalDB;'
                'DATABASE=bd_et;'
                'Trusted_Connection=yes;'
                'TrustServerCertificate=yes;'
            )
            cursor = conn.cursor()
            query = """
                SELECT v.CodigoVenta, v.Fecha, p.CodigoProducto, p.Nombre, c.CodigoCategoria, c.Nombre
                FROM Venta v
                JOIN Producto p ON v.CodigoProducto = p.CodigoProducto
                JOIN Categoria c ON p.CodigoCategoria = c.CodigoCategoria
                WHERE 1=1
            """
            params = []
            if categoria_filtro:
                query += " AND c.CodigoCategoria = ?"
                params.append(categoria_filtro)
            if anio_filtro:
                query += " AND YEAR(v.Fecha) = ?"
                params.append(anio_filtro)
            cursor.execute(query, params)
            ventas = [
                {
                    'CodigoVenta': row[0],
                    'Fecha': row[1],
                    'CodigoProducto': row[2],
                    'NombreProducto': row[3],
                    'CodigoCategoria': row[4],
                    'NombreCategoria': row[5]
                }
                for row in cursor.fetchall()
            ]
            cursor.close()
            conn.close()

        # Buscador2 (2019)
        if 'buscar_2019' in request.form:
            categoria_2019_filtro = request.form.get('categoria_2019', '')
            conn = pyodbc.connect(
                'DRIVER={ODBC Driver 18 for SQL Server};'
                'SERVER=(localdb)\\MSSQLLocalDB;'
                'DATABASE=bd_et;'
                'Trusted_Connection=yes;'
                'TrustServerCertificate=yes;'
            )
            cursor = conn.cursor()
            query_2019 = """
                SELECT v.CodigoVenta, v.Fecha, p.CodigoProducto, p.Nombre, c.CodigoCategoria, c.Nombre
                FROM Venta v
                JOIN Producto p ON v.CodigoProducto = p.CodigoProducto
                JOIN Categoria c ON p.CodigoCategoria = c.CodigoCategoria
                WHERE YEAR(v.Fecha) = 2019
            """
            params_2019 = []
            if categoria_2019_filtro:
                query_2019 += " AND c.CodigoCategoria = ?"
                params_2019.append(categoria_2019_filtro)
            cursor.execute(query_2019, params_2019)
            ventas_2019 = [
                {
                    'CodigoVenta': row[0],
                    'Fecha': row[1],
                    'CodigoProducto': row[2],
                    'NombreProducto': row[3],
                    'CodigoCategoria': row[4],
                    'NombreCategoria': row[5]
                }
                for row in cursor.fetchall()
            ]
            cursor.close()
            conn.close()

    categorias = obtener_categorias()
    anios = obtener_anios()

    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Lista de Ventas</title>
        <style>
            body {
                background-color: #f8f9fa;
                font-family: Arial, sans-serif;
            }
            table {
                border-collapse: collapse;
                width: 90%;
                margin: 30px auto;
                background-color: #e6f0fa;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            }
            th, td {
                border: 1px solid #b3c6e0;
                padding: 10px 15px;
                text-align: center;
            }
            th {
                background-color: #0056b3;
                color: white;
                font-weight: bold;
            }
            tr:nth-child(even) {
                background-color: #d6e6f7;
            }
            h1 {
                text-align: center;
                color: #0056b3;
                margin-top: 30px;
            }
            .form-container {
                width: 90%;
                margin: 30px auto 0 auto;
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 10px;
            }
            select, button {
                padding: 10px 15px;
                border: 1px solid #b3c6e0;
                border-radius: 4px;
                background-color: #e6f0fa;
                color: #0056b3;
                font-size: 1em;
            }
            button[type="submit"] {
                background-color: #007bff;
                color: white;
                font-weight: bold;
                border: 1px solid #007bff;
                margin-left: 10px;
            }
            button[type="submit"]:hover {
                background-color: #0056b3;
            }
            button[name="limpiar"] {
                background-color: #e6f0fa;
                color: #0056b3;
                font-weight: bold;
                border: 1px solid #b3c6e0;
                margin-left: 5px;
            }
            button[name="limpiar"]:hover {
                background-color: #b3c6e0;
            }
            label {
                font-weight: bold;
                color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h1>Ventas registradas</h1>
        <form method="post" class="form-container">
            <label for="categoria">Filtrar por categoría:</label>
            <select name="categoria" id="categoria">
                <option value="">Todas</option>
                {% for cat in categorias %}
                    <option value="{{ cat }}" {% if cat == categoria_filtro %}selected{% endif %}>{{ cat }}</option>
                {% endfor %}
            </select>
            <label for="anio">Año:</label>
            <select name="anio" id="anio">
                <option value="">Todos</option>
                {% for anio in anios %}
                    <option value="{{ anio }}" {% if anio|string == anio_filtro|string %}selected{% endif %}>{{ anio }}</option>
                {% endfor %}
            </select>
            <button type="submit" name="buscar_principal">Buscar</button>
            <button type="submit" name="limpiar">Limpiar</button>
        </form>
        {% if ventas %}
        <table>
            <tr>
                <th>ID Venta</th>
                <th>Fecha</th>
                <th>Código Producto</th>
                <th>Nombre Producto</th>
                <th>Código Categoría</th>
                <th>Nombre Categoría</th>
            </tr>
            {% for venta in ventas %}
            <tr>
                <td>{{ venta.CodigoVenta }}</td>
                <td>{{ venta.Fecha }}</td>
                <td>{{ venta.CodigoProducto }}</td>
                <td>{{ venta.NombreProducto }}</td>
                <td>{{ venta.CodigoCategoria }}</td>
                <td>{{ venta.NombreCategoria }}</td>
            </tr>
            {% endfor %}
        </table>
        {% endif %}

        <h1>Ventas del año 2019</h1>
        <form method="post" class="form-container">
            <label for="categoria_2019">Filtrar por categoría (2019):</label>
            <select name="categoria_2019" id="categoria_2019">
                <option value="">Todas</option>
                {% for cat in categorias_2019 %}
                    <option value="{{ cat }}" {% if cat == categoria_2019_filtro %}selected{% endif %}>{{ cat }}</option>
                {% endfor %}
            </select>
            <button type="submit" name="buscar_2019">Buscar</button>
            <button type="submit" name="limpiar">Limpiar</button>
        </form>
        {% if ventas_2019 %}
        <table>
            <tr>
                <th>ID Venta</th>
                <th>Fecha</th>
                <th>Código Producto</th>
                <th>Nombre Producto</th>
                <th>Código Categoría</th>
                <th>Nombre Categoría</th>
            </tr>
            {% for venta in ventas_2019 %}
            <tr>
                <td>{{ venta.CodigoVenta }}</td>
                <td>{{ venta.Fecha }}</td>
                <td>{{ venta.CodigoProducto }}</td>
                <td>{{ venta.NombreProducto }}</td>
                <td>{{ venta.CodigoCategoria }}</td>
                <td>{{ venta.NombreCategoria }}</td>
            </tr>
            {% endfor %}
        </table>
        {% endif %}
    </body>
    </html>
    '''
    return render_template_string(
        html,
        ventas=ventas,
        categorias=obtener_categorias(),
        categoria_filtro=categoria_filtro,
        anios=obtener_anios(),
        anio_filtro=anio_filtro,
        ventas_2019=ventas_2019,
        categorias_2019=categorias_2019,
        categoria_2019_filtro=categoria_2019_filtro
    )

if __name__ == '__main__':
    app.run(debug=True)