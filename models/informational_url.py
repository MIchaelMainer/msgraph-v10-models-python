# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class InformationalUrl(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def logo_url(self):
        """Gets and sets the logoUrl
        
        Returns: 
            str:
                The logoUrl
        """
        if "logoUrl" in self._prop_dict:
            return self._prop_dict["logoUrl"]
        else:
            return None

    @logo_url.setter
    def logo_url(self, val):
        self._prop_dict["logoUrl"] = val

    @property
    def marketing_url(self):
        """Gets and sets the marketingUrl
        
        Returns: 
            str:
                The marketingUrl
        """
        if "marketingUrl" in self._prop_dict:
            return self._prop_dict["marketingUrl"]
        else:
            return None

    @marketing_url.setter
    def marketing_url(self, val):
        self._prop_dict["marketingUrl"] = val

    @property
    def privacy_statement_url(self):
        """Gets and sets the privacyStatementUrl
        
        Returns: 
            str:
                The privacyStatementUrl
        """
        if "privacyStatementUrl" in self._prop_dict:
            return self._prop_dict["privacyStatementUrl"]
        else:
            return None

    @privacy_statement_url.setter
    def privacy_statement_url(self, val):
        self._prop_dict["privacyStatementUrl"] = val

    @property
    def support_url(self):
        """Gets and sets the supportUrl
        
        Returns: 
            str:
                The supportUrl
        """
        if "supportUrl" in self._prop_dict:
            return self._prop_dict["supportUrl"]
        else:
            return None

    @support_url.setter
    def support_url(self, val):
        self._prop_dict["supportUrl"] = val

    @property
    def terms_of_service_url(self):
        """Gets and sets the termsOfServiceUrl
        
        Returns: 
            str:
                The termsOfServiceUrl
        """
        if "termsOfServiceUrl" in self._prop_dict:
            return self._prop_dict["termsOfServiceUrl"]
        else:
            return None

    @terms_of_service_url.setter
    def terms_of_service_url(self, val):
        self._prop_dict["termsOfServiceUrl"] = val

