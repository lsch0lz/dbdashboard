FROM python:3.8
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 8080
RUN cd flask_web && pip install -r requirements.txt
CMD ["python", "app.py"]
