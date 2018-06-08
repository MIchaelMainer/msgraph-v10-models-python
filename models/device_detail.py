# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class DeviceDetail(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def device_id(self):
        """Gets and sets the deviceId
        
        Returns: 
            str:
                The deviceId
        """
        if "deviceId" in self._prop_dict:
            return self._prop_dict["deviceId"]
        else:
            return None

    @device_id.setter
    def device_id(self, val):
        self._prop_dict["deviceId"] = val

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
    def operating_system(self):
        """Gets and sets the operatingSystem
        
        Returns: 
            str:
                The operatingSystem
        """
        if "operatingSystem" in self._prop_dict:
            return self._prop_dict["operatingSystem"]
        else:
            return None

    @operating_system.setter
    def operating_system(self, val):
        self._prop_dict["operatingSystem"] = val

    @property
    def browser(self):
        """Gets and sets the browser
        
        Returns: 
            str:
                The browser
        """
        if "browser" in self._prop_dict:
            return self._prop_dict["browser"]
        else:
            return None

    @browser.setter
    def browser(self, val):
        self._prop_dict["browser"] = val

    @property
    def is_compliant(self):
        """Gets and sets the isCompliant
        
        Returns: 
            bool:
                The isCompliant
        """
        if "isCompliant" in self._prop_dict:
            return self._prop_dict["isCompliant"]
        else:
            return None

    @is_compliant.setter
    def is_compliant(self, val):
        self._prop_dict["isCompliant"] = val

    @property
    def is_managed(self):
        """Gets and sets the isManaged
        
        Returns: 
            bool:
                The isManaged
        """
        if "isManaged" in self._prop_dict:
            return self._prop_dict["isManaged"]
        else:
            return None

    @is_managed.setter
    def is_managed(self, val):
        self._prop_dict["isManaged"] = val

    @property
    def trust_type(self):
        """Gets and sets the trustType
        
        Returns: 
            str:
                The trustType
        """
        if "trustType" in self._prop_dict:
            return self._prop_dict["trustType"]
        else:
            return None

    @trust_type.setter
    def trust_type(self, val):
        self._prop_dict["trustType"] = val

