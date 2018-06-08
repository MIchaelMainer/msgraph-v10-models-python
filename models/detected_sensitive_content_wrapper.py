# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.detected_sensitive_content import DetectedSensitiveContent
from ..one_drive_object_base import OneDriveObjectBase


class DetectedSensitiveContentWrapper(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def classification(self):
        """
        Gets and sets the classification
        
        Returns: 
            :class:`DetectedSensitiveContent<onedrivesdk.model.detected_sensitive_content.DetectedSensitiveContent>`:
                The classification
        """
        if "classification" in self._prop_dict:
            if isinstance(self._prop_dict["classification"], OneDriveObjectBase):
                return self._prop_dict["classification"]
            else :
                self._prop_dict["classification"] = DetectedSensitiveContent(self._prop_dict["classification"])
                return self._prop_dict["classification"]

        return None

    @classification.setter
    def classification(self, val):
        self._prop_dict["classification"] = val
