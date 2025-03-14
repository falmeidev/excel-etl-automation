FROM apache/airflow:2.10.5

# Copy the file with the requirements
COPY requirements.txt /requirements.txt
# Update pip 
RUN pip install --upgrade pip
# Install the packages
RUN pip install --no-cache-dir -r /requirements.txt