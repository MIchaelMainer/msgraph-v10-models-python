# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mac_os_gatekeeper_app_sources import MacOSGatekeeperAppSources
from ..model.mac_os_firewall_application import MacOSFirewallApplication
from ..one_drive_object_base import OneDriveObjectBase


class MacOSEndpointProtectionConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def gatekeeper_allowed_app_source(self):
        """
        Gets and sets the gatekeeperAllowedAppSource
        
        Returns: 
            :class:`MacOSGatekeeperAppSources<onedrivesdk.model.mac_os_gatekeeper_app_sources.MacOSGatekeeperAppSources>`:
                The gatekeeperAllowedAppSource
        """
        if "gatekeeperAllowedAppSource" in self._prop_dict:
            if isinstance(self._prop_dict["gatekeeperAllowedAppSource"], OneDriveObjectBase):
                return self._prop_dict["gatekeeperAllowedAppSource"]
            else :
                self._prop_dict["gatekeeperAllowedAppSource"] = MacOSGatekeeperAppSources(self._prop_dict["gatekeeperAllowedAppSource"])
                return self._prop_dict["gatekeeperAllowedAppSource"]

        return None

    @gatekeeper_allowed_app_source.setter
    def gatekeeper_allowed_app_source(self, val):
        self._prop_dict["gatekeeperAllowedAppSource"] = val

    @property
    def gatekeeper_block_override(self):
        """
        Gets and sets the gatekeeperBlockOverride
        
        Returns:
            bool:
                The gatekeeperBlockOverride
        """
        if "gatekeeperBlockOverride" in self._prop_dict:
            return self._prop_dict["gatekeeperBlockOverride"]
        else:
            return None

    @gatekeeper_block_override.setter
    def gatekeeper_block_override(self, val):
        self._prop_dict["gatekeeperBlockOverride"] = val

    @property
    def firewall_enabled(self):
        """
        Gets and sets the firewallEnabled
        
        Returns:
            bool:
                The firewallEnabled
        """
        if "firewallEnabled" in self._prop_dict:
            return self._prop_dict["firewallEnabled"]
        else:
            return None

    @firewall_enabled.setter
    def firewall_enabled(self, val):
        self._prop_dict["firewallEnabled"] = val

    @property
    def firewall_block_all_incoming(self):
        """
        Gets and sets the firewallBlockAllIncoming
        
        Returns:
            bool:
                The firewallBlockAllIncoming
        """
        if "firewallBlockAllIncoming" in self._prop_dict:
            return self._prop_dict["firewallBlockAllIncoming"]
        else:
            return None

    @firewall_block_all_incoming.setter
    def firewall_block_all_incoming(self, val):
        self._prop_dict["firewallBlockAllIncoming"] = val

    @property
    def firewall_enable_stealth_mode(self):
        """
        Gets and sets the firewallEnableStealthMode
        
        Returns:
            bool:
                The firewallEnableStealthMode
        """
        if "firewallEnableStealthMode" in self._prop_dict:
            return self._prop_dict["firewallEnableStealthMode"]
        else:
            return None

    @firewall_enable_stealth_mode.setter
    def firewall_enable_stealth_mode(self, val):
        self._prop_dict["firewallEnableStealthMode"] = val

    @property
    def firewall_applications(self):
        """Gets and sets the firewallApplications
        
        Returns: 
            :class:`FirewallApplicationsCollectionPage<onedrivesdk.request.firewall_applications_collection.FirewallApplicationsCollectionPage>`:
                The firewallApplications
        """
        if "firewallApplications" in self._prop_dict:
            return FirewallApplicationsCollectionPage(self._prop_dict["firewallApplications"])
        else:
            return None

