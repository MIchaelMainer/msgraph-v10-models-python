# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.insight_identity import InsightIdentity
from ..model.resource_reference import ResourceReference
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class SharingDetail(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def shared_by(self):
        """
        Gets and sets the sharedBy
        
        Returns: 
            :class:`InsightIdentity<onedrivesdk.model.insight_identity.InsightIdentity>`:
                The sharedBy
        """
        if "sharedBy" in self._prop_dict:
            if isinstance(self._prop_dict["sharedBy"], OneDriveObjectBase):
                return self._prop_dict["sharedBy"]
            else :
                self._prop_dict["sharedBy"] = InsightIdentity(self._prop_dict["sharedBy"])
                return self._prop_dict["sharedBy"]

        return None

    @shared_by.setter
    def shared_by(self, val):
        self._prop_dict["sharedBy"] = val
    @property
    def shared_date_time(self):
        """Gets and sets the sharedDateTime
        
        Returns: 
            datetime:
                The sharedDateTime
        """
        if "sharedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["sharedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @shared_date_time.setter
    def shared_date_time(self, val):
        self._prop_dict["sharedDateTime"] = val.isoformat()+"Z"

    @property
    def sharing_subject(self):
        """Gets and sets the sharingSubject
        
        Returns: 
            str:
                The sharingSubject
        """
        if "sharingSubject" in self._prop_dict:
            return self._prop_dict["sharingSubject"]
        else:
            return None

    @sharing_subject.setter
    def sharing_subject(self, val):
        self._prop_dict["sharingSubject"] = val

    @property
    def sharing_type(self):
        """Gets and sets the sharingType
        
        Returns: 
            str:
                The sharingType
        """
        if "sharingType" in self._prop_dict:
            return self._prop_dict["sharingType"]
        else:
            return None

    @sharing_type.setter
    def sharing_type(self, val):
        self._prop_dict["sharingType"] = val

    @property
    def sharing_reference(self):
        """
        Gets and sets the sharingReference
        
        Returns: 
            :class:`ResourceReference<onedrivesdk.model.resource_reference.ResourceReference>`:
                The sharingReference
        """
        if "sharingReference" in self._prop_dict:
            if isinstance(self._prop_dict["sharingReference"], OneDriveObjectBase):
                return self._prop_dict["sharingReference"]
            else :
                self._prop_dict["sharingReference"] = ResourceReference(self._prop_dict["sharingReference"])
                return self._prop_dict["sharingReference"]

        return None

    @sharing_reference.setter
    def sharing_reference(self, val):
        self._prop_dict["sharingReference"] = val
