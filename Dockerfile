ARG PYTHON_VERSION=3.12.6
FROM python:${PYTHON_VERSION}-slim as base

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

EXPOSE 8000

CMD fastapi dev /app/src/main.py --host 0.0.0.0 --port 81
