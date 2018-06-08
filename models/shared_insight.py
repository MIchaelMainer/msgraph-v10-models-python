# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.sharing_detail import SharingDetail
from ..model.resource_visualization import ResourceVisualization
from ..model.resource_reference import ResourceReference
from ..model.entity import Entity
from ..one_drive_object_base import OneDriveObjectBase


class SharedInsight(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def last_shared(self):
        """
        Gets and sets the lastShared
        
        Returns: 
            :class:`SharingDetail<onedrivesdk.model.sharing_detail.SharingDetail>`:
                The lastShared
        """
        if "lastShared" in self._prop_dict:
            if isinstance(self._prop_dict["lastShared"], OneDriveObjectBase):
                return self._prop_dict["lastShared"]
            else :
                self._prop_dict["lastShared"] = SharingDetail(self._prop_dict["lastShared"])
                return self._prop_dict["lastShared"]

        return None

    @last_shared.setter
    def last_shared(self, val):
        self._prop_dict["lastShared"] = val

    @property
    def sharing_history(self):
        """Gets and sets the sharingHistory
        
        Returns: 
            :class:`SharingHistoryCollectionPage<onedrivesdk.request.sharing_history_collection.SharingHistoryCollectionPage>`:
                The sharingHistory
        """
        if "sharingHistory" in self._prop_dict:
            return SharingHistoryCollectionPage(self._prop_dict["sharingHistory"])
        else:
            return None

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
    def last_shared_method(self):
        """
        Gets and sets the lastSharedMethod
        
        Returns: 
            :class:`Entity<onedrivesdk.model.entity.Entity>`:
                The lastSharedMethod
        """
        if "lastSharedMethod" in self._prop_dict:
            if isinstance(self._prop_dict["lastSharedMethod"], OneDriveObjectBase):
                return self._prop_dict["lastSharedMethod"]
            else :
                self._prop_dict["lastSharedMethod"] = Entity(self._prop_dict["lastSharedMethod"])
                return self._prop_dict["lastSharedMethod"]

        return None

    @last_shared_method.setter
    def last_shared_method(self, val):
        self._prop_dict["lastSharedMethod"] = val

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

