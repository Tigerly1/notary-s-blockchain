FROM python:3.9
COPY . .
RUN pip3 install -r requirements.txt
ENV PYTHONPATH="src"
ENV FLASK_APP=src/node/main.py
ENV IP=127.0.0.1
ENV PORT=5000
CMD ["python3", "-m" , "flask", "run", "--host=127.0.0.1", "--port=5002"]
