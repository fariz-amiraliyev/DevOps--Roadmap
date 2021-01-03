data "aws_iam_policy_document" "awsconfig" {
  statement {
    effect  = "Allow"
    actions = ["s3:PutObject"]
    resources = [
      "${aws_s3_bucket.awsconfig_bucket.arn}/*",
    ]
    condition {
      test     = "StringEquals"
      variable = "s3:x-amz-acl"
      values   = ["bucket-owner-full-control"]
    }
  }
  statement {
    effect  = "Allow"
    actions = ["s3:GetBucketAcl"]
    resources = [
      aws_s3_bucket.awsconfig_bucket.arn,
    ]
  }
}

resource "aws_iam_policy" "awsconfig" {
  name_prefix = "awsconfig-"
  policy      = data.aws_iam_policy_document.awsconfig.json
}

data "aws_iam_policy_document" "assume" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["config.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "awsconfig" {
  name_prefix        = "aws-config-role"
  assume_role_policy = data.aws_iam_policy_document.assume.json
}

resource "aws_iam_role_policy_attachment" "awsconfig_managed_policy" {
  role       = aws_iam_role.awsconfig.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSConfigRole"
}

resource "aws_iam_role_policy_attachment" "awsconfig_local_policy" {
  role       = aws_iam_role.awsconfig.name
  policy_arn = aws_iam_policy.awsconfig.arn
}
