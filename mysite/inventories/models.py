"""
PENDING: in Service model, have to figure how to incorporate the field
<InstanceType>default</InstanceType>
to a L3VPN service instance
"""

from django.db import models

class Client(models.Model):
    """
    Model representing a client.
    """
    name = models.CharField(max_length=100,
        verbose_name = "Client name",
        help_text = "Client name as shown in Juniper CSD")
    id_csd = models.PositiveIntegerField(null=False, blank=False,
        verbose_name = "ID CSD",
        help_text = "ID in Juniper CSD")
    id_cdb = models.CharField(max_length=100,
        verbose_name = "ID ClientDB",
        help_text = "ID in HEAnet ClientDB")
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Client in CSD"
        verbose_name_plural = "Clients in CSD"

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

class Ne(models.Model):
    """
    Model representing a NE
    """
    fqdn = models.CharField(max_length=100)
    id_csd = models.PositiveIntegerField(null=False, blank=False)
    role = models.CharField(max_length=100)
    meid = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['fqdn']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.fqdn


class ElineLdp(models.Model):
    """
    Model representing an ELNE LDP
    """
    name = models.CharField(max_length=100)
    id_csd = models.PositiveIntegerField(null=False, blank=False)
    state = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    functional_audit = models.CharField(max_length=100)
    configuration_audit = models.CharField(max_length=100)
    fault_status = models.CharField(max_length=100)
    overall_status = models.CharField(max_length=100)
    client = models.ForeignKey(
        Client,
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    #a_ne = models.ForeignKey(
    #    Ne,
    #    on_delete = models.SET_NULL,
    #    null = True,
    #    blank = True,
    #    related_name='a_ne'
    #)
    #b_ne = models.ForeignKey(
    #    Ne,
    #    on_delete = models.SET_NULL,
    #    null = True,
    #    blank = True,
    #    related_name='b_ne'
    #)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name


class L3vpn(models.Model):
    """
    Model representing a L3VPN
    """
    name = models.CharField(max_length=100)
    id_csd = models.PositiveIntegerField(null=False, blank=False)
    state = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    functional_audit = models.CharField(max_length=100)
    configuration_audit = models.CharField(max_length=100)
    fault_status = models.CharField(max_length=100)
    overall_status = models.CharField(max_length=100)
    client = models.ForeignKey(
        Client,
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    service_type = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name


class ServiceType(models.Model):
    """
    Model representing a Service Type (e.g. ELINE, L3VPN, etc.)
    """
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name



class Service(models.Model):
    """
    Model representing a Service instance
    """
    name = models.CharField(max_length=100)
    csd_id = models.PositiveIntegerField(null=False, blank=False)
    state = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    csd_created = models.DateTimeField()
    csd_updated = models.DateTimeField()

    service_type = models.ForeignKey(
        ServiceType,
        on_delete = models.CASCADE,
        null = False,
        blank = False
    )
    functional_audit = models.CharField(max_length=100)
    configuration_audit = models.CharField(max_length=100)
    fault_status = models.CharField(max_length=100)
    overall_status = models.CharField(max_length=100)

    service_definition = models.CharField(max_length=100)

    client = models.ForeignKey(
        Client,
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name


class ServiceEndpoint(models.Model):
    """
    Model representing a ServiceEndpoint instance
    """
    service = models.ForeignKey(
        Service,
        on_delete = models.CASCADE,
        null = False,
        blank = False
    )
    ne = models.ForeignKey(
        Ne,
        on_delete = models.CASCADE,
        null = False,
        blank = False
    )
    interface_name = models.CharField(max_length=100)
    interface_index = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        ordering = ['ne']
        verbose_name = "Service Endpoints"
        verbose_name_plural = "Service Endpoints in CSD"

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.ne.fqdn
