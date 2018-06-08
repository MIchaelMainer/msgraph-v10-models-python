# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.activity_group_state import ActivityGroupState
from ..model.malware_state import MalwareState
from ..model.security_vendor_information import SecurityVendorInformation
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class FileSecurityProfile(OneDriveObjectBase):

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
    def authenticode_hash256(self):
        """
        Gets and sets the authenticodeHash256
        
        Returns:
            str:
                The authenticodeHash256
        """
        if "authenticodeHash256" in self._prop_dict:
            return self._prop_dict["authenticodeHash256"]
        else:
            return None

    @authenticode_hash256.setter
    def authenticode_hash256(self, val):
        self._prop_dict["authenticodeHash256"] = val

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
    def md5(self):
        """
        Gets and sets the md5
        
        Returns:
            str:
                The md5
        """
        if "md5" in self._prop_dict:
            return self._prop_dict["md5"]
        else:
            return None

    @md5.setter
    def md5(self, val):
        self._prop_dict["md5"] = val

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
    def path(self):
        """
        Gets and sets the path
        
        Returns:
            str:
                The path
        """
        if "path" in self._prop_dict:
            return self._prop_dict["path"]
        else:
            return None

    @path.setter
    def path(self, val):
        self._prop_dict["path"] = val

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
    def sha1(self):
        """
        Gets and sets the sha1
        
        Returns:
            str:
                The sha1
        """
        if "sha1" in self._prop_dict:
            return self._prop_dict["sha1"]
        else:
            return None

    @sha1.setter
    def sha1(self, val):
        self._prop_dict["sha1"] = val

    @property
    def sha256(self):
        """
        Gets and sets the sha256
        
        Returns:
            str:
                The sha256
        """
        if "sha256" in self._prop_dict:
            return self._prop_dict["sha256"]
        else:
            return None

    @sha256.setter
    def sha256(self, val):
        self._prop_dict["sha256"] = val

    @property
    def size(self):
        """
        Gets and sets the size
        
        Returns:
            int:
                The size
        """
        if "size" in self._prop_dict:
            return self._prop_dict["size"]
        else:
            return None

    @size.setter
    def size(self, val):
        self._prop_dict["size"] = val

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

