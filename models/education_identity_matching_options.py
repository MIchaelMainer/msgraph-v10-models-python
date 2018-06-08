# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_user_role import EducationUserRole
from ..one_drive_object_base import OneDriveObjectBase


class EducationIdentityMatchingOptions(OneDriveObjectBase):

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
    def source_property_name(self):
        """Gets and sets the sourcePropertyName
        
        Returns: 
            str:
                The sourcePropertyName
        """
        if "sourcePropertyName" in self._prop_dict:
            return self._prop_dict["sourcePropertyName"]
        else:
            return None

    @source_property_name.setter
    def source_property_name(self, val):
        self._prop_dict["sourcePropertyName"] = val

    @property
    def target_property_name(self):
        """Gets and sets the targetPropertyName
        
        Returns: 
            str:
                The targetPropertyName
        """
        if "targetPropertyName" in self._prop_dict:
            return self._prop_dict["targetPropertyName"]
        else:
            return None

    @target_property_name.setter
    def target_property_name(self, val):
        self._prop_dict["targetPropertyName"] = val

    @property
    def target_domain(self):
        """Gets and sets the targetDomain
        
        Returns: 
            str:
                The targetDomain
        """
        if "targetDomain" in self._prop_dict:
            return self._prop_dict["targetDomain"]
        else:
            return None

    @target_domain.setter
    def target_domain(self, val):
        self._prop_dict["targetDomain"] = val

