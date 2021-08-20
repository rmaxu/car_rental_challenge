FROM postgres:latest

# Set enviroment varibles
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=database

# Expose port 5432
EXPOSE 5432

WORKDIR /code

# Install tools and dependencies
RUN apt-get update && apt-get install -y python3.9 python3-pip
RUN apt-get -y install python3.7-dev
RUN apt-get install -y python3-dev libpq-dev gcc

# Copy needed files
COPY script script/
RUN python3 -m pip install -r script/requirements.txt --default-timeout=1000
COPY queries queries/
COPY run_flow.sh run_flow.sh