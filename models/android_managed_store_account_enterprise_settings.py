# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.android_managed_store_account_bind_status import AndroidManagedStoreAccountBindStatus
from ..model.android_managed_store_account_app_sync_status import AndroidManagedStoreAccountAppSyncStatus
from ..model.android_managed_store_account_enrollment_target import AndroidManagedStoreAccountEnrollmentTarget
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class AndroidManagedStoreAccountEnterpriseSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def bind_status(self):
        """
        Gets and sets the bindStatus
        
        Returns: 
            :class:`AndroidManagedStoreAccountBindStatus<onedrivesdk.model.android_managed_store_account_bind_status.AndroidManagedStoreAccountBindStatus>`:
                The bindStatus
        """
        if "bindStatus" in self._prop_dict:
            if isinstance(self._prop_dict["bindStatus"], OneDriveObjectBase):
                return self._prop_dict["bindStatus"]
            else :
                self._prop_dict["bindStatus"] = AndroidManagedStoreAccountBindStatus(self._prop_dict["bindStatus"])
                return self._prop_dict["bindStatus"]

        return None

    @bind_status.setter
    def bind_status(self, val):
        self._prop_dict["bindStatus"] = val

    @property
    def last_app_sync_date_time(self):
        """
        Gets and sets the lastAppSyncDateTime
        
        Returns:
            datetime:
                The lastAppSyncDateTime
        """
        if "lastAppSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastAppSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_app_sync_date_time.setter
    def last_app_sync_date_time(self, val):
        self._prop_dict["lastAppSyncDateTime"] = val.isoformat()+"Z"

    @property
    def last_app_sync_status(self):
        """
        Gets and sets the lastAppSyncStatus
        
        Returns: 
            :class:`AndroidManagedStoreAccountAppSyncStatus<onedrivesdk.model.android_managed_store_account_app_sync_status.AndroidManagedStoreAccountAppSyncStatus>`:
                The lastAppSyncStatus
        """
        if "lastAppSyncStatus" in self._prop_dict:
            if isinstance(self._prop_dict["lastAppSyncStatus"], OneDriveObjectBase):
                return self._prop_dict["lastAppSyncStatus"]
            else :
                self._prop_dict["lastAppSyncStatus"] = AndroidManagedStoreAccountAppSyncStatus(self._prop_dict["lastAppSyncStatus"])
                return self._prop_dict["lastAppSyncStatus"]

        return None

    @last_app_sync_status.setter
    def last_app_sync_status(self, val):
        self._prop_dict["lastAppSyncStatus"] = val

    @property
    def owner_user_principal_name(self):
        """
        Gets and sets the ownerUserPrincipalName
        
        Returns:
            str:
                The ownerUserPrincipalName
        """
        if "ownerUserPrincipalName" in self._prop_dict:
            return self._prop_dict["ownerUserPrincipalName"]
        else:
            return None

    @owner_user_principal_name.setter
    def owner_user_principal_name(self, val):
        self._prop_dict["ownerUserPrincipalName"] = val

    @property
    def owner_organization_name(self):
        """
        Gets and sets the ownerOrganizationName
        
        Returns:
            str:
                The ownerOrganizationName
        """
        if "ownerOrganizationName" in self._prop_dict:
            return self._prop_dict["ownerOrganizationName"]
        else:
            return None

    @owner_organization_name.setter
    def owner_organization_name(self, val):
        self._prop_dict["ownerOrganizationName"] = val

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
    def enrollment_target(self):
        """
        Gets and sets the enrollmentTarget
        
        Returns: 
            :class:`AndroidManagedStoreAccountEnrollmentTarget<onedrivesdk.model.android_managed_store_account_enrollment_target.AndroidManagedStoreAccountEnrollmentTarget>`:
                The enrollmentTarget
        """
        if "enrollmentTarget" in self._prop_dict:
            if isinstance(self._prop_dict["enrollmentTarget"], OneDriveObjectBase):
                return self._prop_dict["enrollmentTarget"]
            else :
                self._prop_dict["enrollmentTarget"] = AndroidManagedStoreAccountEnrollmentTarget(self._prop_dict["enrollmentTarget"])
                return self._prop_dict["enrollmentTarget"]

        return None

    @enrollment_target.setter
    def enrollment_target(self, val):
        self._prop_dict["enrollmentTarget"] = val

    @property
    def target_group_ids(self):
        """
        Gets and sets the targetGroupIds
        
        Returns:
            str:
                The targetGroupIds
        """
        if "targetGroupIds" in self._prop_dict:
            return self._prop_dict["targetGroupIds"]
        else:
            return None

    @target_group_ids.setter
    def target_group_ids(self, val):
        self._prop_dict["targetGroupIds"] = val

    @property
    def device_owner_management_enabled(self):
        """
        Gets and sets the deviceOwnerManagementEnabled
        
        Returns:
            bool:
                The deviceOwnerManagementEnabled
        """
        if "deviceOwnerManagementEnabled" in self._prop_dict:
            return self._prop_dict["deviceOwnerManagementEnabled"]
        else:
            return None

    @device_owner_management_enabled.setter
    def device_owner_management_enabled(self, val):
        self._prop_dict["deviceOwnerManagementEnabled"] = val

