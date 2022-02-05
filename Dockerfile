FROM python

WORKDIR /PSMBot-Virtual-Assistant

COPY /main.py .
COPY /weather.py .
COPY news.py .

COPY requirements.txt .
RUN pip install requirements.txt

CMD [ "python", "main.py" ]