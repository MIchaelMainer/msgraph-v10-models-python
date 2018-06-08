# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class MailSearchFolder(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def is_supported(self):
        """
        Gets and sets the isSupported
        
        Returns:
            bool:
                The isSupported
        """
        if "isSupported" in self._prop_dict:
            return self._prop_dict["isSupported"]
        else:
            return None

    @is_supported.setter
    def is_supported(self, val):
        self._prop_dict["isSupported"] = val

    @property
    def include_nested_folders(self):
        """
        Gets and sets the includeNestedFolders
        
        Returns:
            bool:
                The includeNestedFolders
        """
        if "includeNestedFolders" in self._prop_dict:
            return self._prop_dict["includeNestedFolders"]
        else:
            return None

    @include_nested_folders.setter
    def include_nested_folders(self, val):
        self._prop_dict["includeNestedFolders"] = val

    @property
    def source_folder_i_ds(self):
        """
        Gets and sets the sourceFolderIDs
        
        Returns:
            str:
                The sourceFolderIDs
        """
        if "sourceFolderIDs" in self._prop_dict:
            return self._prop_dict["sourceFolderIDs"]
        else:
            return None

    @source_folder_i_ds.setter
    def source_folder_i_ds(self, val):
        self._prop_dict["sourceFolderIDs"] = val

    @property
    def filter_query(self):
        """
        Gets and sets the filterQuery
        
        Returns:
            str:
                The filterQuery
        """
        if "filterQuery" in self._prop_dict:
            return self._prop_dict["filterQuery"]
        else:
            return None

    @filter_query.setter
    def filter_query(self, val):
        self._prop_dict["filterQuery"] = val

