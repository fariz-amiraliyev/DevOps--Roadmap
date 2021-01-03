var AWS = require('aws-sdk');

exports.updateConfig = function (region) {
  AWS.CredentialProviderChain.defaultProviders = [
    function () {
      return new AWS.EnvironmentCredentials('AWS');
    },
    function () {
      return new AWS.EnvironmentCredentials('AMAZON');
    },
    function () {
      return new AWS.SharedIniFileCredentials({
        profile: process.env.AWS_PROFILE
      });
    },
    function () {
      return new AWS.EC2MetadataCredentials();
    }
  ]

  var chain = new AWS.CredentialProviderChain();

  AWS.config.update({
    region: region
  });

  return new Promise((resolve, reject) => {
    chain.resolve((err, cred) => {
      if (err) {
        return reject(err);
      }
      AWS.config.credentials = cred;
      resolve();
    });
  })
}