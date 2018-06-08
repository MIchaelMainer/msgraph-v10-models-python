# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_synchronization_data_provider import EducationSynchronizationDataProvider
from ..model.education_identity_synchronization_configuration import EducationIdentitySynchronizationConfiguration
from ..model.education_synchronization_license_assignment import EducationSynchronizationLicenseAssignment
from ..model.education_synchronization_profile_state import EducationSynchronizationProfileState
from ..model.education_synchronization_error import EducationSynchronizationError
from ..model.education_synchronization_profile_status import EducationSynchronizationProfileStatus
from ..one_drive_object_base import OneDriveObjectBase


class EducationSynchronizationProfile(OneDriveObjectBase):

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
    def data_provider(self):
        """
        Gets and sets the dataProvider
        
        Returns: 
            :class:`EducationSynchronizationDataProvider<onedrivesdk.model.education_synchronization_data_provider.EducationSynchronizationDataProvider>`:
                The dataProvider
        """
        if "dataProvider" in self._prop_dict:
            if isinstance(self._prop_dict["dataProvider"], OneDriveObjectBase):
                return self._prop_dict["dataProvider"]
            else :
                self._prop_dict["dataProvider"] = EducationSynchronizationDataProvider(self._prop_dict["dataProvider"])
                return self._prop_dict["dataProvider"]

        return None

    @data_provider.setter
    def data_provider(self, val):
        self._prop_dict["dataProvider"] = val

    @property
    def identity_synchronization_configuration(self):
        """
        Gets and sets the identitySynchronizationConfiguration
        
        Returns: 
            :class:`EducationIdentitySynchronizationConfiguration<onedrivesdk.model.education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration>`:
                The identitySynchronizationConfiguration
        """
        if "identitySynchronizationConfiguration" in self._prop_dict:
            if isinstance(self._prop_dict["identitySynchronizationConfiguration"], OneDriveObjectBase):
                return self._prop_dict["identitySynchronizationConfiguration"]
            else :
                self._prop_dict["identitySynchronizationConfiguration"] = EducationIdentitySynchronizationConfiguration(self._prop_dict["identitySynchronizationConfiguration"])
                return self._prop_dict["identitySynchronizationConfiguration"]

        return None

    @identity_synchronization_configuration.setter
    def identity_synchronization_configuration(self, val):
        self._prop_dict["identitySynchronizationConfiguration"] = val

    @property
    def licenses_to_assign(self):
        """Gets and sets the licensesToAssign
        
        Returns: 
            :class:`LicensesToAssignCollectionPage<onedrivesdk.request.licenses_to_assign_collection.LicensesToAssignCollectionPage>`:
                The licensesToAssign
        """
        if "licensesToAssign" in self._prop_dict:
            return LicensesToAssignCollectionPage(self._prop_dict["licensesToAssign"])
        else:
            return None

    @property
    def state(self):
        """
        Gets and sets the state
        
        Returns: 
            :class:`EducationSynchronizationProfileState<onedrivesdk.model.education_synchronization_profile_state.EducationSynchronizationProfileState>`:
                The state
        """
        if "state" in self._prop_dict:
            if isinstance(self._prop_dict["state"], OneDriveObjectBase):
                return self._prop_dict["state"]
            else :
                self._prop_dict["state"] = EducationSynchronizationProfileState(self._prop_dict["state"])
                return self._prop_dict["state"]

        return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def handle_special_character_constraint(self):
        """
        Gets and sets the handleSpecialCharacterConstraint
        
        Returns:
            bool:
                The handleSpecialCharacterConstraint
        """
        if "handleSpecialCharacterConstraint" in self._prop_dict:
            return self._prop_dict["handleSpecialCharacterConstraint"]
        else:
            return None

    @handle_special_character_constraint.setter
    def handle_special_character_constraint(self, val):
        self._prop_dict["handleSpecialCharacterConstraint"] = val

    @property
    def term_start_date(self):
        """
        Gets and sets the termStartDate
        
        Returns:
            str:
                The termStartDate
        """
        if "termStartDate" in self._prop_dict:
            return self._prop_dict["termStartDate"]
        else:
            return None

    @term_start_date.setter
    def term_start_date(self, val):
        self._prop_dict["termStartDate"] = val

    @property
    def term_end_date(self):
        """
        Gets and sets the termEndDate
        
        Returns:
            str:
                The termEndDate
        """
        if "termEndDate" in self._prop_dict:
            return self._prop_dict["termEndDate"]
        else:
            return None

    @term_end_date.setter
    def term_end_date(self, val):
        self._prop_dict["termEndDate"] = val

    @property
    def date_format(self):
        """
        Gets and sets the dateFormat
        
        Returns:
            str:
                The dateFormat
        """
        if "dateFormat" in self._prop_dict:
            return self._prop_dict["dateFormat"]
        else:
            return None

    @date_format.setter
    def date_format(self, val):
        self._prop_dict["dateFormat"] = val

    @property
    def errors(self):
        """Gets and sets the errors
        
        Returns: 
            :class:`ErrorsCollectionPage<onedrivesdk.request.errors_collection.ErrorsCollectionPage>`:
                The errors
        """
        if "errors" in self._prop_dict:
            return ErrorsCollectionPage(self._prop_dict["errors"])
        else:
            return None

    @property
    def profile_status(self):
        """
        Gets and sets the profileStatus
        
        Returns: 
            :class:`EducationSynchronizationProfileStatus<onedrivesdk.model.education_synchronization_profile_status.EducationSynchronizationProfileStatus>`:
                The profileStatus
        """
        if "profileStatus" in self._prop_dict:
            if isinstance(self._prop_dict["profileStatus"], OneDriveObjectBase):
                return self._prop_dict["profileStatus"]
            else :
                self._prop_dict["profileStatus"] = EducationSynchronizationProfileStatus(self._prop_dict["profileStatus"])
                return self._prop_dict["profileStatus"]

        return None

    @profile_status.setter
    def profile_status(self, val):
        self._prop_dict["profileStatus"] = val

