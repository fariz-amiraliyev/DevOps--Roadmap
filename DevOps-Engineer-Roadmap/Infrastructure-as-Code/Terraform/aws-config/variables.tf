variable "bucket_prefix" {
  default     = "awsconfig"
  description = "Name of the S3 bucket to log to"
  type        = string
}

variable "config_regions" {
  default = [
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-south-1",
    "sa-east-1",
  ]
  description = "Regions to enable AWS Config in"
  type        = list(string)
}

variable "delivery_channel_name" {
  default     = "awsconfig-s3"
  description = "Name of the delivery channel"
  type        = string
}

variable "logging_bucket" {
  description = "Bucket to log requests to the config bucket to"
  type        = string
}

variable "recorder_name" {
  default     = "awsconfig"
  description = "Name of the config recorder"
  type        = string
}

variable "region" {
  description = "Region S3 bucket will be created in"
  type        = string
}

variable "snapshot_delivery_frequency" {
  default     = "Six_Hours"
  description = "Deliery frequency: One_Hour, Three_Hours, Six_Hours, Twelve_Hours, TwentyFour_Hours"
  type        = string
}

variable "sns_topic_arn" {
  default     = ""
  description = "SNS topic to deliver config rule notifications to"
  type        = string
}

variable "tags" {
  default     = {}
  description = "Tags to add to resources that support it"
  type        = map(string)
}
