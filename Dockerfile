ARG PYTHON_VERSION=3.12
ARG USERNAME=user-name-goes-here
ARG USER_UID=1000
ARG USER_GID=$USER_UID

FROM python:${PYTHON_VERSION}-slim as builder
WORKDIR /bot
RUN pip install --no-cache-dir --upgrade poetry
COPY poetry.lock pyproject.toml ./
RUN poetry export --without-hashes -f requirements.txt --output requirements.txt

FROM python:${PYTHON_VERSION}-slim
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y
USER $USERNAME
COPY --from=builder /bot/requirements.txt /bot/requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY ./bot/ /bot/
EXPOSE 27017
CMD ["python3", "-m", "bot"]