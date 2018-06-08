# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.activity_group_state import ActivityGroupState
from ..model.security_vendor_information import SecurityVendorInformation
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class IpSecurityProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def activity_group_states(self):
        """Gets and sets the activityGroupStates
        
        Returns: 
            :class:`ActivityGroupStatesCollectionPage<onedrivesdk.request.activity_group_states_collection.ActivityGroupStatesCollectionPage>`:
                The activityGroupStates
        """
        if "activityGroupStates" in self._prop_dict:
            return ActivityGroupStatesCollectionPage(self._prop_dict["activityGroupStates"])
        else:
            return None

    @property
    def address(self):
        """
        Gets and sets the address
        
        Returns:
            str:
                The address
        """
        if "address" in self._prop_dict:
            return self._prop_dict["address"]
        else:
            return None

    @address.setter
    def address(self, val):
        self._prop_dict["address"] = val

    @property
    def asn(self):
        """
        Gets and sets the asn
        
        Returns:
            int:
                The asn
        """
        if "asn" in self._prop_dict:
            return self._prop_dict["asn"]
        else:
            return None

    @asn.setter
    def asn(self, val):
        self._prop_dict["asn"] = val

    @property
    def azure_subscription_id(self):
        """
        Gets and sets the azureSubscriptionId
        
        Returns:
            str:
                The azureSubscriptionId
        """
        if "azureSubscriptionId" in self._prop_dict:
            return self._prop_dict["azureSubscriptionId"]
        else:
            return None

    @azure_subscription_id.setter
    def azure_subscription_id(self, val):
        self._prop_dict["azureSubscriptionId"] = val

    @property
    def azure_tenant_id(self):
        """
        Gets and sets the azureTenantId
        
        Returns:
            str:
                The azureTenantId
        """
        if "azureTenantId" in self._prop_dict:
            return self._prop_dict["azureTenantId"]
        else:
            return None

    @azure_tenant_id.setter
    def azure_tenant_id(self, val):
        self._prop_dict["azureTenantId"] = val

    @property
    def city(self):
        """
        Gets and sets the city
        
        Returns:
            str:
                The city
        """
        if "city" in self._prop_dict:
            return self._prop_dict["city"]
        else:
            return None

    @city.setter
    def city(self, val):
        self._prop_dict["city"] = val

    @property
    def country_or_region_code(self):
        """
        Gets and sets the countryOrRegionCode
        
        Returns:
            str:
                The countryOrRegionCode
        """
        if "countryOrRegionCode" in self._prop_dict:
            return self._prop_dict["countryOrRegionCode"]
        else:
            return None

    @country_or_region_code.setter
    def country_or_region_code(self, val):
        self._prop_dict["countryOrRegionCode"] = val

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime
        
        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def organization(self):
        """
        Gets and sets the organization
        
        Returns:
            str:
                The organization
        """
        if "organization" in self._prop_dict:
            return self._prop_dict["organization"]
        else:
            return None

    @organization.setter
    def organization(self, val):
        self._prop_dict["organization"] = val

    @property
    def risk_score(self):
        """
        Gets and sets the riskScore
        
        Returns:
            str:
                The riskScore
        """
        if "riskScore" in self._prop_dict:
            return self._prop_dict["riskScore"]
        else:
            return None

    @risk_score.setter
    def risk_score(self, val):
        self._prop_dict["riskScore"] = val

    @property
    def state(self):
        """
        Gets and sets the state
        
        Returns:
            str:
                The state
        """
        if "state" in self._prop_dict:
            return self._prop_dict["state"]
        else:
            return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def tags(self):
        """
        Gets and sets the tags
        
        Returns:
            str:
                The tags
        """
        if "tags" in self._prop_dict:
            return self._prop_dict["tags"]
        else:
            return None

    @tags.setter
    def tags(self, val):
        self._prop_dict["tags"] = val

    @property
    def vendor_information(self):
        """
        Gets and sets the vendorInformation
        
        Returns: 
            :class:`SecurityVendorInformation<onedrivesdk.model.security_vendor_information.SecurityVendorInformation>`:
                The vendorInformation
        """
        if "vendorInformation" in self._prop_dict:
            if isinstance(self._prop_dict["vendorInformation"], OneDriveObjectBase):
                return self._prop_dict["vendorInformation"]
            else :
                self._prop_dict["vendorInformation"] = SecurityVendorInformation(self._prop_dict["vendorInformation"])
                return self._prop_dict["vendorInformation"]

        return None

    @vendor_information.setter
    def vendor_information(self, val):
        self._prop_dict["vendorInformation"] = val

