data "aws_caller_identity" "current" {
}

locals {
  account_id = data.aws_caller_identity.current.account_id
}

resource "aws_s3_bucket" "awsconfig_bucket" {
  bucket = "${local.account_id}-${var.region}-awsconfig"
  acl    = "private"
  tags   = var.tags

  versioning {
    enabled = true
  }

  logging {
    target_bucket = var.logging_bucket
    target_prefix = "${local.account_id}-${var.region}-awsconfig/"
  }

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "aws:kms"
      }
    }
  }

}

resource "aws_s3_bucket_public_access_block" "awsconfig_bucket_block_public_access" {
  block_public_acls       = true
  block_public_policy     = true
  bucket                  = aws_s3_bucket.awsconfig_bucket.id
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_config_configuration_recorder" "awsconfig_recorder" {
  name     = var.recorder_name
  role_arn = aws_iam_role.awsconfig.arn

  recording_group {
    all_supported                 = true
    include_global_resource_types = true
  }
}

resource "aws_config_delivery_channel" "awsconfig_delivery_channel" {
  name           = var.delivery_channel_name
  s3_bucket_name = aws_s3_bucket.awsconfig_bucket.bucket
  sns_topic_arn  = var.sns_topic_arn

  snapshot_delivery_properties {
    delivery_frequency = var.snapshot_delivery_frequency
  }

  depends_on = [aws_config_configuration_recorder.awsconfig_recorder]
}

resource "aws_config_configuration_recorder_status" "awsconfig_recorder_status" {
  name       = var.recorder_name
  is_enabled = true

  depends_on = [aws_config_delivery_channel.awsconfig_delivery_channel]
}
