# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_network_isolation_policy import WindowsNetworkIsolationPolicy
from ..one_drive_object_base import OneDriveObjectBase


class Windows10NetworkBoundaryConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def windows_network_isolation_policy(self):
        """
        Gets and sets the windowsNetworkIsolationPolicy
        
        Returns: 
            :class:`WindowsNetworkIsolationPolicy<onedrivesdk.model.windows_network_isolation_policy.WindowsNetworkIsolationPolicy>`:
                The windowsNetworkIsolationPolicy
        """
        if "windowsNetworkIsolationPolicy" in self._prop_dict:
            if isinstance(self._prop_dict["windowsNetworkIsolationPolicy"], OneDriveObjectBase):
                return self._prop_dict["windowsNetworkIsolationPolicy"]
            else :
                self._prop_dict["windowsNetworkIsolationPolicy"] = WindowsNetworkIsolationPolicy(self._prop_dict["windowsNetworkIsolationPolicy"])
                return self._prop_dict["windowsNetworkIsolationPolicy"]

        return None

    @windows_network_isolation_policy.setter
    def windows_network_isolation_policy(self, val):
        self._prop_dict["windowsNetworkIsolationPolicy"] = val

