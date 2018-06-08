# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DriveRecipient(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def alias(self):
        """Gets and sets the alias
        
        Returns: 
            str:
                The alias
        """
        if "alias" in self._prop_dict:
            return self._prop_dict["alias"]
        else:
            return None

    @alias.setter
    def alias(self, val):
        self._prop_dict["alias"] = val

    @property
    def email(self):
        """Gets and sets the email
        
        Returns: 
            str:
                The email
        """
        if "email" in self._prop_dict:
            return self._prop_dict["email"]
        else:
            return None

    @email.setter
    def email(self, val):
        self._prop_dict["email"] = val

    @property
    def object_id(self):
        """Gets and sets the objectId
        
        Returns: 
            str:
                The objectId
        """
        if "objectId" in self._prop_dict:
            return self._prop_dict["objectId"]
        else:
            return None

    @object_id.setter
    def object_id(self, val):
        self._prop_dict["objectId"] = val

