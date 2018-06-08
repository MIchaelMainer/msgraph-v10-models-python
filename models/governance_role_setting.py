# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.governance_rule_setting import GovernanceRuleSetting
from ..model.governance_role_definition import GovernanceRoleDefinition
from ..model.governance_resource import GovernanceResource
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class GovernanceRoleSetting(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def resource_id(self):
        """
        Gets and sets the resourceId
        
        Returns:
            str:
                The resourceId
        """
        if "resourceId" in self._prop_dict:
            return self._prop_dict["resourceId"]
        else:
            return None

    @resource_id.setter
    def resource_id(self, val):
        self._prop_dict["resourceId"] = val

    @property
    def role_definition_id(self):
        """
        Gets and sets the roleDefinitionId
        
        Returns:
            str:
                The roleDefinitionId
        """
        if "roleDefinitionId" in self._prop_dict:
            return self._prop_dict["roleDefinitionId"]
        else:
            return None

    @role_definition_id.setter
    def role_definition_id(self, val):
        self._prop_dict["roleDefinitionId"] = val

    @property
    def is_default(self):
        """
        Gets and sets the isDefault
        
        Returns:
            bool:
                The isDefault
        """
        if "isDefault" in self._prop_dict:
            return self._prop_dict["isDefault"]
        else:
            return None

    @is_default.setter
    def is_default(self, val):
        self._prop_dict["isDefault"] = val

    @property
    def last_updated_date_time(self):
        """
        Gets and sets the lastUpdatedDateTime
        
        Returns:
            datetime:
                The lastUpdatedDateTime
        """
        if "lastUpdatedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastUpdatedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_updated_date_time.setter
    def last_updated_date_time(self, val):
        self._prop_dict["lastUpdatedDateTime"] = val.isoformat()+"Z"

    @property
    def last_updated_by(self):
        """
        Gets and sets the lastUpdatedBy
        
        Returns:
            str:
                The lastUpdatedBy
        """
        if "lastUpdatedBy" in self._prop_dict:
            return self._prop_dict["lastUpdatedBy"]
        else:
            return None

    @last_updated_by.setter
    def last_updated_by(self, val):
        self._prop_dict["lastUpdatedBy"] = val

    @property
    def admin_eligible_settings(self):
        """Gets and sets the adminEligibleSettings
        
        Returns: 
            :class:`AdminEligibleSettingsCollectionPage<onedrivesdk.request.admin_eligible_settings_collection.AdminEligibleSettingsCollectionPage>`:
                The adminEligibleSettings
        """
        if "adminEligibleSettings" in self._prop_dict:
            return AdminEligibleSettingsCollectionPage(self._prop_dict["adminEligibleSettings"])
        else:
            return None

    @property
    def admin_member_settings(self):
        """Gets and sets the adminMemberSettings
        
        Returns: 
            :class:`AdminMemberSettingsCollectionPage<onedrivesdk.request.admin_member_settings_collection.AdminMemberSettingsCollectionPage>`:
                The adminMemberSettings
        """
        if "adminMemberSettings" in self._prop_dict:
            return AdminMemberSettingsCollectionPage(self._prop_dict["adminMemberSettings"])
        else:
            return None

    @property
    def user_eligible_settings(self):
        """Gets and sets the userEligibleSettings
        
        Returns: 
            :class:`UserEligibleSettingsCollectionPage<onedrivesdk.request.user_eligible_settings_collection.UserEligibleSettingsCollectionPage>`:
                The userEligibleSettings
        """
        if "userEligibleSettings" in self._prop_dict:
            return UserEligibleSettingsCollectionPage(self._prop_dict["userEligibleSettings"])
        else:
            return None

    @property
    def user_member_settings(self):
        """Gets and sets the userMemberSettings
        
        Returns: 
            :class:`UserMemberSettingsCollectionPage<onedrivesdk.request.user_member_settings_collection.UserMemberSettingsCollectionPage>`:
                The userMemberSettings
        """
        if "userMemberSettings" in self._prop_dict:
            return UserMemberSettingsCollectionPage(self._prop_dict["userMemberSettings"])
        else:
            return None

    @property
    def role_definition(self):
        """
        Gets and sets the roleDefinition
        
        Returns: 
            :class:`GovernanceRoleDefinition<onedrivesdk.model.governance_role_definition.GovernanceRoleDefinition>`:
                The roleDefinition
        """
        if "roleDefinition" in self._prop_dict:
            if isinstance(self._prop_dict["roleDefinition"], OneDriveObjectBase):
                return self._prop_dict["roleDefinition"]
            else :
                self._prop_dict["roleDefinition"] = GovernanceRoleDefinition(self._prop_dict["roleDefinition"])
                return self._prop_dict["roleDefinition"]

        return None

    @role_definition.setter
    def role_definition(self, val):
        self._prop_dict["roleDefinition"] = val

    @property
    def resource(self):
        """
        Gets and sets the resource
        
        Returns: 
            :class:`GovernanceResource<onedrivesdk.model.governance_resource.GovernanceResource>`:
                The resource
        """
        if "resource" in self._prop_dict:
            if isinstance(self._prop_dict["resource"], OneDriveObjectBase):
                return self._prop_dict["resource"]
            else :
                self._prop_dict["resource"] = GovernanceResource(self._prop_dict["resource"])
                return self._prop_dict["resource"]

        return None

    @resource.setter
    def resource(self, val):
        self._prop_dict["resource"] = val

