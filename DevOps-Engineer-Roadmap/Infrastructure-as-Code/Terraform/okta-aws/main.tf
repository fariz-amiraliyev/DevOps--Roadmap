provider "aws" {
  profile     = "${var.aws_profile}"
  region      = "${var.aws_region}"
  max_retries = 1
}

# storing the terraform state file in the sandbox account.

terraform {
  required_version = "~> 0.11"
  backend "s3" {
    bucket  = "terraform-state"
    key     = "global/s3/terraform.tfstate"
    encrypt = true
    region  = "us-east-3"
  }
}

# Creating  S3 for terraform_state backend

resource "aws_s3_bucket" "terraform_state" {

  bucket = "terraform-state"
  acl    = "private"

  versioning {
    enabled = true
  }

  lifecycle {
    prevent_destroy = true
  }
  tags = {
    Name        = "terraform-remote-state"
    Environment = "myself"
  }
}

module "okta_saml_provider" {
  source = "../modules/okta-provider"

  account_name   = "${var.account_name}"
  saml_file_path = "${path.module}/okta-saml.xml"
}

module "engineer_role" {
  source = "../modules/user-role-module"

  name               = "${var.roles_prefix}Engineer"
  account_number     = "${var.account_number}"
  saml_provider_arn  = "${module.okta_saml_provider.saml_provider_arn}"
  policy_key         = "${var.account_name}/Engineer"
  policy_parts_count = "${lookup(local.policy_parts_count, "Engineer")}"

  # 4 hr
  max_session_duration = "14400"
}

module "administrator_role" {
  source = "../modules/user-role-module"

  name               = "${var.roles_prefix}Administrator"
  account_number     = "${var.account_number}"
  saml_provider_arn  = "${module.okta_saml_provider.saml_provider_arn}"
  policy_key         = "${var.account_name}/Administrator"
  policy_parts_count = "${lookup(local.policy_parts_count, "Administrator")}"

  # 1 hr
  max_session_duration = "3600"
}

module "infrastructure_engineer_read_role" {
  source = "../modules/user-role-module"

  name               = "${var.roles_prefix}InfraRead"
  account_number     = "${var.account_number}"
  saml_provider_arn  = "${module.okta_saml_provider.saml_provider_arn}"
  policy_key         = "${var.account_name}/InfrastructureRead"
  policy_parts_count = "${lookup(local.policy_parts_count, "InfrastructureRead")}"

  # 4 hr
  max_session_duration = "14400"
}

module "infrastructure_engineer_write_role" {
  source = "../modules/user-role-module"

  name               = "${var.roles_prefix}InfraWrite"
  account_number     = "${var.account_number}"
  saml_provider_arn  = "${module.okta_saml_provider.saml_provider_arn}"
  policy_key         = "${var.account_name}/InfrastructureWrite"
  policy_parts_count = "${lookup(local.policy_parts_count, "InfrastructureWrite")}"

  # 1 hr
  max_session_duration = "3600"
}

module "engineer_audit_role" {
  source = "../modules/user-role-module"

  name               = "${var.roles_prefix}EngineerAudit"
  account_number     = "${var.account_number}"
  saml_provider_arn  = "${module.okta_saml_provider.saml_provider_arn}"
  policy_key         = "${var.account_name}/EngineerAudit"
  policy_parts_count = "${lookup(local.policy_parts_count, "EngineerAudit")}"

  # 4 hr
  max_session_duration = "14400"
}

module "data_engineer_role" {
  source             = "../modules/user-role-module"
  name               = "${var.roles_prefix}DataEng"
  account_number     = "${var.account_number}"
  saml_provider_arn  = "${module.okta_saml_provider.saml_provider_arn}"
  policy_key         = "${var.account_name}/DataEngineer"
  policy_parts_count = "${lookup(local.policy_parts_count, "DataEngineer")}"

  # 4 hr
  max_session_duration = "14400"
}


module "developer_productivity_read_role" {
  source = "../modules/user-role-module"

  name               = "${var.roles_prefix}DevProdRead"
  account_number     = "${var.account_number}"
  saml_provider_arn  = "${module.okta_saml_provider.saml_provider_arn}"
  policy_key         = "${var.account_name}/DeveloperProductivityRead"
  policy_parts_count = "${lookup(local.policy_parts_count, "DeveloperProductivityRead")}"

  # 4 hr
  max_session_duration = "14400"
}

module "developer_productivity_write_role" {
  source = "../modules/user-role-module"

  name               = "${var.roles_prefix}DevProdWrite"
  account_number     = "${var.account_number}"
  saml_provider_arn  = "${module.okta_saml_provider.saml_provider_arn}"
  policy_key         = "${var.account_name}/DeveloperProductivityWrite"
  policy_parts_count = "${lookup(local.policy_parts_count, "DeveloperProductivityWrite")}"

  # 1 hr
  max_session_duration = "3600"
}

module "developer_productivity_admin_role" {
  source = "../modules/user-role-module"

  name               = "${var.roles_prefix}DevProdAdmin"
  account_number     = "${var.account_number}"
  saml_provider_arn  = "${module.okta_saml_provider.saml_provider_arn}"
  policy_key         = "${var.account_name}/DeveloperProductivityAdmin"
  policy_parts_count = "${lookup(local.policy_parts_count, "DeveloperProductivityAdmin")}"

  # 1 hr
  max_session_duration = "3600"
}

module "security_role" {
  source = "../modules/user-role-module"

  name               = "${var.roles_prefix}Security"
  account_number     = "${var.account_number}"
  saml_provider_arn  = "${module.okta_saml_provider.saml_provider_arn}"
  policy_key         = "${var.account_name}/Security"
  policy_parts_count = "${lookup(local.policy_parts_count, "Security")}"

  # 1 hr
  max_session_duration = "3600"
}

output "okta_saml_provider_arn" {
  value = "${module.okta_saml_provider.saml_provider_arn}"
}
