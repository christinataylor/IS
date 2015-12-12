
SFUSER = auth.SFUSER
SFPW = auth.SFPW
SF_TOKEN = auth.SF_TOKEN

DBUSER=auth.DBUSER
DBPW=auth.DBPW
DBHOST=auth.DBHOST
DBNAME=auth.DBNAME


program_directory = """/Users/ctaylor/SFDC/"""
user_directory = """/Users/ctaylor/SFDC/"""
project_directory = """/Users/ctaylor/SFDC/"""
account_directory = """/Users/ctaylor/SFDC/"""
opportunity_directory = """/Users/ctaylor/SFDC/"""
lineitem_directory = """/Users/ctaylor/SFDC/"""
product2_directory = """/Users/ctaylor/SFDC/"""
opportunityhistory_directory = """/Users/ctaylor/SFDC/"""
pricebookentry_directory = """/Users/ctaylor/SFDC/"""


USER_FIELD_TYPE_MAP = {
	"sf_id" : "id",
	#"profile_id" : "id",
	"role_name" : "string",
	"name" : "string",
	"email" : "string",
	"profile_name" : "string"
}
USER_FIELD_DICT = {
	"sf_id" : "Id",
	"name" : "Name",
	"email" : "Email",
	#"profile_id" : "ProfileId",
	"role_name" : "UserRole.Name",
	"profile_name" : "Profile.Name"
}

USER_ORDERED_FIELDS = ORDERED_FIELDS = [
	"sf_id",
	"name", 
	"role_name",
	"profile_name",
	"email"]


ACCOUNT_FIELD_TYPE_MAP = {
	"account_id" : "id",
	"client_segment" : "string",
	"account_type" : "string",
	"parent_account_id" : "string", 
	"owner_id" : "id", 
	"name" : "string",
	"type_detail" : "string",
	"geo_region" : "string",
	"business_unit" : "string"
}

ACCOUNT_FIELD_DICT = {
	"account_id" : "Id",
	"client_segment" : "Client_Tier__c",
	"account_type" : "Type",
	"parent_account_id" : "ParentId", 
	"owner_id" : "OwnerId", 
	"name" : "Name",
	"type_detail" : "Type_Detail__c",
	"geo_region" : "Region__c",
	"business_unit" : "Business_Unit__c"
}

ACCOUNT_ORDERED_FIELDS = ["account_id", "client_segment","account_type", "parent_account_id", "owner_id","name","type_detail","geo_region","business_unit"]
	

PROGRAM_FIELD_TYPE_MAP = {
	"program_id" : "id",
	"Account" : "id",
	"Opportunity" : "id",
	"program_owner" : "id",
	"program_type" : "string",
	"program_name" : "string",
	"program_status" : "string",
	"date_start_target" : "datetime",
	"date_live_target" : "datetime",
	"date_start_actual" : "datetime",
	"date_live_estimate" : "datetime",
	"program_home_page" : "string",
	"date_created" : "datetime",
	"date_last_activity" : "datetime",
	"deleted_flag" : "string", 
	"program_SE" : "multivalue_string"
}

PROGRAM_FIELD_DICT = { 
	"program_id" : "Id",
	"Account" : "Account_Program__c",
	"Opportunity" : "Program_Opportunities__c",
	"program_owner" : "Program_Owner__c",
	"program_type" : "Program_Type__c",
	"program_name" : "Name",
	"program_status" : "Program_Status__c",
	"date_start_target" : "Target_Start__c",
	"date_live_target" : "Target_Completion__c",
	"date_start_actual" : "Actual_Program_Start__c",
	"date_live_estimate" : "Actual_Program_Go_Live__c",
	"program_home_page" : "Program_Home_Page__c",
	"date_created" : "CreatedDate",
	"date_last_activity" : "LastActivityDate",
	"deleted_flag" : "IsDeleted",
	"program_SE" : "Program_SE_s__c"
}

PROGRAM_ORDERED_FIELDS = ["program_id","Account","Opportunity","program_owner","program_type","program_name","program_status","date_start_target","date_live_target","date_start_actual","date_live_estimate","program_home_page","date_created","date_last_activity","deleted_flag", "program_SE"]


PROJECT_FIELD_TYPE_MAP = {
	"project_id" : "id",
	"account_id" : "id",
	"opportunity_id" : "id",
	"project_owner_id" : "id",
	"project_type" : "string",
	"project_name" : "string",
	"project_status" : "string",
	"assigned_SE" : "multivalue_string", #; delimited
	"date_start_target" : "datetime",
	"date_live_target" : "datetime",
	"date_start_actual" : "datetime",
	"date_live_estimate" : "datetime",
	"project_home_page" : "string",
	"date_created" : "datetime",
	"date_last_activity" : "datetime",
	"date_last_modified" : "datetime",
	"date_last_referenced" : "datetime",
	"date_last_viewed" : "datetime",
	#"date_system_modified" : "datetime",
	"creator_id" : "id",
	"last_modifier_id" : "id",
	"deleted_flag" : "string"
}

