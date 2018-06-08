# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.identity_set import IdentitySet
from ..model.physical_address import PhysicalAddress
from ..model.education_class import EducationClass
from ..model.education_user import EducationUser
from ..model.administrative_unit import AdministrativeUnit
from ..one_drive_object_base import OneDriveObjectBase


class EducationSchool(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def principal_email(self):
        """
        Gets and sets the principalEmail
        
        Returns:
            str:
                The principalEmail
        """
        if "principalEmail" in self._prop_dict:
            return self._prop_dict["principalEmail"]
        else:
            return None

    @principal_email.setter
    def principal_email(self, val):
        self._prop_dict["principalEmail"] = val

    @property
    def principal_name(self):
        """
        Gets and sets the principalName
        
        Returns:
            str:
                The principalName
        """
        if "principalName" in self._prop_dict:
            return self._prop_dict["principalName"]
        else:
            return None

    @principal_name.setter
    def principal_name(self, val):
        self._prop_dict["principalName"] = val

    @property
    def external_principal_id(self):
        """
        Gets and sets the externalPrincipalId
        
        Returns:
            str:
                The externalPrincipalId
        """
        if "externalPrincipalId" in self._prop_dict:
            return self._prop_dict["externalPrincipalId"]
        else:
            return None

    @external_principal_id.setter
    def external_principal_id(self, val):
        self._prop_dict["externalPrincipalId"] = val

    @property
    def lowest_grade(self):
        """
        Gets and sets the lowestGrade
        
        Returns:
            str:
                The lowestGrade
        """
        if "lowestGrade" in self._prop_dict:
            return self._prop_dict["lowestGrade"]
        else:
            return None

    @lowest_grade.setter
    def lowest_grade(self, val):
        self._prop_dict["lowestGrade"] = val

    @property
    def highest_grade(self):
        """
        Gets and sets the highestGrade
        
        Returns:
            str:
                The highestGrade
        """
        if "highestGrade" in self._prop_dict:
            return self._prop_dict["highestGrade"]
        else:
            return None

    @highest_grade.setter
    def highest_grade(self, val):
        self._prop_dict["highestGrade"] = val

    @property
    def school_number(self):
        """
        Gets and sets the schoolNumber
        
        Returns:
            str:
                The schoolNumber
        """
        if "schoolNumber" in self._prop_dict:
            return self._prop_dict["schoolNumber"]
        else:
            return None

    @school_number.setter
    def school_number(self, val):
        self._prop_dict["schoolNumber"] = val

    @property
    def external_id(self):
        """
        Gets and sets the externalId
        
        Returns:
            str:
                The externalId
        """
        if "externalId" in self._prop_dict:
            return self._prop_dict["externalId"]
        else:
            return None

    @external_id.setter
    def external_id(self, val):
        self._prop_dict["externalId"] = val

    @property
    def phone(self):
        """
        Gets and sets the phone
        
        Returns:
            str:
                The phone
        """
        if "phone" in self._prop_dict:
            return self._prop_dict["phone"]
        else:
            return None

    @phone.setter
    def phone(self, val):
        self._prop_dict["phone"] = val

    @property
    def fax(self):
        """
        Gets and sets the fax
        
        Returns:
            str:
                The fax
        """
        if "fax" in self._prop_dict:
            return self._prop_dict["fax"]
        else:
            return None

    @fax.setter
    def fax(self, val):
        self._prop_dict["fax"] = val

    @property
    def created_by(self):
        """
        Gets and sets the createdBy
        
        Returns: 
            :class:`IdentitySet<onedrivesdk.model.identity_set.IdentitySet>`:
                The createdBy
        """
        if "createdBy" in self._prop_dict:
            if isinstance(self._prop_dict["createdBy"], OneDriveObjectBase):
                return self._prop_dict["createdBy"]
            else :
                self._prop_dict["createdBy"] = IdentitySet(self._prop_dict["createdBy"])
                return self._prop_dict["createdBy"]

        return None

    @created_by.setter
    def created_by(self, val):
        self._prop_dict["createdBy"] = val

    @property
    def address(self):
        """
        Gets and sets the address
        
        Returns: 
            :class:`PhysicalAddress<onedrivesdk.model.physical_address.PhysicalAddress>`:
                The address
        """
        if "address" in self._prop_dict:
            if isinstance(self._prop_dict["address"], OneDriveObjectBase):
                return self._prop_dict["address"]
            else :
                self._prop_dict["address"] = PhysicalAddress(self._prop_dict["address"])
                return self._prop_dict["address"]

        return None

    @address.setter
    def address(self, val):
        self._prop_dict["address"] = val

    @property
    def classes(self):
        """Gets and sets the classes
        
        Returns: 
            :class:`ClassesCollectionPage<onedrivesdk.request.classes_collection.ClassesCollectionPage>`:
                The classes
        """
        if "classes" in self._prop_dict:
            return ClassesCollectionPage(self._prop_dict["classes"])
        else:
            return None

    @property
    def users(self):
        """Gets and sets the users
        
        Returns: 
            :class:`UsersCollectionPage<onedrivesdk.request.users_collection.UsersCollectionPage>`:
                The users
        """
        if "users" in self._prop_dict:
            return UsersCollectionPage(self._prop_dict["users"])
        else:
            return None

    @property
    def administrative_unit(self):
        """
        Gets and sets the administrativeUnit
        
        Returns: 
            :class:`AdministrativeUnit<onedrivesdk.model.administrative_unit.AdministrativeUnit>`:
                The administrativeUnit
        """
        if "administrativeUnit" in self._prop_dict:
            if isinstance(self._prop_dict["administrativeUnit"], OneDriveObjectBase):
                return self._prop_dict["administrativeUnit"]
            else :
                self._prop_dict["administrativeUnit"] = AdministrativeUnit(self._prop_dict["administrativeUnit"])
                return self._prop_dict["administrativeUnit"]

        return None

    @administrative_unit.setter
    def administrative_unit(self, val):
        self._prop_dict["administrativeUnit"] = val

