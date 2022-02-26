FROM python:3.8
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 8080
RUN pwd
RUN ls -l
RUN pip install -r requirements.txt && pip install -r flask_web/requirements.txt
CMD ["python", "app.py"]
