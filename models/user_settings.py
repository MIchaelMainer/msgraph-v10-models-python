# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class UserSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def contribution_to_content_discovery_disabled(self):
        """
        Gets and sets the contributionToContentDiscoveryDisabled
        
        Returns:
            bool:
                The contributionToContentDiscoveryDisabled
        """
        if "contributionToContentDiscoveryDisabled" in self._prop_dict:
            return self._prop_dict["contributionToContentDiscoveryDisabled"]
        else:
            return None

    @contribution_to_content_discovery_disabled.setter
    def contribution_to_content_discovery_disabled(self, val):
        self._prop_dict["contributionToContentDiscoveryDisabled"] = val

    @property
    def contribution_to_content_discovery_as_organization_disabled(self):
        """
        Gets and sets the contributionToContentDiscoveryAsOrganizationDisabled
        
        Returns:
            bool:
                The contributionToContentDiscoveryAsOrganizationDisabled
        """
        if "contributionToContentDiscoveryAsOrganizationDisabled" in self._prop_dict:
            return self._prop_dict["contributionToContentDiscoveryAsOrganizationDisabled"]
        else:
            return None

    @contribution_to_content_discovery_as_organization_disabled.setter
    def contribution_to_content_discovery_as_organization_disabled(self, val):
        self._prop_dict["contributionToContentDiscoveryAsOrganizationDisabled"] = val

