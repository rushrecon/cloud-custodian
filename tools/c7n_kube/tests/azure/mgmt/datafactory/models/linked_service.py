# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LinkedService(Model):
    """The Azure Data Factory nested object which contains the information and
    credential which can be used to connect with related store or compute
    resource.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AzureDatabricksLinkedService,
    AzureDataLakeAnalyticsLinkedService, HDInsightOnDemandLinkedService,
    SalesforceMarketingCloudLinkedService, NetezzaLinkedService,
    VerticaLinkedService, ZohoLinkedService, XeroLinkedService,
    SquareLinkedService, SparkLinkedService, ShopifyLinkedService,
    ServiceNowLinkedService, QuickBooksLinkedService, PrestoLinkedService,
    PhoenixLinkedService, PaypalLinkedService, MarketoLinkedService,
    MariaDBLinkedService, MagentoLinkedService, JiraLinkedService,
    ImpalaLinkedService, HubspotLinkedService, HiveLinkedService,
    HBaseLinkedService, GreenplumLinkedService, GoogleBigQueryLinkedService,
    EloquaLinkedService, DrillLinkedService, CouchbaseLinkedService,
    ConcurLinkedService, AzurePostgreSqlLinkedService, AmazonMWSLinkedService,
    SapHanaLinkedService, SapBWLinkedService, SftpServerLinkedService,
    FtpServerLinkedService, HttpLinkedService, AzureSearchLinkedService,
    CustomDataSourceLinkedService, AmazonRedshiftLinkedService,
    AmazonS3LinkedService, SapEccLinkedService,
    SapCloudForCustomerLinkedService, SalesforceLinkedService,
    AzureDataLakeStoreLinkedService, MongoDbLinkedService,
    CassandraLinkedService, WebLinkedService, ODataLinkedService,
    HdfsLinkedService, OdbcLinkedService, AzureMLLinkedService,
    TeradataLinkedService, Db2LinkedService, SybaseLinkedService,
    PostgreSqlLinkedService, MySqlLinkedService, AzureMySqlLinkedService,
    OracleLinkedService, FileServerLinkedService, HDInsightLinkedService,
    DynamicsLinkedService, CosmosDbLinkedService, AzureKeyVaultLinkedService,
    AzureBatchLinkedService, AzureSqlDatabaseLinkedService,
    SqlServerLinkedService, AzureSqlDWLinkedService, AzureStorageLinkedService

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param type: Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'AzureDatabricks': 'AzureDatabricksLinkedService', 'AzureDataLakeAnalytics': 'AzureDataLakeAnalyticsLinkedService', 'HDInsightOnDemand': 'HDInsightOnDemandLinkedService', 'SalesforceMarketingCloud': 'SalesforceMarketingCloudLinkedService', 'Netezza': 'NetezzaLinkedService', 'Vertica': 'VerticaLinkedService', 'Zoho': 'ZohoLinkedService', 'Xero': 'XeroLinkedService', 'Square': 'SquareLinkedService', 'Spark': 'SparkLinkedService', 'Shopify': 'ShopifyLinkedService', 'ServiceNow': 'ServiceNowLinkedService', 'QuickBooks': 'QuickBooksLinkedService', 'Presto': 'PrestoLinkedService', 'Phoenix': 'PhoenixLinkedService', 'Paypal': 'PaypalLinkedService', 'Marketo': 'MarketoLinkedService', 'MariaDB': 'MariaDBLinkedService', 'Magento': 'MagentoLinkedService', 'Jira': 'JiraLinkedService', 'Impala': 'ImpalaLinkedService', 'Hubspot': 'HubspotLinkedService', 'Hive': 'HiveLinkedService', 'HBase': 'HBaseLinkedService', 'Greenplum': 'GreenplumLinkedService', 'GoogleBigQuery': 'GoogleBigQueryLinkedService', 'Eloqua': 'EloquaLinkedService', 'Drill': 'DrillLinkedService', 'Couchbase': 'CouchbaseLinkedService', 'Concur': 'ConcurLinkedService', 'AzurePostgreSql': 'AzurePostgreSqlLinkedService', 'AmazonMWS': 'AmazonMWSLinkedService', 'SapHana': 'SapHanaLinkedService', 'SapBW': 'SapBWLinkedService', 'Sftp': 'SftpServerLinkedService', 'FtpServer': 'FtpServerLinkedService', 'HttpServer': 'HttpLinkedService', 'AzureSearch': 'AzureSearchLinkedService', 'CustomDataSource': 'CustomDataSourceLinkedService', 'AmazonRedshift': 'AmazonRedshiftLinkedService', 'AmazonS3': 'AmazonS3LinkedService', 'SapEcc': 'SapEccLinkedService', 'SapCloudForCustomer': 'SapCloudForCustomerLinkedService', 'Salesforce': 'SalesforceLinkedService', 'AzureDataLakeStore': 'AzureDataLakeStoreLinkedService', 'MongoDb': 'MongoDbLinkedService', 'Cassandra': 'CassandraLinkedService', 'Web': 'WebLinkedService', 'OData': 'ODataLinkedService', 'Hdfs': 'HdfsLinkedService', 'Odbc': 'OdbcLinkedService', 'AzureML': 'AzureMLLinkedService', 'Teradata': 'TeradataLinkedService', 'Db2': 'Db2LinkedService', 'Sybase': 'SybaseLinkedService', 'PostgreSql': 'PostgreSqlLinkedService', 'MySql': 'MySqlLinkedService', 'AzureMySql': 'AzureMySqlLinkedService', 'Oracle': 'OracleLinkedService', 'FileServer': 'FileServerLinkedService', 'HDInsight': 'HDInsightLinkedService', 'Dynamics': 'DynamicsLinkedService', 'CosmosDb': 'CosmosDbLinkedService', 'AzureKeyVault': 'AzureKeyVaultLinkedService', 'AzureBatch': 'AzureBatchLinkedService', 'AzureSqlDatabase': 'AzureSqlDatabaseLinkedService', 'SqlServer': 'SqlServerLinkedService', 'AzureSqlDW': 'AzureSqlDWLinkedService', 'AzureStorage': 'AzureStorageLinkedService'}
    }

    def __init__(self, additional_properties=None, connect_via=None, description=None, parameters=None, annotations=None):
        super(LinkedService, self).__init__()
        self.additional_properties = additional_properties
        self.connect_via = connect_via
        self.description = description
        self.parameters = parameters
        self.annotations = annotations
        self.type = None
