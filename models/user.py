# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.assigned_license import AssignedLicense
from ..model.assigned_plan import AssignedPlan
from ..model.device_key import DeviceKey
from ..model.on_premises_extension_attributes import OnPremisesExtensionAttributes
from ..model.on_premises_provisioning_error import OnPremisesProvisioningError
from ..model.password_profile import PasswordProfile
from ..model.provisioned_plan import ProvisionedPlan
from ..model.mailbox_settings import MailboxSettings
from ..model.identity_user_risk import IdentityUserRisk
from ..model.extension import Extension
from ..model.directory_object import DirectoryObject
from ..model.scoped_role_membership import ScopedRoleMembership
from ..model.license_details import LicenseDetails
from ..model.user_activity import UserActivity
from ..model.outlook_user import OutlookUser
from ..model.message import Message
from ..model.group import Group
from ..model.mail_folder import MailFolder
from ..model.calendar import Calendar
from ..model.calendar_group import CalendarGroup
from ..model.event import Event
from ..model.person import Person
from ..model.contact import Contact
from ..model.contact_folder import ContactFolder
from ..model.inference_classification import InferenceClassification
from ..model.profile_photo import ProfilePhoto
from ..model.drive import Drive
from ..model.office_graph_insights import OfficeGraphInsights
from ..model.user_settings import UserSettings
from ..model.planner_user import PlannerUser
from ..model.onenote import Onenote
from ..model.managed_device import ManagedDevice
from ..model.device_enrollment_configuration import DeviceEnrollmentConfiguration
from ..model.managed_app_registration import ManagedAppRegistration
from ..model.device import Device
from ..model.device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
from ..model.mobile_app_intent_and_state import MobileAppIntentAndState
from ..model.mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
from ..model.agreement_acceptance import AgreementAcceptance
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class User(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def age_group(self):
        """
        Gets and sets the ageGroup
        
        Returns:
            str:
                The ageGroup
        """
        if "ageGroup" in self._prop_dict:
            return self._prop_dict["ageGroup"]
        else:
            return None

    @age_group.setter
    def age_group(self, val):
        self._prop_dict["ageGroup"] = val

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
    def city(self):
        """
        Gets and sets the city
        
        Returns:
            str:
                The city
        """
        if "city" in self._prop_dict:
            return self._prop_dict["city"]
        else:
            return None

    @city.setter
    def city(self, val):
        self._prop_dict["city"] = val

    @property
    def company_name(self):
        """
        Gets and sets the companyName
        
        Returns:
            str:
                The companyName
        """
        if "companyName" in self._prop_dict:
            return self._prop_dict["companyName"]
        else:
            return None

    @company_name.setter
    def company_name(self, val):
        self._prop_dict["companyName"] = val

    @property
    def consent_provided_for_minor(self):
        """
        Gets and sets the consentProvidedForMinor
        
        Returns:
            str:
                The consentProvidedForMinor
        """
        if "consentProvidedForMinor" in self._prop_dict:
            return self._prop_dict["consentProvidedForMinor"]
        else:
            return None

    @consent_provided_for_minor.setter
    def consent_provided_for_minor(self, val):
        self._prop_dict["consentProvidedForMinor"] = val

    @property
    def country(self):
        """
        Gets and sets the country
        
        Returns:
            str:
                The country
        """
        if "country" in self._prop_dict:
            return self._prop_dict["country"]
        else:
            return None

    @country.setter
    def country(self, val):
        self._prop_dict["country"] = val

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
    def device_keys(self):
        """Gets and sets the deviceKeys
        
        Returns: 
            :class:`DeviceKeysCollectionPage<onedrivesdk.request.device_keys_collection.DeviceKeysCollectionPage>`:
                The deviceKeys
        """
        if "deviceKeys" in self._prop_dict:
            return DeviceKeysCollectionPage(self._prop_dict["deviceKeys"])
        else:
            return None

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
    def employee_id(self):
        """
        Gets and sets the employeeId
        
        Returns:
            str:
                The employeeId
        """
        if "employeeId" in self._prop_dict:
            return self._prop_dict["employeeId"]
        else:
            return None

    @employee_id.setter
    def employee_id(self, val):
        self._prop_dict["employeeId"] = val

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
    def im_addresses(self):
        """
        Gets and sets the imAddresses
        
        Returns:
            str:
                The imAddresses
        """
        if "imAddresses" in self._prop_dict:
            return self._prop_dict["imAddresses"]
        else:
            return None

    @im_addresses.setter
    def im_addresses(self, val):
        self._prop_dict["imAddresses"] = val

    @property
    def job_title(self):
        """
        Gets and sets the jobTitle
        
        Returns:
            str:
                The jobTitle
        """
        if "jobTitle" in self._prop_dict:
            return self._prop_dict["jobTitle"]
        else:
            return None

    @job_title.setter
    def job_title(self, val):
        self._prop_dict["jobTitle"] = val

    @property
    def legal_age_group_classification(self):
        """
        Gets and sets the legalAgeGroupClassification
        
        Returns:
            str:
                The legalAgeGroupClassification
        """
        if "legalAgeGroupClassification" in self._prop_dict:
            return self._prop_dict["legalAgeGroupClassification"]
        else:
            return None

    @legal_age_group_classification.setter
    def legal_age_group_classification(self, val):
        self._prop_dict["legalAgeGroupClassification"] = val

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
    def on_premises_extension_attributes(self):
        """
        Gets and sets the onPremisesExtensionAttributes
        
        Returns: 
            :class:`OnPremisesExtensionAttributes<onedrivesdk.model.on_premises_extension_attributes.OnPremisesExtensionAttributes>`:
                The onPremisesExtensionAttributes
        """
        if "onPremisesExtensionAttributes" in self._prop_dict:
            if isinstance(self._prop_dict["onPremisesExtensionAttributes"], OneDriveObjectBase):
                return self._prop_dict["onPremisesExtensionAttributes"]
            else :
                self._prop_dict["onPremisesExtensionAttributes"] = OnPremisesExtensionAttributes(self._prop_dict["onPremisesExtensionAttributes"])
                return self._prop_dict["onPremisesExtensionAttributes"]

        return None

    @on_premises_extension_attributes.setter
    def on_premises_extension_attributes(self, val):
        self._prop_dict["onPremisesExtensionAttributes"] = val

    @property
    def on_premises_immutable_id(self):
        """
        Gets and sets the onPremisesImmutableId
        
        Returns:
            str:
                The onPremisesImmutableId
        """
        if "onPremisesImmutableId" in self._prop_dict:
            return self._prop_dict["onPremisesImmutableId"]
        else:
            return None

    @on_premises_immutable_id.setter
    def on_premises_immutable_id(self, val):
        self._prop_dict["onPremisesImmutableId"] = val

    @property
    def on_premises_last_sync_date_time(self):
        """
        Gets and sets the onPremisesLastSyncDateTime
        
        Returns:
            datetime:
                The onPremisesLastSyncDateTime
        """
        if "onPremisesLastSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["onPremisesLastSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @on_premises_last_sync_date_time.setter
    def on_premises_last_sync_date_time(self, val):
        self._prop_dict["onPremisesLastSyncDateTime"] = val.isoformat()+"Z"

    @property
    def on_premises_provisioning_errors(self):
        """Gets and sets the onPremisesProvisioningErrors
        
        Returns: 
            :class:`OnPremisesProvisioningErrorsCollectionPage<onedrivesdk.request.on_premises_provisioning_errors_collection.OnPremisesProvisioningErrorsCollectionPage>`:
                The onPremisesProvisioningErrors
        """
        if "onPremisesProvisioningErrors" in self._prop_dict:
            return OnPremisesProvisioningErrorsCollectionPage(self._prop_dict["onPremisesProvisioningErrors"])
        else:
            return None

    @property
    def on_premises_security_identifier(self):
        """
        Gets and sets the onPremisesSecurityIdentifier
        
        Returns:
            str:
                The onPremisesSecurityIdentifier
        """
        if "onPremisesSecurityIdentifier" in self._prop_dict:
            return self._prop_dict["onPremisesSecurityIdentifier"]
        else:
            return None

    @on_premises_security_identifier.setter
    def on_premises_security_identifier(self, val):
        self._prop_dict["onPremisesSecurityIdentifier"] = val

    @property
    def on_premises_sync_enabled(self):
        """
        Gets and sets the onPremisesSyncEnabled
        
        Returns:
            bool:
                The onPremisesSyncEnabled
        """
        if "onPremisesSyncEnabled" in self._prop_dict:
            return self._prop_dict["onPremisesSyncEnabled"]
        else:
            return None

    @on_premises_sync_enabled.setter
    def on_premises_sync_enabled(self, val):
        self._prop_dict["onPremisesSyncEnabled"] = val

    @property
    def on_premises_domain_name(self):
        """
        Gets and sets the onPremisesDomainName
        
        Returns:
            str:
                The onPremisesDomainName
        """
        if "onPremisesDomainName" in self._prop_dict:
            return self._prop_dict["onPremisesDomainName"]
        else:
            return None

    @on_premises_domain_name.setter
    def on_premises_domain_name(self, val):
        self._prop_dict["onPremisesDomainName"] = val

    @property
    def on_premises_sam_account_name(self):
        """
        Gets and sets the onPremisesSamAccountName
        
        Returns:
            str:
                The onPremisesSamAccountName
        """
        if "onPremisesSamAccountName" in self._prop_dict:
            return self._prop_dict["onPremisesSamAccountName"]
        else:
            return None

    @on_premises_sam_account_name.setter
    def on_premises_sam_account_name(self, val):
        self._prop_dict["onPremisesSamAccountName"] = val

    @property
    def on_premises_user_principal_name(self):
        """
        Gets and sets the onPremisesUserPrincipalName
        
        Returns:
            str:
                The onPremisesUserPrincipalName
        """
        if "onPremisesUserPrincipalName" in self._prop_dict:
            return self._prop_dict["onPremisesUserPrincipalName"]
        else:
            return None

    @on_premises_user_principal_name.setter
    def on_premises_user_principal_name(self, val):
        self._prop_dict["onPremisesUserPrincipalName"] = val

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
    def postal_code(self):
        """
        Gets and sets the postalCode
        
        Returns:
            str:
                The postalCode
        """
        if "postalCode" in self._prop_dict:
            return self._prop_dict["postalCode"]
        else:
            return None

    @postal_code.setter
    def postal_code(self, val):
        self._prop_dict["postalCode"] = val

    @property
    def preferred_data_location(self):
        """
        Gets and sets the preferredDataLocation
        
        Returns:
            str:
                The preferredDataLocation
        """
        if "preferredDataLocation" in self._prop_dict:
            return self._prop_dict["preferredDataLocation"]
        else:
            return None

    @preferred_data_location.setter
    def preferred_data_location(self, val):
        self._prop_dict["preferredDataLocation"] = val

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
    def proxy_addresses(self):
        """
        Gets and sets the proxyAddresses
        
        Returns:
            str:
                The proxyAddresses
        """
        if "proxyAddresses" in self._prop_dict:
            return self._prop_dict["proxyAddresses"]
        else:
            return None

    @proxy_addresses.setter
    def proxy_addresses(self, val):
        self._prop_dict["proxyAddresses"] = val

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
    def state(self):
        """
        Gets and sets the state
        
        Returns:
            str:
                The state
        """
        if "state" in self._prop_dict:
            return self._prop_dict["state"]
        else:
            return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def street_address(self):
        """
        Gets and sets the streetAddress
        
        Returns:
            str:
                The streetAddress
        """
        if "streetAddress" in self._prop_dict:
            return self._prop_dict["streetAddress"]
        else:
            return None

    @street_address.setter
    def street_address(self, val):
        self._prop_dict["streetAddress"] = val

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
    def mailbox_settings(self):
        """
        Gets and sets the mailboxSettings
        
        Returns: 
            :class:`MailboxSettings<onedrivesdk.model.mailbox_settings.MailboxSettings>`:
                The mailboxSettings
        """
        if "mailboxSettings" in self._prop_dict:
            if isinstance(self._prop_dict["mailboxSettings"], OneDriveObjectBase):
                return self._prop_dict["mailboxSettings"]
            else :
                self._prop_dict["mailboxSettings"] = MailboxSettings(self._prop_dict["mailboxSettings"])
                return self._prop_dict["mailboxSettings"]

        return None

    @mailbox_settings.setter
    def mailbox_settings(self, val):
        self._prop_dict["mailboxSettings"] = val

    @property
    def about_me(self):
        """
        Gets and sets the aboutMe
        
        Returns:
            str:
                The aboutMe
        """
        if "aboutMe" in self._prop_dict:
            return self._prop_dict["aboutMe"]
        else:
            return None

    @about_me.setter
    def about_me(self, val):
        self._prop_dict["aboutMe"] = val

    @property
    def birthday(self):
        """
        Gets and sets the birthday
        
        Returns:
            datetime:
                The birthday
        """
        if "birthday" in self._prop_dict:
            return datetime.strptime(self._prop_dict["birthday"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @birthday.setter
    def birthday(self, val):
        self._prop_dict["birthday"] = val.isoformat()+"Z"

    @property
    def hire_date(self):
        """
        Gets and sets the hireDate
        
        Returns:
            datetime:
                The hireDate
        """
        if "hireDate" in self._prop_dict:
            return datetime.strptime(self._prop_dict["hireDate"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @hire_date.setter
    def hire_date(self, val):
        self._prop_dict["hireDate"] = val.isoformat()+"Z"

    @property
    def interests(self):
        """
        Gets and sets the interests
        
        Returns:
            str:
                The interests
        """
        if "interests" in self._prop_dict:
            return self._prop_dict["interests"]
        else:
            return None

    @interests.setter
    def interests(self, val):
        self._prop_dict["interests"] = val

    @property
    def my_site(self):
        """
        Gets and sets the mySite
        
        Returns:
            str:
                The mySite
        """
        if "mySite" in self._prop_dict:
            return self._prop_dict["mySite"]
        else:
            return None

    @my_site.setter
    def my_site(self, val):
        self._prop_dict["mySite"] = val

    @property
    def past_projects(self):
        """
        Gets and sets the pastProjects
        
        Returns:
            str:
                The pastProjects
        """
        if "pastProjects" in self._prop_dict:
            return self._prop_dict["pastProjects"]
        else:
            return None

    @past_projects.setter
    def past_projects(self, val):
        self._prop_dict["pastProjects"] = val

    @property
    def preferred_name(self):
        """
        Gets and sets the preferredName
        
        Returns:
            str:
                The preferredName
        """
        if "preferredName" in self._prop_dict:
            return self._prop_dict["preferredName"]
        else:
            return None

    @preferred_name.setter
    def preferred_name(self, val):
        self._prop_dict["preferredName"] = val

    @property
    def responsibilities(self):
        """
        Gets and sets the responsibilities
        
        Returns:
            str:
                The responsibilities
        """
        if "responsibilities" in self._prop_dict:
            return self._prop_dict["responsibilities"]
        else:
            return None

    @responsibilities.setter
    def responsibilities(self, val):
        self._prop_dict["responsibilities"] = val

    @property
    def schools(self):
        """
        Gets and sets the schools
        
        Returns:
            str:
                The schools
        """
        if "schools" in self._prop_dict:
            return self._prop_dict["schools"]
        else:
            return None

    @schools.setter
    def schools(self, val):
        self._prop_dict["schools"] = val

    @property
    def skills(self):
        """
        Gets and sets the skills
        
        Returns:
            str:
                The skills
        """
        if "skills" in self._prop_dict:
            return self._prop_dict["skills"]
        else:
            return None

    @skills.setter
    def skills(self, val):
        self._prop_dict["skills"] = val

    @property
    def identity_user_risk(self):
        """
        Gets and sets the identityUserRisk
        
        Returns: 
            :class:`IdentityUserRisk<onedrivesdk.model.identity_user_risk.IdentityUserRisk>`:
                The identityUserRisk
        """
        if "identityUserRisk" in self._prop_dict:
            if isinstance(self._prop_dict["identityUserRisk"], OneDriveObjectBase):
                return self._prop_dict["identityUserRisk"]
            else :
                self._prop_dict["identityUserRisk"] = IdentityUserRisk(self._prop_dict["identityUserRisk"])
                return self._prop_dict["identityUserRisk"]

        return None

    @identity_user_risk.setter
    def identity_user_risk(self, val):
        self._prop_dict["identityUserRisk"] = val

    @property
    def device_enrollment_limit(self):
        """
        Gets and sets the deviceEnrollmentLimit
        
        Returns:
            int:
                The deviceEnrollmentLimit
        """
        if "deviceEnrollmentLimit" in self._prop_dict:
            return self._prop_dict["deviceEnrollmentLimit"]
        else:
            return None

    @device_enrollment_limit.setter
    def device_enrollment_limit(self, val):
        self._prop_dict["deviceEnrollmentLimit"] = val

    @property
    def extensions(self):
        """Gets and sets the extensions
        
        Returns: 
            :class:`ExtensionsCollectionPage<onedrivesdk.request.extensions_collection.ExtensionsCollectionPage>`:
                The extensions
        """
        if "extensions" in self._prop_dict:
            return ExtensionsCollectionPage(self._prop_dict["extensions"])
        else:
            return None

    @property
    def owned_devices(self):
        """Gets and sets the ownedDevices
        
        Returns: 
            :class:`OwnedDevicesCollectionPage<onedrivesdk.request.owned_devices_collection.OwnedDevicesCollectionPage>`:
                The ownedDevices
        """
        if "ownedDevices" in self._prop_dict:
            return OwnedDevicesCollectionPage(self._prop_dict["ownedDevices"])
        else:
            return None

    @property
    def registered_devices(self):
        """Gets and sets the registeredDevices
        
        Returns: 
            :class:`RegisteredDevicesCollectionPage<onedrivesdk.request.registered_devices_collection.RegisteredDevicesCollectionPage>`:
                The registeredDevices
        """
        if "registeredDevices" in self._prop_dict:
            return RegisteredDevicesCollectionPage(self._prop_dict["registeredDevices"])
        else:
            return None

    @property
    def manager(self):
        """
        Gets and sets the manager
        
        Returns: 
            :class:`DirectoryObject<onedrivesdk.model.directory_object.DirectoryObject>`:
                The manager
        """
        if "manager" in self._prop_dict:
            if isinstance(self._prop_dict["manager"], OneDriveObjectBase):
                return self._prop_dict["manager"]
            else :
                self._prop_dict["manager"] = DirectoryObject(self._prop_dict["manager"])
                return self._prop_dict["manager"]

        return None

    @manager.setter
    def manager(self, val):
        self._prop_dict["manager"] = val

    @property
    def direct_reports(self):
        """Gets and sets the directReports
        
        Returns: 
            :class:`DirectReportsCollectionPage<onedrivesdk.request.direct_reports_collection.DirectReportsCollectionPage>`:
                The directReports
        """
        if "directReports" in self._prop_dict:
            return DirectReportsCollectionPage(self._prop_dict["directReports"])
        else:
            return None

    @property
    def member_of(self):
        """Gets and sets the memberOf
        
        Returns: 
            :class:`MemberOfCollectionPage<onedrivesdk.request.member_of_collection.MemberOfCollectionPage>`:
                The memberOf
        """
        if "memberOf" in self._prop_dict:
            return MemberOfCollectionPage(self._prop_dict["memberOf"])
        else:
            return None

    @property
    def created_objects(self):
        """Gets and sets the createdObjects
        
        Returns: 
            :class:`CreatedObjectsCollectionPage<onedrivesdk.request.created_objects_collection.CreatedObjectsCollectionPage>`:
                The createdObjects
        """
        if "createdObjects" in self._prop_dict:
            return CreatedObjectsCollectionPage(self._prop_dict["createdObjects"])
        else:
            return None

    @property
    def owned_objects(self):
        """Gets and sets the ownedObjects
        
        Returns: 
            :class:`OwnedObjectsCollectionPage<onedrivesdk.request.owned_objects_collection.OwnedObjectsCollectionPage>`:
                The ownedObjects
        """
        if "ownedObjects" in self._prop_dict:
            return OwnedObjectsCollectionPage(self._prop_dict["ownedObjects"])
        else:
            return None

    @property
    def scoped_role_member_of(self):
        """Gets and sets the scopedRoleMemberOf
        
        Returns: 
            :class:`ScopedRoleMemberOfCollectionPage<onedrivesdk.request.scoped_role_member_of_collection.ScopedRoleMemberOfCollectionPage>`:
                The scopedRoleMemberOf
        """
        if "scopedRoleMemberOf" in self._prop_dict:
            return ScopedRoleMemberOfCollectionPage(self._prop_dict["scopedRoleMemberOf"])
        else:
            return None

    @property
    def license_details(self):
        """Gets and sets the licenseDetails
        
        Returns: 
            :class:`LicenseDetailsCollectionPage<onedrivesdk.request.license_details_collection.LicenseDetailsCollectionPage>`:
                The licenseDetails
        """
        if "licenseDetails" in self._prop_dict:
            return LicenseDetailsCollectionPage(self._prop_dict["licenseDetails"])
        else:
            return None

    @property
    def activities(self):
        """Gets and sets the activities
        
        Returns: 
            :class:`ActivitiesCollectionPage<onedrivesdk.request.activities_collection.ActivitiesCollectionPage>`:
                The activities
        """
        if "activities" in self._prop_dict:
            return ActivitiesCollectionPage(self._prop_dict["activities"])
        else:
            return None

    @property
    def outlook(self):
        """
        Gets and sets the outlook
        
        Returns: 
            :class:`OutlookUser<onedrivesdk.model.outlook_user.OutlookUser>`:
                The outlook
        """
        if "outlook" in self._prop_dict:
            if isinstance(self._prop_dict["outlook"], OneDriveObjectBase):
                return self._prop_dict["outlook"]
            else :
                self._prop_dict["outlook"] = OutlookUser(self._prop_dict["outlook"])
                return self._prop_dict["outlook"]

        return None

    @outlook.setter
    def outlook(self, val):
        self._prop_dict["outlook"] = val

    @property
    def messages(self):
        """Gets and sets the messages
        
        Returns: 
            :class:`MessagesCollectionPage<onedrivesdk.request.messages_collection.MessagesCollectionPage>`:
                The messages
        """
        if "messages" in self._prop_dict:
            return MessagesCollectionPage(self._prop_dict["messages"])
        else:
            return None

    @property
    def joined_groups(self):
        """Gets and sets the joinedGroups
        
        Returns: 
            :class:`JoinedGroupsCollectionPage<onedrivesdk.request.joined_groups_collection.JoinedGroupsCollectionPage>`:
                The joinedGroups
        """
        if "joinedGroups" in self._prop_dict:
            return JoinedGroupsCollectionPage(self._prop_dict["joinedGroups"])
        else:
            return None

    @property
    def mail_folders(self):
        """Gets and sets the mailFolders
        
        Returns: 
            :class:`MailFoldersCollectionPage<onedrivesdk.request.mail_folders_collection.MailFoldersCollectionPage>`:
                The mailFolders
        """
        if "mailFolders" in self._prop_dict:
            return MailFoldersCollectionPage(self._prop_dict["mailFolders"])
        else:
            return None

    @property
    def calendar(self):
        """
        Gets and sets the calendar
        
        Returns: 
            :class:`Calendar<onedrivesdk.model.calendar.Calendar>`:
                The calendar
        """
        if "calendar" in self._prop_dict:
            if isinstance(self._prop_dict["calendar"], OneDriveObjectBase):
                return self._prop_dict["calendar"]
            else :
                self._prop_dict["calendar"] = Calendar(self._prop_dict["calendar"])
                return self._prop_dict["calendar"]

        return None

    @calendar.setter
    def calendar(self, val):
        self._prop_dict["calendar"] = val

    @property
    def calendars(self):
        """Gets and sets the calendars
        
        Returns: 
            :class:`CalendarsCollectionPage<onedrivesdk.request.calendars_collection.CalendarsCollectionPage>`:
                The calendars
        """
        if "calendars" in self._prop_dict:
            return CalendarsCollectionPage(self._prop_dict["calendars"])
        else:
            return None

    @property
    def calendar_groups(self):
        """Gets and sets the calendarGroups
        
        Returns: 
            :class:`CalendarGroupsCollectionPage<onedrivesdk.request.calendar_groups_collection.CalendarGroupsCollectionPage>`:
                The calendarGroups
        """
        if "calendarGroups" in self._prop_dict:
            return CalendarGroupsCollectionPage(self._prop_dict["calendarGroups"])
        else:
            return None

    @property
    def calendar_view(self):
        """Gets and sets the calendarView
        
        Returns: 
            :class:`CalendarViewCollectionPage<onedrivesdk.request.calendar_view_collection.CalendarViewCollectionPage>`:
                The calendarView
        """
        if "calendarView" in self._prop_dict:
            return CalendarViewCollectionPage(self._prop_dict["calendarView"])
        else:
            return None

    @property
    def events(self):
        """Gets and sets the events
        
        Returns: 
            :class:`EventsCollectionPage<onedrivesdk.request.events_collection.EventsCollectionPage>`:
                The events
        """
        if "events" in self._prop_dict:
            return EventsCollectionPage(self._prop_dict["events"])
        else:
            return None

    @property
    def people(self):
        """Gets and sets the people
        
        Returns: 
            :class:`PeopleCollectionPage<onedrivesdk.request.people_collection.PeopleCollectionPage>`:
                The people
        """
        if "people" in self._prop_dict:
            return PeopleCollectionPage(self._prop_dict["people"])
        else:
            return None

    @property
    def contacts(self):
        """Gets and sets the contacts
        
        Returns: 
            :class:`ContactsCollectionPage<onedrivesdk.request.contacts_collection.ContactsCollectionPage>`:
                The contacts
        """
        if "contacts" in self._prop_dict:
            return ContactsCollectionPage(self._prop_dict["contacts"])
        else:
            return None

    @property
    def contact_folders(self):
        """Gets and sets the contactFolders
        
        Returns: 
            :class:`ContactFoldersCollectionPage<onedrivesdk.request.contact_folders_collection.ContactFoldersCollectionPage>`:
                The contactFolders
        """
        if "contactFolders" in self._prop_dict:
            return ContactFoldersCollectionPage(self._prop_dict["contactFolders"])
        else:
            return None

    @property
    def inference_classification(self):
        """
        Gets and sets the inferenceClassification
        
        Returns: 
            :class:`InferenceClassification<onedrivesdk.model.inference_classification.InferenceClassification>`:
                The inferenceClassification
        """
        if "inferenceClassification" in self._prop_dict:
            if isinstance(self._prop_dict["inferenceClassification"], OneDriveObjectBase):
                return self._prop_dict["inferenceClassification"]
            else :
                self._prop_dict["inferenceClassification"] = InferenceClassification(self._prop_dict["inferenceClassification"])
                return self._prop_dict["inferenceClassification"]

        return None

    @inference_classification.setter
    def inference_classification(self, val):
        self._prop_dict["inferenceClassification"] = val

    @property
    def photo(self):
        """
        Gets and sets the photo
        
        Returns: 
            :class:`ProfilePhoto<onedrivesdk.model.profile_photo.ProfilePhoto>`:
                The photo
        """
        if "photo" in self._prop_dict:
            if isinstance(self._prop_dict["photo"], OneDriveObjectBase):
                return self._prop_dict["photo"]
            else :
                self._prop_dict["photo"] = ProfilePhoto(self._prop_dict["photo"])
                return self._prop_dict["photo"]

        return None

    @photo.setter
    def photo(self, val):
        self._prop_dict["photo"] = val

    @property
    def photos(self):
        """Gets and sets the photos
        
        Returns: 
            :class:`PhotosCollectionPage<onedrivesdk.request.photos_collection.PhotosCollectionPage>`:
                The photos
        """
        if "photos" in self._prop_dict:
            return PhotosCollectionPage(self._prop_dict["photos"])
        else:
            return None

    @property
    def drive(self):
        """
        Gets and sets the drive
        
        Returns: 
            :class:`Drive<onedrivesdk.model.drive.Drive>`:
                The drive
        """
        if "drive" in self._prop_dict:
            if isinstance(self._prop_dict["drive"], OneDriveObjectBase):
                return self._prop_dict["drive"]
            else :
                self._prop_dict["drive"] = Drive(self._prop_dict["drive"])
                return self._prop_dict["drive"]

        return None

    @drive.setter
    def drive(self, val):
        self._prop_dict["drive"] = val

    @property
    def drives(self):
        """Gets and sets the drives
        
        Returns: 
            :class:`DrivesCollectionPage<onedrivesdk.request.drives_collection.DrivesCollectionPage>`:
                The drives
        """
        if "drives" in self._prop_dict:
            return DrivesCollectionPage(self._prop_dict["drives"])
        else:
            return None

    @property
    def insights(self):
        """
        Gets and sets the insights
        
        Returns: 
            :class:`OfficeGraphInsights<onedrivesdk.model.office_graph_insights.OfficeGraphInsights>`:
                The insights
        """
        if "insights" in self._prop_dict:
            if isinstance(self._prop_dict["insights"], OneDriveObjectBase):
                return self._prop_dict["insights"]
            else :
                self._prop_dict["insights"] = OfficeGraphInsights(self._prop_dict["insights"])
                return self._prop_dict["insights"]

        return None

    @insights.setter
    def insights(self, val):
        self._prop_dict["insights"] = val

    @property
    def settings(self):
        """
        Gets and sets the settings
        
        Returns: 
            :class:`UserSettings<onedrivesdk.model.user_settings.UserSettings>`:
                The settings
        """
        if "settings" in self._prop_dict:
            if isinstance(self._prop_dict["settings"], OneDriveObjectBase):
                return self._prop_dict["settings"]
            else :
                self._prop_dict["settings"] = UserSettings(self._prop_dict["settings"])
                return self._prop_dict["settings"]

        return None

    @settings.setter
    def settings(self, val):
        self._prop_dict["settings"] = val

    @property
    def planner(self):
        """
        Gets and sets the planner
        
        Returns: 
            :class:`PlannerUser<onedrivesdk.model.planner_user.PlannerUser>`:
                The planner
        """
        if "planner" in self._prop_dict:
            if isinstance(self._prop_dict["planner"], OneDriveObjectBase):
                return self._prop_dict["planner"]
            else :
                self._prop_dict["planner"] = PlannerUser(self._prop_dict["planner"])
                return self._prop_dict["planner"]

        return None

    @planner.setter
    def planner(self, val):
        self._prop_dict["planner"] = val

    @property
    def onenote(self):
        """
        Gets and sets the onenote
        
        Returns: 
            :class:`Onenote<onedrivesdk.model.onenote.Onenote>`:
                The onenote
        """
        if "onenote" in self._prop_dict:
            if isinstance(self._prop_dict["onenote"], OneDriveObjectBase):
                return self._prop_dict["onenote"]
            else :
                self._prop_dict["onenote"] = Onenote(self._prop_dict["onenote"])
                return self._prop_dict["onenote"]

        return None

    @onenote.setter
    def onenote(self, val):
        self._prop_dict["onenote"] = val

    @property
    def managed_devices(self):
        """Gets and sets the managedDevices
        
        Returns: 
            :class:`ManagedDevicesCollectionPage<onedrivesdk.request.managed_devices_collection.ManagedDevicesCollectionPage>`:
                The managedDevices
        """
        if "managedDevices" in self._prop_dict:
            return ManagedDevicesCollectionPage(self._prop_dict["managedDevices"])
        else:
            return None

    @property
    def device_enrollment_configurations(self):
        """Gets and sets the deviceEnrollmentConfigurations
        
        Returns: 
            :class:`DeviceEnrollmentConfigurationsCollectionPage<onedrivesdk.request.device_enrollment_configurations_collection.DeviceEnrollmentConfigurationsCollectionPage>`:
                The deviceEnrollmentConfigurations
        """
        if "deviceEnrollmentConfigurations" in self._prop_dict:
            return DeviceEnrollmentConfigurationsCollectionPage(self._prop_dict["deviceEnrollmentConfigurations"])
        else:
            return None

    @property
    def managed_app_registrations(self):
        """Gets and sets the managedAppRegistrations
        
        Returns: 
            :class:`ManagedAppRegistrationsCollectionPage<onedrivesdk.request.managed_app_registrations_collection.ManagedAppRegistrationsCollectionPage>`:
                The managedAppRegistrations
        """
        if "managedAppRegistrations" in self._prop_dict:
            return ManagedAppRegistrationsCollectionPage(self._prop_dict["managedAppRegistrations"])
        else:
            return None

    @property
    def devices(self):
        """Gets and sets the devices
        
        Returns: 
            :class:`DevicesCollectionPage<onedrivesdk.request.devices_collection.DevicesCollectionPage>`:
                The devices
        """
        if "devices" in self._prop_dict:
            return DevicesCollectionPage(self._prop_dict["devices"])
        else:
            return None

    @property
    def joined_teams(self):
        """Gets and sets the joinedTeams
        
        Returns: 
            :class:`JoinedTeamsCollectionPage<onedrivesdk.request.joined_teams_collection.JoinedTeamsCollectionPage>`:
                The joinedTeams
        """
        if "joinedTeams" in self._prop_dict:
            return JoinedTeamsCollectionPage(self._prop_dict["joinedTeams"])
        else:
            return None

    @property
    def device_management_troubleshooting_events(self):
        """Gets and sets the deviceManagementTroubleshootingEvents
        
        Returns: 
            :class:`DeviceManagementTroubleshootingEventsCollectionPage<onedrivesdk.request.device_management_troubleshooting_events_collection.DeviceManagementTroubleshootingEventsCollectionPage>`:
                The deviceManagementTroubleshootingEvents
        """
        if "deviceManagementTroubleshootingEvents" in self._prop_dict:
            return DeviceManagementTroubleshootingEventsCollectionPage(self._prop_dict["deviceManagementTroubleshootingEvents"])
        else:
            return None

    @property
    def mobile_app_intent_and_states(self):
        """Gets and sets the mobileAppIntentAndStates
        
        Returns: 
            :class:`MobileAppIntentAndStatesCollectionPage<onedrivesdk.request.mobile_app_intent_and_states_collection.MobileAppIntentAndStatesCollectionPage>`:
                The mobileAppIntentAndStates
        """
        if "mobileAppIntentAndStates" in self._prop_dict:
            return MobileAppIntentAndStatesCollectionPage(self._prop_dict["mobileAppIntentAndStates"])
        else:
            return None

    @property
    def mobile_app_troubleshooting_events(self):
        """Gets and sets the mobileAppTroubleshootingEvents
        
        Returns: 
            :class:`MobileAppTroubleshootingEventsCollectionPage<onedrivesdk.request.mobile_app_troubleshooting_events_collection.MobileAppTroubleshootingEventsCollectionPage>`:
                The mobileAppTroubleshootingEvents
        """
        if "mobileAppTroubleshootingEvents" in self._prop_dict:
            return MobileAppTroubleshootingEventsCollectionPage(self._prop_dict["mobileAppTroubleshootingEvents"])
        else:
            return None

    @property
    def agreement_acceptances(self):
        """Gets and sets the agreementAcceptances
        
        Returns: 
            :class:`AgreementAcceptancesCollectionPage<onedrivesdk.request.agreement_acceptances_collection.AgreementAcceptancesCollectionPage>`:
                The agreementAcceptances
        """
        if "agreementAcceptances" in self._prop_dict:
            return AgreementAcceptancesCollectionPage(self._prop_dict["agreementAcceptances"])
        else:
            return None

