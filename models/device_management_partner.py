# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.device_management_partner_tenant_state import DeviceManagementPartnerTenantState
from ..model.device_management_partner_app_type import DeviceManagementPartnerAppType
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DeviceManagementPartner(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def last_heartbeat_date_time(self):
        """
        Gets and sets the lastHeartbeatDateTime
        
        Returns:
            datetime:
                The lastHeartbeatDateTime
        """
        if "lastHeartbeatDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastHeartbeatDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_heartbeat_date_time.setter
    def last_heartbeat_date_time(self, val):
        self._prop_dict["lastHeartbeatDateTime"] = val.isoformat()+"Z"

    @property
    def partner_state(self):
        """
        Gets and sets the partnerState
        
        Returns: 
            :class:`DeviceManagementPartnerTenantState<onedrivesdk.model.device_management_partner_tenant_state.DeviceManagementPartnerTenantState>`:
                The partnerState
        """
        if "partnerState" in self._prop_dict:
            if isinstance(self._prop_dict["partnerState"], OneDriveObjectBase):
                return self._prop_dict["partnerState"]
            else :
                self._prop_dict["partnerState"] = DeviceManagementPartnerTenantState(self._prop_dict["partnerState"])
                return self._prop_dict["partnerState"]

        return None

    @partner_state.setter
    def partner_state(self, val):
        self._prop_dict["partnerState"] = val

    @property
    def partner_app_type(self):
        """
        Gets and sets the partnerAppType
        
        Returns: 
            :class:`DeviceManagementPartnerAppType<onedrivesdk.model.device_management_partner_app_type.DeviceManagementPartnerAppType>`:
                The partnerAppType
        """
        if "partnerAppType" in self._prop_dict:
            if isinstance(self._prop_dict["partnerAppType"], OneDriveObjectBase):
                return self._prop_dict["partnerAppType"]
            else :
                self._prop_dict["partnerAppType"] = DeviceManagementPartnerAppType(self._prop_dict["partnerAppType"])
                return self._prop_dict["partnerAppType"]

        return None

    @partner_app_type.setter
    def partner_app_type(self, val):
        self._prop_dict["partnerAppType"] = val

    @property
    def single_tenant_app_id(self):
        """
        Gets and sets the singleTenantAppId
        
        Returns:
            str:
                The singleTenantAppId
        """
        if "singleTenantAppId" in self._prop_dict:
            return self._prop_dict["singleTenantAppId"]
        else:
            return None

    @single_tenant_app_id.setter
    def single_tenant_app_id(self, val):
        self._prop_dict["singleTenantAppId"] = val

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
    def is_configured(self):
        """
        Gets and sets the isConfigured
        
        Returns:
            bool:
                The isConfigured
        """
        if "isConfigured" in self._prop_dict:
            return self._prop_dict["isConfigured"]
        else:
            return None

    @is_configured.setter
    def is_configured(self, val):
        self._prop_dict["isConfigured"] = val

    @property
    def when_partner_devices_will_be_removed_date_time(self):
        """
        Gets and sets the whenPartnerDevicesWillBeRemovedDateTime
        
        Returns:
            datetime:
                The whenPartnerDevicesWillBeRemovedDateTime
        """
        if "whenPartnerDevicesWillBeRemovedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["whenPartnerDevicesWillBeRemovedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @when_partner_devices_will_be_removed_date_time.setter
    def when_partner_devices_will_be_removed_date_time(self, val):
        self._prop_dict["whenPartnerDevicesWillBeRemovedDateTime"] = val.isoformat()+"Z"

    @property
    def when_partner_devices_will_be_marked_as_non_compliant_date_time(self):
        """
        Gets and sets the whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime
        
        Returns:
            datetime:
                The whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime
        """
        if "whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @when_partner_devices_will_be_marked_as_non_compliant_date_time.setter
    def when_partner_devices_will_be_marked_as_non_compliant_date_time(self, val):
        self._prop_dict["whenPartnerDevicesWillBeMarkedAsNonCompliantDateTime"] = val.isoformat()+"Z"

