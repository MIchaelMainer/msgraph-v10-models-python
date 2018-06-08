# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.directory_definition import DirectoryDefinition
from ..model.synchronization_rule import SynchronizationRule
from ..one_drive_object_base import OneDriveObjectBase


class SynchronizationSchema(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def directories(self):
        """Gets and sets the directories
        
        Returns: 
            :class:`DirectoriesCollectionPage<onedrivesdk.request.directories_collection.DirectoriesCollectionPage>`:
                The directories
        """
        if "directories" in self._prop_dict:
            return DirectoriesCollectionPage(self._prop_dict["directories"])
        else:
            return None

    @property
    def synchronization_rules(self):
        """Gets and sets the synchronizationRules
        
        Returns: 
            :class:`SynchronizationRulesCollectionPage<onedrivesdk.request.synchronization_rules_collection.SynchronizationRulesCollectionPage>`:
                The synchronizationRules
        """
        if "synchronizationRules" in self._prop_dict:
            return SynchronizationRulesCollectionPage(self._prop_dict["synchronizationRules"])
        else:
            return None

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

