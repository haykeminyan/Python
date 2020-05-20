FROM joyzoursky/python-chromedriver:3.7-selenium

WORKDIR /home/haykeminyan/Python/Test_Oblako_group

ADD test.py /

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

CMD [ "python3", "test.py" ]
