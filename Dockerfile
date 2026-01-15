FROM python:3.11-slim

# Copy the uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin 

# Create workspace folder inside the container
WORKDIR /app

# Copy only dependency files first (for better caching)
COPY pyproject.toml uv.lock ./

# Sync dependencies
RUN uv sync --frozen --no-install-project

# Copy the rest of the code
COPY . .

# Final sync to install the app itself
RUN uv sync --frozen

# Ensure the virtual environment's bin is in the PATH
ENV PATH="/app/.venv/bin/:$PATH"

# set the Port
EXPOSE 7860

# The start command
# CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
CMD ["python", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
