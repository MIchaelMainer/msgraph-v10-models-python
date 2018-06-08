# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_user_role import EducationUserRole
from ..one_drive_object_base import OneDriveObjectBase


class EducationIdentityDomain(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def applies_to(self):
        """
        Gets and sets the appliesTo
        
        Returns: 
            :class:`EducationUserRole<onedrivesdk.model.education_user_role.EducationUserRole>`:
                The appliesTo
        """
        if "appliesTo" in self._prop_dict:
            if isinstance(self._prop_dict["appliesTo"], OneDriveObjectBase):
                return self._prop_dict["appliesTo"]
            else :
                self._prop_dict["appliesTo"] = EducationUserRole(self._prop_dict["appliesTo"])
                return self._prop_dict["appliesTo"]

        return None

    @applies_to.setter
    def applies_to(self, val):
        self._prop_dict["appliesTo"] = val
    @property
    def name(self):
        """Gets and sets the name
        
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

