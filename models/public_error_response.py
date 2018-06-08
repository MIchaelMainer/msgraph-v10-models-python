# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.public_error import PublicError
from ..one_drive_object_base import OneDriveObjectBase


class PublicErrorResponse(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def error(self):
        """
        Gets and sets the error
        
        Returns: 
            :class:`PublicError<onedrivesdk.model.public_error.PublicError>`:
                The error
        """
        if "error" in self._prop_dict:
            if isinstance(self._prop_dict["error"], OneDriveObjectBase):
                return self._prop_dict["error"]
            else :
                self._prop_dict["error"] = PublicError(self._prop_dict["error"])
                return self._prop_dict["error"]

        return None

    @error.setter
    def error(self, val):
        self._prop_dict["error"] = val
