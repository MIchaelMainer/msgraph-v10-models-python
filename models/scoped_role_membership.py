# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity import Identity
from ..one_drive_object_base import OneDriveObjectBase


class ScopedRoleMembership(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def role_id(self):
        """
        Gets and sets the roleId
        
        Returns:
            str:
                The roleId
        """
        if "roleId" in self._prop_dict:
            return self._prop_dict["roleId"]
        else:
            return None

    @role_id.setter
    def role_id(self, val):
        self._prop_dict["roleId"] = val

    @property
    def administrative_unit_id(self):
        """
        Gets and sets the administrativeUnitId
        
        Returns:
            str:
                The administrativeUnitId
        """
        if "administrativeUnitId" in self._prop_dict:
            return self._prop_dict["administrativeUnitId"]
        else:
            return None

    @administrative_unit_id.setter
    def administrative_unit_id(self, val):
        self._prop_dict["administrativeUnitId"] = val

    @property
    def role_member_info(self):
        """
        Gets and sets the roleMemberInfo
        
        Returns: 
            :class:`Identity<onedrivesdk.model.identity.Identity>`:
                The roleMemberInfo
        """
        if "roleMemberInfo" in self._prop_dict:
            if isinstance(self._prop_dict["roleMemberInfo"], OneDriveObjectBase):
                return self._prop_dict["roleMemberInfo"]
            else :
                self._prop_dict["roleMemberInfo"] = Identity(self._prop_dict["roleMemberInfo"])
                return self._prop_dict["roleMemberInfo"]

        return None

    @role_member_info.setter
    def role_member_info(self, val):
        self._prop_dict["roleMemberInfo"] = val

