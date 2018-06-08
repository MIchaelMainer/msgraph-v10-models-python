# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.activity_group_state import ActivityGroupState
from ..model.malware_state import MalwareState
from ..model.application_permissions_required import ApplicationPermissionsRequired
from ..model.security_vendor_information import SecurityVendorInformation
from ..model.vulnerability_state import VulnerabilityState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ApplicationSecurityProfile(OneDriveObjectBase):

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
    def certificate_thumbprint(self):
        """
        Gets and sets the certificateThumbprint
        
        Returns:
            str:
                The certificateThumbprint
        """
        if "certificateThumbprint" in self._prop_dict:
            return self._prop_dict["certificateThumbprint"]
        else:
            return None

    @certificate_thumbprint.setter
    def certificate_thumbprint(self, val):
        self._prop_dict["certificateThumbprint"] = val

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
    def deployment_package_url(self):
        """
        Gets and sets the deploymentPackageUrl
        
        Returns:
            str:
                The deploymentPackageUrl
        """
        if "deploymentPackageUrl" in self._prop_dict:
            return self._prop_dict["deploymentPackageUrl"]
        else:
            return None

    @deployment_package_url.setter
    def deployment_package_url(self, val):
        self._prop_dict["deploymentPackageUrl"] = val

    @property
    def is_signed(self):
        """
        Gets and sets the isSigned
        
        Returns:
            bool:
                The isSigned
        """
        if "isSigned" in self._prop_dict:
            return self._prop_dict["isSigned"]
        else:
            return None

    @is_signed.setter
    def is_signed(self, val):
        self._prop_dict["isSigned"] = val

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
    def malware_states(self):
        """Gets and sets the malwareStates
        
        Returns: 
            :class:`MalwareStatesCollectionPage<onedrivesdk.request.malware_states_collection.MalwareStatesCollectionPage>`:
                The malwareStates
        """
        if "malwareStates" in self._prop_dict:
            return MalwareStatesCollectionPage(self._prop_dict["malwareStates"])
        else:
            return None

    @property
    def manifest(self):
        """
        Gets and sets the manifest
        
        Returns:
            str:
                The manifest
        """
        if "manifest" in self._prop_dict:
            return self._prop_dict["manifest"]
        else:
            return None

    @manifest.setter
    def manifest(self, val):
        self._prop_dict["manifest"] = val

    @property
    def name(self):
        """
        Gets and sets the name
        
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
    def permissions_required(self):
        """
        Gets and sets the permissionsRequired
        
        Returns: 
            :class:`ApplicationPermissionsRequired<onedrivesdk.model.application_permissions_required.ApplicationPermissionsRequired>`:
                The permissionsRequired
        """
        if "permissionsRequired" in self._prop_dict:
            if isinstance(self._prop_dict["permissionsRequired"], OneDriveObjectBase):
                return self._prop_dict["permissionsRequired"]
            else :
                self._prop_dict["permissionsRequired"] = ApplicationPermissionsRequired(self._prop_dict["permissionsRequired"])
                return self._prop_dict["permissionsRequired"]

        return None

    @permissions_required.setter
    def permissions_required(self, val):
        self._prop_dict["permissionsRequired"] = val

    @property
    def platform(self):
        """
        Gets and sets the platform
        
        Returns:
            str:
                The platform
        """
        if "platform" in self._prop_dict:
            return self._prop_dict["platform"]
        else:
            return None

    @platform.setter
    def platform(self, val):
        self._prop_dict["platform"] = val

    @property
    def publisher(self):
        """
        Gets and sets the publisher
        
        Returns:
            str:
                The publisher
        """
        if "publisher" in self._prop_dict:
            return self._prop_dict["publisher"]
        else:
            return None

    @publisher.setter
    def publisher(self, val):
        self._prop_dict["publisher"] = val

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
    def type(self):
        """
        Gets and sets the type
        
        Returns:
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

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

    @property
    def vulnerability_states(self):
        """Gets and sets the vulnerabilityStates
        
        Returns: 
            :class:`VulnerabilityStatesCollectionPage<onedrivesdk.request.vulnerability_states_collection.VulnerabilityStatesCollectionPage>`:
                The vulnerabilityStates
        """
        if "vulnerabilityStates" in self._prop_dict:
            return VulnerabilityStatesCollectionPage(self._prop_dict["vulnerabilityStates"])
        else:
            return None

