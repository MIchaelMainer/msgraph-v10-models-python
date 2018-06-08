# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.imported_windows_autopilot_device_identity_import_status import ImportedWindowsAutopilotDeviceIdentityImportStatus
from ..one_drive_object_base import OneDriveObjectBase


class ImportedWindowsAutopilotDeviceIdentityState(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def device_import_status(self):
        """
        Gets and sets the deviceImportStatus
        
        Returns: 
            :class:`ImportedWindowsAutopilotDeviceIdentityImportStatus<onedrivesdk.model.imported_windows_autopilot_device_identity_import_status.ImportedWindowsAutopilotDeviceIdentityImportStatus>`:
                The deviceImportStatus
        """
        if "deviceImportStatus" in self._prop_dict:
            if isinstance(self._prop_dict["deviceImportStatus"], OneDriveObjectBase):
                return self._prop_dict["deviceImportStatus"]
            else :
                self._prop_dict["deviceImportStatus"] = ImportedWindowsAutopilotDeviceIdentityImportStatus(self._prop_dict["deviceImportStatus"])
                return self._prop_dict["deviceImportStatus"]

        return None

    @device_import_status.setter
    def device_import_status(self, val):
        self._prop_dict["deviceImportStatus"] = val
    @property
    def device_registration_id(self):
        """Gets and sets the deviceRegistrationId
        
        Returns: 
            str:
                The deviceRegistrationId
        """
        if "deviceRegistrationId" in self._prop_dict:
            return self._prop_dict["deviceRegistrationId"]
        else:
            return None

    @device_registration_id.setter
    def device_registration_id(self, val):
        self._prop_dict["deviceRegistrationId"] = val

    @property
    def device_error_code(self):
        """Gets and sets the deviceErrorCode
        
        Returns: 
            int:
                The deviceErrorCode
        """
        if "deviceErrorCode" in self._prop_dict:
            return self._prop_dict["deviceErrorCode"]
        else:
            return None

    @device_error_code.setter
    def device_error_code(self, val):
        self._prop_dict["deviceErrorCode"] = val

    @property
    def device_error_name(self):
        """Gets and sets the deviceErrorName
        
        Returns: 
            str:
                The deviceErrorName
        """
        if "deviceErrorName" in self._prop_dict:
            return self._prop_dict["deviceErrorName"]
        else:
            return None

    @device_error_name.setter
    def device_error_name(self, val):
        self._prop_dict["deviceErrorName"] = val

