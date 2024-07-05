from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.database_query import get_record_count  # Importa la función para consultar la base de datos
from drf_yasg.utils import swagger_auto_schema  # Importa utilidades para documentación Swagger
from psycopg2 import Error as Psycopg2Error  # Importa el tipo de error específico de PostgreSQL
from drf_yasg import openapi  # Importa herramientas para Swagger

# Configura la documentación de Swagger para esta vista
@swagger_auto_schema(
    methods=['get'],  # Especifica que esta vista acepta el método GET
    operation_description="Número total de empleados",  # Descripción de la operación
    responses={
        200: openapi.Response(  # Respuesta para un código de estado 200 (éxito)
            'Exitoso',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'total_records': openapi.Schema(type=openapi.TYPE_INTEGER)  # Define la estructura de la respuesta exitosa
                },
                example={
                    "total_records": 10,  # Ejemplo de cómo se vería la respuesta exitosa
                }
            )
        ),
        400: openapi.Response(  # Respuesta para un código de estado 400 (solicitud incorrecta)
            'Solicitud incorrecta',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING),  # Define la estructura de la respuesta de error
                },
                example={
                    "error": "La tabla ingresada no existe"  # Ejemplo de cómo se vería la respuesta de error
                }
            )
        ),
        500: openapi.Response(  # Respuesta para un código de estado 500 (error interno del servidor)
            'Error interno del servidor',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING),  # Define la estructura de la respuesta de error
                },
                example={
                    "error": "Error interno de servidor BD"  # Ejemplo de cómo se vería la respuesta de error
                }
            )
        )
    },
    manual_parameters=[  # Parámetros de la solicitud que no están en el cuerpo, como 'table_name'
        openapi.Parameter('table_name', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, description='Nombre de la tabla a consultar', required=True)
    ]
)

# Define la vista de API utilizando el decorador api_view de DRF
@api_view(['GET'])
def employee_count(request):
    """
    Número total de empleados

    Respuestas:
    - 200: Consulta exitosa.
    - 400: Solicitud incorrecta.
    - 500: Error interno del servidor.
    """
    # Configuración de conexión a la base de datos PostgreSQL
    dbname = "desarrollo_db"
    user = "postgres"
    password = ""
    host = "localhost"
    port = "5432"

    # Obtiene el nombre de la tabla desde los parámetros de la solicitud GET
    table_name = request.GET.get('table_name', None)

    try:
        # Intenta obtener el conteo de registros utilizando la función de utilidad 'get_record_count'
        count = get_record_count(dbname, user, password, host, port, table_name)
        
        if count is not None:
            return count  # Retorna la respuesta del conteo de registros
        else:
            return Response({"error": "Falla en la obtencion de los datos"}, status=500)  # Retorna un error si no se pudo obtener el conteo

    except TypeError as e:
        error_msg = f"Error: {e}"
        return Response({"error": error_msg}, status=500)  # Retorna un error si hubo un error de tipo durante la ejecución
