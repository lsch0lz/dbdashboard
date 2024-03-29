FROM python:3.8
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 8080
RUN pip install -r flask_web/requirements.txt
ENTRYPOINT ["./flask_web"]
CMD ["python", "app.py"]
