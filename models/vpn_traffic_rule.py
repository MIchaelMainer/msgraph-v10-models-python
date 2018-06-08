# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.number_range import NumberRange
from ..model.i_pv4_range import IPv4Range
from ..model.vpn_traffic_rule_app_type import VpnTrafficRuleAppType
from ..model.vpn_traffic_rule_routing_policy_type import VpnTrafficRuleRoutingPolicyType
from ..one_drive_object_base import OneDriveObjectBase


class VpnTrafficRule(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def name(self):
        """Gets and sets the name
        
        Returns: 
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def protocols(self):
        """Gets and sets the protocols
        
        Returns: 
            int:
                The protocols
        """
        if "protocols" in self._prop_dict:
            return self._prop_dict["protocols"]
        else:
            return None

    @protocols.setter
    def protocols(self, val):
        self._prop_dict["protocols"] = val

    @property
    def local_port_ranges(self):
        """
        Gets and sets the localPortRanges
        
        Returns: 
            :class:`NumberRange<onedrivesdk.model.number_range.NumberRange>`:
                The localPortRanges
        """
        if "localPortRanges" in self._prop_dict:
            if isinstance(self._prop_dict["localPortRanges"], OneDriveObjectBase):
                return self._prop_dict["localPortRanges"]
            else :
                self._prop_dict["localPortRanges"] = NumberRange(self._prop_dict["localPortRanges"])
                return self._prop_dict["localPortRanges"]

        return None

    @local_port_ranges.setter
    def local_port_ranges(self, val):
        self._prop_dict["localPortRanges"] = val
    @property
    def remote_port_ranges(self):
        """
        Gets and sets the remotePortRanges
        
        Returns: 
            :class:`NumberRange<onedrivesdk.model.number_range.NumberRange>`:
                The remotePortRanges
        """
        if "remotePortRanges" in self._prop_dict:
            if isinstance(self._prop_dict["remotePortRanges"], OneDriveObjectBase):
                return self._prop_dict["remotePortRanges"]
            else :
                self._prop_dict["remotePortRanges"] = NumberRange(self._prop_dict["remotePortRanges"])
                return self._prop_dict["remotePortRanges"]

        return None

    @remote_port_ranges.setter
    def remote_port_ranges(self, val):
        self._prop_dict["remotePortRanges"] = val
    @property
    def local_address_ranges(self):
        """
        Gets and sets the localAddressRanges
        
        Returns: 
            :class:`IPv4Range<onedrivesdk.model.i_pv4_range.IPv4Range>`:
                The localAddressRanges
        """
        if "localAddressRanges" in self._prop_dict:
            if isinstance(self._prop_dict["localAddressRanges"], OneDriveObjectBase):
                return self._prop_dict["localAddressRanges"]
            else :
                self._prop_dict["localAddressRanges"] = IPv4Range(self._prop_dict["localAddressRanges"])
                return self._prop_dict["localAddressRanges"]

        return None

    @local_address_ranges.setter
    def local_address_ranges(self, val):
        self._prop_dict["localAddressRanges"] = val
    @property
    def remote_address_ranges(self):
        """
        Gets and sets the remoteAddressRanges
        
        Returns: 
            :class:`IPv4Range<onedrivesdk.model.i_pv4_range.IPv4Range>`:
                The remoteAddressRanges
        """
        if "remoteAddressRanges" in self._prop_dict:
            if isinstance(self._prop_dict["remoteAddressRanges"], OneDriveObjectBase):
                return self._prop_dict["remoteAddressRanges"]
            else :
                self._prop_dict["remoteAddressRanges"] = IPv4Range(self._prop_dict["remoteAddressRanges"])
                return self._prop_dict["remoteAddressRanges"]

        return None

    @remote_address_ranges.setter
    def remote_address_ranges(self, val):
        self._prop_dict["remoteAddressRanges"] = val
    @property
    def app_id(self):
        """Gets and sets the appId
        
        Returns: 
            str:
                The appId
        """
        if "appId" in self._prop_dict:
            return self._prop_dict["appId"]
        else:
            return None

    @app_id.setter
    def app_id(self, val):
        self._prop_dict["appId"] = val

    @property
    def app_type(self):
        """
        Gets and sets the appType
        
        Returns: 
            :class:`VpnTrafficRuleAppType<onedrivesdk.model.vpn_traffic_rule_app_type.VpnTrafficRuleAppType>`:
                The appType
        """
        if "appType" in self._prop_dict:
            if isinstance(self._prop_dict["appType"], OneDriveObjectBase):
                return self._prop_dict["appType"]
            else :
                self._prop_dict["appType"] = VpnTrafficRuleAppType(self._prop_dict["appType"])
                return self._prop_dict["appType"]

        return None

    @app_type.setter
    def app_type(self, val):
        self._prop_dict["appType"] = val
    @property
    def routing_policy_type(self):
        """
        Gets and sets the routingPolicyType
        
        Returns: 
            :class:`VpnTrafficRuleRoutingPolicyType<onedrivesdk.model.vpn_traffic_rule_routing_policy_type.VpnTrafficRuleRoutingPolicyType>`:
                The routingPolicyType
        """
        if "routingPolicyType" in self._prop_dict:
            if isinstance(self._prop_dict["routingPolicyType"], OneDriveObjectBase):
                return self._prop_dict["routingPolicyType"]
            else :
                self._prop_dict["routingPolicyType"] = VpnTrafficRuleRoutingPolicyType(self._prop_dict["routingPolicyType"])
                return self._prop_dict["routingPolicyType"]

        return None

    @routing_policy_type.setter
    def routing_policy_type(self, val):
        self._prop_dict["routingPolicyType"] = val
    @property
    def claims(self):
        """Gets and sets the claims
        
        Returns: 
            str:
                The claims
        """
        if "claims" in self._prop_dict:
            return self._prop_dict["claims"]
        else:
            return None

    @claims.setter
    def claims(self, val):
        self._prop_dict["claims"] = val

