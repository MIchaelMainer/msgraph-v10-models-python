# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.office_product_id import OfficeProductId
from ..model.excluded_apps import ExcludedApps
from ..model.office_update_channel import OfficeUpdateChannel
from ..model.windows_architecture import WindowsArchitecture
from ..model.office_suite_install_progress_display_level import OfficeSuiteInstallProgressDisplayLevel
from ..one_drive_object_base import OneDriveObjectBase


class OfficeSuiteApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def auto_accept_eula(self):
        """
        Gets and sets the autoAcceptEula
        
        Returns:
            bool:
                The autoAcceptEula
        """
        if "autoAcceptEula" in self._prop_dict:
            return self._prop_dict["autoAcceptEula"]
        else:
            return None

    @auto_accept_eula.setter
    def auto_accept_eula(self, val):
        self._prop_dict["autoAcceptEula"] = val

    @property
    def product_ids(self):
        """Gets and sets the productIds
        
        Returns: 
            :class:`ProductIdsCollectionPage<onedrivesdk.request.product_ids_collection.ProductIdsCollectionPage>`:
                The productIds
        """
        if "productIds" in self._prop_dict:
            return ProductIdsCollectionPage(self._prop_dict["productIds"])
        else:
            return None

    @property
    def excluded_apps(self):
        """
        Gets and sets the excludedApps
        
        Returns: 
            :class:`ExcludedApps<onedrivesdk.model.excluded_apps.ExcludedApps>`:
                The excludedApps
        """
        if "excludedApps" in self._prop_dict:
            if isinstance(self._prop_dict["excludedApps"], OneDriveObjectBase):
                return self._prop_dict["excludedApps"]
            else :
                self._prop_dict["excludedApps"] = ExcludedApps(self._prop_dict["excludedApps"])
                return self._prop_dict["excludedApps"]

        return None

    @excluded_apps.setter
    def excluded_apps(self, val):
        self._prop_dict["excludedApps"] = val

    @property
    def use_shared_computer_activation(self):
        """
        Gets and sets the useSharedComputerActivation
        
        Returns:
            bool:
                The useSharedComputerActivation
        """
        if "useSharedComputerActivation" in self._prop_dict:
            return self._prop_dict["useSharedComputerActivation"]
        else:
            return None

    @use_shared_computer_activation.setter
    def use_shared_computer_activation(self, val):
        self._prop_dict["useSharedComputerActivation"] = val

    @property
    def update_channel(self):
        """
        Gets and sets the updateChannel
        
        Returns: 
            :class:`OfficeUpdateChannel<onedrivesdk.model.office_update_channel.OfficeUpdateChannel>`:
                The updateChannel
        """
        if "updateChannel" in self._prop_dict:
            if isinstance(self._prop_dict["updateChannel"], OneDriveObjectBase):
                return self._prop_dict["updateChannel"]
            else :
                self._prop_dict["updateChannel"] = OfficeUpdateChannel(self._prop_dict["updateChannel"])
                return self._prop_dict["updateChannel"]

        return None

    @update_channel.setter
    def update_channel(self, val):
        self._prop_dict["updateChannel"] = val

    @property
    def office_platform_architecture(self):
        """
        Gets and sets the officePlatformArchitecture
        
        Returns: 
            :class:`WindowsArchitecture<onedrivesdk.model.windows_architecture.WindowsArchitecture>`:
                The officePlatformArchitecture
        """
        if "officePlatformArchitecture" in self._prop_dict:
            if isinstance(self._prop_dict["officePlatformArchitecture"], OneDriveObjectBase):
                return self._prop_dict["officePlatformArchitecture"]
            else :
                self._prop_dict["officePlatformArchitecture"] = WindowsArchitecture(self._prop_dict["officePlatformArchitecture"])
                return self._prop_dict["officePlatformArchitecture"]

        return None

    @office_platform_architecture.setter
    def office_platform_architecture(self, val):
        self._prop_dict["officePlatformArchitecture"] = val

    @property
    def locales_to_install(self):
        """
        Gets and sets the localesToInstall
        
        Returns:
            str:
                The localesToInstall
        """
        if "localesToInstall" in self._prop_dict:
            return self._prop_dict["localesToInstall"]
        else:
            return None

    @locales_to_install.setter
    def locales_to_install(self, val):
        self._prop_dict["localesToInstall"] = val

    @property
    def install_progress_display_level(self):
        """
        Gets and sets the installProgressDisplayLevel
        
        Returns: 
            :class:`OfficeSuiteInstallProgressDisplayLevel<onedrivesdk.model.office_suite_install_progress_display_level.OfficeSuiteInstallProgressDisplayLevel>`:
                The installProgressDisplayLevel
        """
        if "installProgressDisplayLevel" in self._prop_dict:
            if isinstance(self._prop_dict["installProgressDisplayLevel"], OneDriveObjectBase):
                return self._prop_dict["installProgressDisplayLevel"]
            else :
                self._prop_dict["installProgressDisplayLevel"] = OfficeSuiteInstallProgressDisplayLevel(self._prop_dict["installProgressDisplayLevel"])
                return self._prop_dict["installProgressDisplayLevel"]

        return None

    @install_progress_display_level.setter
    def install_progress_display_level(self, val):
        self._prop_dict["installProgressDisplayLevel"] = val

    @property
    def should_uninstall_older_versions_of_office(self):
        """
        Gets and sets the shouldUninstallOlderVersionsOfOffice
        
        Returns:
            bool:
                The shouldUninstallOlderVersionsOfOffice
        """
        if "shouldUninstallOlderVersionsOfOffice" in self._prop_dict:
            return self._prop_dict["shouldUninstallOlderVersionsOfOffice"]
        else:
            return None

    @should_uninstall_older_versions_of_office.setter
    def should_uninstall_older_versions_of_office(self, val):
        self._prop_dict["shouldUninstallOlderVersionsOfOffice"] = val

