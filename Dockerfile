From python:3.11
copy morthyc /root/morthyc
RUN pip3 install pip --upgrade
RUN pip3 install discord.py
RUN pip3 install python-dotenv requests
CMD ["python3", "/root/morthyc/main.py"]
