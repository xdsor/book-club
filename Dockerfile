FROM python:3.12.11-slim
RUN pip install uv && apt-get update && apt-get install -y make && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY pyproject.toml .
COPY uv.lock .
RUN uv venv && uv sync --python=/app/.venv/bin/python
COPY . .
EXPOSE 8000
CMD ["make", "start"]
