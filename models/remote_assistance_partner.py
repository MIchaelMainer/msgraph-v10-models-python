# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.remote_assistance_onboarding_status import RemoteAssistanceOnboardingStatus
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class RemoteAssistancePartner(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
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
    def onboarding_url(self):
        """
        Gets and sets the onboardingUrl
        
        Returns:
            str:
                The onboardingUrl
        """
        if "onboardingUrl" in self._prop_dict:
            return self._prop_dict["onboardingUrl"]
        else:
            return None

    @onboarding_url.setter
    def onboarding_url(self, val):
        self._prop_dict["onboardingUrl"] = val

    @property
    def onboarding_status(self):
        """
        Gets and sets the onboardingStatus
        
        Returns: 
            :class:`RemoteAssistanceOnboardingStatus<onedrivesdk.model.remote_assistance_onboarding_status.RemoteAssistanceOnboardingStatus>`:
                The onboardingStatus
        """
        if "onboardingStatus" in self._prop_dict:
            if isinstance(self._prop_dict["onboardingStatus"], OneDriveObjectBase):
                return self._prop_dict["onboardingStatus"]
            else :
                self._prop_dict["onboardingStatus"] = RemoteAssistanceOnboardingStatus(self._prop_dict["onboardingStatus"])
                return self._prop_dict["onboardingStatus"]

        return None

    @onboarding_status.setter
    def onboarding_status(self, val):
        self._prop_dict["onboardingStatus"] = val

    @property
    def last_connection_date_time(self):
        """
        Gets and sets the lastConnectionDateTime
        
        Returns:
            datetime:
                The lastConnectionDateTime
        """
        if "lastConnectionDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastConnectionDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_connection_date_time.setter
    def last_connection_date_time(self, val):
        self._prop_dict["lastConnectionDateTime"] = val.isoformat()+"Z"

