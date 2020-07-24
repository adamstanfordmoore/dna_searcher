FROM python:3
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY . ./

#RUN python manage.py collectstatic
#RUN python manage.py makemigrations && python manage.py migrate

# run gunicorn
CMD gunicorn DNA_form.wsgi:application --bind 0.0.0.0::$PORT

