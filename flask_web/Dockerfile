FROM python:3.8
RUN mkdir /usr/src/app/
COPY .. /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 8080
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
CMD ["python", "app.py"]
