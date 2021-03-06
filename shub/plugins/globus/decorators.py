'''

Copyright (C) 2017-2018 Vanessa Sochat.
Copyright (C) 2017-2018 The Board of Trustees of the Leland Stanford Junior
University.


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

from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse


def has_globus_association(function):
    '''ensure that a user has globus before continuing. If not, redirect
       to profile where the user can connect the account.
    '''
    def wrap(request, *args, **kwargs):
        # Double check for Globus associated account
        if request.user.get_credentials('globus') is None:
            messages.info(request, "You must have an associated Globus account to perform this action.")
            return redirect('profile')
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
