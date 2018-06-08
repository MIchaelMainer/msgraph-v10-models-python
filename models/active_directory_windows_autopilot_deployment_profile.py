# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_domain_join_configuration import WindowsDomainJoinConfiguration
from ..one_drive_object_base import OneDriveObjectBase


class ActiveDirectoryWindowsAutopilotDeploymentProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def domain_join_configuration(self):
        """
        Gets and sets the domainJoinConfiguration
        
        Returns: 
            :class:`WindowsDomainJoinConfiguration<onedrivesdk.model.windows_domain_join_configuration.WindowsDomainJoinConfiguration>`:
                The domainJoinConfiguration
        """
        if "domainJoinConfiguration" in self._prop_dict:
            if isinstance(self._prop_dict["domainJoinConfiguration"], OneDriveObjectBase):
                return self._prop_dict["domainJoinConfiguration"]
            else :
                self._prop_dict["domainJoinConfiguration"] = WindowsDomainJoinConfiguration(self._prop_dict["domainJoinConfiguration"])
                return self._prop_dict["domainJoinConfiguration"]

        return None

    @domain_join_configuration.setter
    def domain_join_configuration(self, val):
        self._prop_dict["domainJoinConfiguration"] = val

