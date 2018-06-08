# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.sensitive_content_location import SensitiveContentLocation
from ..one_drive_object_base import OneDriveObjectBase


class DetectedSensitiveContent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def id(self):
        """Gets and sets the id
        
        Returns: 
            UUID:
                The id
        """
        if "id" in self._prop_dict:
            return self._prop_dict["id"]
        else:
            return None

    @id.setter
    def id(self, val):
        self._prop_dict["id"] = val

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
    def unique_count(self):
        """Gets and sets the uniqueCount
        
        Returns: 
            int:
                The uniqueCount
        """
        if "uniqueCount" in self._prop_dict:
            return self._prop_dict["uniqueCount"]
        else:
            return None

    @unique_count.setter
    def unique_count(self, val):
        self._prop_dict["uniqueCount"] = val

    @property
    def confidence(self):
        """Gets and sets the confidence
        
        Returns: 
            int:
                The confidence
        """
        if "confidence" in self._prop_dict:
            return self._prop_dict["confidence"]
        else:
            return None

    @confidence.setter
    def confidence(self, val):
        self._prop_dict["confidence"] = val

    @property
    def matches(self):
        """
        Gets and sets the matches
        
        Returns: 
            :class:`SensitiveContentLocation<onedrivesdk.model.sensitive_content_location.SensitiveContentLocation>`:
                The matches
        """
        if "matches" in self._prop_dict:
            if isinstance(self._prop_dict["matches"], OneDriveObjectBase):
                return self._prop_dict["matches"]
            else :
                self._prop_dict["matches"] = SensitiveContentLocation(self._prop_dict["matches"])
                return self._prop_dict["matches"]

        return None

    @matches.setter
    def matches(self, val):
        self._prop_dict["matches"] = val
