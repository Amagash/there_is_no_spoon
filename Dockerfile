FROM python:3.7

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install --upgrade there_is_no_spoon

ENTRYPOINT ["there_is_no_spoon"]