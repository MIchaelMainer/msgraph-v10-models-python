# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.agreement_file import AgreementFile
from ..one_drive_object_base import OneDriveObjectBase


class Agreement(OneDriveObjectBase):

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
    def is_viewing_before_acceptance_required(self):
        """
        Gets and sets the isViewingBeforeAcceptanceRequired
        
        Returns:
            bool:
                The isViewingBeforeAcceptanceRequired
        """
        if "isViewingBeforeAcceptanceRequired" in self._prop_dict:
            return self._prop_dict["isViewingBeforeAcceptanceRequired"]
        else:
            return None

    @is_viewing_before_acceptance_required.setter
    def is_viewing_before_acceptance_required(self, val):
        self._prop_dict["isViewingBeforeAcceptanceRequired"] = val

    @property
    def files(self):
        """Gets and sets the files
        
        Returns: 
            :class:`FilesCollectionPage<onedrivesdk.request.files_collection.FilesCollectionPage>`:
                The files
        """
        if "files" in self._prop_dict:
            return FilesCollectionPage(self._prop_dict["files"])
        else:
            return None

