FROM python:3.9-slim-bullseye

ARG user_id=1001
ARG group_id=1002
ARG user=circleci
ARG group=dev
RUN addgroup --system $group --gid $group_id \
    && adduser $user --gid $group_id --uid $user_id --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
RUN mkdir -p /srv/app && chown $user:$group /srv/app


ARG PYTHON_PACKAGES_REQUIRING_COMPILATION="psycopg2==2.9.3"
ARG psycopg2_install_deps="gcc python3-dev"
ARG ALL_INSTALL_DEPS="$psycopg2_install_deps"
ARG psycopg2_runtime_deps="libpq-dev"
ARG ALL_RUNTIME_DEPS="$psycopg2_runtime_deps"
RUN python3 -m pip install --user --upgrade pip
RUN apt-get update && apt-get install $ALL_RUNTIME_DEPS $ALL_INSTALL_DEPS -y --no-install-recommends \
    && pip install $PYTHON_PACKAGES_REQUIRING_COMPILATION --no-cache-dir \
    && apt-get clean \
    && apt-get purge $ALL_INSTALL_DEPS -y \
    && apt autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip --no-cache-dir \
    && pip install pip-tools --no-cache-dir


USER $user
ENV PATH /home/$user/.local/bin:/home/$user/bin:$PATH

COPY ./app /app

WORKDIR /app


COPY --chown=${user}:${group} app/requirements* ./
RUN pip install --no-cache-dir --user -r requirements.txt
COPY --chown=${user}:${group} app /app

ENV PYTHONPATH=${PYTHONPATH}:/app/
EXPOSE 5000

CMD ["./start.sh"]