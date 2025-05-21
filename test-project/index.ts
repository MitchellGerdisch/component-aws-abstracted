import * as pulumi from "@pulumi/pulumi";
import * as random from "@pulumi/random";

import * as awsAbstracted from "@mitchellgerdisch/aws-abstracted";

// This resource will not show up in the Pulumi Cloud graph view for the resources.
const randomThing = new random.RandomString("example-random-string", {
    length: 8,
});

// This resource and children will show up in the Pulumi Cloud graph view for the resources.
// BUT if you look at the stack resource itself, this network resource will not show up as a child of the stack resource.
const network = new awsAbstracted.Network("example-network")
