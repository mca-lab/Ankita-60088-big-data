FROM python:3.10-slim

WORKDIR /app

# Install Java for Spark
RUN apt-get update && \
    apt-get install -y default-jdk && \
    rm -rf /var/lib/apt/lists/*

# Set Java environment
ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV PATH=$PATH:$JAVA_HOME/bin

# Install PySpark
COPY requirements.txt .
RUN pip install --default-timeout=300 --no-cache-dir -r requirements.txt


# Copy source code
COPY src/ src/

# Run cleaning script
CMD ["python", "src/clean_data.py"]
