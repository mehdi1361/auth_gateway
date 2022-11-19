FROM python
RUN apt update
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
