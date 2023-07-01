# a recognised image
FROM python

# what file do we want to run
WORKDIR /app

# which port
ENV PORT 5000
EXPOSE 5000

# stuff we need to load
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy from here to the local directory on docker
COPY . .

# start the program
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
