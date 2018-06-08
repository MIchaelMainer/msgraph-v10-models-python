# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.governance_resource import GovernanceResource
from ..model.governance_role_setting import GovernanceRoleSetting
from ..one_drive_object_base import OneDriveObjectBase


class GovernanceRoleDefinition(OneDriveObjectBase):

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
    def external_id(self):
        """
        Gets and sets the externalId
        
        Returns:
            str:
                The externalId
        """
        if "externalId" in self._prop_dict:
            return self._prop_dict["externalId"]
        else:
            return None

    @external_id.setter
    def external_id(self, val):
        self._prop_dict["externalId"] = val

    @property
    def template_id(self):
        """
        Gets and sets the templateId
        
        Returns:
            str:
                The templateId
        """
        if "templateId" in self._prop_dict:
            return self._prop_dict["templateId"]
        else:
            return None

    @template_id.setter
    def template_id(self, val):
        self._prop_dict["templateId"] = val

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

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

    @property
    def role_setting(self):
        """
        Gets and sets the roleSetting
        
        Returns: 
            :class:`GovernanceRoleSetting<onedrivesdk.model.governance_role_setting.GovernanceRoleSetting>`:
                The roleSetting
        """
        if "roleSetting" in self._prop_dict:
            if isinstance(self._prop_dict["roleSetting"], OneDriveObjectBase):
                return self._prop_dict["roleSetting"]
            else :
                self._prop_dict["roleSetting"] = GovernanceRoleSetting(self._prop_dict["roleSetting"])
                return self._prop_dict["roleSetting"]

        return None

    @role_setting.setter
    def role_setting(self, val):
        self._prop_dict["roleSetting"] = val

