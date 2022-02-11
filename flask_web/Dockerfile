FROM python:3.8
RUN mkdir /usr/src/app/
COPY .. /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 8080
COPY . .
RUN pip install Flask requests
CMD ["python", "app.py"]
