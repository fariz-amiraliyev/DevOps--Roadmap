output "arn" {
  description = "Certificate ARN."
  value       = aws_acm_certificate.this.arn
}

output "distinct_domain_names" {
  description = "Distinct domain names."
  value       = local.distinct_domain_names
}
