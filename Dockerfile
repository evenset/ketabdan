## Dockerfile:
FROM python:3
ENV BUILD_ENV=PRODUCTION
RUN mkdir /code
WORKDIR /code
# Copy requirment first and install it rather than run it directly from code to cache pip
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000
# CMD specifcies the command to execute to start the server running.
CMD ["/code/start.sh"]
# done!
