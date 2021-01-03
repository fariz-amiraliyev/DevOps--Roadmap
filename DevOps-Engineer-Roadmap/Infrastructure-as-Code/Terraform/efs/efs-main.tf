module "efs-sg" {
  source                       = "../modules/global/generic-security-group"
  region                       = var.region
  env                          = var.env
  cost-center                  = var.cost-center
  department                   = var.department
  encryption                   = var.encryption
  os                           = var.os
  consumer-tags                = var.consumer-tags
  internet-cidr                = var.internet-cidr
  security-group-resource-type = var.security-group-resource-type
  security-application         = var.security-application
  app-name                     = var.efs-app-name
  vpc-id                       = module.vpc.vpc-id

}
/*
module "kms-efs" {
  source               = "../modules/global/kms"
  region               = var.region
  env                  = var.env
  aws-account-id       = var.aws-account-id
  cost-center          = var.cost-center
  department           = var.department
  encryption           = var.encryption
  os                   = var.os
  security-application = var.security-application
  consumer-tags        = var.consumer-tags
  description          = var.kms-efs-description
  app-name             = var.kms-efs-app-name
  is-key-enabled       = var.is-efs-create

}
*/
module "efs" {
  source                = "../modules/global/efs"
  is-create             = var.is-efs-create
  region                = var.region
  env                   = var.env
  aws-account-id        = var.aws-account-id
  cost-center           = var.cost-center
  department            = var.department
  encryption            = var.encryption
  os                    = var.os
  consumer-tags         = var.consumer-tags
  security-application  = var.security-application
  app-name              = var.efs-app-name
  is-encrypted          = var.is-encrypted
  subnet-private-ids    = [module.vpc.subnet-private-ids]
  global-sg-ingress-efs = [module.generic-compute-private-sg.security-group-id, ]
  efs-security-group-id = module.efs-sg.efs-sg-id
  # efs-kms-key-id        = module.kms-efs.kms-efs-key-arn
}
