FROM ubuntu:22.04

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libcurl4 \
    libb2-1 \
    libstdc++6 \
    libxml2 \
    ca-certificates \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir fastapi uvicorn requests numpy

EXPOSE 8080

CMD ["./run.sh"]

