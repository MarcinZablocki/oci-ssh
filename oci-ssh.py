#!/usr/bin/env python3

import click
import oci

@click.command()
@click.argument('hostname')
@click.argument('region')
@click.argument('profile', default='DEFAULT')
def cli(hostname, region, profile='DEFAULT'):
    
    config = oci.config.from_file(profile_name=profile)
    if not region: 
        region = config['region']
    else: 
        config['region'] = region

    #print(hostname, region, compartment, profile)
    c = oci.core.ComputeClient(config)
    n = oci.core.VirtualNetworkClient(config)
    s = oci.resource_search.ResourceSearchClient(config)

    q = s.search_resources(oci.resource_search.models.StructuredSearchDetails(query=f"query instance resources where displayName = '{hostname}'")).data
    if len(q.items) > 0: 
        va = c.list_vnic_attachments(q.items[0].compartment_id, instance_id=q.items[0].identifier).data
        vn = n.get_vnic(va[0].vnic_id).data
        print(vn.public_ip)
        
if __name__ == "__main__":
    cli()
