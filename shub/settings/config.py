'''

Copyright (C) 2017-2018 The Board of Trustees of the Leland Stanford Junior
University.
Copyright (C) 2017-2018 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

# Root directories

MEDIA_ROOT='/data/sregistry/www/images'
STATIC_ROOT='/data/sregistry/www/static'

# AUTHENTICATION

SECRET_KEY = 'r1ujq^aetezi8#d!#)7mxw2qv9&kh(t+043x)(=e3owl9)mf$8'

# Which social auths do you want to use?
ENABLE_GOOGLE_AUTH=False
ENABLE_TWITTER_AUTH=False
ENABLE_GITHUB_AUTH=False
ENABLE_GITLAB_AUTH=False

# NOTE you will need to set autehtication methods up.
# Configuration goes into secrets.py
# see https://singularityhub.github.io/sregistry/install.html
# secrets.py.example provides a template to work from

# See below for additional authentication module, e.g. LDAP that are
# available, and configured, as plugins.


ADMINS = (( 'goinac', 'goinac@janelia.hhmi.org'),)
MANAGERS = ADMINS

HELP_CONTACT_EMAIL = 'goinac@janelia.hhmi.org'
HELP_INSTITUTION_SITE = 'janelia.hhmi.org'
REGISTRY_NAME = "HHMI Janelia SRegistry"
REGISTRY_URI = "hhmi-janelia"


# PERMISSIONS

# Allow users to create public collections
USER_COLLECTIONS = True

# Should registries by default be private, with no option for public?
PRIVATE_ONLY = False

# Should the default for a new registry be private or public?
DEFAULT_PRIVATE = False


# DOMAIN NAMES

DOMAIN_NAME = "http://c11u16.int.janelia.org:3033"
DOMAIN_NAME_HTTP = "http://c11u16.int.janelia.org:3033"
DOMAIN_NAKED = DOMAIN_NAME_HTTP.replace('http://','')


# DATABASE

# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sregistry',
        'USER': 'sregistry',
        'PASSWORD': 'sregistry',
        'HOST': 'localdb',
        'PORT': '5432',
    }
}


# Visualizations

# After how many single containers should we switch to showing collections
# only? >= 1000
VISUALIZATION_TREEMAP_COLLECTION_SWITCH=1000


# Logging

# Do you want to save complete response metadata per each pull?
# If you disable, we still keep track of collection pull counts, but not specific versions
LOGGING_SAVE_RESPONSES=True


# SAML Configuration

AUTH_SAML_IDP = "hhmi-janelia"
AUTH_SAML_INSTITUTION = "HHMI | Janelia Research Campus"


# Plugins
# Add the name of a plugin under shub.plugins here to enable it


# Available Plugins:

# - ldap_auth: Allows sregistry to authenitcate against an LDAP directory
# - globus: allows connection from sregistry to endpoints
# - saml_auth: authentication with SAML

PLUGINS_ENABLED = [
    'ldap_auth',
    'globus',
    'saml_auth'
]
