locals {
  redshift_subnet_group_name             = "${coalesce(var.redshift_subnet_group_name, element(concat(aws_redshift_subnet_group.this.*.name, list("")), 0))}"
  enable_create_redshift_subnet_group    = "${var.redshift_subnet_group_name == "" ? 0 : 1}"
  parameter_group_name                   = "${coalesce(var.parameter_group_name, element(concat(aws_redshift_parameter_group.this.*.id, list("")), 0))}"
  enable_create_redshift_parameter_group = "${var.parameter_group_name == "" ? 0 : 1}"
}

resource "aws_redshift_cluster" "this" {
  cluster_identifier = "${var.cluster_identifier}"
  cluster_version    = "${var.cluster_version}"
  node_type          = "${var.cluster_node_type}"
  number_of_nodes    = "${var.cluster_number_of_nodes}"
  database_name      = "${var.cluster_database_name}"
  master_username    = "${var.cluster_master_username}"
  master_password    = "${var.cluster_master_password}"

  port = "${var.cluster_port}"

  vpc_security_group_ids = ["${var.vpc_security_group_ids}"]

  cluster_subnet_group_name    = "${local.redshift_subnet_group_name}"
  cluster_parameter_group_name = "${local.parameter_group_name}"

  publicly_accessible = "${var.publicly_accessible}"

  # Snapshots and backups
  skip_final_snapshot                 = "${var.skip_final_snapshot}"
  automated_snapshot_retention_period = "${var.automated_snapshot_retention_period }"
  preferred_maintenance_window        = "${var.preferred_maintenance_window}"

  # IAM Roles
  iam_roles = ["${var.cluster_iam_roles}"]

  # Encryption
  encrypted  = "${var.encrypted}"
  kms_key_id = "${var.kms_key_id}"

  tags = "${var.tags}"

  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_redshift_parameter_group" "this" {
  count = "${local.enable_create_redshift_parameter_group}"

  name   = "${var.cluster_identifier}-${replace(var.cluster_parameter_group, ".", "-")}-custom-params"
  family = "${var.cluster_parameter_group}"

  parameter {
    name  = "wlm_json_configuration"
    value = "${var.wlm_json_configuration}"
  }
}

resource "aws_redshift_subnet_group" "this" {
  count = "${local.enable_create_redshift_subnet_group}"

  name        = "${var.cluster_identifier}"
  description = "Redshift subnet group of ${var.cluster_identifier}"
  subnet_ids  = ["${var.subnets}"]

  tags = "${var.tags}"
}
© 2020 GitHub, Inc.
