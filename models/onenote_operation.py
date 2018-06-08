# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.onenote_operation_error import OnenoteOperationError
from ..one_drive_object_base import OneDriveObjectBase


class OnenoteOperation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def resource_location(self):
        """
        Gets and sets the resourceLocation
        
        Returns:
            str:
                The resourceLocation
        """
        if "resourceLocation" in self._prop_dict:
            return self._prop_dict["resourceLocation"]
        else:
            return None

    @resource_location.setter
    def resource_location(self, val):
        self._prop_dict["resourceLocation"] = val

    @property
    def resource_id(self):
        """
        Gets and sets the resourceId
        
        Returns:
            str:
                The resourceId
        """
        if "resourceId" in self._prop_dict:
            return self._prop_dict["resourceId"]
        else:
            return None

    @resource_id.setter
    def resource_id(self, val):
        self._prop_dict["resourceId"] = val

    @property
    def error(self):
        """
        Gets and sets the error
        
        Returns: 
            :class:`OnenoteOperationError<onedrivesdk.model.onenote_operation_error.OnenoteOperationError>`:
                The error
        """
        if "error" in self._prop_dict:
            if isinstance(self._prop_dict["error"], OneDriveObjectBase):
                return self._prop_dict["error"]
            else :
                self._prop_dict["error"] = OnenoteOperationError(self._prop_dict["error"])
                return self._prop_dict["error"]

        return None

    @error.setter
    def error(self, val):
        self._prop_dict["error"] = val

    @property
    def percent_complete(self):
        """
        Gets and sets the percentComplete
        
        Returns:
            str:
                The percentComplete
        """
        if "percentComplete" in self._prop_dict:
            return self._prop_dict["percentComplete"]
        else:
            return None

    @percent_complete.setter
    def percent_complete(self, val):
        self._prop_dict["percentComplete"] = val

