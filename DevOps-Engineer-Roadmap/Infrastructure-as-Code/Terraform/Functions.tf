1. flatten Function
flatten takes a list and replaces any elements that are lists with a flattened sequence of the list contents.
flatten([["a", "b"], [], ["c"]])
["a", "b", "c"]
If any of the nested lists also contain directly-nested lists, these too are flattened recursively:

flatten([[["a", "b"], []], ["c"]])
["a", "b", "c"]

resource "aws_db_subnet_group" "db-network-subnet" {
  count       = var.is-dbcreate == true ? 1 : 0
  name_prefix = "${var.app-name}-${var.env}-${var.region}-"
  description = "Database subnet group for ${var.app-name}-${var.env}-${var.region}"
  subnet_ids  = flatten(var.subnet-private-ids)


2. merge Function
   merge takes an arbitrary number of maps or objects, and returns
   a single map or object that contains a merged set of elements from all arguments.
   tags = merge({
       Name             = "${var.app-name}-${var.env}-${var.region}"
       application-name = var.app-name
       resource-name    = "${var.app-name}-${var.db-subnet-resource-type}"
       resource-type    = var.db-subnet-resource-type

     }, local.common-tags, var.consumer-tags)


3. element Function
element retrieves a single element from a list.

element(list, index)
> element(["a", "b", "c"], 1)
b
If the given index is greater than the length of the list then the index is
"wrapped around" by taking the index modulo the length of the list:

> element(["a", "b", "c"], 3)
a


resource "aws_security_group_rule" "db-ingress" {
  count                    = length(var.global-sg-ingress-db)
  type                     = "ingress"
  description              = "Inbound postgres connection no - ${count.index + 1}"
  from_port                = var.db-port
  to_port                  = var.db-port
  protocol                 = "tcp"
  source_security_group_id = element(var.global-sg-ingress-db, count.index)
  security_group_id        = var.db-security-group-id

}
resource "aws_route_table" "infra-route-private" {
  vpc_id = aws_vpc.infra-vpc.id
  count  = local.number-zones
  tags = merge({
    Name             = "${var.private-cidr-name}-${var.env}-${element(split(",", lookup(var.az-map, var.region)), count.index)}"
    application-name = var.private-cidr-name
    resource-name    = "${var.public-cidr-name}-${var.routetable-resource-type}"
    resource-type    = var.routetable-resource-type
  }, local.common-tags, var.consumer-tags)

}


resource "aws_route_table_association" "infra-rt-public" {
  count          = local.number-zones
  subnet_id      = element(aws_subnet.infra-subnets-public.*.id, count.index)
  route_table_id = aws_route_table.infra-route-public.id
}

4. concat Function
   concat takes two or more lists and combines them into a single list.
   > concat(["a", ""], ["b", "c"])
[
  "a",
  "",
  "b",
  "c",
]
  db_subnet_group_name   = element(concat(aws_db_subnet_group.db-network-subnet.*.name, [""]), 0)


  5. timestamp Function
  > timestamp()
2018-05-13T07:44:12Z

  final_snapshot_identifier   = "${var.final-snapshot-identifier}-${var.app-name}-${var.env}-${var.region}-${formatdate("YYYYMMDDhhmmss", timestamp())}"

6. lookup Function
lookup retrieves the value of a single element from a map, given its key.
If the given key does not exist, a the given default value is returned instead.

lookup(map, key, default)
> lookup({a="ay", b="bee"}, "a", "what?")
ay
> lookup({a="ay", b="bee"}, "c", "what?")
what?

timeouts {
    create = lookup(var.timeouts, "create", null)
    delete = lookup(var.timeouts, "delete", null)
    update = lookup(var.timeouts, "update", null)
  }
7.
number-zones = "${length(split(",", lookup(var.az-map, var.region)))}"

8.resource "aws_subnet" "infra-subnets-public" {
  count             = local.number-zones
  vpc_id            = aws_vpc.infra-vpc.id
  availability_zone = element(split(",", lookup(var.az-map, var.region)), count.index)
  cidr_block        = lookup(var.public-cidr-map, "${element(split(",", lookup(var.az-map, var.region)), count.index)}")

  tags = merge({
    Name             = "${var.public-cidr-name}-${var.env}-${element(split(",", lookup(var.az-map, var.region)), count.index)}"
    application-name = var.public-cidr-name
    resource-name    = "${var.public-cidr-name}-${var.subnet-resource-type}"
    resource-type    = var.subnet-resource-type
  }, local.common-tags, var.consumer-tags)

}


# Private Subnets

resource "aws_subnet" "infra-subnets-private" {
  count             = local.number-zones
  vpc_id            = aws_vpc.infra-vpc.id
  availability_zone = element(split(",", lookup(var.az-map, var.region)), count.index)
  cidr_block        = lookup(var.private-cidr-map, "${element(split(",", lookup(var.az-map, var.region)), count.index)}")

  tags = merge({
    Name             = "${var.private-cidr-name}-${var.env}-${element(split(",", lookup(var.az-map, var.region)), count.index)}"
    application-name = var.private-cidr-name
    resource-name    = "${var.private-cidr-name}-${var.subnet-resource-type}"
    resource-type    = var.subnet-resource-type

  }, local.common-tags, var.consumer-tags)

}

9. map Function
map takes an even number of arguments and returns a map whose elements are constructed from consecutive pairs of arguments.
