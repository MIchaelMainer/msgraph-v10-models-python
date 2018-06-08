# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.education_user_role import EducationUserRole
from ..model.education_external_source import EducationExternalSource
from ..model.physical_address import PhysicalAddress
from ..model.education_student import EducationStudent
from ..model.education_teacher import EducationTeacher
from ..model.identity_set import IdentitySet
from ..model.education_related_contact import EducationRelatedContact
from ..model.assigned_license import AssignedLicense
from ..model.assigned_plan import AssignedPlan
from ..model.password_profile import PasswordProfile
from ..model.provisioned_plan import ProvisionedPlan
from ..model.education_school import EducationSchool
from ..model.education_class import EducationClass
from ..model.user import User
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class EducationUser(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def primary_role(self):
        """
        Gets and sets the primaryRole
        
        Returns: 
            :class:`EducationUserRole<onedrivesdk.model.education_user_role.EducationUserRole>`:
                The primaryRole
        """
        if "primaryRole" in self._prop_dict:
            if isinstance(self._prop_dict["primaryRole"], OneDriveObjectBase):
                return self._prop_dict["primaryRole"]
            else :
                self._prop_dict["primaryRole"] = EducationUserRole(self._prop_dict["primaryRole"])
                return self._prop_dict["primaryRole"]

        return None

    @primary_role.setter
    def primary_role(self, val):
        self._prop_dict["primaryRole"] = val

    @property
    def middle_name(self):
        """
        Gets and sets the middleName
        
        Returns:
            str:
                The middleName
        """
        if "middleName" in self._prop_dict:
            return self._prop_dict["middleName"]
        else:
            return None

    @middle_name.setter
    def middle_name(self, val):
        self._prop_dict["middleName"] = val

    @property
    def external_source(self):
        """
        Gets and sets the externalSource
        
        Returns: 
            :class:`EducationExternalSource<onedrivesdk.model.education_external_source.EducationExternalSource>`:
                The externalSource
        """
        if "externalSource" in self._prop_dict:
            if isinstance(self._prop_dict["externalSource"], OneDriveObjectBase):
                return self._prop_dict["externalSource"]
            else :
                self._prop_dict["externalSource"] = EducationExternalSource(self._prop_dict["externalSource"])
                return self._prop_dict["externalSource"]

        return None

    @external_source.setter
    def external_source(self, val):
        self._prop_dict["externalSource"] = val

    @property
    def residence_address(self):
        """
        Gets and sets the residenceAddress
        
        Returns: 
            :class:`PhysicalAddress<onedrivesdk.model.physical_address.PhysicalAddress>`:
                The residenceAddress
        """
        if "residenceAddress" in self._prop_dict:
            if isinstance(self._prop_dict["residenceAddress"], OneDriveObjectBase):
                return self._prop_dict["residenceAddress"]
            else :
                self._prop_dict["residenceAddress"] = PhysicalAddress(self._prop_dict["residenceAddress"])
                return self._prop_dict["residenceAddress"]

        return None

    @residence_address.setter
    def residence_address(self, val):
        self._prop_dict["residenceAddress"] = val

    @property
    def mailing_address(self):
        """
        Gets and sets the mailingAddress
        
        Returns: 
            :class:`PhysicalAddress<onedrivesdk.model.physical_address.PhysicalAddress>`:
                The mailingAddress
        """
        if "mailingAddress" in self._prop_dict:
            if isinstance(self._prop_dict["mailingAddress"], OneDriveObjectBase):
                return self._prop_dict["mailingAddress"]
            else :
                self._prop_dict["mailingAddress"] = PhysicalAddress(self._prop_dict["mailingAddress"])
                return self._prop_dict["mailingAddress"]

        return None

    @mailing_address.setter
    def mailing_address(self, val):
        self._prop_dict["mailingAddress"] = val

    @property
    def student(self):
        """
        Gets and sets the student
        
        Returns: 
            :class:`EducationStudent<onedrivesdk.model.education_student.EducationStudent>`:
                The student
        """
        if "student" in self._prop_dict:
            if isinstance(self._prop_dict["student"], OneDriveObjectBase):
                return self._prop_dict["student"]
            else :
                self._prop_dict["student"] = EducationStudent(self._prop_dict["student"])
                return self._prop_dict["student"]

        return None

    @student.setter
    def student(self, val):
        self._prop_dict["student"] = val

    @property
    def teacher(self):
        """
        Gets and sets the teacher
        
        Returns: 
            :class:`EducationTeacher<onedrivesdk.model.education_teacher.EducationTeacher>`:
                The teacher
        """
        if "teacher" in self._prop_dict:
            if isinstance(self._prop_dict["teacher"], OneDriveObjectBase):
                return self._prop_dict["teacher"]
            else :
                self._prop_dict["teacher"] = EducationTeacher(self._prop_dict["teacher"])
                return self._prop_dict["teacher"]

        return None

    @teacher.setter
    def teacher(self, val):
        self._prop_dict["teacher"] = val

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
    def related_contacts(self):
        """Gets and sets the relatedContacts
        
        Returns: 
            :class:`RelatedContactsCollectionPage<onedrivesdk.request.related_contacts_collection.RelatedContactsCollectionPage>`:
                The relatedContacts
        """
        if "relatedContacts" in self._prop_dict:
            return RelatedContactsCollectionPage(self._prop_dict["relatedContacts"])
        else:
            return None

    @property
    def account_enabled(self):
        """
        Gets and sets the accountEnabled
        
        Returns:
            bool:
                The accountEnabled
        """
        if "accountEnabled" in self._prop_dict:
            return self._prop_dict["accountEnabled"]
        else:
            return None

    @account_enabled.setter
    def account_enabled(self, val):
        self._prop_dict["accountEnabled"] = val

    @property
    def assigned_licenses(self):
        """Gets and sets the assignedLicenses
        
        Returns: 
            :class:`AssignedLicensesCollectionPage<onedrivesdk.request.assigned_licenses_collection.AssignedLicensesCollectionPage>`:
                The assignedLicenses
        """
        if "assignedLicenses" in self._prop_dict:
            return AssignedLicensesCollectionPage(self._prop_dict["assignedLicenses"])
        else:
            return None

    @property
    def assigned_plans(self):
        """Gets and sets the assignedPlans
        
        Returns: 
            :class:`AssignedPlansCollectionPage<onedrivesdk.request.assigned_plans_collection.AssignedPlansCollectionPage>`:
                The assignedPlans
        """
        if "assignedPlans" in self._prop_dict:
            return AssignedPlansCollectionPage(self._prop_dict["assignedPlans"])
        else:
            return None

    @property
    def business_phones(self):
        """
        Gets and sets the businessPhones
        
        Returns:
            str:
                The businessPhones
        """
        if "businessPhones" in self._prop_dict:
            return self._prop_dict["businessPhones"]
        else:
            return None

    @business_phones.setter
    def business_phones(self, val):
        self._prop_dict["businessPhones"] = val

    @property
    def department(self):
        """
        Gets and sets the department
        
        Returns:
            str:
                The department
        """
        if "department" in self._prop_dict:
            return self._prop_dict["department"]
        else:
            return None

    @department.setter
    def department(self, val):
        self._prop_dict["department"] = val

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
    def given_name(self):
        """
        Gets and sets the givenName
        
        Returns:
            str:
                The givenName
        """
        if "givenName" in self._prop_dict:
            return self._prop_dict["givenName"]
        else:
            return None

    @given_name.setter
    def given_name(self, val):
        self._prop_dict["givenName"] = val

    @property
    def mail(self):
        """
        Gets and sets the mail
        
        Returns:
            str:
                The mail
        """
        if "mail" in self._prop_dict:
            return self._prop_dict["mail"]
        else:
            return None

    @mail.setter
    def mail(self, val):
        self._prop_dict["mail"] = val

    @property
    def mail_nickname(self):
        """
        Gets and sets the mailNickname
        
        Returns:
            str:
                The mailNickname
        """
        if "mailNickname" in self._prop_dict:
            return self._prop_dict["mailNickname"]
        else:
            return None

    @mail_nickname.setter
    def mail_nickname(self, val):
        self._prop_dict["mailNickname"] = val

    @property
    def mobile_phone(self):
        """
        Gets and sets the mobilePhone
        
        Returns:
            str:
                The mobilePhone
        """
        if "mobilePhone" in self._prop_dict:
            return self._prop_dict["mobilePhone"]
        else:
            return None

    @mobile_phone.setter
    def mobile_phone(self, val):
        self._prop_dict["mobilePhone"] = val

    @property
    def password_policies(self):
        """
        Gets and sets the passwordPolicies
        
        Returns:
            str:
                The passwordPolicies
        """
        if "passwordPolicies" in self._prop_dict:
            return self._prop_dict["passwordPolicies"]
        else:
            return None

    @password_policies.setter
    def password_policies(self, val):
        self._prop_dict["passwordPolicies"] = val

    @property
    def password_profile(self):
        """
        Gets and sets the passwordProfile
        
        Returns: 
            :class:`PasswordProfile<onedrivesdk.model.password_profile.PasswordProfile>`:
                The passwordProfile
        """
        if "passwordProfile" in self._prop_dict:
            if isinstance(self._prop_dict["passwordProfile"], OneDriveObjectBase):
                return self._prop_dict["passwordProfile"]
            else :
                self._prop_dict["passwordProfile"] = PasswordProfile(self._prop_dict["passwordProfile"])
                return self._prop_dict["passwordProfile"]

        return None

    @password_profile.setter
    def password_profile(self, val):
        self._prop_dict["passwordProfile"] = val

    @property
    def office_location(self):
        """
        Gets and sets the officeLocation
        
        Returns:
            str:
                The officeLocation
        """
        if "officeLocation" in self._prop_dict:
            return self._prop_dict["officeLocation"]
        else:
            return None

    @office_location.setter
    def office_location(self, val):
        self._prop_dict["officeLocation"] = val

    @property
    def preferred_language(self):
        """
        Gets and sets the preferredLanguage
        
        Returns:
            str:
                The preferredLanguage
        """
        if "preferredLanguage" in self._prop_dict:
            return self._prop_dict["preferredLanguage"]
        else:
            return None

    @preferred_language.setter
    def preferred_language(self, val):
        self._prop_dict["preferredLanguage"] = val

    @property
    def provisioned_plans(self):
        """Gets and sets the provisionedPlans
        
        Returns: 
            :class:`ProvisionedPlansCollectionPage<onedrivesdk.request.provisioned_plans_collection.ProvisionedPlansCollectionPage>`:
                The provisionedPlans
        """
        if "provisionedPlans" in self._prop_dict:
            return ProvisionedPlansCollectionPage(self._prop_dict["provisionedPlans"])
        else:
            return None

    @property
    def refresh_tokens_valid_from_date_time(self):
        """
        Gets and sets the refreshTokensValidFromDateTime
        
        Returns:
            datetime:
                The refreshTokensValidFromDateTime
        """
        if "refreshTokensValidFromDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["refreshTokensValidFromDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @refresh_tokens_valid_from_date_time.setter
    def refresh_tokens_valid_from_date_time(self, val):
        self._prop_dict["refreshTokensValidFromDateTime"] = val.isoformat()+"Z"

    @property
    def show_in_address_list(self):
        """
        Gets and sets the showInAddressList
        
        Returns:
            bool:
                The showInAddressList
        """
        if "showInAddressList" in self._prop_dict:
            return self._prop_dict["showInAddressList"]
        else:
            return None

    @show_in_address_list.setter
    def show_in_address_list(self, val):
        self._prop_dict["showInAddressList"] = val

    @property
    def surname(self):
        """
        Gets and sets the surname
        
        Returns:
            str:
                The surname
        """
        if "surname" in self._prop_dict:
            return self._prop_dict["surname"]
        else:
            return None

    @surname.setter
    def surname(self, val):
        self._prop_dict["surname"] = val

    @property
    def usage_location(self):
        """
        Gets and sets the usageLocation
        
        Returns:
            str:
                The usageLocation
        """
        if "usageLocation" in self._prop_dict:
            return self._prop_dict["usageLocation"]
        else:
            return None

    @usage_location.setter
    def usage_location(self, val):
        self._prop_dict["usageLocation"] = val

    @property
    def user_principal_name(self):
        """
        Gets and sets the userPrincipalName
        
        Returns:
            str:
                The userPrincipalName
        """
        if "userPrincipalName" in self._prop_dict:
            return self._prop_dict["userPrincipalName"]
        else:
            return None

    @user_principal_name.setter
    def user_principal_name(self, val):
        self._prop_dict["userPrincipalName"] = val

    @property
    def user_type(self):
        """
        Gets and sets the userType
        
        Returns:
            str:
                The userType
        """
        if "userType" in self._prop_dict:
            return self._prop_dict["userType"]
        else:
            return None

    @user_type.setter
    def user_type(self, val):
        self._prop_dict["userType"] = val

    @property
    def schools(self):
        """Gets and sets the schools
        
        Returns: 
            :class:`SchoolsCollectionPage<onedrivesdk.request.schools_collection.SchoolsCollectionPage>`:
                The schools
        """
        if "schools" in self._prop_dict:
            return SchoolsCollectionPage(self._prop_dict["schools"])
        else:
            return None

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
    def user(self):
        """
        Gets and sets the user
        
        Returns: 
            :class:`User<onedrivesdk.model.user.User>`:
                The user
        """
        if "user" in self._prop_dict:
            if isinstance(self._prop_dict["user"], OneDriveObjectBase):
                return self._prop_dict["user"]
            else :
                self._prop_dict["user"] = User(self._prop_dict["user"])
                return self._prop_dict["user"]

        return None

    @user.setter
    def user(self, val):
        self._prop_dict["user"] = val

