# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.email_address import EmailAddress
from ..one_drive_object_base import OneDriveObjectBase


class Recipient(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def email_address(self):
        """
        Gets and sets the emailAddress
        
        Returns: 
            :class:`EmailAddress<onedrivesdk.model.email_address.EmailAddress>`:
                The emailAddress
        """
        if "emailAddress" in self._prop_dict:
            if isinstance(self._prop_dict["emailAddress"], OneDriveObjectBase):
                return self._prop_dict["emailAddress"]
            else :
                self._prop_dict["emailAddress"] = EmailAddress(self._prop_dict["emailAddress"])
                return self._prop_dict["emailAddress"]

        return None

    @email_address.setter
    def email_address(self, val):
        self._prop_dict["emailAddress"] = val
