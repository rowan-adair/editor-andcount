FROM python:3.10.0-alpine3.14
WORKDIR /app
RUN pip3 install Flask
COPY ./src /app
RUN pip install --upgrade pip
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD ["app.py"]