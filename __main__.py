from pulumi.provider.experimental import Metadata, component_provider_host

if __name__ == "__main__":
    # Call the component provider host. This will discover any ComponentResource
    # subclasses in this package, infer their schema and host a provider that
    # allows constructing these components from a Pulumi program.
    component_provider_host(Metadata("aws-abstracted", "0.1.0"))