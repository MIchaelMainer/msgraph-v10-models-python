# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_management_exchange_connector_status import DeviceManagementExchangeConnectorStatus
from ..model.device_management_exchange_connector_type import DeviceManagementExchangeConnectorType
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagementExchangeConnector(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`DeviceManagementExchangeConnectorStatus<onedrivesdk.model.device_management_exchange_connector_status.DeviceManagementExchangeConnectorStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = DeviceManagementExchangeConnectorStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def primary_smtp_address(self):
        """
        Gets and sets the primarySmtpAddress
        
        Returns:
            str:
                The primarySmtpAddress
        """
        if "primarySmtpAddress" in self._prop_dict:
            return self._prop_dict["primarySmtpAddress"]
        else:
            return None

    @primary_smtp_address.setter
    def primary_smtp_address(self, val):
        self._prop_dict["primarySmtpAddress"] = val

    @property
    def server_name(self):
        """
        Gets and sets the serverName
        
        Returns:
            str:
                The serverName
        """
        if "serverName" in self._prop_dict:
            return self._prop_dict["serverName"]
        else:
            return None

    @server_name.setter
    def server_name(self, val):
        self._prop_dict["serverName"] = val

    @property
    def exchange_connector_type(self):
        """
        Gets and sets the exchangeConnectorType
        
        Returns: 
            :class:`DeviceManagementExchangeConnectorType<onedrivesdk.model.device_management_exchange_connector_type.DeviceManagementExchangeConnectorType>`:
                The exchangeConnectorType
        """
        if "exchangeConnectorType" in self._prop_dict:
            if isinstance(self._prop_dict["exchangeConnectorType"], OneDriveObjectBase):
                return self._prop_dict["exchangeConnectorType"]
            else :
                self._prop_dict["exchangeConnectorType"] = DeviceManagementExchangeConnectorType(self._prop_dict["exchangeConnectorType"])
                return self._prop_dict["exchangeConnectorType"]

        return None

    @exchange_connector_type.setter
    def exchange_connector_type(self, val):
        self._prop_dict["exchangeConnectorType"] = val

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

    @property
    def exchange_alias(self):
        """
        Gets and sets the exchangeAlias
        
        Returns:
            str:
                The exchangeAlias
        """
        if "exchangeAlias" in self._prop_dict:
            return self._prop_dict["exchangeAlias"]
        else:
            return None

    @exchange_alias.setter
    def exchange_alias(self, val):
        self._prop_dict["exchangeAlias"] = val

    @property
    def exchange_organization(self):
        """
        Gets and sets the exchangeOrganization
        
        Returns:
            str:
                The exchangeOrganization
        """
        if "exchangeOrganization" in self._prop_dict:
            return self._prop_dict["exchangeOrganization"]
        else:
            return None

    @exchange_organization.setter
    def exchange_organization(self, val):
        self._prop_dict["exchangeOrganization"] = val

