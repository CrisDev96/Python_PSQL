# Desarrollo_PythonPSQL

## Tabla de contenido
- [Resumen](#resumen)
- [Requerimientos](#requerimientos)
- [Instalacion](#instalacion)
- [Endpoints](#endpoints)
- [Documentacion] (#documentacion)

## Resumen
Desarrollo_PythonPSQL es un proyecto basado en Django que demuestra la integración con PostgreSQL. El proyecto incluye una API REST para la gestión y obtención del número total de registros en una tabla específica.

## Requerimientos
- Python 3.10.5
- PostgreSQL
- Django 5.0.6
- Archivo 'requirements.txt'

## Instalacion
1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/yourusername/desarrollo_PythonPSQL.git
   cd desarrollo_PythonPSQL
2. **Crear entorno virtual**
   python -m venv myenv
   python3 -m venv myenv
4. **Activar entorno virtual**
   - Windows:
      myenv\Scripts\activate
   - macOS y Linux:
      source myenv/bin/activate
5. **Instalar los requerimientos**
   pip install -r requirements.txt
6. **Correr proyecto**
   python manage.py runserver


## Endpoints
**Obtener el número total de registros**
http://127.0.0.1:8000/employees/employee_count/

## Documentacion
**Para más detalles sobre el uso del endpoint, visita:**
http://127.0.0.1:8000/employees/employee_count/

