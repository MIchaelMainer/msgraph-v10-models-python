# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.state_management_setting import StateManagementSetting
from ..one_drive_object_base import OneDriveObjectBase


class WindowsFirewallNetworkProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def firewall_enabled(self):
        """
        Gets and sets the firewallEnabled
        
        Returns: 
            :class:`StateManagementSetting<onedrivesdk.model.state_management_setting.StateManagementSetting>`:
                The firewallEnabled
        """
        if "firewallEnabled" in self._prop_dict:
            if isinstance(self._prop_dict["firewallEnabled"], OneDriveObjectBase):
                return self._prop_dict["firewallEnabled"]
            else :
                self._prop_dict["firewallEnabled"] = StateManagementSetting(self._prop_dict["firewallEnabled"])
                return self._prop_dict["firewallEnabled"]

        return None

    @firewall_enabled.setter
    def firewall_enabled(self, val):
        self._prop_dict["firewallEnabled"] = val
    @property
    def stealth_mode_blocked(self):
        """Gets and sets the stealthModeBlocked
        
        Returns: 
            bool:
                The stealthModeBlocked
        """
        if "stealthModeBlocked" in self._prop_dict:
            return self._prop_dict["stealthModeBlocked"]
        else:
            return None

    @stealth_mode_blocked.setter
    def stealth_mode_blocked(self, val):
        self._prop_dict["stealthModeBlocked"] = val

    @property
    def incoming_traffic_blocked(self):
        """Gets and sets the incomingTrafficBlocked
        
        Returns: 
            bool:
                The incomingTrafficBlocked
        """
        if "incomingTrafficBlocked" in self._prop_dict:
            return self._prop_dict["incomingTrafficBlocked"]
        else:
            return None

    @incoming_traffic_blocked.setter
    def incoming_traffic_blocked(self, val):
        self._prop_dict["incomingTrafficBlocked"] = val

    @property
    def unicast_responses_to_multicast_broadcasts_blocked(self):
        """Gets and sets the unicastResponsesToMulticastBroadcastsBlocked
        
        Returns: 
            bool:
                The unicastResponsesToMulticastBroadcastsBlocked
        """
        if "unicastResponsesToMulticastBroadcastsBlocked" in self._prop_dict:
            return self._prop_dict["unicastResponsesToMulticastBroadcastsBlocked"]
        else:
            return None

    @unicast_responses_to_multicast_broadcasts_blocked.setter
    def unicast_responses_to_multicast_broadcasts_blocked(self, val):
        self._prop_dict["unicastResponsesToMulticastBroadcastsBlocked"] = val

    @property
    def inbound_notifications_blocked(self):
        """Gets and sets the inboundNotificationsBlocked
        
        Returns: 
            bool:
                The inboundNotificationsBlocked
        """
        if "inboundNotificationsBlocked" in self._prop_dict:
            return self._prop_dict["inboundNotificationsBlocked"]
        else:
            return None

    @inbound_notifications_blocked.setter
    def inbound_notifications_blocked(self, val):
        self._prop_dict["inboundNotificationsBlocked"] = val

    @property
    def authorized_application_rules_from_group_policy_merged(self):
        """Gets and sets the authorizedApplicationRulesFromGroupPolicyMerged
        
        Returns: 
            bool:
                The authorizedApplicationRulesFromGroupPolicyMerged
        """
        if "authorizedApplicationRulesFromGroupPolicyMerged" in self._prop_dict:
            return self._prop_dict["authorizedApplicationRulesFromGroupPolicyMerged"]
        else:
            return None

    @authorized_application_rules_from_group_policy_merged.setter
    def authorized_application_rules_from_group_policy_merged(self, val):
        self._prop_dict["authorizedApplicationRulesFromGroupPolicyMerged"] = val

    @property
    def global_port_rules_from_group_policy_merged(self):
        """Gets and sets the globalPortRulesFromGroupPolicyMerged
        
        Returns: 
            bool:
                The globalPortRulesFromGroupPolicyMerged
        """
        if "globalPortRulesFromGroupPolicyMerged" in self._prop_dict:
            return self._prop_dict["globalPortRulesFromGroupPolicyMerged"]
        else:
            return None

    @global_port_rules_from_group_policy_merged.setter
    def global_port_rules_from_group_policy_merged(self, val):
        self._prop_dict["globalPortRulesFromGroupPolicyMerged"] = val

    @property
    def connection_security_rules_from_group_policy_merged(self):
        """Gets and sets the connectionSecurityRulesFromGroupPolicyMerged
        
        Returns: 
            bool:
                The connectionSecurityRulesFromGroupPolicyMerged
        """
        if "connectionSecurityRulesFromGroupPolicyMerged" in self._prop_dict:
            return self._prop_dict["connectionSecurityRulesFromGroupPolicyMerged"]
        else:
            return None

    @connection_security_rules_from_group_policy_merged.setter
    def connection_security_rules_from_group_policy_merged(self, val):
        self._prop_dict["connectionSecurityRulesFromGroupPolicyMerged"] = val

    @property
    def outbound_connections_blocked(self):
        """Gets and sets the outboundConnectionsBlocked
        
        Returns: 
            bool:
                The outboundConnectionsBlocked
        """
        if "outboundConnectionsBlocked" in self._prop_dict:
            return self._prop_dict["outboundConnectionsBlocked"]
        else:
            return None

    @outbound_connections_blocked.setter
    def outbound_connections_blocked(self, val):
        self._prop_dict["outboundConnectionsBlocked"] = val

    @property
    def inbound_connections_blocked(self):
        """Gets and sets the inboundConnectionsBlocked
        
        Returns: 
            bool:
                The inboundConnectionsBlocked
        """
        if "inboundConnectionsBlocked" in self._prop_dict:
            return self._prop_dict["inboundConnectionsBlocked"]
        else:
            return None

    @inbound_connections_blocked.setter
    def inbound_connections_blocked(self, val):
        self._prop_dict["inboundConnectionsBlocked"] = val

    @property
    def secured_packet_exemption_allowed(self):
        """Gets and sets the securedPacketExemptionAllowed
        
        Returns: 
            bool:
                The securedPacketExemptionAllowed
        """
        if "securedPacketExemptionAllowed" in self._prop_dict:
            return self._prop_dict["securedPacketExemptionAllowed"]
        else:
            return None

    @secured_packet_exemption_allowed.setter
    def secured_packet_exemption_allowed(self, val):
        self._prop_dict["securedPacketExemptionAllowed"] = val

    @property
    def policy_rules_from_group_policy_merged(self):
        """Gets and sets the policyRulesFromGroupPolicyMerged
        
        Returns: 
            bool:
                The policyRulesFromGroupPolicyMerged
        """
        if "policyRulesFromGroupPolicyMerged" in self._prop_dict:
            return self._prop_dict["policyRulesFromGroupPolicyMerged"]
        else:
            return None

    @policy_rules_from_group_policy_merged.setter
    def policy_rules_from_group_policy_merged(self, val):
        self._prop_dict["policyRulesFromGroupPolicyMerged"] = val

