output "efs-id" {
  description = "EFS File System ID"
  value       = element(concat(aws_efs_file_system.efs.id, [""]), 0)
}
