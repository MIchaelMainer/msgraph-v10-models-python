# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.vpn_on_demand_rule_connection_action import VpnOnDemandRuleConnectionAction
from ..model.vpn_on_demand_rule_connection_domain_action import VpnOnDemandRuleConnectionDomainAction
from ..one_drive_object_base import OneDriveObjectBase


class VpnOnDemandRule(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def ssids(self):
        """Gets and sets the ssids
        
        Returns: 
            str:
                The ssids
        """
        if "ssids" in self._prop_dict:
            return self._prop_dict["ssids"]
        else:
            return None

    @ssids.setter
    def ssids(self, val):
        self._prop_dict["ssids"] = val

    @property
    def dns_search_domains(self):
        """Gets and sets the dnsSearchDomains
        
        Returns: 
            str:
                The dnsSearchDomains
        """
        if "dnsSearchDomains" in self._prop_dict:
            return self._prop_dict["dnsSearchDomains"]
        else:
            return None

    @dns_search_domains.setter
    def dns_search_domains(self, val):
        self._prop_dict["dnsSearchDomains"] = val

    @property
    def probe_url(self):
        """Gets and sets the probeUrl
        
        Returns: 
            str:
                The probeUrl
        """
        if "probeUrl" in self._prop_dict:
            return self._prop_dict["probeUrl"]
        else:
            return None

    @probe_url.setter
    def probe_url(self, val):
        self._prop_dict["probeUrl"] = val

    @property
    def action(self):
        """
        Gets and sets the action
        
        Returns: 
            :class:`VpnOnDemandRuleConnectionAction<onedrivesdk.model.vpn_on_demand_rule_connection_action.VpnOnDemandRuleConnectionAction>`:
                The action
        """
        if "action" in self._prop_dict:
            if isinstance(self._prop_dict["action"], OneDriveObjectBase):
                return self._prop_dict["action"]
            else :
                self._prop_dict["action"] = VpnOnDemandRuleConnectionAction(self._prop_dict["action"])
                return self._prop_dict["action"]

        return None

    @action.setter
    def action(self, val):
        self._prop_dict["action"] = val
    @property
    def domain_action(self):
        """
        Gets and sets the domainAction
        
        Returns: 
            :class:`VpnOnDemandRuleConnectionDomainAction<onedrivesdk.model.vpn_on_demand_rule_connection_domain_action.VpnOnDemandRuleConnectionDomainAction>`:
                The domainAction
        """
        if "domainAction" in self._prop_dict:
            if isinstance(self._prop_dict["domainAction"], OneDriveObjectBase):
                return self._prop_dict["domainAction"]
            else :
                self._prop_dict["domainAction"] = VpnOnDemandRuleConnectionDomainAction(self._prop_dict["domainAction"])
                return self._prop_dict["domainAction"]

        return None

    @domain_action.setter
    def domain_action(self, val):
        self._prop_dict["domainAction"] = val
    @property
    def domains(self):
        """Gets and sets the domains
        
        Returns: 
            str:
                The domains
        """
        if "domains" in self._prop_dict:
            return self._prop_dict["domains"]
        else:
            return None

    @domains.setter
    def domains(self, val):
        self._prop_dict["domains"] = val

    @property
    def probe_required_url(self):
        """Gets and sets the probeRequiredUrl
        
        Returns: 
            str:
                The probeRequiredUrl
        """
        if "probeRequiredUrl" in self._prop_dict:
            return self._prop_dict["probeRequiredUrl"]
        else:
            return None

    @probe_required_url.setter
    def probe_required_url(self, val):
        self._prop_dict["probeRequiredUrl"] = val

