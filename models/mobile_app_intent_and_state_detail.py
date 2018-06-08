# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_app_intent import MobileAppIntent
from ..model.resultant_app_state import ResultantAppState
from ..one_drive_object_base import OneDriveObjectBase


class MobileAppIntentAndStateDetail(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def application_id(self):
        """Gets and sets the applicationId
        
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
    def mobile_app_intent(self):
        """
        Gets and sets the mobileAppIntent
        
        Returns: 
            :class:`MobileAppIntent<onedrivesdk.model.mobile_app_intent.MobileAppIntent>`:
                The mobileAppIntent
        """
        if "mobileAppIntent" in self._prop_dict:
            if isinstance(self._prop_dict["mobileAppIntent"], OneDriveObjectBase):
                return self._prop_dict["mobileAppIntent"]
            else :
                self._prop_dict["mobileAppIntent"] = MobileAppIntent(self._prop_dict["mobileAppIntent"])
                return self._prop_dict["mobileAppIntent"]

        return None

    @mobile_app_intent.setter
    def mobile_app_intent(self, val):
        self._prop_dict["mobileAppIntent"] = val
    @property
    def display_version(self):
        """Gets and sets the displayVersion
        
        Returns: 
            str:
                The displayVersion
        """
        if "displayVersion" in self._prop_dict:
            return self._prop_dict["displayVersion"]
        else:
            return None

    @display_version.setter
    def display_version(self, val):
        self._prop_dict["displayVersion"] = val

    @property
    def install_state(self):
        """
        Gets and sets the installState
        
        Returns: 
            :class:`ResultantAppState<onedrivesdk.model.resultant_app_state.ResultantAppState>`:
                The installState
        """
        if "installState" in self._prop_dict:
            if isinstance(self._prop_dict["installState"], OneDriveObjectBase):
                return self._prop_dict["installState"]
            else :
                self._prop_dict["installState"] = ResultantAppState(self._prop_dict["installState"])
                return self._prop_dict["installState"]

        return None

    @install_state.setter
    def install_state(self, val):
        self._prop_dict["installState"] = val
