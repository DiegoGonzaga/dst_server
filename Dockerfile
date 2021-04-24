FROM cm2network/steamcmd:root
# WORKDIR /app

# RUN yum update -y

# COPY requirements.txt ./requirements.txt
ENV KLEIDIR "${HOMEDIR}/.klei"
# RUN pip install -r requirements.txt
RUN apt-get update && \
    apt-get install libcurl3-gnutls:i386 -y  \
    && mkdir "${KLEIDIR}" \
    && chown -R "${USER}:${USER}" "${KLEIDIR}" \
    && echo /home/steam/steamcmd/steamcmd.sh \
        +login anonymous \
        +app_update 343050 \
        -beta none validate > "${HOMEDIR}/entry.sh"


WORKDIR $HOMEDIR

ENTRYPOINT [ "/bin/bash", "entry.sh" ]

USER $USER
# CMD [ "+login", "anonymous", "+app_update", "343050", "-beta", "none", "validate" ] 
# CMD [  ] 
# RUN /home/steam/steamcmd/steamcmd.sh +login anonymous +app_update 343050 -beta none validate +quit

# COPY .   ./

# CMD ["main.handler"]
# ENTRYPOINT [ "bash" ]
# CMD ["bash"]
