# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class PrivacyProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def contact_email(self):
        """Gets and sets the contactEmail
        
        Returns: 
            str:
                The contactEmail
        """
        if "contactEmail" in self._prop_dict:
            return self._prop_dict["contactEmail"]
        else:
            return None

    @contact_email.setter
    def contact_email(self, val):
        self._prop_dict["contactEmail"] = val

    @property
    def statement_url(self):
        """Gets and sets the statementUrl
        
        Returns: 
            str:
                The statementUrl
        """
        if "statementUrl" in self._prop_dict:
            return self._prop_dict["statementUrl"]
        else:
            return None

    @statement_url.setter
    def statement_url(self, val):
        self._prop_dict["statementUrl"] = val

