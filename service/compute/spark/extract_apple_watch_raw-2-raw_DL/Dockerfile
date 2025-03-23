FROM apache/spark:3.3.2

USER root

# Install Python + pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Create a working directory
WORKDIR /pyspark/pipeline/raw-2-raw_DL

# Copy in requirements first so Docker can cache pip installs
COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Copy in all your code (including main.py)
COPY . .

# (Optional) switch back to non-root
USER 185

# Use spark-submit on main.py by default
ENTRYPOINT ["/opt/spark/bin/spark-submit", "main.py"]
