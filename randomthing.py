from pulumi import ComponentResource, ResourceOptions, Input
from typing import Optional, Sequence, TypedDict
from pulumi_random import RandomPet

# Network abstraction for AWS VPC, IGW, Route Table and Subnets


class RandomThingArgs(TypedDict):
    length: Optional[Input[int]]

class RandomThing(ComponentResource):

    def __init__(self,
                 name: str,
                 args: RandomThingArgs,
                 opts: ResourceOptions = None):

        super().__init__('aws-abstracted:resource:randomthing', name, {}, opts)

        length = args.get('length', 4)

        self.randomthing= randomPet(name,
            length=length,
            opts=ResourceOptions(parent=self)
            )

        self.register_outputs({})
