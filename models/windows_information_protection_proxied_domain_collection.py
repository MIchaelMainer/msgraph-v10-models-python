# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.proxied_domain import ProxiedDomain
from ..one_drive_object_base import OneDriveObjectBase


class WindowsInformationProtectionProxiedDomainCollection(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """Gets and sets the displayName
        
        Returns: 
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def proxied_domains(self):
        """
        Gets and sets the proxiedDomains
        
        Returns: 
            :class:`ProxiedDomain<onedrivesdk.model.proxied_domain.ProxiedDomain>`:
                The proxiedDomains
        """
        if "proxiedDomains" in self._prop_dict:
            if isinstance(self._prop_dict["proxiedDomains"], OneDriveObjectBase):
                return self._prop_dict["proxiedDomains"]
            else :
                self._prop_dict["proxiedDomains"] = ProxiedDomain(self._prop_dict["proxiedDomains"])
                return self._prop_dict["proxiedDomains"]

        return None

    @proxied_domains.setter
    def proxied_domains(self, val):
        self._prop_dict["proxiedDomains"] = val