PROJECT_FIELD_DICT = { 
	"project_id" : "Id",
	"account_id" : "Account_ServicesProject__c",
	"opportunity_id" : "Project_Opportunity__c",
	"project_owner_id" : "Services_Project_Owner__c",
	"project_type" : "Services_Project_Type__c",
	"project_name" : "Name",
	"project_status" : "Services_Project_Status__c",
	"assigned_SE" : "Services_Project_SE__c",
	"date_start_target" : "Target_Project_Start__c", #start of gantt when project status == new
	"date_live_target" : "Target_Project_Live__c", #asterick 
	"date_start_actual" : "Actual_Project_Start__c", #start of gantt
	"date_live_estimate" : "Actual_Project_Go_Live__c", #end of gantt
	"project_home_page" : "Services_Project_Home_Page__c",
	"date_created" : "CreatedDate",
	"date_last_activity" : "LastActivityDate",
	"date_last_modified" : "LastModifiedDate",
	"date_last_referenced" : "LastReferencedDate",
	"date_last_viewed" : "LastViewedDate",
	#"date_system_modified" : "SystemModstamp", 
	"creator_id" : "CreatedById",
	"last_modifier_id" : "LastModifiedById",
	"deleted_flag" : "IsDeleted"
}

PROJECT_ORDERED_FIELDS = ["project_id","account_id","opportunity_id","project_owner_id","project_type","project_name","project_status","assigned_SE","date_start_target","date_live_target","date_start_actual","date_live_estimate","project_home_page","date_created","date_last_activity","date_last_modified","date_last_referenced","date_last_viewed", "creator_id","last_modifier_id","deleted_flag"]


OPPORTUNITY_FIELD_TYPE_MAP = {
	"opportunity_id" : "id",
	"deleted" : "string", 
	"account_id" : "id",
	"record_type_id" : "id",
	"name" : "string",
	"description" : "string",
	"stage" : "string",
	"total_deal_amount" : "decimal",
	"probability_percent" : "decimal",
	"close_date" : "datetime",
	"opportunity_type" : "string",
	"won" : "bool",
	"closed" : "bool",
	"owner_id" : "id",
	"created_date" : "datetime",
	"average_revenue_monthly" : "decimal",
	"attach_start" : "datetime",
	"attach_end" : "datetime",
	"deal_term_months" : "int",
	"estimated_live_date" : "datetime",
	"renewal_option" : "string",
	"Renewal_ACV" : "decimal",
	"Upsell_ACV" : "decimal",
	"ACV" : "decimal",
	"TCV" : "decimal", 
	"fourfronts_role" : "string",
	"reason_lost" : "string"
}

OPPORTUNITY_FIELD_DICT = { 
	"opportunity_id" : "Id",
	"deleted" : "IsDeleted", 
	"account_id" : "AccountId",
	"record_type_id" : "RecordTypeId",
	"name" : "Name",
	"description" : "Description",
	"stage" : "StageName",
	"total_deal_amount" : "Amount",
	"probability_percent" : "Probability",
	"close_date" : "CloseDate",
	"opportunity_type" : "Type",
	"won" : "IsWon",
	"closed" : "IsClosed",
	"owner_id" : "OwnerId",
	"created_date" : "CreatedDate",
	"average_revenue_monthly" : "Average_Revenue_monthly__c",
	"attach_start" : "Attach_Start__c",
	"attach_end" : "Attach_End__c",
	"deal_term_months" : "Deal_Term_Months__c",
	"estimated_live_date" : "Live_Date__c",
	"renewal_option" : "Renewal_Option__c",
	"Renewal_ACV" : "Renewal_ACV__c",
	"Upsell_ACV" : "Upsell_ACV__c",
	"ACV" : "Opportunity_ACV__c",
	"TCV" : "Opportunity_TCV__c", 
	"fourfronts_role" : "FourFronts_Role__c",
	"reason_lost" : "Reason_Lost__c"
}

OPPORTUNITY_ORDERED_FIELDS = ['opportunity_id', 
'deleted',
'account_id',
'record_type_id',
'name',
'description',
'stage',
'total_deal_amount',
'probability_percent',
'close_date',
'opportunity_type',
'won',
'closed',
'owner_id',
'created_date',
'average_revenue_monthly',
'attach_start',
'attach_end',
'deal_term_months',
'estimated_live_date',
'renewal_option',
'Renewal_ACV',
'Upsell_ACV',
'ACV',
'TCV',
'fourfronts_role',
'reason_lost']


LINEITEM_FIELD_TYPE_MAP = {
	'lineitem_id' : 'id',
	'opportunity_id' : 'id',
	'price_book_entry_id': 'id', 
	'quantity' : 'decimal',
	'sales_price_legacy' : 'decimal',
	'description' : 'string',
	'last_modified_date' : 'datetime',
	'deleted' : 'string',
	'ACV' : 'decimal',
	'TCV' : 'decimal',
	'product2_id' : 'dummy'
}

