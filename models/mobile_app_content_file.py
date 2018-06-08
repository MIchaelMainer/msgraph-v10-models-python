# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.mobile_app_content_file_upload_state import MobileAppContentFileUploadState
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class MobileAppContentFile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def azure_storage_uri(self):
        """
        Gets and sets the azureStorageUri
        
        Returns:
            str:
                The azureStorageUri
        """
        if "azureStorageUri" in self._prop_dict:
            return self._prop_dict["azureStorageUri"]
        else:
            return None

    @azure_storage_uri.setter
    def azure_storage_uri(self, val):
        self._prop_dict["azureStorageUri"] = val

    @property
    def is_committed(self):
        """
        Gets and sets the isCommitted
        
        Returns:
            bool:
                The isCommitted
        """
        if "isCommitted" in self._prop_dict:
            return self._prop_dict["isCommitted"]
        else:
            return None

    @is_committed.setter
    def is_committed(self, val):
        self._prop_dict["isCommitted"] = val

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime
        
        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def name(self):
        """
        Gets and sets the name
        
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

    @property
    def size(self):
        """
        Gets and sets the size
        
        Returns:
            int:
                The size
        """
        if "size" in self._prop_dict:
            return self._prop_dict["size"]
        else:
            return None

    @size.setter
    def size(self, val):
        self._prop_dict["size"] = val

    @property
    def size_encrypted(self):
        """
        Gets and sets the sizeEncrypted
        
        Returns:
            int:
                The sizeEncrypted
        """
        if "sizeEncrypted" in self._prop_dict:
            return self._prop_dict["sizeEncrypted"]
        else:
            return None

    @size_encrypted.setter
    def size_encrypted(self, val):
        self._prop_dict["sizeEncrypted"] = val

    @property
    def azure_storage_uri_expiration_date_time(self):
        """
        Gets and sets the azureStorageUriExpirationDateTime
        
        Returns:
            datetime:
                The azureStorageUriExpirationDateTime
        """
        if "azureStorageUriExpirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["azureStorageUriExpirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @azure_storage_uri_expiration_date_time.setter
    def azure_storage_uri_expiration_date_time(self, val):
        self._prop_dict["azureStorageUriExpirationDateTime"] = val.isoformat()+"Z"

    @property
    def upload_state(self):
        """
        Gets and sets the uploadState
        
        Returns: 
            :class:`MobileAppContentFileUploadState<onedrivesdk.model.mobile_app_content_file_upload_state.MobileAppContentFileUploadState>`:
                The uploadState
        """
        if "uploadState" in self._prop_dict:
            if isinstance(self._prop_dict["uploadState"], OneDriveObjectBase):
                return self._prop_dict["uploadState"]
            else :
                self._prop_dict["uploadState"] = MobileAppContentFileUploadState(self._prop_dict["uploadState"])
                return self._prop_dict["uploadState"]

        return None

    @upload_state.setter
    def upload_state(self, val):
        self._prop_dict["uploadState"] = val

    @property
    def is_framework_file(self):
        """
        Gets and sets the isFrameworkFile
        
        Returns:
            bool:
                The isFrameworkFile
        """
        if "isFrameworkFile" in self._prop_dict:
            return self._prop_dict["isFrameworkFile"]
        else:
            return None

    @is_framework_file.setter
    def is_framework_file(self, val):
        self._prop_dict["isFrameworkFile"] = val

    @property
    def is_dependency(self):
        """
        Gets and sets the isDependency
        
        Returns:
            bool:
                The isDependency
        """
        if "isDependency" in self._prop_dict:
            return self._prop_dict["isDependency"]
        else:
            return None

    @is_dependency.setter
    def is_dependency(self, val):
        self._prop_dict["isDependency"] = val

