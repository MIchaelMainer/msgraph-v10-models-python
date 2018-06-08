# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.vpp_token_account_type import VppTokenAccountType
from ..model.vpp_token_state import VppTokenState
from ..model.vpp_token_action_result import VppTokenActionResult
from ..model.vpp_token_sync_status import VppTokenSyncStatus
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class VppToken(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def organization_name(self):
        """
        Gets and sets the organizationName
        
        Returns:
            str:
                The organizationName
        """
        if "organizationName" in self._prop_dict:
            return self._prop_dict["organizationName"]
        else:
            return None

    @organization_name.setter
    def organization_name(self, val):
        self._prop_dict["organizationName"] = val

    @property
    def vpp_token_account_type(self):
        """
        Gets and sets the vppTokenAccountType
        
        Returns: 
            :class:`VppTokenAccountType<onedrivesdk.model.vpp_token_account_type.VppTokenAccountType>`:
                The vppTokenAccountType
        """
        if "vppTokenAccountType" in self._prop_dict:
            if isinstance(self._prop_dict["vppTokenAccountType"], OneDriveObjectBase):
                return self._prop_dict["vppTokenAccountType"]
            else :
                self._prop_dict["vppTokenAccountType"] = VppTokenAccountType(self._prop_dict["vppTokenAccountType"])
                return self._prop_dict["vppTokenAccountType"]

        return None

    @vpp_token_account_type.setter
    def vpp_token_account_type(self, val):
        self._prop_dict["vppTokenAccountType"] = val

    @property
    def apple_id(self):
        """
        Gets and sets the appleId
        
        Returns:
            str:
                The appleId
        """
        if "appleId" in self._prop_dict:
            return self._prop_dict["appleId"]
        else:
            return None

    @apple_id.setter
    def apple_id(self, val):
        self._prop_dict["appleId"] = val

    @property
    def expiration_date_time(self):
        """
        Gets and sets the expirationDateTime
        
        Returns:
            datetime:
                The expirationDateTime
        """
        if "expirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["expirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @expiration_date_time.setter
    def expiration_date_time(self, val):
        self._prop_dict["expirationDateTime"] = val.isoformat()+"Z"

    @property
    def last_sync_date_time(self):
        """
        Gets and sets the lastSyncDateTime
        
        Returns:
            datetime:
                The lastSyncDateTime
        """
        if "lastSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_sync_date_time.setter
    def last_sync_date_time(self, val):
        self._prop_dict["lastSyncDateTime"] = val.isoformat()+"Z"

    @property
    def token(self):
        """
        Gets and sets the token
        
        Returns:
            str:
                The token
        """
        if "token" in self._prop_dict:
            return self._prop_dict["token"]
        else:
            return None

    @token.setter
    def token(self, val):
        self._prop_dict["token"] = val

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
    def state(self):
        """
        Gets and sets the state
        
        Returns: 
            :class:`VppTokenState<onedrivesdk.model.vpp_token_state.VppTokenState>`:
                The state
        """
        if "state" in self._prop_dict:
            if isinstance(self._prop_dict["state"], OneDriveObjectBase):
                return self._prop_dict["state"]
            else :
                self._prop_dict["state"] = VppTokenState(self._prop_dict["state"])
                return self._prop_dict["state"]

        return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def token_action_results(self):
        """Gets and sets the tokenActionResults
        
        Returns: 
            :class:`TokenActionResultsCollectionPage<onedrivesdk.request.token_action_results_collection.TokenActionResultsCollectionPage>`:
                The tokenActionResults
        """
        if "tokenActionResults" in self._prop_dict:
            return TokenActionResultsCollectionPage(self._prop_dict["tokenActionResults"])
        else:
            return None

    @property
    def last_sync_status(self):
        """
        Gets and sets the lastSyncStatus
        
        Returns: 
            :class:`VppTokenSyncStatus<onedrivesdk.model.vpp_token_sync_status.VppTokenSyncStatus>`:
                The lastSyncStatus
        """
        if "lastSyncStatus" in self._prop_dict:
            if isinstance(self._prop_dict["lastSyncStatus"], OneDriveObjectBase):
                return self._prop_dict["lastSyncStatus"]
            else :
                self._prop_dict["lastSyncStatus"] = VppTokenSyncStatus(self._prop_dict["lastSyncStatus"])
                return self._prop_dict["lastSyncStatus"]

        return None

    @last_sync_status.setter
    def last_sync_status(self, val):
        self._prop_dict["lastSyncStatus"] = val

    @property
    def automatically_update_apps(self):
        """
        Gets and sets the automaticallyUpdateApps
        
        Returns:
            bool:
                The automaticallyUpdateApps
        """
        if "automaticallyUpdateApps" in self._prop_dict:
            return self._prop_dict["automaticallyUpdateApps"]
        else:
            return None

    @automatically_update_apps.setter
    def automatically_update_apps(self, val):
        self._prop_dict["automaticallyUpdateApps"] = val

    @property
    def country_or_region(self):
        """
        Gets and sets the countryOrRegion
        
        Returns:
            str:
                The countryOrRegion
        """
        if "countryOrRegion" in self._prop_dict:
            return self._prop_dict["countryOrRegion"]
        else:
            return None

    @country_or_region.setter
    def country_or_region(self, val):
        self._prop_dict["countryOrRegion"] = val

    @property
    def data_sharing_consent_granted(self):
        """
        Gets and sets the dataSharingConsentGranted
        
        Returns:
            bool:
                The dataSharingConsentGranted
        """
        if "dataSharingConsentGranted" in self._prop_dict:
            return self._prop_dict["dataSharingConsentGranted"]
        else:
            return None

    @data_sharing_consent_granted.setter
    def data_sharing_consent_granted(self, val):
        self._prop_dict["dataSharingConsentGranted"] = val

