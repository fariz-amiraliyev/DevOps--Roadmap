variable "name" {}

variable "saml_provider_arn" {}

variable "account_number" {}

variable "max_session_duration" {
  # 60 min
  default = "3600"
}

variable "policy_key" {}

variable "policy_parts_count" {
  default = 1
}

resource "aws_iam_role" "user" {
  name                 = "${var.name}"
  max_session_duration = "${var.max_session_duration}"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "${var.saml_provider_arn}"
      },
      "Action": "sts:AssumeRoleWithSAML",
      "Condition": {
        "StringEquals": {
          "SAML:aud": "https://signin.aws.amazon.com/saml"
        }
      }
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "user" {
  name = "${var.name}"
  role = "${aws_iam_role.user.id}"

  policy = "${file("${path.module}/../../policy-generator/generated-roles/${var.policy_key}.json")}"
}

resource "aws_iam_role_policy" "user_parts" {
  count = "${var.policy_parts_count <= 1 ? 0 : var.policy_parts_count - 1}"
  name  = "${var.name}-${count.index + 1}"
  role  = "${aws_iam_role.user.id}"

  policy = "${file("${path.module}/../../policy-generator/generated-roles/${var.policy_key}_${count.index + 1}.json")}"
}

output "role_id" {
  value = "${aws_iam_role.user.id}"
}
