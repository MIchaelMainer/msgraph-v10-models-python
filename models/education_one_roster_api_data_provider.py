# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_synchronization_connection_settings import EducationSynchronizationConnectionSettings
from ..model.education_synchronization_customizations import EducationSynchronizationCustomizations
from ..one_drive_object_base import OneDriveObjectBase


class EducationOneRosterApiDataProvider(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def connection_url(self):
        """Gets and sets the connectionUrl
        
        Returns: 
            str:
                The connectionUrl
        """
        if "connectionUrl" in self._prop_dict:
            return self._prop_dict["connectionUrl"]
        else:
            return None

    @connection_url.setter
    def connection_url(self, val):
        self._prop_dict["connectionUrl"] = val

    @property
    def connection_settings(self):
        """
        Gets and sets the connectionSettings
        
        Returns: 
            :class:`EducationSynchronizationConnectionSettings<onedrivesdk.model.education_synchronization_connection_settings.EducationSynchronizationConnectionSettings>`:
                The connectionSettings
        """
        if "connectionSettings" in self._prop_dict:
            if isinstance(self._prop_dict["connectionSettings"], OneDriveObjectBase):
                return self._prop_dict["connectionSettings"]
            else :
                self._prop_dict["connectionSettings"] = EducationSynchronizationConnectionSettings(self._prop_dict["connectionSettings"])
                return self._prop_dict["connectionSettings"]

        return None

    @connection_settings.setter
    def connection_settings(self, val):
        self._prop_dict["connectionSettings"] = val
    @property
    def schools_ids(self):
        """Gets and sets the schoolsIds
        
        Returns: 
            str:
                The schoolsIds
        """
        if "schoolsIds" in self._prop_dict:
            return self._prop_dict["schoolsIds"]
        else:
            return None

    @schools_ids.setter
    def schools_ids(self, val):
        self._prop_dict["schoolsIds"] = val

    @property
    def provider_name(self):
        """Gets and sets the providerName
        
        Returns: 
            str:
                The providerName
        """
        if "providerName" in self._prop_dict:
            return self._prop_dict["providerName"]
        else:
            return None

    @provider_name.setter
    def provider_name(self, val):
        self._prop_dict["providerName"] = val

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
