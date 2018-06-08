# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_synchronization_customizations import EducationSynchronizationCustomizations
from ..one_drive_object_base import OneDriveObjectBase


class EducationCsvDataProvider(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def customizations(self):
        """
        Gets and sets the customizations
        
        Returns: 
            :class:`EducationSynchronizationCustomizations<onedrivesdk.model.education_synchronization_customizations.EducationSynchronizationCustomizations>`:
                The customizations
        """
        if "customizations" in self._prop_dict:
            if isinstance(self._prop_dict["customizations"], OneDriveObjectBase):
                return self._prop_dict["customizations"]
            else :
                self._prop_dict["customizations"] = EducationSynchronizationCustomizations(self._prop_dict["customizations"])
                return self._prop_dict["customizations"]

        return None

    @customizations.setter
    def customizations(self, val):
        self._prop_dict["customizations"] = val
