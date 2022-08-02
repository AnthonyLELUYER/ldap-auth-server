FROM python:3.8.7-slim-buster

RUN groupadd -g 1000 lancelot \
  && useradd --shell /bin/bash --gid 1000 --uid 1000 lancelot

COPY ./requirements.txt /var/www/

RUN buildDeps='gcc' \
  && set -x \
  && apt-get update \
  && apt-get install -y $buildDeps libsasl2-dev libldap2-dev libssl-dev --no-install-recommends \
  && pip install -r /var/www/requirements.txt \
  && apt-get purge -y --auto-remove $buildDeps

COPY ./__init__.py /var/www/
COPY ./config.yaml /var/www/
COPY ./healthcheck.py /var/www/
COPY ./setup.py /var/www/
COPY ./openapi_server /var/www/openapi_server
COPY ./core /var/www/core
COPY ./certificates /var/www/certificates

RUN chown -R 1000:1000 /var

HEALTHCHECK --interval=30s --retries=2 CMD python3 /var/www/healthcheck.py
USER lancelot

ENV PYTHONPATH "${PYTHONPATH}:/var/www"
RUN echo 'export SECRET=`python3 -c "import os; print(os.urandom(24))"`' >> /var/www/envfile
CMD . /var/www/envfile && cd /var/www/ \
  && python3 setup.py docker \
  && python3 -m openapi_server