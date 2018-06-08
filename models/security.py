# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.alert import Alert
from ..model.application_security_profile import ApplicationSecurityProfile
from ..model.file_security_profile import FileSecurityProfile
from ..model.host_security_profile import HostSecurityProfile
from ..model.ip_security_profile import IpSecurityProfile
from ..model.user_security_profile import UserSecurityProfile
from ..one_drive_object_base import OneDriveObjectBase


class Security(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def alerts(self):
        """Gets and sets the alerts
        
        Returns: 
            :class:`AlertsCollectionPage<onedrivesdk.request.alerts_collection.AlertsCollectionPage>`:
                The alerts
        """
        if "alerts" in self._prop_dict:
            return AlertsCollectionPage(self._prop_dict["alerts"])
        else:
            return None

    @property
    def application_security_profiles(self):
        """Gets and sets the applicationSecurityProfiles
        
        Returns: 
            :class:`ApplicationSecurityProfilesCollectionPage<onedrivesdk.request.application_security_profiles_collection.ApplicationSecurityProfilesCollectionPage>`:
                The applicationSecurityProfiles
        """
        if "applicationSecurityProfiles" in self._prop_dict:
            return ApplicationSecurityProfilesCollectionPage(self._prop_dict["applicationSecurityProfiles"])
        else:
            return None

    @property
    def file_security_profiles(self):
        """Gets and sets the fileSecurityProfiles
        
        Returns: 
            :class:`FileSecurityProfilesCollectionPage<onedrivesdk.request.file_security_profiles_collection.FileSecurityProfilesCollectionPage>`:
                The fileSecurityProfiles
        """
        if "fileSecurityProfiles" in self._prop_dict:
            return FileSecurityProfilesCollectionPage(self._prop_dict["fileSecurityProfiles"])
        else:
            return None

    @property
    def host_security_profiles(self):
        """Gets and sets the hostSecurityProfiles
        
        Returns: 
            :class:`HostSecurityProfilesCollectionPage<onedrivesdk.request.host_security_profiles_collection.HostSecurityProfilesCollectionPage>`:
                The hostSecurityProfiles
        """
        if "hostSecurityProfiles" in self._prop_dict:
            return HostSecurityProfilesCollectionPage(self._prop_dict["hostSecurityProfiles"])
        else:
            return None

    @property
    def ip_security_profiles(self):
        """Gets and sets the ipSecurityProfiles
        
        Returns: 
            :class:`IpSecurityProfilesCollectionPage<onedrivesdk.request.ip_security_profiles_collection.IpSecurityProfilesCollectionPage>`:
                The ipSecurityProfiles
        """
        if "ipSecurityProfiles" in self._prop_dict:
            return IpSecurityProfilesCollectionPage(self._prop_dict["ipSecurityProfiles"])
        else:
            return None

    @property
    def user_security_profiles(self):
        """Gets and sets the userSecurityProfiles
        
        Returns: 
            :class:`UserSecurityProfilesCollectionPage<onedrivesdk.request.user_security_profiles_collection.UserSecurityProfilesCollectionPage>`:
                The userSecurityProfiles
        """
        if "userSecurityProfiles" in self._prop_dict:
            return UserSecurityProfilesCollectionPage(self._prop_dict["userSecurityProfiles"])
        else:
            return None

