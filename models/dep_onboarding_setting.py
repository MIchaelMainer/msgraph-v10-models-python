# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DepOnboardingSetting(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def apple_identifier(self):
        """
        Gets and sets the appleIdentifier
        
        Returns:
            str:
                The appleIdentifier
        """
        if "appleIdentifier" in self._prop_dict:
            return self._prop_dict["appleIdentifier"]
        else:
            return None

    @apple_identifier.setter
    def apple_identifier(self, val):
        self._prop_dict["appleIdentifier"] = val

    @property
    def token_expiration_date_time(self):
        """
        Gets and sets the tokenExpirationDateTime
        
        Returns:
            datetime:
                The tokenExpirationDateTime
        """
        if "tokenExpirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["tokenExpirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @token_expiration_date_time.setter
    def token_expiration_date_time(self, val):
        self._prop_dict["tokenExpirationDateTime"] = val.isoformat()+"Z"

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

    @property
    def last_successful_sync_date_time(self):
        """
        Gets and sets the lastSuccessfulSyncDateTime
        
        Returns:
            datetime:
                The lastSuccessfulSyncDateTime
        """
        if "lastSuccessfulSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastSuccessfulSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_successful_sync_date_time.setter
    def last_successful_sync_date_time(self, val):
        self._prop_dict["lastSuccessfulSyncDateTime"] = val.isoformat()+"Z"

    @property
    def last_sync_triggered_date_time(self):
        """
        Gets and sets the lastSyncTriggeredDateTime
        
        Returns:
            datetime:
                The lastSyncTriggeredDateTime
        """
        if "lastSyncTriggeredDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastSyncTriggeredDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_sync_triggered_date_time.setter
    def last_sync_triggered_date_time(self, val):
        self._prop_dict["lastSyncTriggeredDateTime"] = val.isoformat()+"Z"

    @property
    def share_token_with_school_data_sync_service(self):
        """
        Gets and sets the shareTokenWithSchoolDataSyncService
        
        Returns:
            bool:
                The shareTokenWithSchoolDataSyncService
        """
        if "shareTokenWithSchoolDataSyncService" in self._prop_dict:
            return self._prop_dict["shareTokenWithSchoolDataSyncService"]
        else:
            return None

    @share_token_with_school_data_sync_service.setter
    def share_token_with_school_data_sync_service(self, val):
        self._prop_dict["shareTokenWithSchoolDataSyncService"] = val

    @property
    def last_sync_error_code(self):
        """
        Gets and sets the lastSyncErrorCode
        
        Returns:
            int:
                The lastSyncErrorCode
        """
        if "lastSyncErrorCode" in self._prop_dict:
            return self._prop_dict["lastSyncErrorCode"]
        else:
            return None

    @last_sync_error_code.setter
    def last_sync_error_code(self, val):
        self._prop_dict["lastSyncErrorCode"] = val

