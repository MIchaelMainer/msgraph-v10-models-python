# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.security_vendor_information import SecurityVendorInformation
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class UserSecurityProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def account_name(self):
        """
        Gets and sets the accountName
        
        Returns:
            str:
                The accountName
        """
        if "accountName" in self._prop_dict:
            return self._prop_dict["accountName"]
        else:
            return None

    @account_name.setter
    def account_name(self, val):
        self._prop_dict["accountName"] = val

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
    def domain_name(self):
        """
        Gets and sets the domainName
        
        Returns:
            str:
                The domainName
        """
        if "domainName" in self._prop_dict:
            return self._prop_dict["domainName"]
        else:
            return None

    @domain_name.setter
    def domain_name(self, val):
        self._prop_dict["domainName"] = val

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
    def on_premises_security_identifier(self):
        """
        Gets and sets the onPremisesSecurityIdentifier
        
        Returns:
            str:
                The onPremisesSecurityIdentifier
        """
        if "onPremisesSecurityIdentifier" in self._prop_dict:
            return self._prop_dict["onPremisesSecurityIdentifier"]
        else:
            return None

    @on_premises_security_identifier.setter
    def on_premises_security_identifier(self, val):
        self._prop_dict["onPremisesSecurityIdentifier"] = val

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
    def user_principal_name(self):
        """
        Gets and sets the userPrincipalName
        
        Returns:
            str:
                The userPrincipalName
        """
        if "userPrincipalName" in self._prop_dict:
            return self._prop_dict["userPrincipalName"]
        else:
            return None

    @user_principal_name.setter
    def user_principal_name(self, val):
        self._prop_dict["userPrincipalName"] = val

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

