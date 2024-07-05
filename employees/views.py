from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.database_query import get_record_count
from drf_yasg.utils import swagger_auto_schema
from psycopg2 import Error as Psycopg2Error
from drf_yasg import openapi


@swagger_auto_schema(
    methods=['get'],
    operation_description="Número total de empleados",
    responses={
        200: openapi.Response(
            'Exitoso',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'total_records': openapi.Schema(type=openapi.TYPE_INTEGER)
                },
                example={
                    "total_records": 10,
                }
            )
        ),
        400: openapi.Response(
            'Solicitud incorrecta',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING),
                },
                example={
                    "error": "La tabla ingresada no existe"
                }
            )
        ),
        500: openapi.Response(
            'Error interno del servidor',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING),
                },
                example={
                    "error": "Error interno de servidor BD"
                }
            )
        )
    },
    manual_parameters = [openapi.Parameter('table_name', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, description='Nombre de la tabla a consultar', required=True)]

)

@api_view(['GET'])

def employee_count(request):
    """
    Número total de empleados

    Respuestas:
    - 200: Consulta exitosa.
    - 400: Solicitud incorrecta.
    - 500: Error interno del servidor.
    """
    dbname = "desarrollo_db"
    user = "postgres"
    password = ""
    host = "localhost"
    port = "5432"

    table_name = request.GET.get('table_name', None)

    try:
        count = get_record_count(dbname, user, password, host, port, table_name)
        
        if count is not None:
            return count
        else:
            return Response({"error": "Falla en la obtencion de los datos"}, status=500)

    except TypeError as e:
        error_msg = f"Error: {e}"
        return Response({"error": error_msg}, status=500)