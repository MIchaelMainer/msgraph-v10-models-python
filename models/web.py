# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Web(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def redirect_urls(self):
        """Gets and sets the redirectUrls
        
        Returns: 
            str:
                The redirectUrls
        """
        if "redirectUrls" in self._prop_dict:
            return self._prop_dict["redirectUrls"]
        else:
            return None

    @redirect_urls.setter
    def redirect_urls(self, val):
        self._prop_dict["redirectUrls"] = val

    @property
    def logout_url(self):
        """Gets and sets the logoutUrl
        
        Returns: 
            str:
                The logoutUrl
        """
        if "logoutUrl" in self._prop_dict:
            return self._prop_dict["logoutUrl"]
        else:
            return None

    @logout_url.setter
    def logout_url(self, val):
        self._prop_dict["logoutUrl"] = val

    @property
    def oauth2_allow_implicit_flow(self):
        """Gets and sets the oauth2AllowImplicitFlow
        
        Returns: 
            bool:
                The oauth2AllowImplicitFlow
        """
        if "oauth2AllowImplicitFlow" in self._prop_dict:
            return self._prop_dict["oauth2AllowImplicitFlow"]
        else:
            return None

    @oauth2_allow_implicit_flow.setter
    def oauth2_allow_implicit_flow(self, val):
        self._prop_dict["oauth2AllowImplicitFlow"] = val

