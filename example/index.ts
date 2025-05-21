import * as pulumi from "@pulumi/pulumi";
import * as random from "@pulumi/random";

import * as awsAbstracted from "@mitchellgerdisch/aws-abstracted";

const randomThing = new random.RandomString("example-random-string", {
    length: 8,
});

const network = new awsAbstracted.Network("example-network")
