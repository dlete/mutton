
# set the Python environment to use Django.
# Equivalent to "python manage.py startshell"
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from inventories.models import Ne

def add_ne(fqdn, identity, role, meid):
    c = Ne.objects.get_or_create(
        fqdn = fqdn,
        id_csd = identity,
        role = role,
        meid = meid,
    )[0]
    return c


def populate():
    import logging
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    
    # import lxml so that we can work with xml
    from lxml import etree

    # To work with a local file
    doc_to_read = 'get_pe_all.xml'
    tree = etree.parse(doc_to_read)
    root = tree.getroot()

    for element in root.findall('.//{services.schema.networkapi.jmp.juniper.net}Device'):
        name = element.find('.//{services.schema.networkapi.jmp.juniper.net}Name').text
        fqdn = name + ".nn.hea.net"
        identity = element.find('.//{services.schema.networkapi.jmp.juniper.net}Identity').text
        role = element.find('.//{services.schema.networkapi.jmp.juniper.net}Role').text
        meid = element.find('.//{services.schema.networkapi.jmp.juniper.net}MEId').text
        #create_date = element.find('.//{services.schema.networkapi.jmp.juniper.net}CreatedDate').text
        #last_update_date = element.find('.//{services.schema.networkapi.jmp.juniper.net}LastUpdatedDate').text
        #account_number = element.find('.//{services.schema.networkapi.jmp.juniper.net}AccountNo').text

        logger.info('name is: %s', name)
        logger.info('fqdn is: %s', fqdn)
        logger.info('identity is: %s', identity)
        logger.info('role is: %s', role)
        logger.info('meid is: %s', meid)
        #logger.info('create_date is: %s', create_date)
        #logger.info('last_update_date is: %s', last_update_date)
        #logger.info('account_number is: %s', account_number)

        a = add_ne(fqdn, identity, role, meid)
        print(a)

populate()
