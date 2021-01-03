
output "efs-id" {
  description = "EFS File System ID"
  value       = module.efs-id
}

output "efs-sg-id" {
  description = "EFS Security group ID"
  value       = module.efs-sg.security-group-id
}
/*
# KMS outputs
output "kms-efs-alias-arn" {
  description = "The Amazon Resource Name (ARN) of the key alias."
  value       = module.kms-efs.kms-alias-arn
}

output "kms-efs-alias-name" {
  description = "The display name of the key alias."
  value       = module.kms-efs.kms-alias-name
}

output "kms-efs-key-arn" {
  description = "The Amazon Resource Name (ARN) of the key."
  value       = module.kms-efs.kms-key-arn
}

output "kms-efs-key-id" {
  description = "The globally unique identifier for the key"
  value       = module.kms-efs.kms-key-id
}
*/
