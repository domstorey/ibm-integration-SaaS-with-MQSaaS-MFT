apiVersion: appconnect.ibm.com/v1beta1
kind: IntegrationRuntime
metadata:
  name: aceaas-mft-agent
  namespace: default
spec:
  version: 13.0.9
  replicas: 1
  forceFlowBasicAuth:
    enabled: true
  barURL:
    - <Your BAR URL>
  configurations:
    - key.jks
    - key.kdb
    - key.sth
    - mftsetupfiles
    - mftserverconf
    - mftqmgruser
    - mftsaasdemo
