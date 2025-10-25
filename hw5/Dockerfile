FROM agrigorev/zoomcamp-model:2025

WORKDIR /code

# Install uv (fast Python package manager)
RUN pip install uv

COPY ["pyproject.toml", "uv.lock", "app.py", "./"]

# Install dependencies using uv (fast Python package manager)
RUN uv sync --frozen --no-dev

# Expose FastAPI port
EXPOSE 9696

# Start the FastAPI app with uvicorn through uv
ENTRYPOINT ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9696"]