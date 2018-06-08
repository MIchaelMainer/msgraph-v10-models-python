# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_package_information import WindowsPackageInformation
from ..one_drive_object_base import OneDriveObjectBase


class WindowsPhone81AppXBundle(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def app_x_package_information_list(self):
        """Gets and sets the appXPackageInformationList
        
        Returns: 
            :class:`AppXPackageInformationListCollectionPage<onedrivesdk.request.app_x_package_information_list_collection.AppXPackageInformationListCollectionPage>`:
                The appXPackageInformationList
        """
        if "appXPackageInformationList" in self._prop_dict:
            return AppXPackageInformationListCollectionPage(self._prop_dict["appXPackageInformationList"])
        else:
            return None

