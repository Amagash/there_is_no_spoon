FROM tensorflow/tensorflow:2.1.0-py3

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install there_is_no_spoon

ENTRYPOINT ["there_is_no_spoon"]