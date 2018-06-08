# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Windows10EnrollmentCompletionPageConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def show_installation_progress(self):
        """
        Gets and sets the showInstallationProgress
        
        Returns:
            bool:
                The showInstallationProgress
        """
        if "showInstallationProgress" in self._prop_dict:
            return self._prop_dict["showInstallationProgress"]
        else:
            return None

    @show_installation_progress.setter
    def show_installation_progress(self, val):
        self._prop_dict["showInstallationProgress"] = val

    @property
    def block_device_setup_retry_by_user(self):
        """
        Gets and sets the blockDeviceSetupRetryByUser
        
        Returns:
            bool:
                The blockDeviceSetupRetryByUser
        """
        if "blockDeviceSetupRetryByUser" in self._prop_dict:
            return self._prop_dict["blockDeviceSetupRetryByUser"]
        else:
            return None

    @block_device_setup_retry_by_user.setter
    def block_device_setup_retry_by_user(self, val):
        self._prop_dict["blockDeviceSetupRetryByUser"] = val

    @property
    def allow_device_reset_on_install_failure(self):
        """
        Gets and sets the allowDeviceResetOnInstallFailure
        
        Returns:
            bool:
                The allowDeviceResetOnInstallFailure
        """
        if "allowDeviceResetOnInstallFailure" in self._prop_dict:
            return self._prop_dict["allowDeviceResetOnInstallFailure"]
        else:
            return None

    @allow_device_reset_on_install_failure.setter
    def allow_device_reset_on_install_failure(self, val):
        self._prop_dict["allowDeviceResetOnInstallFailure"] = val

    @property
    def allow_log_collection_on_install_failure(self):
        """
        Gets and sets the allowLogCollectionOnInstallFailure
        
        Returns:
            bool:
                The allowLogCollectionOnInstallFailure
        """
        if "allowLogCollectionOnInstallFailure" in self._prop_dict:
            return self._prop_dict["allowLogCollectionOnInstallFailure"]
        else:
            return None

    @allow_log_collection_on_install_failure.setter
    def allow_log_collection_on_install_failure(self, val):
        self._prop_dict["allowLogCollectionOnInstallFailure"] = val

    @property
    def custom_error_message(self):
        """
        Gets and sets the customErrorMessage
        
        Returns:
            str:
                The customErrorMessage
        """
        if "customErrorMessage" in self._prop_dict:
            return self._prop_dict["customErrorMessage"]
        else:
            return None

    @custom_error_message.setter
    def custom_error_message(self, val):
        self._prop_dict["customErrorMessage"] = val

    @property
    def install_progress_timeout_in_minutes(self):
        """
        Gets and sets the installProgressTimeoutInMinutes
        
        Returns:
            int:
                The installProgressTimeoutInMinutes
        """
        if "installProgressTimeoutInMinutes" in self._prop_dict:
            return self._prop_dict["installProgressTimeoutInMinutes"]
        else:
            return None

    @install_progress_timeout_in_minutes.setter
    def install_progress_timeout_in_minutes(self, val):
        self._prop_dict["installProgressTimeoutInMinutes"] = val

    @property
    def allow_device_use_on_install_failure(self):
        """
        Gets and sets the allowDeviceUseOnInstallFailure
        
        Returns:
            bool:
                The allowDeviceUseOnInstallFailure
        """
        if "allowDeviceUseOnInstallFailure" in self._prop_dict:
            return self._prop_dict["allowDeviceUseOnInstallFailure"]
        else:
            return None

    @allow_device_use_on_install_failure.setter
    def allow_device_use_on_install_failure(self, val):
        self._prop_dict["allowDeviceUseOnInstallFailure"] = val

