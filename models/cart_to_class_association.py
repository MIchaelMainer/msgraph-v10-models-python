# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class CartToClassAssociation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime
        
        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def version(self):
        """
        Gets and sets the version
        
        Returns:
            int:
                The version
        """
        if "version" in self._prop_dict:
            return self._prop_dict["version"]
        else:
            return None

    @version.setter
    def version(self, val):
        self._prop_dict["version"] = val

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
    def device_cart_ids(self):
        """
        Gets and sets the deviceCartIds
        
        Returns:
            str:
                The deviceCartIds
        """
        if "deviceCartIds" in self._prop_dict:
            return self._prop_dict["deviceCartIds"]
        else:
            return None

    @device_cart_ids.setter
    def device_cart_ids(self, val):
        self._prop_dict["deviceCartIds"] = val

    @property
    def classroom_ids(self):
        """
        Gets and sets the classroomIds
        
        Returns:
            str:
                The classroomIds
        """
        if "classroomIds" in self._prop_dict:
            return self._prop_dict["classroomIds"]
        else:
            return None

    @classroom_ids.setter
    def classroom_ids(self, val):
        self._prop_dict["classroomIds"] = val
