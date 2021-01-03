locals {
  distinct_domain_names = distinct(concat([var.domain_name], [for s in var.subject_alternative_names : replace(s, "*.", "")]))

  validation_domains = [for k, v in aws_acm_certificate.this.domain_validation_options : tomap(v) if contains(local.distinct_domain_names, v.domain_name)]
}

resource aws_acm_certificate this {
  domain_name               = var.domain_name
  subject_alternative_names = var.subject_alternative_names
  validation_method         = var.validation_method
  tags                      = var.tags

  lifecycle {
    create_before_destroy = true
    ignore_changes = [
      subject_alternative_names,
    ]
  }
}

resource aws_route53_record validation {
  count = var.validation_method == "DNS" && var.validate_certificate ? length(local.distinct_domain_names) : 0

  zone_id         = var.zone_id
  name            = element(local.validation_domains, count.index)["resource_record_name"]
  type            = element(local.validation_domains, count.index)["resource_record_type"]
  ttl             = var.ttl
  allow_overwrite = var.allow_overwrite_records

  records = [
    element(local.validation_domains, count.index)["resource_record_value"]
  ]

  depends_on = [aws_acm_certificate.this]
}

resource aws_acm_certificate_validation this {
  count                   = var.validation_method == "DNS" && var.validate_certificate ? 1 : 0
  certificate_arn         = aws_acm_certificate.this.arn
  validation_record_fqdns = aws_route53_record.validation.*.fqdn
}
