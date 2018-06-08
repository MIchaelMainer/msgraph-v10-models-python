# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_app_troubleshooting_history_item import MobileAppTroubleshootingHistoryItem
from ..one_drive_object_base import OneDriveObjectBase


class MobileAppTroubleshootingEvent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def managed_device_identifier(self):
        """
        Gets and sets the managedDeviceIdentifier
        
        Returns:
            str:
                The managedDeviceIdentifier
        """
        if "managedDeviceIdentifier" in self._prop_dict:
            return self._prop_dict["managedDeviceIdentifier"]
        else:
            return None

    @managed_device_identifier.setter
    def managed_device_identifier(self, val):
        self._prop_dict["managedDeviceIdentifier"] = val

    @property
    def user_id(self):
        """
        Gets and sets the userId
        
        Returns:
            str:
                The userId
        """
        if "userId" in self._prop_dict:
            return self._prop_dict["userId"]
        else:
            return None

    @user_id.setter
    def user_id(self, val):
        self._prop_dict["userId"] = val

    @property
    def application_id(self):
        """
        Gets and sets the applicationId
        
        Returns:
            str:
                The applicationId
        """
        if "applicationId" in self._prop_dict:
            return self._prop_dict["applicationId"]
        else:
            return None

    @application_id.setter
    def application_id(self, val):
        self._prop_dict["applicationId"] = val

    @property
    def history(self):
        """Gets and sets the history
        
        Returns: 
            :class:`HistoryCollectionPage<onedrivesdk.request.history_collection.HistoryCollectionPage>`:
                The history
        """
        if "history" in self._prop_dict:
            return HistoryCollectionPage(self._prop_dict["history"])
        else:
            return None

