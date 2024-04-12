FROM python:3.8.18

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /code/

# Descarga wait-for-it.sh
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it.sh

# Dale permisos de ejecución
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Copia el script de entrada y establece permisos de ejecución
COPY entrypoints.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoints.sh

# Establece el comando de inicio del contenedor
ENTRYPOINT ["entrypoints.sh"]

