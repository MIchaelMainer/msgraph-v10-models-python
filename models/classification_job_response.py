# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.detected_sensitive_content_wrapper import DetectedSensitiveContentWrapper
from ..one_drive_object_base import OneDriveObjectBase


class ClassificationJobResponse(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def result(self):
        """
        Gets and sets the result
        
        Returns: 
            :class:`DetectedSensitiveContentWrapper<onedrivesdk.model.detected_sensitive_content_wrapper.DetectedSensitiveContentWrapper>`:
                The result
        """
        if "result" in self._prop_dict:
            if isinstance(self._prop_dict["result"], OneDriveObjectBase):
                return self._prop_dict["result"]
            else :
                self._prop_dict["result"] = DetectedSensitiveContentWrapper(self._prop_dict["result"])
                return self._prop_dict["result"]

        return None

    @result.setter
    def result(self, val):
        self._prop_dict["result"] = val

