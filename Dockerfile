FROM ghcr.io/astral-sh/uv:python3.13-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 9191
WORKDIR /app

COPY pickpockett_webhook ./pickpockett_webhook
COPY pyproject.toml uv.lock ./

RUN uv --no-cache sync --locked

CMD ["uv", "run" , "-m", "pickpockett_webhook"]
