variable "account_name" {}
variable "saml_file_path" {}

resource "aws_iam_saml_provider" "saml_provider" {
  name                   = "Okta-${var.account_name}-SAML"
  saml_metadata_document = "${file("${var.saml_file_path}")}"
}

resource "aws_iam_user" "master" {
  name = "okta-${var.account_name}-SAML-master"
}

resource "aws_iam_policy" "master" {
  name        = "okta-${var.account_name}-SAML-master"
  description = "okta-${var.account_name}-SAML-master"
  policy      = "${data.aws_iam_policy_document.master.json}"
}

data "aws_iam_policy_document" "master" {
  statement {
    sid = "1"

    actions = [
      "iam:ListRoles",
      "iam:ListAccountAliases",
    ]

    resources = [
      "*",
    ]
  }
}

resource "aws_iam_user_policy_attachment" "okta_master" {
  user       = "${aws_iam_user.master.name}"
  policy_arn = "${aws_iam_policy.master.arn}"
}

output "saml_provider_arn" {
  value = "${aws_iam_saml_provider.saml_provider.arn}"
}
