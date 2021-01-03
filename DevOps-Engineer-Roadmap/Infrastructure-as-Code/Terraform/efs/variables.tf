
variable "region" {
  description = "The AWS region like us-east-1/us-east-2"
}

variable "aws-account-id" {
  description = "AWS account ID or number"
}

variable "profile" {
  description = "profile used to create infrastructure"
}

variable "env" {
  description = "environment like tools/stg/prod/dev/sandbx"
}

variable "app-name" {
  description = "Application name or Its purpose example config, logs"
}

variable "cost-center" {
  description = "Cost center Code - for billing"
}

variable "department" {
  description = "Earnest various department Engineering/Infra"
}

variable "os" {
  description = "Operating system version like Ubuntu, AmazonLinux"
}


variable "encryption" {
  description = "Rescource encypted like SSE-S3, aes256, none or KMS "
}

variable "security-application" {
  description = "Security scanning tools installed on this resource like laceworks, Mcaffee etc"
}


variable "consumer-tags" {
  description = "Tags provided by consumer for their build"
  type        = map
  default     = {}
}

variable "sg-resource-type" {
  description = "Type of resource like security group"
  default     = "security-group"
}

variable "efs-resource-type" {
  description = "Type of resource like security group"
  default     = "EFS"
}

variable "is-create" {
  description = "is create EFS module or not"
  type        = bool
}

variable "vpc-id" {
  description = "VPC to create EFS file system in"
  type        = string
}

variable "global-sg-ingress-efs" {
  description = "List of Security Group IDs permitted to access EFS mounts"
  type        = list(string)
}
/*
variable "efs-kms-key-id" {
  description = "ARN of KMS key to use for EFS encryption (leave null to create a key, set to `aws/backup` to use AWS default CMK)"
  type        = string
}
*/
variable "performance_mode" {
  description = "Performance mode to run in (`generalPurpose` or `maxIO`)."
  type        = string
  default     = "generalPurpose"
}

variable "throughput_mode" {
  description = "EFS file system throughput mode (`provisioned` or `bursting`)"
  type        = string
  default     = "bursting"
}

variable "is-encrypted" {
  description = "is encypted EFS file system with KMS"
  default     = false
}

variable "subnets" {
  default     = []
  description = "Subnet IDs that the EFS mount points should be created on."
  type        = list(string)
}

variable "efs-port" {
  description = "EFS port"
  default     = "2049"
}

variable "efs-security-group-id" {
  description = "EFS security group ID"
}
