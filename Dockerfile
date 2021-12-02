FROM python:3.7-slim-buster
RUN pip install flask 
CMD python testFlask.py