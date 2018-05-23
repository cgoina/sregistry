FROM python:3.6.5
ENV PYTHONUNBUFFERED 1

################################################################################
# CORE
# Do not modify this section

RUN apt-get update && apt-get install -y \
    pkg-config \
    cmake \
    openssl \
    wget \
    git \
    vim

RUN apt-get update && apt-get install -y \
    anacron \
    autoconf \
    automake \
    libarchive-dev \
    libtool \
    libopenblas-dev \
    libglib2.0-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libhdf5-dev \
    libgeos-dev \
    libsasl2-dev \
    libldap2-dev \
    build-essential

# Install Singularity
RUN git clone https://www.github.com/singularityware/singularity.git
WORKDIR singularity
RUN ./autogen.sh && ./configure --prefix=/usr/local && make && make install

# Install Python requirements out of /tmp so not triggered if other contents of /code change
ADD requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

################################################################################
# PLUGINS
# You are free to comment out those plugins that you don't want to use

# Install LDAP 
RUN pip install python3-ldap
RUN pip install django-auth-ldap

# Install Globus Packages
RUN pip install globus-cli globus-sdk[jwt]

# Install SAML
RUN pip install python3-saml
RUN pip install social-auth-core[saml]

#  Clean up
RUN apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

################################################################################
# BASE

ADD . /code/

WORKDIR /code

CMD uwsgi /code/uwsgi.ini

EXPOSE 3032
