FROM python:3.14-slim

# Install uv
RUN pip install uv

WORKDIR /app

# Copy dependency files
COPY ["pyproject.toml", "uv.lock", "./"]

# Create virtual environment and install dependencies
RUN uv sync --frozen --no-dev --no-install-project

# Make the virtual environment the default Python environment
ENV PATH="/app/.venv/bin:$PATH"

# Copy application files
COPY ["predict.py", "./"]

# Copy artifacts
COPY ["model.bin", "dv.bin", "scaler.bin", "./"]

EXPOSE 9690

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9690", "predict:app"]