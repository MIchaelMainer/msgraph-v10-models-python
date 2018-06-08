# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.user_email_source import UserEmailSource
from ..model.username_source import UsernameSource
from ..model.domain_name_source import DomainNameSource
from ..one_drive_object_base import OneDriveObjectBase


class EasEmailProfileConfigurationBase(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def username_source(self):
        """
        Gets and sets the usernameSource
        
        Returns: 
            :class:`UserEmailSource<onedrivesdk.model.user_email_source.UserEmailSource>`:
                The usernameSource
        """
        if "usernameSource" in self._prop_dict:
            if isinstance(self._prop_dict["usernameSource"], OneDriveObjectBase):
                return self._prop_dict["usernameSource"]
            else :
                self._prop_dict["usernameSource"] = UserEmailSource(self._prop_dict["usernameSource"])
                return self._prop_dict["usernameSource"]

        return None

    @username_source.setter
    def username_source(self, val):
        self._prop_dict["usernameSource"] = val

    @property
    def username_aad_source(self):
        """
        Gets and sets the usernameAADSource
        
        Returns: 
            :class:`UsernameSource<onedrivesdk.model.username_source.UsernameSource>`:
                The usernameAADSource
        """
        if "usernameAADSource" in self._prop_dict:
            if isinstance(self._prop_dict["usernameAADSource"], OneDriveObjectBase):
                return self._prop_dict["usernameAADSource"]
            else :
                self._prop_dict["usernameAADSource"] = UsernameSource(self._prop_dict["usernameAADSource"])
                return self._prop_dict["usernameAADSource"]

        return None

    @username_aad_source.setter
    def username_aad_source(self, val):
        self._prop_dict["usernameAADSource"] = val

    @property
    def user_domain_name_source(self):
        """
        Gets and sets the userDomainNameSource
        
        Returns: 
            :class:`DomainNameSource<onedrivesdk.model.domain_name_source.DomainNameSource>`:
                The userDomainNameSource
        """
        if "userDomainNameSource" in self._prop_dict:
            if isinstance(self._prop_dict["userDomainNameSource"], OneDriveObjectBase):
                return self._prop_dict["userDomainNameSource"]
            else :
                self._prop_dict["userDomainNameSource"] = DomainNameSource(self._prop_dict["userDomainNameSource"])
                return self._prop_dict["userDomainNameSource"]

        return None

    @user_domain_name_source.setter
    def user_domain_name_source(self, val):
        self._prop_dict["userDomainNameSource"] = val

    @property
    def custom_domain_name(self):
        """
        Gets and sets the customDomainName
        
        Returns:
            str:
                The customDomainName
        """
        if "customDomainName" in self._prop_dict:
            return self._prop_dict["customDomainName"]
        else:
            return None

    @custom_domain_name.setter
    def custom_domain_name(self, val):
        self._prop_dict["customDomainName"] = val

