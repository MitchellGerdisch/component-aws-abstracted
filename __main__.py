from pulumi.provider.experimental import component_provider_host

from network import Network 
from randomthing import RandomThing

if __name__ == "__main__":
    component_provider_host(name="aws-abstracted", components=[Network, RandomThing])