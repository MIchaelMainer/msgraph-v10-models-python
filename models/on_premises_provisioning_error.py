# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class OnPremisesProvisioningError(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def value(self):
        """Gets and sets the value
        
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
    def category(self):
        """Gets and sets the category
        
        Returns: 
            str:
                The category
        """
        if "category" in self._prop_dict:
            return self._prop_dict["category"]
        else:
            return None

    @category.setter
    def category(self, val):
        self._prop_dict["category"] = val

    @property
    def property_causing_error(self):
        """Gets and sets the propertyCausingError
        
        Returns: 
            str:
                The propertyCausingError
        """
        if "propertyCausingError" in self._prop_dict:
            return self._prop_dict["propertyCausingError"]
        else:
            return None

    @property_causing_error.setter
    def property_causing_error(self, val):
        self._prop_dict["propertyCausingError"] = val

    @property
    def occurred_date_time(self):
        """Gets and sets the occurredDateTime
        
        Returns: 
            datetime:
                The occurredDateTime
        """
        if "occurredDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["occurredDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @occurred_date_time.setter
    def occurred_date_time(self, val):
        self._prop_dict["occurredDateTime"] = val.isoformat()+"Z"

