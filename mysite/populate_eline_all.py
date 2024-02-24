
# set the Python environment to use Django.
# Equivalent to "python manage.py startshell"
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from inventories.models import Client
from inventories.models import ElineLdp

def add_eline(name, identity, state, comments, created, updated, client_id):
    c = ElineLdp.objects.get_or_create(
        name = name,
        id_csd = identity,
        state = state,
        comments = comments,
        created = created,
        updated = updated,
        client = client_id
    )[0]
    return c


def populate():
    import logging
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    
    # import lxml so that we can work with xml
    from lxml import etree

    # To work with a local file
    doc_to_read = 'get_eline_ldp_all.xml'
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
        functional_audit = element.find('.//{services.schema.networkapi.jmp.juniper.net}FunctionalAudit').text
        configuration_audit = element.find('.//{services.schema.networkapi.jmp.juniper.net}ConfigurationAudit').text
        fault_status = element.find('.//{services.schema.networkapi.jmp.juniper.net}FaultStatus').text
        overall_status = element.find('.//{services.schema.networkapi.jmp.juniper.net}OverallStatus').text
        customer_name = element.find('.//{services.schema.networkapi.jmp.juniper.net}CustomerName').text

        client_id = Client.objects.get(name=customer_name)

        logger.info('name is: %s', name)
        logger.info('identity is: %s', identity)
        logger.info('state is: %s', state)
        logger.info('comments is: %s', comments)
        logger.info('create_date is: %s', create_date)
        logger.info('last_update_date is: %s', last_update_date)
        logger.info('functional_audit is: %s', functional_audit)
        logger.info('configuration_audit is: %s', configuration_audit)
        logger.info('fault_status is: %s', fault_status)
        logger.info('overall_status is: %s', overall_status)
        logger.info('customer_name is: %s', customer_name)
        logger.info('client_id is: %s', client_id)

        a = add_eline(name, identity, state, comments, create_date, last_update_date, client_id)
        print(a)

populate()



def reconcile_client():

    ''' Here we only sets/not logging '''
    import logging
    logger = logging.getLogger(__name__)
    # Set to INFO if you do WANT to see DEBUG and INFO messages.
    # Set to WARNING if you do NOT WANT to see DEBUG and INFO messages.
    logging.basicConfig(level=logging.INFO)
    #logging.basicConfig(level=logging.WARNING)

    logger.info('hola:  %s', "Pepe")

    # import lxml so that we can work with xml
    from lxml import etree

    '''
    f = open('get_customer_all.xml')
    customers_xml = f.read()
    f.close()
    '''
    #customers_xml = etree.parse('get_customer_all.xml')
    #root = customers_xml.getroot()
    #print(root)

    # To work with a local file
    doc_to_read = 'get_customer_all.xml'
    tree = etree.parse(doc_to_read)
    root = tree.getroot()

    for element in root.findall('.//{services.schema.networkapi.jmp.juniper.net}Customer'):
        customer_name = element.find('.//{services.schema.networkapi.jmp.juniper.net}CustomerName').text
        identity = element.find('.//{services.schema.networkapi.jmp.juniper.net}Identity').text
        create_date = element.find('.//{services.schema.networkapi.jmp.juniper.net}CreatedDate').text
        last_update_date = element.find('.//{services.schema.networkapi.jmp.juniper.net}LastUpdatedDate').text
        account_number = element.find('.//{services.schema.networkapi.jmp.juniper.net}AccountNo').text

        logger.info('customer_name is: %s', customer_name)
        logger.info('identity is: %s', identity)
        logger.info('create_date is: %s', create_date)
        logger.info('last_update_date is: %s', last_update_date)
        logger.info('account_number is: %s', account_number)

       


#reconcile_client()
