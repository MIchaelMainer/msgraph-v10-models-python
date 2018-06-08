# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.managed_app_flagged_reason import ManagedAppFlaggedReason
from ..model.mobile_app_identifier import MobileAppIdentifier
from ..model.managed_app_policy import ManagedAppPolicy
from ..model.managed_app_operation import ManagedAppOperation
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ManagedAppRegistration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def last_sync_date_time(self):
        """
        Gets and sets the lastSyncDateTime
        
        Returns:
            datetime:
                The lastSyncDateTime
        """
        if "lastSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_sync_date_time.setter
    def last_sync_date_time(self, val):
        self._prop_dict["lastSyncDateTime"] = val.isoformat()+"Z"

    @property
    def application_version(self):
        """
        Gets and sets the applicationVersion
        
        Returns:
            str:
                The applicationVersion
        """
        if "applicationVersion" in self._prop_dict:
            return self._prop_dict["applicationVersion"]
        else:
            return None

    @application_version.setter
    def application_version(self, val):
        self._prop_dict["applicationVersion"] = val

    @property
    def management_sdk_version(self):
        """
        Gets and sets the managementSdkVersion
        
        Returns:
            str:
                The managementSdkVersion
        """
        if "managementSdkVersion" in self._prop_dict:
            return self._prop_dict["managementSdkVersion"]
        else:
            return None

    @management_sdk_version.setter
    def management_sdk_version(self, val):
        self._prop_dict["managementSdkVersion"] = val

    @property
    def platform_version(self):
        """
        Gets and sets the platformVersion
        
        Returns:
            str:
                The platformVersion
        """
        if "platformVersion" in self._prop_dict:
            return self._prop_dict["platformVersion"]
        else:
            return None

    @platform_version.setter
    def platform_version(self, val):
        self._prop_dict["platformVersion"] = val

    @property
    def device_type(self):
        """
        Gets and sets the deviceType
        
        Returns:
            str:
                The deviceType
        """
        if "deviceType" in self._prop_dict:
            return self._prop_dict["deviceType"]
        else:
            return None

    @device_type.setter
    def device_type(self, val):
        self._prop_dict["deviceType"] = val

    @property
    def device_tag(self):
        """
        Gets and sets the deviceTag
        
        Returns:
            str:
                The deviceTag
        """
        if "deviceTag" in self._prop_dict:
            return self._prop_dict["deviceTag"]
        else:
            return None

    @device_tag.setter
    def device_tag(self, val):
        self._prop_dict["deviceTag"] = val

    @property
    def device_name(self):
        """
        Gets and sets the deviceName
        
        Returns:
            str:
                The deviceName
        """
        if "deviceName" in self._prop_dict:
            return self._prop_dict["deviceName"]
        else:
            return None

    @device_name.setter
    def device_name(self, val):
        self._prop_dict["deviceName"] = val

    @property
    def flagged_reasons(self):
        """Gets and sets the flaggedReasons
        
        Returns: 
            :class:`FlaggedReasonsCollectionPage<onedrivesdk.request.flagged_reasons_collection.FlaggedReasonsCollectionPage>`:
                The flaggedReasons
        """
        if "flaggedReasons" in self._prop_dict:
            return FlaggedReasonsCollectionPage(self._prop_dict["flaggedReasons"])
        else:
            return None

    @property
    def user_id(self):
        """
        Gets and sets the userId
        
        Returns:
            str:
                The userId
        """
        if "userId" in self._prop_dict:
            return self._prop_dict["userId"]
        else:
            return None

    @user_id.setter
    def user_id(self, val):
        self._prop_dict["userId"] = val

    @property
    def app_identifier(self):
        """
        Gets and sets the appIdentifier
        
        Returns: 
            :class:`MobileAppIdentifier<onedrivesdk.model.mobile_app_identifier.MobileAppIdentifier>`:
                The appIdentifier
        """
        if "appIdentifier" in self._prop_dict:
            if isinstance(self._prop_dict["appIdentifier"], OneDriveObjectBase):
                return self._prop_dict["appIdentifier"]
            else :
                self._prop_dict["appIdentifier"] = MobileAppIdentifier(self._prop_dict["appIdentifier"])
                return self._prop_dict["appIdentifier"]

        return None

    @app_identifier.setter
    def app_identifier(self, val):
        self._prop_dict["appIdentifier"] = val

    @property
    def version(self):
        """
        Gets and sets the version
        
        Returns:
            str:
                The version
        """
        if "version" in self._prop_dict:
            return self._prop_dict["version"]
        else:
            return None

    @version.setter
    def version(self, val):
        self._prop_dict["version"] = val

    @property
    def applied_policies(self):
        """Gets and sets the appliedPolicies
        
        Returns: 
            :class:`AppliedPoliciesCollectionPage<onedrivesdk.request.applied_policies_collection.AppliedPoliciesCollectionPage>`:
                The appliedPolicies
        """
        if "appliedPolicies" in self._prop_dict:
            return AppliedPoliciesCollectionPage(self._prop_dict["appliedPolicies"])
        else:
            return None

    @property
    def intended_policies(self):
        """Gets and sets the intendedPolicies
        
        Returns: 
            :class:`IntendedPoliciesCollectionPage<onedrivesdk.request.intended_policies_collection.IntendedPoliciesCollectionPage>`:
                The intendedPolicies
        """
        if "intendedPolicies" in self._prop_dict:
            return IntendedPoliciesCollectionPage(self._prop_dict["intendedPolicies"])
        else:
            return None

    @property
    def operations(self):
        """Gets and sets the operations
        
        Returns: 
            :class:`OperationsCollectionPage<onedrivesdk.request.operations_collection.OperationsCollectionPage>`:
                The operations
        """
        if "operations" in self._prop_dict:
            return OperationsCollectionPage(self._prop_dict["operations"])
        else:
            return None

