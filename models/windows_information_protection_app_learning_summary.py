# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.application_type import ApplicationType
from ..one_drive_object_base import OneDriveObjectBase


class WindowsInformationProtectionAppLearningSummary(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def application_name(self):
        """
        Gets and sets the applicationName
        
        Returns:
            str:
                The applicationName
        """
        if "applicationName" in self._prop_dict:
            return self._prop_dict["applicationName"]
        else:
            return None

    @application_name.setter
    def application_name(self, val):
        self._prop_dict["applicationName"] = val

    @property
    def application_type(self):
        """
        Gets and sets the applicationType
        
        Returns: 
            :class:`ApplicationType<onedrivesdk.model.application_type.ApplicationType>`:
                The applicationType
        """
        if "applicationType" in self._prop_dict:
            if isinstance(self._prop_dict["applicationType"], OneDriveObjectBase):
                return self._prop_dict["applicationType"]
            else :
                self._prop_dict["applicationType"] = ApplicationType(self._prop_dict["applicationType"])
                return self._prop_dict["applicationType"]

        return None

    @application_type.setter
    def application_type(self, val):
        self._prop_dict["applicationType"] = val

    @property
    def device_count(self):
        """
        Gets and sets the deviceCount
        
        Returns:
            int:
                The deviceCount
        """
        if "deviceCount" in self._prop_dict:
            return self._prop_dict["deviceCount"]
        else:
            return None

    @device_count.setter
    def device_count(self, val):
        self._prop_dict["deviceCount"] = val

