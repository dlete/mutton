
# set the Python environment to use Django.
# Equivalent to "python manage.py startshell"
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from inventories.models import Client
from inventories.models import ElineLdp
from inventories.models import ServiceType
from inventories.models import Service

def add_object(name, identity, state, comments, created, updated, client_id, service_type, service_definition):
    s = Service.objects.get_or_create(
        name = name,
        csd_id = identity,
        state = state,
        comments = comments,
        csd_created = created,
        csd_updated = updated,
        client = client_id,
        service_type = service_type,
        service_definition = service_definition
    )[0]
    return s


def populate():
    import logging
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    
    # import lxml so that we can work with xml
    from lxml import etree

    # To work with a local file
    #doc_to_read = 'get_eline_ldp_all.xml'
    doc_to_read = 'get_l3vpn_all.xml'
    tree = etree.parse(doc_to_read)
    root = tree.getroot()

    for element in root.findall('.//{services.schema.networkapi.jmp.juniper.net}Service'):
        name = element.find('.//{services.schema.networkapi.jmp.juniper.net}Name').text
        identity = element.find('.//{services.schema.networkapi.jmp.juniper.net}Identity').text
        state = element.find('.//{services.schema.networkapi.jmp.juniper.net}State').text
        try:
            comments = element.find('.//{services.schema.networkapi.jmp.juniper.net}Comments').text
        except:
            comments = ''
        create_date = element.find('.//{services.schema.networkapi.jmp.juniper.net}CreatedDate').text
        last_update_date = element.find('.//{services.schema.networkapi.jmp.juniper.net}LastUpdatedDate').text

        service_type = element.find('.//{services.schema.networkapi.jmp.juniper.net}ServiceType').text
        service_type_id = ServiceType.objects.get(name=service_type)

        functional_audit = element.find('.//{services.schema.networkapi.jmp.juniper.net}FunctionalAudit').text
        configuration_audit = element.find('.//{services.schema.networkapi.jmp.juniper.net}ConfigurationAudit').text
        fault_status = element.find('.//{services.schema.networkapi.jmp.juniper.net}FaultStatus').text
        overall_status = element.find('.//{services.schema.networkapi.jmp.juniper.net}OverallStatus').text

        service_definition = element.find('.//{services.schema.networkapi.jmp.juniper.net}ServiceDefinitionName').text

        customer_name = element.find('.//{services.schema.networkapi.jmp.juniper.net}CustomerName').text
        client_id = Client.objects.get(name=customer_name)

        logger.info('name is: %s', name)
        logger.info('identity is: %s', identity)
        logger.info('state is: %s', state)
        logger.info('comments is: %s', comments)
        logger.info('create_date is: %s', create_date)
        logger.info('last_update_date is: %s', last_update_date)

        logger.info('service_type is: %s', service_type)
        logger.info('service_type_id is: %s', service_type_id)

        logger.info('functional_audit is: %s', functional_audit)
        logger.info('configuration_audit is: %s', configuration_audit)
        logger.info('fault_status is: %s', fault_status)
        logger.info('overall_status is: %s', overall_status)

        logger.info('service_definition is: %s', service_definition)

        logger.info('customer_name is: %s', customer_name)
        logger.info('client_id is: %s', client_id)

        a = add_object(name, identity, state, comments, create_date, last_update_date, client_id, service_type_id, service_definition)
        print(a)

populate()
