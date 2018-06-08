# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class PasswordCredential(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def end_date_time(self):
        """Gets and sets the endDateTime
        
        Returns: 
            datetime:
                The endDateTime
        """
        if "endDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["endDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @end_date_time.setter
    def end_date_time(self, val):
        self._prop_dict["endDateTime"] = val.isoformat()+"Z"

    @property
    def key_id(self):
        """Gets and sets the keyId
        
        Returns: 
            UUID:
                The keyId
        """
        if "keyId" in self._prop_dict:
            return self._prop_dict["keyId"]
        else:
            return None

    @key_id.setter
    def key_id(self, val):
        self._prop_dict["keyId"] = val

    @property
    def start_date_time(self):
        """Gets and sets the startDateTime
        
        Returns: 
            datetime:
                The startDateTime
        """
        if "startDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["startDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @start_date_time.setter
    def start_date_time(self, val):
        self._prop_dict["startDateTime"] = val.isoformat()+"Z"

    @property
    def secret_text(self):
        """Gets and sets the secretText
        
        Returns: 
            str:
                The secretText
        """
        if "secretText" in self._prop_dict:
            return self._prop_dict["secretText"]
        else:
            return None

    @secret_text.setter
    def secret_text(self, val):
        self._prop_dict["secretText"] = val

    @property
    def hint(self):
        """Gets and sets the hint
        
        Returns: 
            str:
                The hint
        """
        if "hint" in self._prop_dict:
            return self._prop_dict["hint"]
        else:
            return None

    @hint.setter
    def hint(self, val):
        self._prop_dict["hint"] = val

