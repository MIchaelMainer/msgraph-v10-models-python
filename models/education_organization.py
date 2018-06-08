# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_external_source import EducationExternalSource
from ..one_drive_object_base import OneDriveObjectBase


class EducationOrganization(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def external_source(self):
        """
        Gets and sets the externalSource
        
        Returns: 
            :class:`EducationExternalSource<onedrivesdk.model.education_external_source.EducationExternalSource>`:
                The externalSource
        """
        if "externalSource" in self._prop_dict:
            if isinstance(self._prop_dict["externalSource"], OneDriveObjectBase):
                return self._prop_dict["externalSource"]
            else :
                self._prop_dict["externalSource"] = EducationExternalSource(self._prop_dict["externalSource"])
                return self._prop_dict["externalSource"]

        return None

    @external_source.setter
    def external_source(self, val):
        self._prop_dict["externalSource"] = val

