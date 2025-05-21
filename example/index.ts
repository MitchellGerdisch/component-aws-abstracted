import * as pulumi from "@pulumi/pulumi";

import * as awsAbstracted from "@mitchellgerdisch/aws-abstracted";

const network = new awsAbstracted.Network("example-network")
