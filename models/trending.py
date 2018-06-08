# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.resource_visualization import ResourceVisualization
from ..model.resource_reference import ResourceReference
from ..model.entity import Entity
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Trending(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def weight(self):
        """
        Gets and sets the weight
        
        Returns:
            float:
                The weight
        """
        if "weight" in self._prop_dict:
            return self._prop_dict["weight"]
        else:
            return None

    @weight.setter
    def weight(self, val):
        self._prop_dict["weight"] = val

    @property
    def resource_visualization(self):
        """
        Gets and sets the resourceVisualization
        
        Returns: 
            :class:`ResourceVisualization<onedrivesdk.model.resource_visualization.ResourceVisualization>`:
                The resourceVisualization
        """
        if "resourceVisualization" in self._prop_dict:
            if isinstance(self._prop_dict["resourceVisualization"], OneDriveObjectBase):
                return self._prop_dict["resourceVisualization"]
            else :
                self._prop_dict["resourceVisualization"] = ResourceVisualization(self._prop_dict["resourceVisualization"])
                return self._prop_dict["resourceVisualization"]

        return None

    @resource_visualization.setter
    def resource_visualization(self, val):
        self._prop_dict["resourceVisualization"] = val

    @property
    def resource_reference(self):
        """
        Gets and sets the resourceReference
        
        Returns: 
            :class:`ResourceReference<onedrivesdk.model.resource_reference.ResourceReference>`:
                The resourceReference
        """
        if "resourceReference" in self._prop_dict:
            if isinstance(self._prop_dict["resourceReference"], OneDriveObjectBase):
                return self._prop_dict["resourceReference"]
            else :
                self._prop_dict["resourceReference"] = ResourceReference(self._prop_dict["resourceReference"])
                return self._prop_dict["resourceReference"]

        return None

    @resource_reference.setter
    def resource_reference(self, val):
        self._prop_dict["resourceReference"] = val

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
    def resource(self):
        """
        Gets and sets the resource
        
        Returns: 
            :class:`Entity<onedrivesdk.model.entity.Entity>`:
                The resource
        """
        if "resource" in self._prop_dict:
            if isinstance(self._prop_dict["resource"], OneDriveObjectBase):
                return self._prop_dict["resource"]
            else :
                self._prop_dict["resource"] = Entity(self._prop_dict["resource"])
                return self._prop_dict["resource"]

        return None

    @resource.setter
    def resource(self, val):
        self._prop_dict["resource"] = val
