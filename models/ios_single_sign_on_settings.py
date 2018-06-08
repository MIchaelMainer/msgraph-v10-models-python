# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.app_list_item import AppListItem
from ..one_drive_object_base import OneDriveObjectBase


class IosSingleSignOnSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def allowed_apps_list(self):
        """
        Gets and sets the allowedAppsList
        
        Returns: 
            :class:`AppListItem<onedrivesdk.model.app_list_item.AppListItem>`:
                The allowedAppsList
        """
        if "allowedAppsList" in self._prop_dict:
            if isinstance(self._prop_dict["allowedAppsList"], OneDriveObjectBase):
                return self._prop_dict["allowedAppsList"]
            else :
                self._prop_dict["allowedAppsList"] = AppListItem(self._prop_dict["allowedAppsList"])
                return self._prop_dict["allowedAppsList"]

        return None

    @allowed_apps_list.setter
    def allowed_apps_list(self, val):
        self._prop_dict["allowedAppsList"] = val
    @property
    def allowed_urls(self):
        """Gets and sets the allowedUrls
        
        Returns: 
            str:
                The allowedUrls
        """
        if "allowedUrls" in self._prop_dict:
            return self._prop_dict["allowedUrls"]
        else:
            return None

    @allowed_urls.setter
    def allowed_urls(self, val):
        self._prop_dict["allowedUrls"] = val

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
    def kerberos_principal_name(self):
        """Gets and sets the kerberosPrincipalName
        
        Returns: 
            str:
                The kerberosPrincipalName
        """
        if "kerberosPrincipalName" in self._prop_dict:
            return self._prop_dict["kerberosPrincipalName"]
        else:
            return None

    @kerberos_principal_name.setter
    def kerberos_principal_name(self, val):
        self._prop_dict["kerberosPrincipalName"] = val

    @property
    def kerberos_realm(self):
        """Gets and sets the kerberosRealm
        
        Returns: 
            str:
                The kerberosRealm
        """
        if "kerberosRealm" in self._prop_dict:
            return self._prop_dict["kerberosRealm"]
        else:
            return None

    @kerberos_realm.setter
    def kerberos_realm(self, val):
        self._prop_dict["kerberosRealm"] = val

