# https://github.com/docker/awesome-compose/blob/master/official-documentation-samples/django/README.md

FROM python:3.10-slim-buster

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:ubuntugis/ppa \
    && apt-get install -y libgeos++-dev \
    && apt-get install -y proj-bin \
    && apt-get install -y gdal-bin \
    && apt-get install -y libgdal-dev \
    && apt-get install -y nano

# Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PTHONUNBUFFERED=1

WORKDIR /backend

COPY requirements.txt /backend/

# Install dependencies.
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy project code
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