LINEITEM_FIELD_DICT = {
	'lineitem_id' : 'Id',
	'opportunity_id' : 'OpportunityId',
	'price_book_entry_id': 'PricebookEntryId', 
	'quantity' : 'Quantity',
	'sales_price_legacy' : 'TotalPrice', #Pricebookentry only has a unitprice. 
	'description' : 'Description',
	'last_modified_date' : 'LastModifiedDate',
	'deleted' : 'IsDeleted',
	'ACV' : 'Product_ACV__c',
	'TCV' : 'Product_TCV__c',
	'product2_id' : 'Advisory_Program_ID__c' #dummy id
}

LINEITEM_ORDERED_FIELDS = [
'lineitem_id',
'opportunity_id',
'price_book_entry_id',
'quantity',
'sales_price_legacy',
'description',
'last_modified_date',
'deleted',
'ACV',
'TCV',
'product2_id']

PRODUCT2_FIELD_TYPE_MAP = {
	'product_id' : 'id',
	'product_name' : 'string',
	'unit_of_measure' : 'string',
	'active' : 'bool',
	'created_date' : 'datetime',
	'created_by_id' : 'string',
	'last_modified_date' : 'datetime',
	'last_modified_by_id' : 'string',
	'product_family' : 'string',
	'deleted' : 'bool'
}

PRODUCT2_FIELD_DICT = {
	'product_id' : 'Id',
	'product_name' : 'Name',
	'unit_of_measure' : 'ProductCode',
	'active' : 'IsActive',
	'created_date' : 'CreatedDate', 
	'created_by_id' : 'CreatedById',
	'last_modified_date' : 'LastModifiedDate',
	'last_modified_by_id' : 'LastModifiedById',
	'product_family' : 'Family',
	'deleted' : 'IsDeleted'
}

PRODUCT2_ORDERED_FIELDS = [
'product_id',
'product_name',
'unit_of_measure',
'active',
'created_date',
'created_by_id',
'last_modified_date',
'last_modified_by_id',
'product_family',
'deleted'
]

PRICEBOOKENTRY_FIELD_TYPE_MAP = {
'Price_book_Entry_Id' : "id",
'Product2_Id' : "id",
'Pricebook2_Id' : "id",
'Name' : "string",
'Product_Code' : "string",
'Unit_Price' : "decimal",
'Use_Standard_Price' : "bool",
'Last_Modified_Date' : "datetime",
'Last_Modified_By_Id' : "id",
'Created_Date' : "datetime",
'Created_By_Id' : "id",
'Is_Deleted' : "bool",
'Is_Active' : "bool"
}

PRICEBOOKENTRY_FIELD_DICT = {
'Price_book_Entry_Id' : "Id",
'Product2_Id' : "Product2Id",
'Pricebook2_Id' : "Pricebook2Id",
'Name' : "Name",
'Product_Code' : "ProductCode",
'Unit_Price' : "UnitPrice",
'Use_Standard_Price' : "UseStandardPrice",
'Last_Modified_Date' : "LastModifiedDate",
'Last_Modified_By_Id' : "LastModifiedById",
'Created_Date' : "CreatedDate",
'Created_By_Id' : "CreatedById",
'Is_Deleted' : "IsDeleted",
'Is_Active' : "IsActive"
}

PRICEBOOKENTRY_ORDERED_FIELDS = [
'Price_book_Entry_Id',
'Product2_Id',
'Pricebook2_Id',
'Name',
'Product_Code',
'Unit_Price',
'Use_Standard_Price',
'Last_Modified_Date',
'Last_Modified_By_Id',
'Created_Date',
'Created_By_Id',
'Is_Deleted',
'Is_Active'
]

OPPORTUNITYHISTORY_FIELD_TYPE_MAP = {
"Opportunity_History_Id" : "id",
"Opportunity_ID" : "id",
"Changer_Id" : "id",
"Created_Date" : "datetime",
"Stage_Name" : "string",
"Total_Deal_Amount" : "decimal",
"Close_Date" : "datetime",
"Probability" : "decimal",
"Forecast_Category" : "string",
"Is_Deleted" : "bool"
}

OPPORTUNITYHISTORY_FIELD_DICT = {
"Opportunity_History_Id" : "Id",
"Opportunity_ID" : "OpportunityId",
"Changer_Id" : "CreatedById",
"Created_Date" : "CreatedDate",
"Stage_Name" : "StageName",
"Total_Deal_Amount" : "Amount",
"Close_Date" : "CloseDate",
"Probability" : "Probability",
"Forecast_Category" : "ForecastCategory",
"Is_Deleted" : "IsDeleted"
}
	
OPPORTUNITYHISTORY_ORDERED_FIELDS = [
"Opportunity_History_Id","Opportunity_ID","Changer_Id",
"Created_Date","Stage_Name","Total_Deal_Amount","Close_Date",
"Probability","Forecast_Category","Is_Deleted"
]                 
