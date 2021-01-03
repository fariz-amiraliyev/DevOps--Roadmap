locals {
  common-tags = {
    cost-center          = var.cost-center
    department           = var.department
    environment          = var.env
    region               = var.region
    operating-system     = var.os
    security-application = var.security-application
    application-name     = var.efs-app-name
  }
}

resource "aws_security_group_rule" "efs-ingress" {
  count                    = var.is-create ? length(var.global-sg-ingress-efs) : 0
  description              = "Inbound EFS connection no - ${count.index + 1}"
  from_port                = var.efs-port
  to_port                  = var.efs-port
  protocol                 = "tcp"
  type                     = "ingress"
  security_group_id        = var.efs-security-group-id
  source_security_group_id = element(var.global-sg-ingress-efs, count.index)

}

resource "aws_efs_file_system" "efs" {
  count     = var.is-create ? 1 : 0
  encrypted = var.is-encrypted
  # kms_key_id       = var.is-encrypted == true ? var.efs-kms-key-id : ""
  performance_mode = var.performance-mode
  throughput_mode  = var.throughput-mode
  tags = merge({
    Name             = "${var.app-name}-${var.env}-${var.region}"
    application-name = var.app-name
    resource-name    = "${var.app-name}-${var.sg-resource-type}"
    resource-type    = var.efs-resource-type
    encryption       = var.encryption
  }, local.common-tags, var.consumer-tags)

}

resource "aws_efs_mount_target" "efs-target" {
  count = var.is-create ? length(var.subnets) : 0

  file_system_id  = element(concat(aws_efs_file_system.efs[""]), 0)
  security_groups = element(var.global-sg-ingress-efs, count.index)
  subnet_id       = element(var.subnets, count.index)
}
