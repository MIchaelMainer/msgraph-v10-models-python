# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class SideLoadingKey(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def value(self):
        """
        Gets and sets the value
        
        Returns:
            str:
                The value
        """
        if "value" in self._prop_dict:
            return self._prop_dict["value"]
        else:
            return None

    @value.setter
    def value(self, val):
        self._prop_dict["value"] = val

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
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
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def total_activation(self):
        """
        Gets and sets the totalActivation
        
        Returns:
            int:
                The totalActivation
        """
        if "totalActivation" in self._prop_dict:
            return self._prop_dict["totalActivation"]
        else:
            return None

    @total_activation.setter
    def total_activation(self, val):
        self._prop_dict["totalActivation"] = val

    @property
    def last_updated_date_time(self):
        """
        Gets and sets the lastUpdatedDateTime
        
        Returns:
            str:
                The lastUpdatedDateTime
        """
        if "lastUpdatedDateTime" in self._prop_dict:
            return self._prop_dict["lastUpdatedDateTime"]
        else:
            return None

    @last_updated_date_time.setter
    def last_updated_date_time(self, val):
        self._prop_dict["lastUpdatedDateTime"] = val

