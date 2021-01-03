variable "is-efs-create" {
  description = "is create EFS module or not"
  type        = bool
}
variable "efs-app-name" {
  description = "Name of the application"
}

variable "global-sg-ingress-efs" {
  description = "List of Security Group IDs permitted to access EFS mounts"
  type        = list(string)
}

variable "efs-security-group-id" {
  description = "EFS Security Group ID."
}
/*
variable "efs-kms-key-id" {
  description = "ARN of KMS key to use for EFS encryption (leave null to create a key, set to `aws/backup` to use AWS default CMK)"
  type        = string
}
*/
variable "is-encrypted" {
  description = "is encypted EFS file system with KMS"
  default     = false
}
