FROM python:3.8.18

# Copia primero el archivo de espera wait-for-it.sh
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it.sh

# Dale permisos de ejecución al archivo de espera
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Copia los archivos requeridos y ejecuta las actualizaciones
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y curl
RUN pip install --upgrade pip && pip install -r /code/requirements.txt

# Copia el script de entrada al directorio /code
COPY entrypoints.sh /code/entrypoints.sh

# Dale permisos de ejecución al script de entrada
RUN chmod +x /code/entrypoints.sh

# Establece el directorio de trabajo
WORKDIR /code

# Establece el script de entrada como el comando de inicio del contenedor
# ENTRYPOINT ["./entrypoints.sh"]